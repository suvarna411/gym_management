# Copyright (c) 2026, suvarna and contributors
# For license information, please see license.txt

import frappe

from frappe.model.document import Document
from frappe.utils import date_diff, nowdate


class GymMembership(Document):

    def validate(self):

        # Calculate remaining days
        if self.end_date:

            self.remaining_days = date_diff(
                self.end_date,
                nowdate()
            )

    def on_submit(self):

        # Activate member
        frappe.db.set_value(
            "Gym Member",
            self.gym_member,
            "status",
            "Active"
        )
