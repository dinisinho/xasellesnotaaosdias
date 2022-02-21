# -*- coding: utf-8 -*-

from config import *
from datos import Arquivo
import logging
import tweepy
from datetime import datetime, date, timedelta

class Info():
    def __init__(self, datos):
        self.client = tweepy.Client(TW_BEAREN_TOKEN, TW_API_KEY, TW_API_KEY_SECRET, TW_ACCESS_TOKEN, TW_ACCESS_TOKEN_SECRET)
        self.hora = datetime.now().strftime("%H:%M")
        self.amencer = datos['amencer']
        self.mediodia = datos['mediodia']
        self.anoitecer = datos['anoitecer']
        self.duracion = datos['duracion']

    def ComprobaHora(self):
        if self.amencer == self.hora:
            texto = f"🌄 Bo día! Son as {self.hora} e acaba de nacer o sol."
            logging.info("Procedemos a publicar o chío do amencer")
            self.PublicaEstado(texto)
        elif self.mediodia == self.hora:
            texto=f"Boa tarde! Son as {self.hora}. Estamos na metade do día."
            logging.info("Procedemos a publicar o chío do mediodía")
            self.PublicaEstado(texto)
        elif self.anoitecer == self.hora:
            texto=f"🌇 Boa noite! Son as {self.hora} e acaba de pórse o sol."
            logging.info("Procedemos a publicar o chío do anoitecer")
            self.PublicaEstado(texto)
        else:
            logging.debug("Non é hora de publicar nada")

    def PublicaEstado(self, texto):
        try:
            self.client.create_tweet(text=texto)
            logging.info("Publicouse o chío")
        except Exception as e:
            logging.error("Produceuse un erro ao executar o chío")

    def converte_a_segundos(self, tempo):
        horas = int(tempo.split(':')[0])
        minutos = int(tempo.split(':')[1])
        return horas * 3600 + minutos * 60

    def converte_a_minutos(self, segundos):
        return int(segundos / 60)

    def CreaResumo(self):
        onte = date.today() - timedelta(days=1)
        datos_onte = Arquivo.selectBD(onte)
        texto_simple =  f"Hoxe naceu o sol ás {self.amencer} e púxose ás {self.anoitecer}. O día durou {self.duracion.split(':')[0]} horas e {self.duracion.split(':')[1]} minutos."
        if datos_onte is not None:
            resta_segundos = int(self.converte_a_segundos(self.duracion)) - int(self.converte_a_segundos(datos_onte['duracion']))
            resta = self.converte_a_minutos(resta_segundos)
            if resta == 0:
                texto = f"{texto_simple} Tivemos as mesmas horas de sol que onte."
            elif resta == 1:
                texto = f"{texto_simple} Medran os días. Tivemos {resta} minuto de luz máis que onte."
            elif resta == -1:
                texto = f"{texto_simple} Minguan os días. Tivemos {abs(resta)} minuto de luz menos que onte."
            elif resta > 1:
                texto = f"{texto_simple} Medran os días. Tivemos {resta} minutos de luz máis que onte."
            elif resta < -1:
                texto = f"{texto_simple} Minguan os días. Tivemos {abs(resta)} minutos de luz menos que onte."
        else:
            texto = texto_simple
        logging.info("Procedemos a publicar o resumo")
        return texto

if __name__ == '__main__':
    tweet = Info({'amencer': '09:03', 'mediodia': '13:37', 'anoitecer': '18:12', 'duracion': '10:1'})
    print(tweet.CreaResumo())
