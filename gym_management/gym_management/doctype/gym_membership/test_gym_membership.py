# Copyright (c) 2026, suvarna and Contributors
# See license.txt

import frappe

from frappe.tests.utils import FrappeTestCase
from frappe.utils import add_days, nowdate


class TestGymMembership(FrappeTestCase):

    def test_remaining_days_calculation(self):

        # Create Gym Member
        member = frappe.get_doc({
                   "doctype": "Gym Member",
                   "name1": frappe.generate_hash(length=6),
                   "member_id": "MEM-001"
        }).insert()

        # Create Membership Plan
        plan = frappe.get_doc({
        "doctype": "Gym Membership Plan",
        "plan_name": frappe.generate_hash(length=6),
        "duration_months": 3,
        "price": 5000
        }).insert()

        # Create Membership
        membership = frappe.get_doc({

            "doctype": "Gym Membership",

            "gym_member": member.name,

            "membership_plan": plan.name,

            "start_date": nowdate(),

            "end_date": add_days(nowdate(), 10),

            "status": "Active"
        })

        membership.insert()

        self.assertEqual(
            membership.remaining_days,
            10
        )
        