import json

class Destinoculinario:
    def __init__(self, id_destino, nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo, disponibilidad, imagen, ubicacion,id_usuario=None, popularidad=None):
        self.id_destino = id_destino
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo= precio_maximo
        self.popularidad= popularidad
        self.disponibilidad= disponibilidad
        self.imagen= imagen
        self.ubicacion= ubicacion
        self.id_usuario=id_usuario

    def cargar_review(self):
        try:
            with open("lista_reviews.json", 'r') as f:
                lista_reviews = json.load(f)
        except:
            print("aun no existe ninguna review")
            return
        c=0
        suma= 0
        comentarios= []
        for rev in lista_reviews:
            if rev["id destino"] == self.id_destino:
                c= c+1
                comentarios.append(rev["comentario"])
                suma= rev["calificacion"] + suma
            
            else:
                print("este destino no tiene reviews")
        if c > 0:
            self.popularidad= suma / c

            
    def __eq__(self, otro):
        return isinstance(otro, Destinoculinario) and self.id_destino == otro.id_destino

    def __hash__(self):
        return hash(self.id_destino)
        
    def a_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def de_json(cls, datos_json):
        datos = json.loads(datos_json)
        return cls(**datos)
    
    @staticmethod
    
    def cargar_destinos(usuario_principal):
        with open("lista_lugares.json", "r") as archivo:
            datos = json.load(archivo)

        destinos = []
        for dato in datos:
            destino = Destinoculinario.de_json(json.dumps(dato))
            if destino.id_usuario is None or (usuario_principal is not None and destino.id_usuario == usuario_principal["id"]):
                destinos.append(destino)

        return destinos
        #return [Destinoculinario.de_json(json.dumps(dato)) for dato in datos]





def agregar_destino_usuario(nombre,coordenadas,id_usuario):
    try:
        with open('lista_lugares.json', 'r') as f:
            lista_lugar = json.load(f)
    except:
        lista_lugar=[]
        with open('lista_lugares.json', 'w') as f:
            json.dump(lista_lugar, f)
    if len(lista_lugar) < 0:
        id_destino= 0
    id_destino = len(lista_lugar)+1
    #nombre = input("Nombre de lugar: ")
    id_usuario= id_usuario
    tipo_cocina = None
    ingredientes = None
    precio_minimo = None
    precio_maximo= None
    popularidad= None
    disponibilidad= True
    imagen= None
    direccion=None

    ubicacion = {
        
        "id ubicacion": id_destino,
        "direccion": direccion,
        "coordenadas": coordenadas    
    }
    destino = {
        
        "id_destino": id_destino,
        "nombre": nombre,
        "id_usuario": id_usuario,
        "tipo_cocina": tipo_cocina,
        "ingredientes": ingredientes,
        "precio_minimo": precio_minimo,
        "precio_maximo": precio_maximo,
        "popularidad": popularidad,
        "disponibilidad": disponibilidad,
        "imagen": imagen,
        "ubicacion": ubicacion
    }
    lista_lugar.append(destino)

    with open('lista_lugares.json', 'w') as f:
        json.dump(lista_lugar, f, indent=4)



def agregar_destino(nombre,tipo_cocina,ingredientes,precio_minimo,precio_maximo,direccion,coord,imagen):
    try:
        with open('lista_lugares.json', 'r') as f:
            lista_lugar = json.load(f)
    except:
        lista_lugar=[]
        with open('lista_lugares.json', 'w') as f:
            json.dump(lista_lugar, f)
    if len(lista_lugar) < 0:
        id_destino= 0
    id_destino = len(lista_lugar)+1
    id_usuario=None
    #nombre = input("Nombre de lugar: ")
    #tipo_cocina = input("tipo de cocina: ")
    ingred=ingredientes.split(',')
    #for i in range (3):
    #    ingrediente = input("ingrediente: ")
    #    ingredientes.append(ingrediente)
    #precio_minimo = float(input("precio minimo: "))
    #precio_maximo= float(input("precio maximo: "))
    popularidad= None
    disponibilidad= True
    #imagen= input("directorio de imagen: ")
    ubicacion = {
        
        "id ubicacion": id_destino,
        "direccion": direccion,
        "coordenadas": coord     
    }
    destino = {
        
        "id_destino": id_destino,
        "nombre": nombre,
        "id_usuario": id_usuario,
        "tipo_cocina": tipo_cocina,
        "ingredientes": ingred,
        "precio_minimo": precio_minimo,
        "precio_maximo": precio_maximo,
        "popularidad": popularidad,
        "disponibilidad": disponibilidad,
        "imagen": imagen,
        "ubicacion": ubicacion
    }
    lista_lugar.append(destino)

    with open('lista_lugares.json', 'w') as f:
        json.dump(lista_lugar, f, indent=4)

def gen_review(usuario_principal, destino,calificacion,comentario,animo):
    try:
        with open('reviews_creadas.json', 'r') as f:
            lista_reviews = json.load(f)
    except:
        lista_reviews=[]
        with open('reviews_creadas.json', 'w') as f:
            json.dump(lista_reviews, f)

    if len(lista_reviews) < 0:
        id_review= 0
    id_review = len(lista_reviews)+1
    id_destino = destino.id_destino
    id_usuario = usuario_principal["id"]
    #calificacion = int(input("Calificaion del 1 al 5: "))
    #comentario= input("Comentario: ")
    #animo= input("positivo o negativo: ")
    review = {
        "id review": id_review,
        "id destino": id_destino,
        "id usuario": id_usuario,
        "calificacion": calificacion,
        "comentario": comentario,
        "animo": animo
    }
    lista_reviews.append(review)

    with open('reviews_creadas.json', 'w') as f:
        json.dump(lista_reviews, f, indent=4)
        print(lista_reviews)


def cargar_review(destino):
    with open('reviews_creadas.json', 'r') as f:
        lista_reviews = json.load(f)
    l_rev =[]
    for rev in lista_reviews:
        if rev["id destino"] == destino.id_destino:
            l_rev.append(rev)
    return l_rev










def registro(archivo,nombre,apellido,password):      
    try:
        with open(archivo, 'r') as f:
            lista_registrados = json.load(f)
    except:
        lista_registrados=[]
        with open('usuarios_registrados.json', 'w') as f:
            json.dump(lista_registrados, f)

    if len(lista_registrados) < 0:
        id_usuario= 0
    id_usuario = len(lista_registrados)+1
    #nombre = input("Nombre: ")
    #apellido = input("Apellido: ")
    #password = input("Contraseña: ")
    usuario = {
        "tipo": "usuario",
        "id": id_usuario,
        "nombre": nombre,
        "apellido": apellido,
        "password": password,
        "historial_ruta": [],
        "agregados": []
    }
    lista_registrados.append(usuario)
    
    with open(archivo, 'w') as f:
        json.dump(lista_registrados, f, indent=4)
    print(lista_registrados)


def iniciar_sesion(usuario, password):
    with open('usuarios_registrados.json', 'r') as f:
        lista_registrados = json.load(f)
    #usuario= input("nombre de usuario: ")
    #password= input("contra: ")
    for datos in lista_registrados:
        if datos["nombre"] == usuario and datos["password"] == password:
            print("bienvenido")
            return datos     
    print("no encontrado")
    return None

#a=Destinoculinario.cargar_destinos()
# print(a)




# def agregar_destino_c():
#     try:
#         with open('lista_lugares.json', 'r') as f:
#             lista_lugar = json.load(f)
#     except:
#         lista_lugar=[]
#         with open('lista_lugares.json', 'w') as f:
#             json.dump(lista_lugar, f)
#     if len(lista_lugar) < 0:
#         id_destino= 0
#     id_destino = len(lista_lugar)+1
#     id_usuario=None
#     nombre = input("Nombre de lugar: ")
#     tipo_cocina = input("tipo de cocina: ")
#     ingred=[]
#     for i in range (3):
#         ingrediente = input("ingrediente: ")
#         ingred.append(ingrediente)
#     precio_minimo = float(input("precio minimo: "))
#     precio_maximo= float(input("precio maximo: "))
#     popularidad= None
#     disponibilidad= True
#     imagen= input("directorio de imagen: ")
#     ubicacion = {
        
#         "id ubicacion": id_destino,
#         "direccion": input("direccion: "),
#         "coordenadas": input("coord")     
#     }
#     destino = {
        
#         "id_destino": id_destino,
#         "nombre": nombre,
#         "id_usuario": id_usuario,
#         "tipo_cocina": tipo_cocina,
#         "ingredientes": ingred,
#         "precio_minimo": precio_minimo,
#         "precio_maximo": precio_maximo,
#         "popularidad": popularidad,
#         "disponibilidad": disponibilidad,
#         "imagen": imagen,
#         "ubicacion": ubicacion
#     }
#     lista_lugar.append(destino)

#     with open('lista_lugares.json', 'w') as f:
#         json.dump(lista_lugar, f, indent=4)


#agregar_destino_c()