from odoo import models, fields, api

class Lead(models.Model):
    _inherit = 'crm.lead'

    province_id = fields.Many2one(
        'res.country.province',
        string='Province/City'
    )

    ward_id = fields.Many2one(
        'res.country.ward',
        string='Ward',
    )

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.province_id = self.partner_id.province_id.id
            self.ward_id = self.partner_id.ward_id.id
            self.street = self.partner_id.street
        else:
            self.province_id = False
            self.ward_id = False
            self.street = False

    def _handle_partner_assignment(self, force_create=False, create_missing=False):
        """Tự động gán hoặc tạo partner khi từ CRM"""
        res = super()._handle_partner_assignment(force_create=force_create, create_missing=create_missing)

        for lead in self:
            if lead.partner_id:
                lead.partner_id.write({
                    'province_id': lead.province_id.id,
                    'ward_id': lead.ward_id.id,
                    'street': lead.street,
                })
        return res

    def _prepare_customer_values(self, partner_name, is_company=False, parent_id=False):
        """Kế thừa để thêm province_id và ward_id khi tạo mới partner từ lead"""
        res = super()._prepare_customer_values(partner_name, is_company=is_company, parent_id=parent_id)
        res.update({
            'province_id': self.province_id.id,
            'ward_id': self.ward_id.id,
            'street': self.street,
        })
        return res

    @api.model
    def write(self, vals):
        res = super().write(vals)
        for lead in self:
            if lead.partner_id:
                update_vals = {}
                if 'province_id' in vals:
                    update_vals['province_id'] = lead.province_id.id
                if 'ward_id' in vals:
                    update_vals['ward_id'] = lead.ward_id.id
                if 'street' in vals:
                    update_vals['street'] = lead.street
                if update_vals:
                    lead.partner_id.write(update_vals)
        return res
