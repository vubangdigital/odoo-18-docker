from odoo import models, fields


class Ward(models.Model):
    _name = 'res.country.ward'
    _description = 'ward'
    _order = 'name'

    code = fields.Char(string='Ward Code')
    name = fields.Char(string='Ward Name')
    slug = fields.Char(string='Slug')
    province_id = fields.Many2one('res.country.province', 'Province/City',
                               domain="[('country_id', '=', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', required=True)
    type = fields.Selection(selection=[
        ('0', 'Phường'),
        ('1', 'Xã')], string='Type')
