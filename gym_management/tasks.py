import frappe


def send_weekly_class_summary():

    total_bookings = frappe.db.count("Gym Class Booking")

    frappe.sendmail(
        recipients=["suvarnatadikamalla64@gmail.com"],
        subject="Gym Weekly Summary",
        message=f"Total Class Bookings: {total_bookings}"
    )

    frappe.msgprint("Scheduler Function Executed")
