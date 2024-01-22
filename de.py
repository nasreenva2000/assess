# import frappe

# @frappe.whitelist(allow_guest=True)
# def delete_quotation(quotation_name):
#     # Find the Quotation based on the name
#     quotation = frappe.get_list(
#         "Quotation",
#         filters={"name": quotation_name},
#         fields=["name", "docstatus"]
#     )

#     if quotation:
#         if quotation[0]["docstatus"] == 1:  # Check if the Quotation is submitted
#             # Cancel the Quotation first
#             frappe.get_doc("Quotation", quotation[0]["name"]).cancel()

#         # Now, delete the Quotation
#         frappe.delete_doc("Quotation", quotation[0]["name"])
#         return f"Quotation with name {quotation_name} deleted successfully"
#     else:
#         return f"No Quotation found with name {quotation_name}"


import frappe

@frappe.whitelist(allow_guest=True)
def delete_quotation(quotation_name):
    # Find the Quotation based on the name
    quotation = frappe.get_list(
        "Quotation",
        filters={"name": quotation_name},
        fields=["name"]
    )

    if quotation:
        # Try to delete the Quotation
        try:
            frappe.delete_doc("Quotation", quotation[0]["name"])
            return f"Quotation with name {quotation_name} deleted successfully"
        except frappe.exceptions.LinkExistsError:
            # If there are links preventing deletion, handle the exception
            return f"Unable to delete Quotation with name {quotation_name}. Check for linked documents."
    else:
        return f"No Quotation found with name {quotation_name}"


