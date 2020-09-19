from odoo import models, fields


class SerialNumber(models.Model):
    _name = "serial.number"

    name = fields.Char(string="Name")
    description = fields.Char(string="Description")