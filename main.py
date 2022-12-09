#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import *
from datos import Arquivo
from publicador import Info
import logging
import schedule
from time import sleep
from datetime import date, timedelta

# Nivel de log
log_level = logging.INFO

logging.basicConfig(
    level=log_level,
    datefmt='%d/%m/%Y %H:%M:%S',
    format='[%(asctime)s] <%(levelname)s> %(message)s'
)

def gardardatos():
    arquivo = Arquivo()
    arquivo.acatualizaBD()

def publicacion():
    hoxe = date.today()
    datos = Arquivo.selectBD(hoxe)
    if datos is not None:
        info = Info(datos)
        info.ComprobaHora()
    else:
        logging.info("Descargamos os datos")
        gardardatos()
        publicacion()

def publicacion_resumo_diario():
    hoxe = date.today()
    datos = Arquivo.selectBD(hoxe)
    info = Info(datos)
    tweet = info.CreaResumoDiario()
    if tweet is not None:
        logging.info("procedemos a publicar o resumo diario")
        info.PublicaEstado(tweet)
    else:
        logging.error("Non se puido publicar o resumo diario porque non había datos suficientes")
    
def publicacion_resumo_semanal():
    onte = date.today() - timedelta(days=1)
    datos_onte = Arquivo.selectBD(onte)
    info = Info(datos_onte)
    tweet = info.CreaResumoSemanal()
    if tweet is not None:
        logging.info("Procedemos a publicar o resumo semanal")
        info.PublicaEstado(tweet)
    else:
        logging.error("Non se puido publicar o resumo semanal porque non había datos suficientes")

if __name__ == '__main__':
    logging.info("Programa iniciado")
    if TWITTER:
        logging.info("Twitter habilitado")
    if MASTODON:
        logging.info("Mastodon habilitado")
    publicacion()
    schedule.every().minute.do(publicacion)
    schedule.every().day.at(HORA_DESCARGA).do(gardardatos)
    schedule.every().day.at(HORA_RESUMO_DIARIO).do(publicacion_resumo_diario)
    schedule.every().friday.at(HORA_RESUMO_SEMANAL).do(publicacion_resumo_semanal)
    while True:
        schedule.run_pending()
        sleep(1)