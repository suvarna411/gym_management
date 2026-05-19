# Copyright (c) 2026, suvarna and Contributors
# See license.txt
# added a comment 
import frappe

from frappe.tests.utils import FrappeTestCase
from frappe.utils import add_days, nowdate


class TestGymMembership(FrappeTestCase):

    def test_remaining_days_calculation(self):

        membership = frappe.get_doc({

            "doctype": "Gym Membership",

            "gym_member": "Tomar",

            "membership_plan": "Gold Plan",

            "start_date": nowdate(),

            "end_date": add_days(nowdate(), 10)
        })

        membership.insert()

        self.assertEqual(
            membership.remaining_days,
            10
        )