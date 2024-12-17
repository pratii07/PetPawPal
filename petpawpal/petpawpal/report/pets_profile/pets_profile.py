# # Copyright (c) 2024, PAS and contributors
# # For license information, please see license.txt

# # import frappe


import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters) 
    # summary = get_summary()
    message = get_message()
    chart = get_chart(data)
    return  columns,data,message,chart

def get_columns():
    return [
        {
            "fieldname": "pet_name",
            "label": _("Pet Name"),
            "fieldtype": "Link",
            "options": "Pet Profiles Management",
            "width": 180
        },
        {
            "fieldname": "vet_name",
            "label": _("Vet Name"),
            "fieldtype": "Link",
            "options" : "Veterinarian",
            "width": 120
        },
        {
			"fieldname": "owner_name",
            "label": _("Owner Name"),
            "fieldtype": "data",
            "width": 120
		},
        {
			"fieldname": "status",
            "label": _("Status"),
            "fieldtype": "Select",
            "width": 120
		},
        {
			"fieldname": "category",
            "label": _("Category"),
            "fieldtype": "Link",
            "options" : "Pet Profiles Management",
            "width": 120
		},
        {
			"fieldname": "appointment_date",
            "label": _("Appointment Date"),
            "fieldtype": "Date",
            "width": 120
		}
    ]
# def get_summary():
#     data = frappe.db.sql("""
#         SELECT pet_name, owner_name, category
#         FROM `tabPet Profiles Management`
#     """, as_dict=True)
    
#     return [
#         {"label": "Total Pets", "value": len(data)},
#         {"label": "Unique Categories", "value": len(set(d['category'] for d in data))}
#     ]
def get_message():
    return "Your Pets, Our Passion."
    
def get_data(filters):

    return frappe.db.get_list(
        "Appointment Booking",
        filters=filters,
        fields=["name as pet_name", "vet_name","owner_name","status","category","appointment_date"]
    )
    
def get_chart(data):

    category_counts = {}
    for row in data:
        category = row.get("category", "Unknown")
        category_counts[category] = category_counts.get(category, 0) + 1

    
    labels = list(category_counts.keys())
    values = list(category_counts.values())

    return {
        "data": {
            "labels": labels,
            "datasets": [
                {
                    "name": "Appointments by Category",
                    "values": values
                }
            ]
        },
        "type": "pie",  
        "height": 300
    }
