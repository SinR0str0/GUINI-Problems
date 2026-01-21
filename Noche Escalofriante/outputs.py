import os
import glob

def main():
    # Obtener la carpeta donde está este script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    inputs_dir = os.path.join(script_dir, "inputs")
    
    if not os.path.exists(inputs_dir):
        print("❌ Carpeta 'inputs' no encontrada junto al script.")
        return

    # Buscar archivos dentro de la carpeta del script
    pattern = os.path.join(inputs_dir, "sample_input_*.in")
    input_files = sorted(glob.glob(pattern))
    
    if not input_files:
        print("❌ No hay archivos sample_input_*.in en la carpeta 'inputs' junto al script.")
        return

    for in_path in input_files:
        # Extraer número del archivo: sample_input_3.in → 3
        try:
            filename = os.path.basename(in_path)
            num = filename.split('_')[-1].replace('.in', '')
            int(num)  # validar que sea número
        except Exception as e:
            print(f"⚠️ Archivo con nombre no estándar: {in_path}")
            continue

        with open(in_path, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]

        if not lines:
            print(f"⚠️ Archivo vacío: {in_path}")
            continue

        t = int(lines[0])
        results = []
        index = 1  # línea actual en el archivo

        for _ in range(t):
            if index >= len(lines):
                break
            # Leer n y k
            n, k = map(int, lines[index].split())
            index += 1
            # Leer lista a
            a = list(map(int, lines[index].split()))
            index += 1

            # Validar que la lista tenga n elementos
            if len(a) != n:
                print(f"⚠️ Advertencia: n={n} pero se leyeron {len(a)} elementos en {in_path}")

            # Tomar las k casas más caras
            a.sort(reverse=True)
            total = sum(a[:k])
            results.append(str(total))

        # Guardar salida en la misma carpeta 'inputs'
        out_filename = os.path.basename(in_path).replace("sample_input_", "sample_output_").replace(".in", ".out")
        out_path = os.path.join(inputs_dir, out_filename)
        
        with open(out_path, 'w') as f:
            f.write("\n".join(results) + "\n")

        print(f"✅ Generado: {out_path}")

if __name__ == "__main__":
    main()