import requests
import frappe


frappe.whitelist()
def getProductById(id):
    try:
        response = requests.get(f"https://60059fcde713.ngrok-free.app/api/Products/{id}")
        if response.status_code ==200:
            data = response.json()
            frappe.msgprint("Data Received successfully")
            return data
        else:
            frappe.throw("Failed to Fetch product")
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "API Fetch Error")
        frappe.throw("Internal Server error")

frappe.whitelist()
def getProducts():
    try:
        response = requests.get(f"https://60059fcde713.ngrok-free.app/api/Products/")
        if response.status_code ==200:
            data = response.json()
            frappe.msgprint("Data Received successfully")
            return data
        else:
            frappe.throw("Failed to Fetch products")
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "API Fetch Error")
        frappe.throw("Internal Server error")

