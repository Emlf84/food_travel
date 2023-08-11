import tkinter as tk
import tkintermapview
import folium
import requests
import polyline


def get_route(pickup_lat, pickup_lon, dropoff_lat, dropoff_lon, url="https://router.project-osrm.org/route/v1/driving/"):

    location = f"{pickup_lat},{pickup_lon};{dropoff_lat},{dropoff_lon}"
    response = requests.get(url + location)

    if response.status_code != 200:
        print(f"Error en la solicitud con código de estado {response.status_code}")
        return None

    response_json = response.json()
    route = polyline.decode(response_json['routes'][0]['geometry'])
    start_point = [response_json['waypoints'][0]['location'][1], response_json['waypoints'][0]['location'][0]]
    end_point = [response_json['waypoints'][1]['location'][1], response_json['waypoints'][1]['location'][0]]
    distance = response_json['routes'][0]['distance']

    return {
        'route': route,
        'start_point': start_point,
        'end_point': end_point,
        'distance': distance
    }

def draw_map(lat_a, lon_a, lat_b, lon_b):

    route_data = get_route(lat_a, lon_a, lat_b, lon_b)

    if not route_data:
        print("No se pudo obtener los datos de la ruta.")
        return None

    map_instance = folium.Map(location=[lon_a, lat_a], zoom_start=15)

    folium.PolyLine(locations=route_data['route'], color="blue").add_to(map_instance)
    folium.Marker(location=[lon_a, lat_a], popup="Origin").add_to(map_instance)
    folium.Marker(location=[lon_b, lat_b], popup="Destination").add_to(map_instance)

    return map_instance

# lat_a, lon_a = -24.723418079805057, -65.40061001034545
# lat_b, lon_b = -24.73039991615085, -65.41403450784667

# drawn_map = draw_map(lat_a, lon_a, lat_b, lon_b)



def ventana():
    ventana = tk.Tk()
    ventana.geometry("800x600")
    ventana.title("Mapa")

    lat_o, lon_o = -24.78848655215894, -65.42342431227226

 
    map_widget = tkintermapview.TkinterMapView(ventana, corner_radius=0, width=800, height=600)
    map_widget.grid(row=0, column=0)

    
    map_widget.set_position(lat_o, lon_o)
    map_widget.set_zoom(15)

    lat_a, lon_a = -24.783616306739752, -65.41072137046753
    lat_b, lon_b = -24.791837169997873, -65.4345393863514

    n=draw_map(lat_a,lon_a,lat_b,lon_b)
    

    ruta=get_route(lat_a,lon_a,lat_b,lon_b)
    print(ruta)
    r=ruta["route"]
    print(r)
    
    path_1 = map_widget.set_path(r)

    path_2 = map_widget.set_path([(-24.723909771244763, -65.40129567016406), (-24.730662137111636, -65.41573061371376)])
    

    ventana.mainloop()

if __name__ == "__main__":
    ventana()