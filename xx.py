# import frappe
# from frappe.model.document import Document
# from frappe.utils import nowdate, add_months

# @frappe.whitelist(allow_guest=True)
# def create_quotation():
#     quotation = frappe.new_doc("Quotation")

#     values = {
#         "quotation_to": "Customer",
#         "order_type": "Shopping Cart",
#         "party_name": frappe.get_value("Party", {"email": frappe.session.user}, "name"),
#         "docstatus": 0,
#         "contact_email": frappe.session.user,
#         "selling_price_list": "_Test Price List Rest of the World",
#         "currency": "USD",
#         "taxes_and_charges": "UAE VAT 5% - AG",
#         "conversion_rate": 1,
#         "transaction_date": nowdate(),
#         "valid_till": add_months(nowdate(), 1),
#         "items": [{"item_code": "_Test Item", "qty": 1}],
#         "taxes": frappe.get_doc("Sales Taxes and Charges Template", "UAE VAT 5% - AG").taxes,
#         "company": "Al Khateeb Global General Trading LLC",
#     }

#     quotation.update(values)

#     quotation.insert(ignore_permissions=True)

#     return quotation


# import frappe
# from frappe.model.document import Document
# from frappe.utils import nowdate, add_months

# @frappe.whitelist(allow_guest=True)
# def create_quotation():
#     # Create a new Quotation document
#     quotation = frappe.new_doc("Quotation")

#     # Set values for the Quotation document
#     values = {
#         "quotation_to": "Customer",
#         "order_type": "Shopping Cart",
#         "party_name": frappe.get_value("Party", {"email": frappe.session.user}, "name"),
#         "docstatus": 0,
#         "contact_email": frappe.session.user,
#         "selling_price_list": "Standard Buying",
#         "currency": "USD",
#         "taxes_and_charges": "UAE VAT 5% - AG",
#         "conversion_rate": 1,
#         "transaction_date": nowdate(),
#         "valid_till": add_months(nowdate(), 1),
#         "items": [{"item_code": "_Test Item", "qty": 1}],
#         "taxes": frappe.get_doc("Sales Taxes and Charges Template", "UAE VAT 5% - AG").taxes,
#         "company": "Al Khateeb Global General Trading LLC",
#     }

#     # Update the Quotation document with values
#     quotation.update(values)

#     # Insert the Quotation document
#     quotation.insert(ignore_permissions=True)

#     # Return the created Quotation
#     return quotation.name




import frappe
from frappe.tests.utils import change_settings
from frappe.utils import add_months, cint, nowdate

from erpnext.accounts.doctype.tax_rule.tax_rule import ConflictingTaxRule
from erpnext.e_commerce.doctype.website_item.website_item import make_website_item
from erpnext.e_commerce.shopping_cart.cart import (
	_get_cart_quotation,
	get_cart_quotation,
	get_party,
	request_for_quotation,
	update_cart,
)
@frappe.whitelist(allow_guest=True)
def create_quotation():
		quotation = frappe.new_doc("Quotation")

		values = {
			"doctype": "Quotation",
			"quotation_to": "Customer",
			"order_type": "Shopping Cart",
			"party_name": get_party(frappe.session.user).name,
			"docstatus": 0,
			"contact_email": frappe.session.user,
			"selling_price_list": "Standard Buying",
			"currency": "USD",
			"taxes_and_charges": "UAE VAT 5% - AG",
			"conversion_rate": 1,
			"transaction_date": nowdate(),
			"valid_till": add_months(nowdate(), 1),
			"items": [{"item_code": "CBK2020URSMNSAIR", "qty": 1}],
			"taxes": frappe.get_doc("Sales Taxes and Charges Template", "UAE VAT 5% - AG").taxes,
			"company": "Al Khateeb Global General Trading LLC",
		}

		quotation.update(values)

		quotation.insert(ignore_permissions=True)

		return quotation