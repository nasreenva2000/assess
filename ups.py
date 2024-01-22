import frappe

@frappe.whitelist(allow_guest=True)
def update_sales_taxes_template(customer_name=None):
    try:
        if not customer_name:
            return "Please provide a valid 'customer_name'."

        # Find Sales Orders with the specified customer name
        sales_orders = frappe.get_list(
            "Sales Order",
            filters={"customer": customer_name},
            fields=["name"]
        )

        # Iterate through Sales Orders and update taxes template
        for sales_order in sales_orders:
            sales_order_name = sales_order["name"]

            # Update 'UAE VAT 5% - AG' to 'UAE VAT Zero - AG' in taxes template
            frappe.db.set_value("Sales Taxes and Charges", {"parent": sales_order_name, "charge_type": "On Net Total", "account_head": "UAE VAT 5% - AG"},
                                "account_head", "UAE VAT Zero - AG")

        return f"Sales Taxes and Charges Template updated for customer {customer_name}"

    except frappe.DoesNotExistError:
        return f"No Sales Orders found for customer {customer_name}"

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example: Update Sales Taxes and Charges Template for customer "javed"
update_sales_taxes_template(customer_name="ABCDE")
