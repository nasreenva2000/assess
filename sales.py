import frappe
from frappe import _
from frappe.utils import cint, cstr, flt, get_datetime, getdate, nowdate
from erpnext.accounts.doctype.tax_rule.tax_rule import ConflictingTaxRule
from ecommerce_integrations.shopify.connection import temp_shopify_session
from ecommerce_integrations.shopify.constants import (
    CUSTOMER_ID_FIELD,
    EVENT_MAPPER,
    ORDER_ID_FIELD,
    ORDER_ITEM_DISCOUNT_FIELD,
    ORDER_NUMBER_FIELD,
    ORDER_STATUS_FIELD,
    SETTING_DOCTYPE,
)
from ecommerce_integrations.shopify.customer import ShopifyCustomer
from ecommerce_integrations.shopify.product import create_items_if_not_exist, get_item_code
from ecommerce_integrations.shopify.utils import create_shopify_log
from ecommerce_integrations.utils.price_list import get_dummy_price_list
from ecommerce_integrations.utils.taxation import get_dummy_tax_category

DEFAULT_TAX_FIELDS = {
    "sales_tax": "default_sales_tax_account",
    "shipping": "default_shipping_charges_account",
}

@frappe.whitelist(allow_guest=True)
def create_sales_order():
    salesorder = frappe.new_doc("Sales Order")

    values = {
        "doctype": "Sales Order",
        "naming_series": "SAL-ORD-.YYYY.-",
        "customer": "jk",
        "transaction_date":nowdate(),
        "delivery_date": nowdate(),
        "company": "Al Khateeb Global General Trading LLC",
        "selling_price_list": "Standard Buying",
        "ignore_pricing_rule": 1,
        "items": [{"item_code": "CBK2020URSMNSAIR", "qty": 1}],
        "taxes": frappe.get_doc("Sales Taxes and Charges Template", "UAE VAT 5% - AG").taxes,
        "tax_category": get_dummy_tax_category()
        
		
		
    }

    salesorder.update(values)

    salesorder.insert(ignore_permissions=True)

    return salesorder
