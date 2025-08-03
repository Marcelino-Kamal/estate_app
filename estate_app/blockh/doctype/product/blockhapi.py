import requests
import frappe


frappe.whitelist()
def getProductById(id):
    try:
        response = requests.get(f"https://233cc35d62c4.ngrok-free.app/api/Products/{id}",timeout=5)
        if response.status_code ==200:
            data = response.json()
            return data
        else:
            frappe.throw("Failed to Fetch product")
    except Exception as e:
        frappe.log_error(f"{frappe.get_traceback()}\nError: {str(e)}", "API Fetch Error")
        frappe.throw("Internal Server error")

frappe.whitelist()
def getProducts():
    try:
        response = requests.get(f"https://c2977c8a684b.ngrok-free.app/api/Products")
        if response.status_code ==200:
            data = response.json()
            frappe.msgprint("Data Received successfully")
            return data
        else:
            frappe.throw("Failed to Fetch products")
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "API Fetch Error")
        frappe.throw("Internal Server error")

