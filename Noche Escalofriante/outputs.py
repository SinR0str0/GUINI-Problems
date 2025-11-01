import os
import glob

def main():
    if not os.path.exists("inputs"):
        print("❌ Carpeta 'inputs' no encontrada.")
        return

    input_files = sorted(glob.glob("inputs/sample_input_*.in"))
    if not input_files:
        print("❌ No hay archivos sample_input_*.in en la carpeta 'inputs'.")
        return

    for in_path in input_files:
        # Extraer número del archivo: sample_input_3.in → 3
        try:
            num = in_path.split('_')[-1].replace('.in', '')
            int(num)  # validar que sea número
        except:
            print(f"⚠️ Archivo con nombre no estándar: {in_path}")
            continue

        with open(in_path, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]

        t = int(lines[0])
        results = []

        for i in range(1, 2+(t + 1),2):
            n,k = map(int, lines[i].split())
            a = map(int,lines[i+1].split())
            
            total = 0
            a = sorted(a, reverse=True)
            for i in range(k):
                total+=a[i]
            results.append(str(total))

        # Guardar salida
        out_path = in_path.replace("sample_input_", "sample_output_").replace(".in", ".out")
        with open(out_path, 'w') as f:
            f.write("\n".join(results) + "\n")

        print(f"✅ Generado: {out_path}")

if __name__ == "__main__":
    main()