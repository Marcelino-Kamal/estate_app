import frappe
from estate_app.blockh.doctype.product.blockhapi import getProductById,getProducts


def save_product(data):
		isExist = frappe.get_all("Product",filters={"product_code":data["code"]},limit=1)
		if isExist:
			frappe.msgprint("Item Exists")
		else:
			doc = frappe.new_doc("Product")
			
		doc.id = data["id"]
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
		
		doc.insert(ignore_permissions=True)
		frappe.db.commit()
		return {"docname":doc.name}

@frappe.whitelist()
def sync_by_id(id):
	result = getProductById(id)
	return save_product(result)

@frappe.whitelist()
def sync_all():
	products=getProducts()
	inserted=[]
	for data in products:
		res = save_product(data)
		inserted.append(res["docname"])
	return  {
        "message": f"{len(inserted)} products synced successfully.",
        "products": inserted
    }
	
   
	