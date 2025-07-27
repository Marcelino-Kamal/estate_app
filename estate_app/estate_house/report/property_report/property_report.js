// Copyright (c) 2025, Marco and contributors
// For license information, please see license.txt

frappe.query_reports["Property Report"] = {
	"filters": [
		{
			"fieldname":"property",
			"label": __("Property Name"),
			"fieldtype": "Data",
			"width": 100,
			"reqd": 0,
		},
		{
			"fieldname":"from",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": 80,
			"reqd": 1,
			"default":frappe.datetime.year_start()
		},
		{
			"fieldname":"end",
			"label": __("End Date"),
			"fieldtype": "Date",
			"width": 80,
			"reqd": 1,
			"default":frappe.datetime.year_end()
		},
		{
			"fieldname":"agent",
			"label": __("Agent"),
			"fieldtype": "Link",
			"options":"Agent",
			"width": 100,
			"reqd": 0,
		},
		{
			"fieldname":"status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": ['','Sale','Rent','Lease'], 
			"width": 80,
			"reqd":0
		},
		
	]
};
