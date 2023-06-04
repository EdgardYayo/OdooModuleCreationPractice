from odoo import api, fields, models, _


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = "mail.thread"
    _description = "Doctor Records"
    # Con _rec_name cambiamos el record que se muestra por defecto en este caso seria la ref
    # _rec_name = "ref"

    name = fields.Char(string="Name", required=True, tracking=True)
    gender = fields.Selection([('male','Male'), ('female', 'Female'), ('others', 'Others')], string="Gender", tracking=True)

    ref = fields.Char(string="Reference", required=True)
    active = fields.Boolean(default=True)


    def name_get(self):
        res = []
        for rec in self:
            name = f'{rec.ref} - {rec.name}'
            res.append((rec.id, name))
        return res