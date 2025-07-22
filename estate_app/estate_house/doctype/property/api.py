import frappe

@frappe.whitelist()
def getPropertyType(type):
    return frappe.db.sql("""SELECT name,type FROM tabProperty WHERE type = %s""",
                         (type),
                         as_dict=True)
