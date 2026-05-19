# Copyright (c) 2026, suvarna and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document


class GymLockerBooking(Document):

    def validate(self):

        existing_booking = frappe.db.exists(
            "Gym Locker Booking",
            {
                "locker": self.locker,
                "name": ["!=", self.name]
            }
        )

        if existing_booking:
            frappe.throw("Locker is already booked")