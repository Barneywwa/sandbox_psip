import requests

miasto = "zamosc"


def pogoda_z(miasto: str):
    url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}"
    response = requests.get(url).json()
    print(response["id_stacji"])
pogoda_z(miasto)


db_params = sqlalchemy.URL.create(
    drivername="postgres"
    username="postgres"
    password="Zimos98103"
    host="localhost"
    database="postgres"
    port=5432
)
engine=sqlalchemy.create_engine(db_params)
connection = engine.connect()

sql_query_1=sqlalchemy.text("INSERT INTO public.my_table(name) VALUES('kepa')")
connection.execute(sql_query_1)

connection.commit()