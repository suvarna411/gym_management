import frappe


def validate_class_capacity(doc, method):

    capacity = frappe.db.get_value(
        "Gym Class",
        doc.gym_class,
        "capacity"
    )

    total_bookings = frappe.db.count(
        "Gym Class Booking",
        {
            "gym_class": doc.gym_class
        }
    )

    if total_bookings >= capacity:

        frappe.throw("Class Capacity Full")
    frappe.msgprint("Hook Triggered")
@frappe.whitelist()
def get_member_profile():

    membership = frappe.get_last_doc("Gym Membership")

    return {
        "plan": membership.membership_plan,
        "remaining_days": membership.remaining_days,
        "trainer": "Rahul Trainer",
        "past_plans": "Silver Plan, Gold Plan"
    }
@frappe.whitelist()
def get_dashboard_data():

    total_members = frappe.db.count("Gym Member")

    total_revenue = frappe.db.sql("""
        SELECT SUM(amount)
        FROM `tabGym Membership`
    """)[0][0] or 0

    active_trainers = frappe.db.count(
        "Gym Trainer",
        {
            "availability": "Available"
        }
    )

    todays_classes = frappe.db.count("Gym Class")

    return {
        "total_members": total_members,
        "total_revenue": total_revenue,
        "active_trainers": active_trainers,
        "todays_classes": todays_classes
    }
