# Copyright (c) 2025, Marco and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Agent(Document):
	def after_delete(self):
		frappe.msgprint(msg="Successfully removed to database",title="Deleted",indicator='red')
