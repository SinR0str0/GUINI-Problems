import random
import string
import os

def generate_inputs(num_files=20):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    inputs_dir = os.path.join(script_dir, "inputs")
    os.makedirs(inputs_dir, exist_ok=True)

    MAX = 10**19
    MIN = 10**3
    for file_idx in range(1, num_files + 1):
        t = random.randint(MIN,MAX)
        cases = []
        for _ in range(t):
            l = random.randrange(1, MAX + 1)
            r = random.randrange(l, MAX + 1)
            cases.append((l,r))
        
        # Guardar en inputs/sample_input_X.in
        filename = os.path.join(inputs_dir, f"sample_input_{file_idx}.in")
        with open(filename, 'w') as f:
            f.write(f"{t}\n")
            for l,r in cases:
                f.write(f"{l} {r}\n")
        print(f"Generado: {filename}")

if __name__ == "__main__":
    print("Comenzando!")
    generate_inputs(num_files=10)
