from odoo import api, fields, models, _

class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"

    name = fields.Char(string="Name", required=True, tracking=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)


    def action_create_appointment(self):
        print(f"A new appointment has been created on {self.create_date} by {self.name} for the patient {self.patient_id}")