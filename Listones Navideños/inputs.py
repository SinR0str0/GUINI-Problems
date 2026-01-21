import random
import os

def generate_inputs(num_files=100):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    inputs_dir = os.path.join(script_dir, "inputs")
    os.makedirs(inputs_dir, exist_ok=True)

    
    for file_idx in range(1, num_files + 1):
        t = random.randint(1, 5940)
        cases = []
        
        for _ in range(t):
            a,b,c,d = random.randint(1, 12),random.randint(1, 12),random.randint(1, 12),random.randint(1, 12)
            cases.append((f"{a} {b} {c} {d}"))
        
        # Guardar en inputs/sample_input_X.in
        filename = os.path.join(inputs_dir, f"sample_input_{file_idx}.in")
        with open(filename, 'w') as f:
            f.write(f"{t}\n")
            for linea1 in cases:
                # ✅ Corregido: no uses {} dentro de f-string sin escapar
                f.write(f"{linea1}\n")
        print(f"Generado: {filename}")

if __name__ == "__main__":
    print("Comenzando!")
    generate_inputs(num_files=100)