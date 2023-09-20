import folium
import time
from utils.json_utils import JsonUtils

json_utils = JsonUtils()


class MapUtils:

    def generate_map_by_address(self, file_name, address, geo_utils):
        print("Salvando...")
        loc = geo_utils.get_location_by_address(address)
        m = folium.Map(location=(loc["lat"], loc["lon"]))
        m.save(f"./data/mapas/{file_name}.html")
        time.sleep(5)
        print(
            f"Informações salvas!\nO arquivo ainda está sendo gerado, e será criado no caminho data/mapas/{file_name}.html")

        data = {
            f"{file_name}": {
                "nome": loc['name'],
                "tipo": loc['type'],
                "importancia": loc['importance'],
                "tipo_endereco": loc['addresstype'],
                "lat": loc['lat'],
                "lon": loc['lon'],
            }
        }
        json_utils.add_citydata_json('./data/cidades_dados.json', data)

    def generate_map_by_location(self, file_name, lat, lon, geo_utils):
        print("Salvando...")
        address = geo_utils.get_address_by_location(lat, lon)
        m = folium.Map(location=(lat, lon))
        m.save(f"./data/mapas/{file_name}.html")
        time.sleep(5)
        print(
            f"Informações salvas!\nO arquivo ainda está sendo gerado, e será criado no caminho data/mapas/{file_name}.html")
        data = {
            f"{file_name}": {
                "nome": address['name'],
                "tipo": address['type'],
                "importancia": address['importance'],
                "tipo_endereco": address['addresstype'],
                "lat": address['lat'],
                "lon": address['lon'],
            }
        }
        json_utils.add_citydata_json('./data/cidades_dados.json', data)
        pass
