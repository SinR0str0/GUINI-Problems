import random
import os

def generate_inputs(num_files=50):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    inputs_dir = os.path.join(script_dir, "inputs")
    os.makedirs(inputs_dir, exist_ok=True)

    
    for file_idx in range(1, num_files + 1):
        t = random.randint(1, 10000)
        cases = []
        
        for _ in range(t):
            n = random.randint(1, 200000)
            k = random.randint(1, 200000)
            A = [random.randint(0, 100) for _ in range(n)]
            cases.append((f"{n} {k}", A))
        
        # Guardar en inputs/sample_input_X.in
        filename = os.path.join(inputs_dir, f"sample_input_{file_idx}.in")
        with open(filename, 'w') as f:
            f.write(f"{t}\n")
            for linea1, linea2 in cases:
                # ✅ Corregido: no uses {} dentro de f-string sin escapar
                f.write(f"{linea1}\n")
                f.write(" ".join(map(str, linea2)) + "\n")
        print(f"Generado: {filename}")

if __name__ == "__main__":
    generate_inputs(num_files=51)