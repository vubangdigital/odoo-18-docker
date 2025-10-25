from odoo import models, fields

class Lead2OpportunityPartner(models.TransientModel):
    _inherit = 'crm.lead2opportunity.partner'

    def _convert_handle_partner(self, lead, action, partner_id):
        """Ghi đè để thêm province_id, ward_id khi tạo liên hệ từ CRM"""
        if action == 'create':
            # Gửi thêm default vào context để khi partner được tạo, nó có 2 trường mới
            self = self.with_context(
                default_province_id=lead.province_id.id,
                default_ward_id=lead.ward_id.id,
            )
        return super(Lead2OpportunityPartner, self)._convert_handle_partner(lead, action, partner_id)
