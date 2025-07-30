import requests
import frappe

@frappe.whitelist()
def getPropertyType(type):
    return frappe.db.sql("""SELECT name,type FROM tabProperty WHERE type = %s""",
                         (type),
                         as_dict=True)

@frappe.whitelist()
def fetch_from_sami():
    try:
        reponse = requests.get('https://60059fcde713.ngrok-free.app/api/Products/6')
        if reponse.status_code == 200:
            data = reponse.json()
            frappe.msgprint(f"Hello this data: {data}")
            return data
        else:
            frappe.throw("Failed to Fetch data")
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "API Fetch Error")
        frappe.throw("Something went wrong while fetching data.")

@frappe.whitelist(allow_guest=True)
def get_property(name):
    return frappe.get_doc("Property", name).as_dict()