# Copyright (c) 2025, Marco and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Property(Document):
   def after_insert(self):
       frappe.msgprint(msg="Successfully added to database",title="Success",indicator='green')
   def on_update(self):
       frappe.msgprint(msg="Successfully Updated to database",title="Success",indicator='green')
       
	#Validate
   def validate(self):
        if self.type == "Flat":
            ##Check in real-time the inputs
            for row in self.get("amenities"):
                if row.amenity == "Outdoor Kitchens":
                    frappe.throw(
                        title='Error',
                        msg=f"Property of type: <b>{self.type}</b> can't have: <b>{row.amenity}</b>"
                    )
         
         #Sql
            # amenity = frappe.db.sql(
            #     """
            #     SELECT amenity  
            #     FROM `tabProperty Amenity Details` 
            #     WHERE parent=%s AND parenttype='Property' AND amenity='Outdoor Kitchens'
            #     """, 
            #     (self.name,), 
            #     as_dict=True
            # )
            
            # if(amenity):
            #     frappe.throw(title='Error',
            #                      msg=f"Property of type: <b>{self.type}</b> can't have : <b>{amenity[0].amenity}</b>")
                
          #  for x in self.amenities:
          #      if(x.amenity == "Outdoor Kitchens"):
          #          frappe.throw(title='Error',
          #                       msg=f"Property of type: <b>{self.type}</b> can't have : <b>{x.amenity}</b>")


def after_insert(self):
       frappe.msgprint(msg="Successfully added to datbase",title="Success",indicator='green')
       
            
                