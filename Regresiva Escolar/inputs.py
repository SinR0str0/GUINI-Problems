import random
import os

def generate_inputs(num_files=10):
    os.makedirs("inputs", exist_ok=True)
    
    for file_idx in range(1, num_files + 1):
        t = random.randint(1001, 10000)
        cases = []
        
        for _ in range(t):
            # 2.1 Generar hora inicial
            h_entrada = random.randint(0, 23)
            
            # 2.2 Generar hora final: duración ≥ 2h y múltiplo de 2
            while True:
                h_salida = random.randint(0, 23)
                if abs(h_salida-h_entrada)<3:
                    continue
                # Calcular duración cronológica
                if h_salida > h_entrada:
                    duracion = h_salida - h_entrada
                else:
                    duracion = h_salida + 24 - h_entrada
                
                if duracion >= 2 and duracion % 2 == 0:
                    break
            
            # 2.3 Generar hora actual (entera) en el intervalo cronológico abierto
            # Convertimos a lista de horas válidas entre entrada y salida
            horas_validas = []
            current = (h_entrada + 1) % 24
            steps = 0
            max_steps = 48  # evitar bucle infinito
            while steps < duracion - 1 and steps < max_steps:
                horas_validas.append(current)
                current = (current + 1) % 24
                steps += 1
            
            if not horas_validas:
                # Fallback: usar h_entrada + 1 (mod 24)
                h_actual_hora = (h_entrada + 1) % 24
            else:
                h_actual_hora = random.choice(horas_validas)
            
            # 2.4 Minutos y segundos aleatorios (para asegurar que esté en descanso)
            mm = random.randint(0, 59)
            ss = random.randint(0, 59)
            
            # 2.5 Formato
            entrada_str = f"{h_entrada:02d}:00:00"
            actual_str = f"{h_actual_hora:02d}:{mm:02d}:{ss:02d}"
            salida_str = f"{h_salida:02d}:00:00"
            
            cases.append((entrada_str, actual_str, salida_str))
        
        # Guardar en archivo
        filename = f"inputs/sample_input_{file_idx}.in"
        with open(filename, 'w') as f:
            f.write(f"{t}\n")
            for entrada, actual, salida in cases:
                f.write(f"{entrada} {actual} {salida}\n")
        print(f"Generado: {filename}")

# Ejecutar
if __name__ == "__main__":
    generate_inputs(num_files=60)