import requests
import json
from quiniela_scraper import show_results_by_type_and_provinces, get_quiniela_type_by_time
import os
def send_results_to_webhook(results):
    # Obtener el valor de la variable de entorno
    webhook_url = os.getenv("WEBHOOK_URL")
    payload = {"tweet": results}
    
    response = requests.post(webhook_url, json=payload)
    
    if response.status_code == 200:
        print("Results sent successfully.")
    else:
        print("Failed to send results.")

if __name__ == "__main__":
    url = "https://www.jugandoonline.com.ar/rHome.aspx"
    provinces_to_show = ["Ciudad", "Provincia", "Santa Fe", "Córdoba", "Entre Ríos", "Mendoza", "Montevideo"]

    auto_selected_quiniela, horario_emoji = get_quiniela_type_by_time()
    
    results = show_results_by_type_and_provinces(url, auto_selected_quiniela, provinces_to_show, horario_emoji)
    print(results)
    
    try:
        with open("previous_result.json", "r") as file:
            data = json.load(file)
            previous_result = data.get("tweet")
    except (FileNotFoundError, json.JSONDecodeError):
        previous_result = None
    
    if results != previous_result:
        send_results_to_webhook(results)
        with open("previous_result.json", "w") as file:
            json.dump({"tweet": results}, file)
    else:
        print("Los resultados no han cambiado.")
