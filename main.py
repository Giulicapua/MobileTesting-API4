import requests

def datos_api():
    endpoint = "https://www.jsonkeeper.com/b/MX0A"
    respuesta = requests.get(endpoint)
    respuesta.raise_for_status()
    json_data = respuesta.json()
    return json_data.get("products", [])

def texto_api(lista_productos):
    if len(lista_productos) == 0:
        return "Nada que mostrar."
    
    info = ["ID: {}\nNombre: {}\nDescripcion: {}\nPrecio: {}\nDivisa: {}\nEstado: {}".format
            (p["id"], p["name"], p["description"], p["price"], p["currency"], "En stock" if p["in_stock"] else "Sin stock") 
            for p in lista_productos]
    
    return "\n".join(info)