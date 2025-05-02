from odoo import models, fields

class HelloWorld(models.Model):
    _name = 'hello.world'
    _description = 'Hello World Model'

    name = fields.Char(string='Mesaj', default="Merhaba Dünya")
