from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    numberContract = fields.Char(string="Contract number")

    protections = fields.Selection(
        [("55", "Protection 55"),
         ("105", "Protection 105"),
         ("155", "Protection 155")],
        string="Protection")

    is_plan = fields.Boolean(string="Plan")
    is_prepaid = fields.Boolean(string="Prepaid")
    is_activation = fields.Boolean(string="Activation")