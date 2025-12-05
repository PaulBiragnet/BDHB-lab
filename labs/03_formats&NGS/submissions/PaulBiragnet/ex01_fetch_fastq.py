import sys
import subprocess
import os

BASE_DIR = "data/work/PaulBiragnet/lab03" 

def main():
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <accession_id>")
        sys.exit(1)
        
    accession = sys.argv[1]
    
    try:
        os.makedirs(BASE_DIR, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory: {e}")
        sys.exit(1)

    try:
        command = [
            "prefetch",
            accession,
            # Utilisation de l'argument long séparé
            "--output-directory", 
            BASE_DIR,
            # NOTE: Nous retirons l'option --force pour éviter l'erreur de valeur manquante.
        ]
        
        subprocess.run(command, check=True)
        
        final_sra_path = os.path.join(BASE_DIR, f"{accession}.sra")

    except subprocess.CalledProcessError as e:
        print(f"Error during download using prefetch (Exit Code {e.returncode}):")
        print("Prefetch failed. Check if sra-toolkit is properly installed.")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: 'prefetch' command not found. You must install sra-toolkit.")
        sys.exit(1)


if __name__ == "__main__":
    main()