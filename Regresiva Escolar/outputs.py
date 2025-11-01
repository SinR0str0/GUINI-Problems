import os
import glob

SEC_PER_DAY = 24 * 3600
TWO_HOURS = 2 * 3600

def to_seconds(time_str):
    """Convierte 'hh:mm:ss' a segundos desde medianoche."""
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

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

        for i in range(1, t + 1):
            parts = lines[i].split()
            h_entrada, h_actual, h_salida = parts

            # Convertir a segundos (reloj)
            tE = to_seconds(h_entrada)  # xx:00:00
            tA = to_seconds(h_actual)   # hh:mm:ss (en descanso)
            tS = to_seconds(h_salida)   # xx:00:00

            # Interpretar salida: si tS <= tE, entonces es al día siguiente
            if tS <= tE:
                tS_abs = tS + SEC_PER_DAY
            else:
                tS_abs = tS

            tE_abs = tE  # entrada en día 0

            # Interpretar h_actual: debe estar en (tE_abs, tS_abs)
            # Probar día 0 y día 1
            tA_abs = tA
            if not (tE_abs < tA_abs < tS_abs):
                tA_abs = tA + SEC_PER_DAY
                # Si aún no está en el intervalo, forzar (debería estar por generación)
                if not (tE_abs < tA_abs < tS_abs):
                    # Fallback: usar tA en día 0 (poco probable en casos válidos)
                    tA_abs = tA

            # Generar todos los inicios de clase: tE, tE+2h, tE+4h, ..., < tS_abs
            class_starts = []
            start = tE_abs
            while start < tS_abs:
                class_starts.append(start)
                start += TWO_HOURS

            # Contar cuántas clases comienzan ESTRICTAMENTE DESPUÉS de tA_abs
            count = 0
            for cs in class_starts:
                if tA_abs < cs:
                    count += 1

            results.append(str(count))

        # Guardar salida
        out_path = in_path.replace("sample_input_", "sample_output_").replace(".in", ".out")
        with open(out_path, 'w') as f:
            f.write("\n".join(results) + "\n")

        print(f"✅ Generado: {out_path}")

if __name__ == "__main__":
    main()