
diccionario= {".gif":"image/gif",
              ".jpg": "image/jpeg",
              ".jpeg": "image/jpeg",
              ".png": "image/png",
              ".pdf": "application/pdf",
              ".txt": "text/plain",
              ".zip": "application/zip"
}
nombre= input("Nombre del archivo: ")   
if ".gif" in nombre:
    print("Salida Esperada: "+ diccionario[".gif"])
elif ".jpg" in nombre:
    print("Salida Esperada: "+ diccionario[".jpg"])
elif ".jpeg" in nombre:
    print("Salida Esperada: "+ diccionario[".jpeg"])
elif ".png" in nombre:
    print("Salida Esperada: "+ diccionario[".png"])
elif ".pdf" in nombre:
    print("Salida Esperada: "+ diccionario[".pdf"])
elif ".txt" in nombre:
    print("Salida Esperada: "+ diccionario[".txt"])
elif ".zip" in nombre:
    print("Salida Esperada: "+ diccionario[".zip"])
else :
    print("Formato no reconocido")