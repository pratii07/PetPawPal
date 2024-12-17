// Copyright (c) 2024, PAS and contributors
// For license information, please see license.txt

frappe.ui.form.on("Appointment Booking", {
	refresh(frm) {
        if(frm.doc.status == "Pending" && frm.doc.docstatus == 0){

            frm.add_custom_button("Approve",function(){
                frm.set_value('status', 'confirmed');
                frm.save();
            },"Action");

            frm.add_custom_button("Reject",function(){
                frm.set_value('status', 'Not Yet');
                frm.save();
            },"Action")
        }

	},
});
