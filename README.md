# Quininow

Este es un proyecto de "bot" para obtener y compartir resultados de la quiniela.

## Descripción

El QuiniNow es una herramienta que te permite obtener resultados de la quiniela de diferentes provincias y compartirlos utilizando un webhook.

## Características

- Obtiene resultados de la quiniela en diferentes horarios.
- Muestra los resultados en un formato legible.
- Permite compartir los resultados a través de un webhook.

## Uso

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias ejecutando `pip install -r requirements.txt`.
3. Asegúrate de tener las provincias que deseas mostrar en la lista `provinces_to_show` en `main.py`.
4. Ejecuta `main.py` para obtener y mostrar los resultados.
5. Si deseas compartir los resultados a través de un webhook, modifica la función `send_results_to_webhook` en `main.py` con la URL de tu webhook y asegúrate de que la función `generate_results_message` en `quiniela_scraper.py` esté generando la cadena de resultados en el formato que necesitas.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras un error o tienes una mejora, no dudes en abrir un "issue" o enviar una solicitud de extracción.

## Licencia

Este proyecto está bajo la Licencia MIT. Puedes obtener más información en el archivo [LICENSE](LICENSE).

