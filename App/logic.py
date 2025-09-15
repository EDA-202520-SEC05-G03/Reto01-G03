import time
import csv
from DataStructures.List import array_list as lt


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
    


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog,pmin,pmax):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    t0=get_time()
    size=lt.size(catalog['trips'])
    cnt=0
    tmin=0
    tpay=0
    tdist=0
    tpeajes=0
    cantpsj=[]
    tprop=0
    dates=[]
    for v in range (1,size+1):
        info=get_data(catalog,v)
        pay=float(info['total_amount'])
        if pmin<=pay<=pmax:
            cnt+=1
            h0= info["pickup_datetime"].split()[1]
            hf=info ["dropoff_datetime"].split()[1]

            hms0=h0.split(':')
            hmsf=hf.split(':')

            h1=int(hms0[0])
            m1=int(hms0[1])
            s1=int(hms0[2])

            h2=int(hmsf[0])
            m2=int(hmsf[1])
            s2=int(hmsf[2])

            d1=h1*3600+m1*60+s1
            d2=h2*3600+m2*60+s2
            if d2<d1:
                d2+=24*3600
            dur=(d2-d1)/60
            tmin+=dur
            
            tpay+=pay
            dist=float(info['trip_distance'])
            tdist+=dist

            peajes=float(info['tolls_amount'])
            tpeajes+=peajes

            psj = int(float(info['passenger_count']))
            cantpsj.append(psj)

            prop=float(info['tip_amount'])
            tprop+=prop

            dt=str(info["dropoff_datetime"].split()[0])
            dates.append(dt)
    
    
    if cnt==0:
        return None
    
    vistospsj={}
    for c in cantpsj:
        if c in vistospsj:
            vistospsj[c]+=1
        else:
            vistospsj[c]=1
    modepsj = str(max(vistospsj, key=vistospsj.get))
    cant_modepsj=str(vistospsj[modepsj])
    freq_pj = f"{modepsj} - {cant_modepsj}"
    vistosdt={}
    for d in dates:
        if d in vistosdt:
            vistosdt[d]+=1
        else:
            vistosdt[d]=1
    modedt = str(max(vistosdt, key=vistosdt.get))
 
    prom_min=tmin/cnt
    prompay=tpay/cnt
    promdist=tdist/cnt
    prompeaj=tpeajes/cnt
    promprop=tprop/cnt
    tf=get_time()
    tiempo=delta_time(tf,t0)
    return tiempo, prom_min, prompay, promdist, prompeaj, freq_pj, promprop, modedt




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

