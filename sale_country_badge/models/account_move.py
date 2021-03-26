from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    country = fields.Char(readonly=True)

    def write(self, values):
        if values.get('state') == 'posted':
            for rec in self:
                rec.country = rec.partner_id.country_id.name
        return super(AccountMove, self).write(values)
