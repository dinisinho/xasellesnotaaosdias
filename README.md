# xasellenotaaosdias
Bot de twitter e mastodon escrito en python, que descarga diariamente os datos das horas de sol que fornece meteogalicia a través da súa API.

## Requerimentos:

[requirements.txt](requirements.txt)

## API MeteoSIX de Meteogalicia
Podes atopar a documentación desta API aquí: https://www.meteogalicia.gal/datosred/infoweb/meteo/proxectos/meteosix/API_MeteoSIX_v4_gl.pdf
Para utilizala é necesario unha clave, pero é gratuíta. Só é necesario enviar un correo a administracion-web.meteogalicia@xunta.gal solicitándoa.
Esta configuración débese incluír no ficheiro [de configuración](config.py)

## API de Twitter
Utiliza a Api V2 de twitter con oauth1. É necesario obter os token de acceso en https://developer.twitter.com/.

## API de Mastodon
A través do módulo de python Mastodon utiliza a API de Mastodon para facer as publicacións.

## Execución
Para a execución completa do programa executarase o ficheiro main.py, que crea un "bucle infinito" e utiliza schedule para a execución puntual das diferentes funcións que crean os tweets.

## datos.py
A clase Arquivo é a encargada de descargar os datos e gardalos na base de datos. Tamén a que nos facilita os datos cando os queremos consultar.

## publicador.py
A clase Info é a que se encarga de crear os tweets e os toots e publicalos. Nela realízase tamén a comprobación de se é hora de publicar o tweet do nacemento, do mediodía ou do pór do sol.

## Base de datos
Utilízase unha base de datos sqlite. O lugar no que se almacene hai que indicálo no parámetro BD do ficheiro de configuración.
É necesario crear a seguinte táboa:
```sql
CREATE TABLE "pordosol" (
	"dia"	TEXT NOT NULL,
	"amencer"	TEXT NOT NULL,
	"mediodia"	TEXT NOT NULL,
	"anoitecer"	TEXT NOT NULL,
	"duracion"	TEXT NOT NULL,
	PRIMARY KEY("dia")
)
```
## Instalación (docker):

### Construír a imaxe:

```bash
    docker build -t xasellesnotaaosdias-imaxe .
```

### Contedor con opcións de exemplo
```bash
    docker run -d --name xasellesnotaaosdias-contedor  -e MGZ_TOKEN='XXXXXXX' -e TWITTER=true -e T_CONSUMER_KEY='XXXXX' -e T_CONSUMER_SECRET='XXXXX' -e T_ACCESS_KEY='XXXXX' -e T_ACCESS_SECRET='XXXXX'  xasellesnotaaosdias-imaxe


### Variábeis que acepta
```
TWITTER : true/false # Se queremos habilitar a publicación en twitter. Por defecto false
MASTODON: true/false #Se queremos habilitar a publicación en mastodon. Por defecto false
TW_BEAREN_TOKEN : Bearen Token de Twitter # Obrigatorio se temos twitter habilitado
TW_API_KEY : Api Key de Twitter # Obrigatorio se temos twitter habilitado
TW_API_KEY_SECRET : Api Key Secret de Twitter # Obrigatorio se temos twitter habilitado
TW_ACCESS_TOKEN : Access Token de Twitter # Obrigatorio se temos twitter habilitado
TW_ACCESS_TOKEN_SECRET : Access Token Secret de Twitter # Obrigatorio se temos twitter habilitado
M_ACCESS_TOKEN : Access token de Mastodon # Obrigatorio se temos mastodon habilitado
M_API_BASE_URL : Url da instancia de Mastodon. # Por defecto https://bots.automatica.dev
DB : Ruta ao ficheiro que contén os datos. # Por defecto data/datos.db
MGZ_TOKEN : Token para acceder á URL de Meteogaliza.  # Obrigatorio
MGZ_URL : Url de metegaliza. # Por defecto https://servizos.meteogalicia.gal/apiv4/getSolarInfo
MGZ_LOCATIONID : Id da localización dos datos de Meteogaliza. # Por defecto 42985 (Arzúa)
HORA_DESCARGA : Hora á que queremos que se faga a descarga dos datos. # Por defecto 00:00
HORA_RESUMO_DIARIO : Hora á que queremos que se publique o resumo diario. # Por defecto 22:45
HORA_RESUMO_SEMANAL : Hora á que queremos que se faga o resumo semanal. # Por defecto 12:15
```
