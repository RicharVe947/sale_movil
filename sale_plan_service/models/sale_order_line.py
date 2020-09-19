from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    activate = fields.Boolean(string="Activate")

    categ_id = fields.Char(related="product_id.product_tmpl_id.categ_id.name",
                           string="Type")

    numberContract = fields.Char(string="Contract")

    protections = fields.Selection(
        [("55", "Protection 55"),
         ("105", "Protection 105"),
         ("155", "Protection 155")],
        string="Protection")

    serialNumber_id = fields.Many2one("serial.number", string="No. Serial")
