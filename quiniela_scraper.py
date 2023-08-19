import requests
from bs4 import BeautifulSoup
from datetime import datetime

def generate_custom_date():
    nombres_meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }

    nombres_dias_semana = {
        0: "Lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
        6: "Domingo"
    }

    fecha_actual = datetime.now()
    dia_semana = fecha_actual.weekday()
    dia_mes = fecha_actual.day
    numero_mes = fecha_actual.month

    cadena_fecha = f"🗓️ {nombres_dias_semana[dia_semana]} {dia_mes} de {nombres_meses[numero_mes]}"
    return cadena_fecha

def extract_results(container):
    province_name = container.find('p', class_='tabla-pizarras-titulos-2021').text.strip()
    results = {}

    result_entries = container.find_all('div', class_='row text-center quinielas2021-desktop')[0]

    for entry in result_entries.find_all('div', class_='col-xs-5'):
        result_type = entry.find('span', class_='no-enlaces-quinielas-2021').text
        result_number = entry.find('span', class_='no-enlaces-numeros').text

        results[result_type] = result_number

    return province_name, results

def get_quiniela_type_by_time():
    current_time = datetime.now().time()
    if current_time >= datetime.strptime("21:00", "%H:%M").time():
        return "Nocturna", "🕘"
    elif current_time >= datetime.strptime("18:00", "%H:%M").time():
        return "Vespertina", "🕕"
    elif current_time >= datetime.strptime("15:00", "%H:%M").time():
        return "Matutina", "🕒"
    elif current_time >= datetime.strptime("12:00", "%H:%M").time():
        return "Primera", "🕛"
    else:
        return None, ""

def show_results_by_type_and_provinces(url, tipo_quiniela, provinces, horario_emoji):
    response = requests.get(url)
    html_code = response.content

    soup = BeautifulSoup(html_code, 'html.parser')

    province_containers = soup.find_all('div', class_='container contenedor-pizarras-2021')
    custom_date = generate_custom_date()
    result_messages = []
    result_messages.append(custom_date)
    result_messages.append(f"{horario_emoji} {tipo_quiniela}")
    for province_container in province_containers:
        province_name, province_results = extract_results(province_container)
        if province_name in provinces and tipo_quiniela in province_results:
            quiniela_result = province_results[tipo_quiniela]
            result_messages.append(f"{province_name}: {quiniela_result}")
        
    return "\n".join(result_messages)

if __name__ == "__main__":
    url = "https://www.jugandoonline.com.ar/rHome.aspx"
    provinces_to_show = ["Ciudad", "Provincia", "Santa Fe", "Córdoba", "Entre Ríos", "Mendoza", "Montevideo"]

    auto_selected_quiniela, horario_emoji = get_quiniela_type_by_time()
    show_results_by_type_and_provinces(url, auto_selected_quiniela, provinces_to_show, horario_emoji)
