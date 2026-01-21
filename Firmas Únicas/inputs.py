import random
import string
import os

def generate_inputs(num_files=20):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    inputs_dir = os.path.join(script_dir, "inputs")
    os.makedirs(inputs_dir, exist_ok=True)

    
    for file_idx in range(1, num_files + 1):
        n = 10
        cases = []
        for i in range(n):
            letras = string.ascii_lowercase
            cases.append("".join(random.choices(letras,k=10**5)))
        print(sum(len(c) for c in cases) <= 10**6)
        print(len(cases) == n)
        # Guardar en inputs/sample_input_X.in
        filename = os.path.join(inputs_dir, f"sample_input_{file_idx+15}.in")
        with open(filename, 'w') as f:
            f.write(f"{n}\n")
            for linea1 in cases:
                f.write(f"{linea1}\n")
        print(f"Generado: {filename}")

if __name__ == "__main__":
    print("Comenzando!")
    generate_inputs(num_files=5)
