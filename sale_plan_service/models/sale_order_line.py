from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order.line"

    serialNumber = fields.Char(string="Serial Number")
