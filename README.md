
## Instalacion

Para la instalacion de este proyecto se requiere **Python +3.9**

* Crear un entorno virtual ```python3 -m venv venv```
* Activar el entorno virtual  ```venv\Scripts\activate ```(Windows),  ```source venv/bin/activate```(Mac o Linux)
* Instalamos el SDK : ```pip install shimoku-api-python```

Con fin de utilizar el playground para el desarrollo de este proyecto se utilizo siguiente set-up:

* MAC M1
* python 3.11

OBS : Si estas trabajando de Windows, el playgraund de Shimaku presentara un error , **uvloop~=0.19.0** no es compatiple con este S.O .Sin embargo se podra deploya la solucion agregando las credenciales **access_token, universe_id y workspace_id**, para obtenerlas debes hacer login en https://shimoku.io/

# Sobre el proyecto
Se dispone de información de venta de productos de la categoría Aguas Saborizadas para los meses de 
junio a noviembre de 2020. 

* **productos.csv** este archivo contiene el listado de los productos de aguas saborizadas con sus respectivos codigos.
* **ventas.csv** este archivo contiene el detalle de los productos vendidos en el ultimo semeste del año 2020, se tiene la informacion de la cantidad de productos vendidos , el codigo de los puntos de venta que los vendieron (PDV), etc.

Con estos datos elaboraremos un DataApp que consta de 4 secciones: header, kpi_indicators, ranking_products_in_more_pdv, monthly_sales_by_product.

![envio de leads drawio](https://github.com/edwinml148/Reto-Shimoku/blob/develop/img/Data%20App.jpg)

## Header

## kpi indicators

## Ranking products in more pdv

## Monthly sales by produc





