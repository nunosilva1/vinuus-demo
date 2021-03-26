from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    country = fields.Char(readonly=True)

    def write(self, values):
        if values.get('state') == 'sent':
            for rec in self:
                rec.country = rec.partner_id.country_id.name
        return super(SaleOrder, self).write(values)
