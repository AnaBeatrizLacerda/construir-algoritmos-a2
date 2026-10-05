import requests
from datetime import datetime, timedelta


def cotar():
    hoje = datetime.now()
    resultado = []

    for i in range(365):
        data = hoje - timedelta(days=i)

        while True:
            data_formatada = data.strftime("%m-%d-%Y")

            url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data_formatada}'&$top=100&$format=json&$select=cotacaoCompra"

            res = requests.get(url)
            res = res.json()

            if res['value']:
                valor = res['value'][0]['cotacaoCompra']
                break

            data = data - timedelta(days=1)

        resultado.append(valor)

    return resultado


resultado = cotar()

print(len(resultado))
print(resultado)