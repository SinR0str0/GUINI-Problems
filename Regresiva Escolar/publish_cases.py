import os
import json
import requests

# ===========================
# CONFIGURACIÓN
# ===========================
JUEZ_URL = "https://guinijuez.org"
SECRET_KEY_FILE = "./Submitter/guini.secret_key"
PROBLEM_ID_FILE = "./Submitter/idproblema.txt"
INPUTS_FOLDER = "inputs"
TYPE_UPLOAD = "peque" # peque, mediano, grande

# ===========================
# FUNCIONES AUXILIARES
# ===========================

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()

def escape_json(text):
    """Escapa texto para JSON (aunque requests lo hace automáticamente, lo incluimos por seguridad)"""
    return text.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\t', '\\t')

def call_api(method, data):
    url = f"{JUEZ_URL}/methods/{method}"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=data)
    if response.status_code != 200:
        print(f"❌ Error en API {method}: {response.status_code}")
        print(response.text)
        return None
    return response.json()

# ===========================
# LÓGICA PRINCIPAL
# ===========================

def main():
    # 1. Leer clave secreta y ID del problema
    if not os.path.exists(SECRET_KEY_FILE):
        print(f"❌ No se encontró: {SECRET_KEY_FILE}")
        return
    if not os.path.exists(PROBLEM_ID_FILE):
        print(f"❌ No se encontró: {PROBLEM_ID_FILE}")
        return

    secret_key = read_file(SECRET_KEY_FILE)
    problem_id = read_file(PROBLEM_ID_FILE)

    print(f"🔑 Clave secreta cargada (longitud: {len(secret_key)})")
    print(f"🆔 ID del problema: {problem_id}")

    # 2. Encontrar todos los pares .in y .out en inputs/
    input_files = sorted([f for f in os.listdir(INPUTS_FOLDER) if f.startswith("sample_input_") and f.endswith(".in")])
    if not input_files:
        print("❌ No se encontraron archivos sample_input_*.in en inputs/")
        return

    print(f"📤 Encontrados {len(input_files)} casos de prueba.")

    # 3. Crear los casos en el juez (tipo "TSubida" para todos)
    case_type = TYPE_UPLOAD
    response = call_api("APIcrearCasos", {
        "llavesecreta": secret_key,
        "caso": case_type,
        "numeroarchivos": len(input_files),
        "idproblema": problem_id
    })

    if not response:
        print("❌ Falló la creación de casos.")
        return

    print("✅ Casos creados en el juez.")

    # 4. Subir cada par .in / .out
    for idx, in_file in enumerate(input_files):
        base_name = in_file.replace(".in", "")
        out_file = base_name.replace("input", "output") + ".out"

        in_path = os.path.join(INPUTS_FOLDER, in_file)
        out_path = os.path.join(INPUTS_FOLDER, out_file)

        if not os.path.exists(out_path):
            print(f"⚠️  Advertencia: No se encontró {out_file}. Saltando.")
            continue

        # Leer contenido
        entrada = read_file(in_path)
        salida = read_file(out_path)

        # Subir entrada
        call_api("APIguardarCasos", {
            "llavesecreta": secret_key,
            "indexcaso": idx,
            "idproblema": problem_id,
            "tipo": "entrada",
            "texto": entrada,
            "caso": case_type
        })

        # Subir salida
        call_api("APIguardarCasos", {
            "llavesecreta": secret_key,
            "indexcaso": idx,
            "idproblema": problem_id,
            "tipo": "salida",
            "texto": salida,
            "caso": case_type
        })

        print(f"✅ Caso {idx+1}/{len(input_files)} subido: {in_file} → {out_file}")

    print("\n🎉 ¡Todos los casos han sido publicados en el juez!")

if __name__ == "__main__":
    main()