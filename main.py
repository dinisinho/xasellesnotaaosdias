#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import *
from datos import Arquivo
from twitter import Info
import logging
import schedule
from time import sleep
from datetime import date

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

def chio():
    hoxe = date.today()
    datos = Arquivo.selectBD(hoxe)
    if datos is not None:
        info = Info(datos)
        info.ComprobaHora()
    else:
        logging.info("Descargamos os datos")
        gardardatos()
        chio()

def chio_resumo():
    hoxe = date.today()
    datos = Arquivo.selectBD(hoxe)
    info = Info(datos)
    tweet = info.CreaResumo()
    info.PublicaEstado(tweet)

if __name__ == '__main__':
    logging.info("Programa iniciado")
    chio()
    schedule.every().minute.do(chio)
    schedule.every().day.at(HORA_DESCARGA).do(gardardatos)
    schedule.every().day.at(HORA_RESUMO).do(chio_resumo)
    while True:
        schedule.run_pending()
        sleep(1)