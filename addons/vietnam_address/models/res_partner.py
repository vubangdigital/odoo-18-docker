from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    province_id = fields.Many2one('res.country.province',
                                  string='Province/City',
                                  )

    ward_id = fields.Many2one(
        'res.country.ward',
        string='Ward',
        domain="[('province_id', '=', province_id)]"
    )

    @api.onchange('province_id')
    def _onchange_province_id(self):
        if self.province_id:
            self.state_id = self.province_id.state_id
            self.country_id = self.province_id.country_id

    @api.onchange('ward_id')
    def _onchange_ward_id(self):
        if self.ward_id and self.province_id:
            self.city = f"{self.ward_id.name}, {self.province_id.name}"



