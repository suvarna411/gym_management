import frappe


def execute():

    memberships = frappe.get_all(
        "Gym Membership",
        filters={
            "membership_status": ["in",["Expired","Cancelled"]]
        },
        fields=["name"]
    )

    for membership in memberships:

        frappe.db.set_value(
            "Gym Membership",
            membership.name,
            "membership_status",
            "Active"
        )

    frappe.db.commit()
