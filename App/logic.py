import time
import csv
from DataStructures import array_list as lt


csv.field_size_limit(2147483647)

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    
    catalog = {
        'trips': None,
        'neighborhoods': None,
    }

    catalog['trips'] = lt.new_list()
    catalog['neighborhoods'] = lt.new_list()

    pass


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos

    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for record in input_file:
        lt.add_last(catalog['trips'], record)
    for neighborhood in input_file:
        lt.add_last(catalog['neighborhoods'], neighborhood)
    return catalog

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    
    return lt.getElement(catalog['trips'], id)
    


def req_1(catalog, passengers):
    """
    Retorna el resultado del requerimiento 1
    
    Tiempo promedio (en minutos) de la duración de los trayectos.
o Costo total promedio (en dólares) de los trayectos.
o Distancia promedio (en millas) de los trayectos.
o Costo promedio pagado en peajes de los trayectos.
o Nombre y cantidad del tipo de pago más usado en los trayectos. (en formato “medio de pago -
cantidad” ej. “CREDIT_CARD - 300”)
o Cantidad de propina promedio pagada en los trayectos.
o Fecha de inicio de trayecto con mayor frecuencia (sin tener en cuenta horas ni minutos). (con
formato “%Y-%m-%d” ej. “2015-04-15”).
    """
    # TODO: Modificar el requerimiento 1
    
    a = get_time()
    
    amount_trips = 0
    total_time = 0 # in seconds
    total_cost = 0
    total_distance = 0
    total_tolls = 0
    total_tip = 0
    payment_types = {}

    date_frequency = {}
    
    for record in catalog['trips']:
        
        if not cmp_function(int(record['passenger_count']), passengers):
            amount_trips += 1
            
            entry = int(record['pickup_datetime'][11:13])*3600 + int(record['pickup_datetime'][14:16])*60 + int(record['pickup_datetime'][17:19])
            exit = int(record['dropoff_datetime'][11:13])*3600 + int(record['dropoff_datetime'][14:16])*60 + int(record['dropoff_datetime'][17:19])
            total_time += (exit - entry)
            # Handle trips that go past midnight
            if cmp_function(record['pickup_datetime'][0:10], record['dropoff_datetime'][0:10]):
                total_time += 86400
        
            total_cost += float(record['fare_amount'])
            
            total_distance += float(record['trip_distance'])
            
            total_tolls += float(record['tolls_amount'])
            
            total_tip += float(record['tip_amount'])
            
            payment_type = record['payment_type']
            if payment_type in payment_types:
                payment_types[payment_type] += 1
            else:
                payment_types[payment_type] = 1
            
            trip_start_date = record['trip_start_timestamp'][0:10]
            if trip_start_date in date_frequency:
                date_frequency[trip_start_date] += 1
            else:
                date_frequency[trip_start_date] = 1
        
    max_payment_type = 0 
    most_used_payment_type = ""   
    for key in payment_types:
        if payment_types[key] > max_payment_type:
            max_payment_type = payment_types[key]
            most_used_payment_type = key
            
    max_date_frequency = 0
    most_frequent_date = ""
    for key in date_frequency:
        if date_frequency[key] > max_date_frequency:
            max_date_frequency = date_frequency[key]
            most_frequent_date = key   
            
    b = get_time()
    time = delta_time(a, b)       
                               
    return total_time/amount_trips,total_distance/amount_trips,total_cost/amount_trips, total_tolls/amount_trips, total_tip/amount_trips, most_used_payment_type, most_frequent_date, time


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def cmp_function(element_a, element_b):
    """
    Función de comparación genérica
    """
    if (element_a > element_b):
        return 1
    elif (element_a < element_b):
        return -1
    else:
        return 0
