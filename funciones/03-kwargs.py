# keywords arguments(**): para empaquetar todos los parametros en uno solo
# tenemos que colocar siemrep el nombre del parametro que queremos que sea asignado en la funcion
def get_producy(**datos):
    print(datos["id"],
          datos["name"])


get_producy(id="23",
            name="IPhone",
            desc="Esto es un IPhone")
