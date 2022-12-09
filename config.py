# -*- coding: utf-8 -*-

from os import getenv

#Configuración secrets para twitter
twitter = {
    'TW_BEAREN_TOKEN':'',
    'TW_API_KEY':'',
    'TW_API_KEY_SECRET':'',
    'TW_ACCESS_TOKEN':'',
    'TW_ACCESS_TOKEN_SECRET' : ''
}

mastodon = {
    'M_ACCESS_TOKEN':'',
    'M_API_BASE_URL':'https://bots.automatica.dev'
}

meteogaliza = {
    'MGZ_TOKEN':'',
    'MGZ_URL':'https://servizos.meteogalicia.gal/apiv4/getSolarInfo',
    'MGZ_LOCATIONID':'42985'
}

db = {
    'DB':'data/datos.db'
}

programacion = {
    'HORA_DESCARGA':'00:00',
    'HORA_RESUMO_DIARIO':'22:45',
    'HORA_RESUMO_SEMANAL':'12:15'
}

def carga():
    # TWITTER
    global TWITTER
    try:
        TWITTER = (getenv('TWITTER') == 'true')
    except:
        pass

    global TW_BEAREN_TOKEN
    try:
        TW_BEAREN_TOKEN = getenv("TW_BEAREN_TOKEN")
    except:
        pass

    global TW_API_KEY
    try:
        TW_API_KEY = getenv("TW_API_KEY")
    except:
        pass

    global TW_API_KEY_SECRET
    try:
        TW_API_KEY_SECRET = getenv("TW_API_KEY_SECRET")
    except:
        pass

    global TW_ACCESS_TOKEN
    try:
        TW_ACCESS_TOKEN = getenv("TW_ACCESS_TOKEN")
    except:
        pass

    global TW_ACCESS_TOKEN_SECRET
    try:
        TW_ACCESS_TOKEN_SECRET = getenv("TW_ACCESS_TOKEN_SECRET")
    except:
        pass

    # MASTODON 
    global MASTODON
    try:
        MASTODON = (getenv('MASTODON') == 'true')
    except:
        pass

    global M_ACCESS_TOKEN
    try:
        M_ACCESS_TOKEN = getenv("M_ACCESS_TOKEN")
    except:
        pass

    global M_API_BASE_URL
    try:
        M_API_BASE_URL = getenv("M_API_BASE_URL")
    except:
        pass

    # METEOGALIZA
    global MGZ_TOKEN
    try:
        MGZ_TOKEN = getenv("MGZ_TOKEN")
    except:
        pass

    global MGZ_URL
    try:
        MGZ_URL = getenv("MGZ_URL")
    except:
        pass

    global MGZ_LOCATIONID
    try:
        MGZ_LOCATIONID = getenv("MGZ_LOCATIONID")
    except:
        pass

    # BASE DE DATOS
    global DB
    try:
        DB = getenv("DB")
    except:
        pass

    # PROGRAMACIÓN
    global HORA_DESCARGA
    try:
        HORA_DESCARGA = getenv("HORA_DESCARGA")
    except:
        pass

    global HORA_RESUMO_DIARIO
    try:
        HORA_RESUMO_DIARIO = getenv("HORA_RESUMO_DIARIO")
    except:
        pass

    global HORA_RESUMO_SEMANAL
    try:
        HORA_RESUMO_SEMANAL = getenv("HORA_RESUMO_SEMANAL")
    except:
        pass

carga()

if TW_BEAREN_TOKEN is None:
    TW_BEAREN_TOKEN = twitter['TW_BEAREN_TOKEN']

if TW_API_KEY is None:
    TW_API_KEY = twitter['TW_API_KEY']

if TW_API_KEY_SECRET is None:
    TW_API_KEY_SECRET = twitter['TW_API_KEY_SECRET']

if TW_ACCESS_TOKEN is None:
    TW_ACCESS_TOKEN = twitter['TW_ACCESS_TOKEN']

if TW_ACCESS_TOKEN_SECRET is None:
    TW_ACCESS_TOKEN_SECRET = twitter['TW_ACCESS_TOKEN_SECRET']

if M_ACCESS_TOKEN is None:
    M_ACCESS_TOKEN = mastodon['M_ACCESS_TOKEN']

if M_API_BASE_URL is None:
    M_API_BASE_URL = mastodon['M_API_BASE_URL']

if MGZ_TOKEN is None:
    MGZ_TOKEN = meteogaliza['MGZ_TOKEN']

if MGZ_URL is None:
    MGZ_URL = meteogaliza['MGZ_URL']

if MGZ_LOCATIONID is None:
    MGZ_LOCATIONID = meteogaliza['MGZ_LOCATIONID']

if DB is None:
    DB = db['DB']

if HORA_DESCARGA is None:
    HORA_DESCARGA = programacion['HORA_DESCARGA']

if HORA_RESUMO_DIARIO is None:
    HORA_RESUMO_DIARIO = programacion['HORA_RESUMO_DIARIO']

if HORA_RESUMO_SEMANAL is None:
    HORA_RESUMO_SEMANAL = programacion['HORA_RESUMO_SEMANAL']