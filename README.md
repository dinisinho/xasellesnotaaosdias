# xasellenotaaosdias-tw
Bot de twitter escrito en python, que descarga diariamente os datos das horas de sol que fornece meteogalicia a través da súa API.

## Requeirmentos:

certifi==2021.10.8    
charset-normalizer==2.0.11  
idna==3.3     
oauthlib==3.2.0     
requests==2.27.1      
requests-oauthlib==1.3.1      
schedule==1.1.0     
tweepy==4.5.0     
urllib3==1.26.8     

## API MeteoSIX de Meteogalicia
Podes atopar a documentación desta API aquí: https://www.meteogalicia.gal/datosred/infoweb/meteo/proxectos/meteosix/API_MeteoSIX_v4_gl.pdf
Para utilizala é necesario unha clave, pero é gratuíta. Só é necesario enviar un correo a administracion-web.meteogalicia@xunta.gal solicitándoa.
Esta configuración débese incluír no ficheiro config.py

## API de Twitter
Utiliza a Api V2 de twitter con oauth1. É necesario obter os token de acceso en https://developer.twitter.com/.
Esta configuración débese incluír no ficheiro config.py

## Execución
Para a execución completa do programa executarase o ficheiro main.py, que crea un "bucle infinito" e utiliza schedule para a execución puntual das diferentes funcións que crean os tweets.

## datos.py
A clase Arquivo é a encargada de descargar os datos e gardalos na base de datos. Tamén a que nos facilita os datos cando os queremos consultar.

## tweeter.py
A clase Info é a que se encarga de crear os tweets e publicalos. Nela realízase tamén a comprobación de se é hora de publicar o tweet do nacemento, do mediodía ou do pór do sol.

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
