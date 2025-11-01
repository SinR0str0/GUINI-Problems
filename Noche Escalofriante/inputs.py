import random
import os

def generate_inputs(num_files=10):
    os.makedirs("inputs", exist_ok=True)
    
    for file_idx in range(1, num_files + 1):
        t = random.randint(1, 100)
        cases = []
        
        for _ in range(t):
            # Generar n,k
            n = random.randint(1, 1000)
            k = random.randint(1, 1000)
            
            # Generar lista de casas ai's
            A = []
            for _ in range(n):
                A.append(random.randint(0,100))
            
            cases.append((f"{n} {k}", A))
        
        # Guardar en archivo
        filename = f"inputs/sample_input_{file_idx}.in"
        with open(filename, 'w') as f:
            f.write(f"{t}\n")
            for linea1, linea2 in cases:
                f.write(f"{linea1}\n{" ".join(map(str, linea2))}\n")
        print(f"Generado: {filename}")

# Ejecutar
if __name__ == "__main__":
    generate_inputs(num_files=5)