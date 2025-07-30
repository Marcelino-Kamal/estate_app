# Copyright (c) 2025, Marco and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from estate_app.blockh.doctype.product.blockhapi import getProductById,getProducts


class Product(Document):
    
	@staticmethod
	@frappe.whitelist()
	def sync_by_id(id):
		result = getProductById(id)
		return Product.save_product(result)
	
	# @staticmethod
	# @frappe.whitelist()
	# def sync_all():
	# 	result = getProducts()
	# 	return Product.save_product(result)
	
	@staticmethod
	def save_product(data):

		isExist = frappe.get_all("Product",filters={"product_code":data["code"]},limit=1)
		if isExist:
			doc = frappe.get_doc("Product",isExist[0].product_code)
		else:
			doc = frappe.new_doc("Product")
		
		doc.product_code = data["code"]
		doc.product_name = data["name"]
		doc.department_name = data["departmentName"]
		doc.uom = data["unitName"]
		doc.hasexpiry= data["hasExpiry"]
		doc.isproduction= data["isProduction"]
		doc.issaleable = data["isSaleable"]
		doc.isrecipe = data["isRecipe"]
		doc.allowdiscount = data["allowDiscount"]
		doc.isactive = data["isActive"]
		doc.notes=data["notes"]
		doc.cost_price=data["costPrice"]
		doc.avg_cost=data["averageCost"]
		doc.sales_price = data["salesPrice"]
		doc.stock_on_hand = data["stockOnHand"]
		doc.base_quantity = data["baseQuantity"]
		doc.min_stock = data["minStock"]
		doc.max_stock = data["maxStock"]
		
		doc.save(ignore_permissions=True)
		frappe.db.commit()
		return {"docname":doc.name}

	

	
