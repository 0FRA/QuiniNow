import time
import subprocess

while True:
    # Ejecutar el comando Python que deseas cada media hora
    subprocess.run(["python", "Main.py"])  # Reemplaza "tu_script.py" con el nombre de tu archivo de script Python
    
    # Pausar durante media hora (1800 segundos)
    time.sleep(1800)