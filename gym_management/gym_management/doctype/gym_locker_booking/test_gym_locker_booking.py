import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymLockerBooking(FrappeTestCase):

    def test_duplicate_locker_prevention(self):

        
        member1 = frappe.get_doc({
            "doctype": "Gym Member",
            "name1": "Member 1"
        }).insert()

        
        member2 = frappe.get_doc({
            "doctype": "Gym Member",
            "name1": "Member 2"
        }).insert()

        
        locker = frappe.get_doc({
            "doctype": "Gym Locker",
            "locker_number": "Locker-1",
            "availability": "Available"
        }).insert()

        
        booking1 = frappe.get_doc({

            "doctype": "Gym Locker Booking",

            "gym_member": member1.name,

            "locker": locker.name
        })

        booking1.insert()

        
        booking2 = frappe.get_doc({

            "doctype": "Gym Locker Booking",

            "gym_member": member2.name,

            "locker": locker.name
        })

        self.assertRaises(
            frappe.ValidationError,
            booking2.insert
        )
        