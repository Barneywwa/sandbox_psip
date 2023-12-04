import requests

miasto = "zamosc"


def pogoda_z(miasto: str):
    url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}"
    response = requests.get(url).json()
    print(response["id_stacji"])
pogoda_z(miasto)