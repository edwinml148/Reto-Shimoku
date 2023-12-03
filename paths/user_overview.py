from board import Board
import pandas as pd
from utils.utils import (
    convert_dataframe_to_array,
    beautiful_indicator,
    get_products_sold_at_pdv,
    get_moth_and_year_from_date,
    get_monthly_sales_by_product_code,
    get_kpi_total_sales,
    get_kpi_total_sales_by_brand
)

class UserOverview(Board):
    """
    This path is responsible for rendering the user overview page.
    """

    def __init__(self, self_board: Board):
        """
        Initializes the HiddenIndicatorsPage with a shimoku client instance.

        Parameters:
            shimoku: An instance of the Shimoku client.
        """
        super().__init__(self_board.shimoku)

        self.order = 0  # Initialize order of plotting elements
        self.menu_path = "Aguas saborizadas"  # Set the menu path for this page
        self.shimoku.set_menu_path(name=self.menu_path)  # Set the menu path in Shimoku

    def plot(self) -> None:
        """
        Plots the Aguas saborizadas.
        Each method is responsible for plotting a specific section of the page.
        """
        self.plot_header()
        self.plot_kpi_indicators()
        self.plot_ranking_products_in_more_pdv() 
        self.plot_monthly_sales_by_product()

    def plot_header(self) -> bool:
        """
        Plots the header of the page.
        """
        title = "Scanntech"
        href = "https://docs.shimoku.com/development/charts/charts/html/background-indicators"
        background_url = "https://uploads-ssl.webflow.com/619f9fe98661d321dc3beec7/62a07a6d9e984908a5aca6a1_shim-anomaly-bg-s.jpg"


        indicator = beautiful_indicator(
            title=title, href=href, background_url=background_url
        )
        self.shimoku.plt.html(
            indicator,
            order=self.order,
            rows_size=1,
            cols_size=12,
        )
        self.order += 1
        
        return True

    def plot_kpi_indicators(self) -> bool:
        """
        Plot KPI indicators are the total amount of sales and the amount of sales in percentage by product brands.
        """
        main_kpis, total_amount = get_kpi_total_sales(self.dfs2['ventas'])
        main_kpis = get_kpi_total_sales_by_brand(self.dfs2["ventas"], self.dfs1["productos"], total_amount, main_kpis)
        main_kpis_df = pd.DataFrame(main_kpis)

        self.shimoku.plt.indicator(
            data=convert_dataframe_to_array(main_kpis_df),
            order=self.order,
            rows_size=1,
            cols_size=12
        )
        self.order += len(main_kpis_df) + 1

        return True

    def plot_monthly_sales_by_product(self) -> bool:
        """
        Plot monthly sales amount for each product, there are some products that have zero sales in the first months.
        """
        moth_year = get_moth_and_year_from_date(self.dfs2["ventas"])
        products = self.dfs1["productos"].loc[:, ["codigo_barras", "descripcion"]]
        products['descripcion'] = products['descripcion'].apply(lambda x: x[16:])

        for i in products.index:
            if i == 0:
                self.shimoku.plt.set_tabs_index(
                    ("Products", products['descripcion'][i]),
                    order=self.order,
                    cols_size=12,
                    rows_size=1,
                    padding="0,1,2,1",
                )
            else:
                self.shimoku.plt.change_current_tab(products['descripcion'][i])
            data = get_monthly_sales_by_product_code(self.dfs2["ventas"], moth_year, products['codigo_barras'][i])
            self.shimoku.plt.bar(data=data, order=self.order, x='moth_and_year',rows_size=2,padding="0,0,1,0")
            self.order += 1

        self.shimoku.plt.pop_out_of_tabs_group()

        return True
    
    def plot_ranking_products_in_more_pdv(self) -> bool:
        """
        Plot ranking of products offered at points of sale.
        """
        data = get_products_sold_at_pdv(self.dfs2["ventas"], self.dfs1["productos"])

        self.shimoku.plt.horizontal_bar(
            title="Ranking de productos ofrecidos por puntos de ventas",
            data=data.sort_values("porcentaje", ascending=True),
            x="producto",
            x_axis_name="Porcentaje",
            y_axis_name="Producto",
            order=self.order,
            rows_size=4,
            cols_size=12,
            padding='0,1,0,1'
        )
        self.order += 1

        return True
