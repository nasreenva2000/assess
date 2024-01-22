import frappe

@frappe.whitelist(allow_guest=True)
def delete_sales_order_by_customer(customer_name):
    try:
        # Get a list of Sales Orders with the specified customer name
        sales_orders = frappe.get_list("Sales Order",
                                       filters={"customer": customer_name},
                                       fields=["name", "docstatus"])

        # Delete each Sales Order
        for sales_order in sales_orders:
            if sales_order.docstatus == 1:  # Check if Sales Order is submitted
                frappe.throw(f"Sales Order {sales_order.name} is already submitted. Cancel it before deletion.")
            else:
                frappe.delete_doc("Sales Order", sales_order.name, ignore_permissions=True)

        return f"Sales Orders for customer {customer_name} deleted successfully"

    except frappe.DoesNotExistError:
        return f"No Sales Orders found for customer {customer_name}"

    except frappe.exceptions.LinkExistsError:
        return f"Unable to delete Sales Orders for customer {customer_name}. Check for linked documents."

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example: Delete Sales Orders for customer "ABU HASERRA"
delete_sales_order_by_customer("ABU HASERRA")
