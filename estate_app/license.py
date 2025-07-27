import frappe
from frappe import _
from frappe.utils import nowdate

def validate_license_on_login(login_manager):
    
    if frappe.session.user == "Administrator":
        return
    if not frappe.session.user or frappe.session.user in ("Guest",):
        return
    else:
        # Get the active license
        license_doc = frappe.get_all("License Config", filters={"active": 1}, limit=1)
        if not license_doc:
            frappe.throw(_("No active license found. Please contact your administrator."))

        license = frappe.get_doc("License Config", license_doc[0].name)

        # ✅ Check if license is expired
        if license.expire_date and nowdate() > str(license.expire_date):
            frappe.throw(_("License has expired on {0}. Please contact your provider.").format(license.expire_date))

        # ✅ Count active users (excluding Admin and Guest)
        active_users = frappe.get_all("User",
            filters={
                "enabled": 1,
                "user_type": "System User",
                "name": ["not in", ["Administrator", "Guest"]]
            },
            fields=["name"]
        )

        if len(active_users) > license.max_users:
            frappe.throw(_("User limit exceeded. Allowed: {0}, Found: {1}").format(license.max_users, len(active_users)))
