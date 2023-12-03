import pandas as pd
import os
from re import sub
from typing import Optional, List, Dict, Any

def get_data(file_name : str) -> Dict:
    """
    Extract data from csv
    Parameters:
        file_name (str): An instance of a Client class for Shimoku API interactions.
    """
    dict_dfs = dict()
    df = pd.read_csv(file_name)

    # Encuentra las columnas que contienen "_fecha" en su nombre
    columnas_fecha = [col for col in df.columns if "fecha_" in col]

    # Convierte las columnas identificadas con "_fecha" a datetime
    df[columnas_fecha] = df[columnas_fecha].apply(pd.to_datetime)

    dict_dfs[os.path.splitext(os.path.basename(file_name))[0]] = df

    return dict_dfs

def convert_dataframe_to_array(df : pd.DataFrame) -> List[Dict]:
    columns_to_include = df.columns.tolist()
    new_data = []

    for __, row in df.iterrows():
        new_dict = {column: row[column] for column in columns_to_include}
        new_data.append(new_dict)

    return new_data

def beautiful_indicator(title : str, background_url : str, href : str) -> str:
    title_style: str = sub(r"\s+", "", title)
    return (
        f"<head>"
        f"<style>.{title_style}{{height:121px; width:100%; border-radius:8px; padding:45px; background-position: center; background-size: cover; background-image: url('{background_url}'); color:#FFFFFF;}}</style>"
        f"</head>"
        f"<a href='{href}'>"
        f"<div class='{title_style}'>"
        f"<h3>"
        f"{title}"
        f"</h3>"
        f"</div>"
        f"</a>"
    )

def get_kpi_total_sales(df_ventas : pd.DataFrame) -> List[Dict]:
        year = df_ventas["fecha_comercial"][0].year
        day_init = df_ventas["fecha_comercial"][0].strftime("%d/%m")
        day_end = df_ventas["fecha_comercial"][len(df_ventas["fecha_comercial"])-1].strftime("%d/%m")
        total_amount = df_ventas["imp_vta"].sum()
        main_kpis = [
            {
                "color": "success",
                "variant": "contained",
                "title": f"Ingresos {year}",
                "description": f"{day_init} - {day_end}",
                "value": f"{total_amount/1000000:.2f} M",
                "align": "center",
            }
        ]
        return main_kpis, total_amount

def get_kpi_total_sales_by_brand(df_ventas : pd.DataFrame, df_productos : pd.DataFrame, total_amount : int, main_kpis : List[Dict]) -> List[Dict]:
        percentages = get_brand_revenue_percentage(df_ventas, df_productos,total_amount)
        for brand, percentage in percentages.items():
            main_kpis.append({
                "color": "caution",
                "variant": "contained",
                "title": "Ingresos por marca",
                "description": brand,
                "value": percentage,
                "align": "center",
            })
        return main_kpis

def get_brand_revenue_percentage(df_ventas : pd.DataFrame, df_productos : pd.DataFrame, total_amount : int) -> Dict:
    marcas = pd.unique(df_productos["marca"])
    res={}
    for marca in marcas:
        codes = list(df_productos[df_productos["marca"] == marca]["codigo_barras"])
        sum = 0
        for code in codes:
            sum = sum + df_ventas["imp_vta"][df_ventas["codigo_barras"] == code].sum()
        res[marca] = f"{100*(sum/total_amount):.2f} %"
    
    return res

def get_products_sold_at_pdv(df_vent : pd.DataFrame, df_prod: pd.DataFrame) -> pd.DataFrame:
    codigo_barra_de_productos = df_prod['codigo_barras']
    nomb_prod = df_prod['descripcion']
    num_pdv_unique = len( pd.unique( df_vent['pdv_codigo'] ) )

    porcentaje_pdv_por_prod = []
    for codigo_barra in codigo_barra_de_productos:
        # Filtramos las ventas por codigo de barrar de los producto
        # Luego obtenemos el numero de pdv que tiene ese producto
        df_vent_filter_prod = df_vent.loc[ df_vent['codigo_barras'] == codigo_barra ]
        num_pdv_unique_por_prod = len( pd.unique(df_vent_filter_prod['pdv_codigo']) )

        # Evaluando el porcentaje
        porcentaje = 100 * num_pdv_unique_por_prod/num_pdv_unique
        porcentaje_pdv_por_prod.append( porcentaje )

    data = pd.concat([nomb_prod,pd.Series(porcentaje_pdv_por_prod)],axis=1)
    data.columns = ["producto","porcentaje"]
    return data

def get_moth_and_year_from_date(df_ventas : pd.DataFrame): 
    df_ventas['moth_and_year'] = df_ventas['fecha_comercial'].apply(lambda x: x.strftime('%m-%Y'))
    return pd.unique(df_ventas['moth_and_year'])

def get_monthly_sales_by_product_code(df_ventas : pd.DataFrame, monthly , product_code : str) -> List[Dict]:
    data = []
    for month in monthly:
        total_sales_for_the_month = df_ventas[(df_ventas['codigo_barras'] == product_code) & (df_ventas['moth_and_year'] == month)]['imp_vta'].sum()
        data.append({'moth_and_year': month, 'ventas': total_sales_for_the_month})
    return data