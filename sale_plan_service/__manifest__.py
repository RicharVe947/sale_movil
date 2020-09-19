# -*- coding: utf-8 -*-Crear:Líneas del pedido    serialNumber_id = fields.One2many(related="serial.number",string="Serial number")

{
    'name': "Sale plan service",
    'summary': """
        Agrega los complementos para poder realizar ventas prepago, plan
        y activación de servicios
    """,
    'description': """
        Agrega los complementos para poder realizar ventas prepago, plan y 
        activación de servicios en los pedidos de ventas
    """,
    'author': "Ricardo Valencia",
    'category': 'Sales',
    'version': '0.1',
    'depends': ['sale'],
    'data': [
        "data/product_category.xml",
        "security/ir.model.access.csv",
        "views/sale_order.xml",
        "report/sale_order_report.xml"
    ],
}
