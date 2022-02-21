# -*- coding: utf-8 -*-

from config import *
import logging
import requests
from datetime import datetime, date
import time
import json
import sqlite3

class Arquivo():
    def __init__(self):
        self.hoxe = date.today()

    def descargar(self):
        end_time = f"{self.hoxe}T23:59:59"

        url_params = {
            'API_KEY':MGZ_TOKEN,
            'locationIds':MGZ_LOCATIONID,
            'lang':'gl',
            'format':'application/json',
            'endTime':end_time
        }
        datos = requests.get(url = MGZ_URL, params = url_params)
        datos_json = json.loads(datos.content)
        for feature in datos_json['features']:
            for dia in feature['properties']['days']:
                for dato in dia['variables']:
                    amencer = dato['sunrise'][11:16]
                    mediodia = dato['midday'][11:16]
                    anoitecer = dato['sunset'][11:16]
                    duracion_time = time.strptime(dato['duration'], "%Hh %Mm")
                    duracion = f"{duracion_time.tm_hour}:{duracion_time.tm_min}"
        
        return {'amencer':amencer, 'mediodia':mediodia, 'anoitecer':anoitecer, 'duracion':duracion}

    def acatualizaBD(self):
        self.datos = self.descargar()
        self.datos['dia']=self.hoxe

        sql = "INSERT INTO pordosol VALUES(?,?,?,?,?)"

        try:
            conexion_bd = sqlite3.connect(DB)
            cursor = conexion_bd.cursor()
            cursor.execute(sql, (self.datos['dia'],self.datos['amencer'],self.datos['mediodia'],self.datos['anoitecer'],self.datos['duracion']))
            conexion_bd.commit()
            conexion_bd.close()
            logging.info(f"Gardáronse os datos do día {self.hoxe} na base de datos")
        except sqlite3.IntegrityError as e:
            logging.warning("Non se gardaron datos de hoxe porque xa están na base de datos")
        except Exception as e:
            logging.error("Erro ao gardar os datos na base de datos")

    def  selectBD(dia):
        sql = "SELECT * FROM pordosol WHERE dia=?;"
        conexion_bd = sqlite3.connect(DB)
        cursor = conexion_bd.cursor()
        cursor.execute(sql,[dia])
        data = cursor.fetchall()
        conexion_bd.close()

        for a in data:
            try:
                dict_datos = {'dia':a[0],'amencer':a[1],'mediodia':a[2],'anoitecer':a[3],'duracion':a[4]}
            except UnboundLocalError as e:
                logging.warning(f"Non hai datos para {dia} na base de datos")
                return

        try:
            return dict_datos
        except UnboundLocalError as e:
            logging.warning(f"Non hai datos para {dia} na base de datos")
            return

if __name__ == '__main__':
    dato = Arquivo()
    dato.acatualizaBD()