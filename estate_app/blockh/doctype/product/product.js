// Copyright (c) 2025, Marco and contributors
// For license information, please see license.txt

frappe.ui.form.on("Product", {
	refresh(frm) {
        frm.add_custom_button('Get Product');
	},
});
