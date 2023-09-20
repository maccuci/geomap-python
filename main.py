from geopy.geocoders import Nominatim
from utils.geo_utils import GeoUtils
from utils.map_utils import MapUtils

app = Nominatim(user_agent="Testando")
geo_utils = GeoUtils(app=app)
map_utils = MapUtils()

while True:
    op = input("Escolha entre: "
               "\n1- Achar por Endereço\n"
               "2- Achar por Lontitude e Longitude\n")

    if op == "1":
        ad = input("Insira o endereço: ")
        em = input("Deseja imprimir o mapa? S/N")
        if em == "S":
            file_name = input("Nome do arquivo: ")
            map_utils.generate_map_by_address(file_name, ad, geo_utils)

    elif op == "2":
        lat = input("Insira a latitude: ")
        lon = input("Insira a longitude: ")
        em = input("Deseja imprimir o mapa? S/N")
        if em == "S":
            file_name = input("Nome do arquivo: ")
            map_utils.generate_map_by_location(file_name, lat, lon, geo_utils)
