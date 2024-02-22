import requests

def descargar_csv_heartfailure(url):
     try:
        response = requests.get(url)
        if response.status_code == 200:
            with open('datos_descargados.csv', 'w') as file:
                file.write(response.text)
            print('El archivo CSV ha sido descargado con exito.')
        else:
            print(f'Error: no ha sido descargado:', response.status_code)
     except Exception as e:
         print('Ocurrio un error:', e)

url = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'
descargar_csv_heartfailure(url)

