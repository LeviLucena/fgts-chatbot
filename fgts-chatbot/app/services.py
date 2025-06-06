import requests

def get_endereco_por_cep(cep):
    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                return data
    except:
        return None
    return None
