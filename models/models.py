# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class real_estate_training(models.Model):
#     _name = 'real_estate_training.real_estate_training'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100