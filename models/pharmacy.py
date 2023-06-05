from odoo import api, fields, models, _


class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.line"
    _description = "Appointment Pharmacy Lines"

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related="product_id.list_price")
    qty = fields.Integer(string="Quantity", default="1")
    patient_id = fields.Many2one('hospital.patient', string="Patient")