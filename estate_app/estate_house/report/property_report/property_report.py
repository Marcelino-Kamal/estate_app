# Copyright (c) 2025, Marco and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	return get_columns(), get_data(filters)

def get_data(filters):
	print(f"\n\n\n{filters}\n\n\n")
	return [{'name': '000001', 'type': 'Flat', 'status': 'Lease', 'agent_name': 'Marco Kamal', 'property_price': 12000000.0},
		  	{'name': '000002', 'type': 'House', 'status': 'Sale', 'agent_name': 'Sami Mohammed', 'property_price': 7000000.0},
		   	{'name': '000003', 'type': 'Flat', 'status': 'Sale', 'agent_name': 'Marco Kamal', 'property_price': 1000000.0}, 
			{'name': '000004', 'type': 'House', 'status': 'Rent', 'agent_name': None, 'property_price': 1900000.0}, 
			{'name': '000006', 'type': 'House', 'status': 'Rent', 'agent_name': 'Sami Mohammed', 'property_price': 750000000.0}, 
			{'name': '000007', 'type': 'Villa', 'status': 'Rent', 'agent_name': 'Marco Kamal', 'property_price': 150000000.0}, 
			{'name': '000008', 'type': 'Villa', 'status': 'Lease', 'agent_name': 'Sami Mohammed', 'property_price': 6000000.0},
			{'name': '000009', 'type': 'Villa', 'status': 'Rent', 'agent_name': 'Marco Kamal', 'property_price': 150000000.0}, 
			{'name': '000012', 'type': 'Condo', 'status': 'Sale', 'agent_name': 'Marco Kamal', 'property_price': 12000000.0},
			{'name': '000013', 'type': 'Deluxe', 'status': 'Lease', 'agent_name': 'Marco Kamal', 'property_price': 90000.0}
		]



def get_columns():
	return [
		 "Name:Link/Property:200",
		 "Type:Data:200"
		 "Status:Data:200",
		 "Agent name:Data:200",
		 "Property Price:Data:200"
		 	
	]