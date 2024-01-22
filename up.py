import frappe
@frappe.whitelist(allow_guest=True)
def update_quotation_order_type():
    """
    Update a specific Quotation with the old order_type.

    After updating Quotations, it is recommended to call this function to correct the order_type.
    """
    try:
        # Find the Quotation with the specific name and old order_type
        quotation_name = "Sales Quotation-0116"
        quotation = frappe.get_doc("Quotation", quotation_name)

        # Update the order_type for the Quotation
        if quotation.order_type == "Sales":
            frappe.db.set_value("Quotation", quotation_name, "order_type", "Shopping Cart")
            return {"success": True, "message": f"Quotation {quotation_name} order_type updated successfully."}
        else:
            return {"success": False, "message": f"Quotation {quotation_name} already has order_type as 'Shopping Cart'."}

    except frappe.DoesNotExistError:
        return {"success": False, "message": f"Quotation {quotation_name} not found."}
    except Exception as e:
        return {"success": False, "message": str(e)}

# Example: Call the function to perform the update
update_quotation_order_type()
