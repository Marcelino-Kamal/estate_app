// Copyright (c) 2025, Marco and contributors
// For license information, please see license.txt

frappe.ui.form.on("Product", {
	refresh(frm) {
        frm.add_custom_button('Get Product',()=>{
			frappe.prompt([
				{
					label: "product id",
					fieldname: "id",
					fieldtype:"Int",
					reqd:1
				}
			],(values)=>{
				frappe.call({
					method:'estate_app.blockh.doctype.product.services.sync_by_id',
					args:{id: values.id},
					callback:function(r){
						if(!r.exc){
							frappe.msgprint('Product Has Arrived yay!!')
						}
					}

				});
			},"Enter Product ID");
		});
		frm.add_custom_button("Get ALL Products",()=>{
			frappe.call({
				method:'estate_app.blockh.doctype.product.services.sync_all',
				callback: function(r){
					if(!r.exc){
						frappe.msgprint("Huge Products incoming TAKE CARE!!!!")
					}else{
						frappe.throw("Something aint right")
					}
				}
			})
		})
	},
});
