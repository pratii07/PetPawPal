# Copyright (c) 2024, PAS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class AppointmentBooking(Document):
    # pass

	def before_submit(self):
		exists = frappe.db.exists("Appointment Booking",{
					"appointment_date": self.appointment_date,
					"docstatus": 1,
				},)
		if exists:
			frappe.throw(f"The vet is already booked for {self.appointment_date}. Please select another date or time.")

		
	def on_update(self):

		if self.status == "confirmed" and self.docstatus == 0:
			self.submit() 
			frappe.msgprint("APPONTMENT BOOKED 🌻🌻") 
        
	def before_save(self):
     		
		if not self.fees :
			self.fees = frappe.db.get_singles_value("Set Default Value","default_fees")

	# def before_save(self):
		if len(self.phone) != 10:
			frappe.throw("Galat number dale ho be")
        
# def throw_emogi(doc,event):
# 	frappe.throw("G🌼🌼D M🌼RN🌻NG")
