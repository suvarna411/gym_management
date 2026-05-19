# Copyright (c) 2026, suvarna and contributors
# For license information, please see license.txt

# import frappe

import frappe


def execute(filters=None):

    columns = [
        {
            "label": "Date",
            "fieldname": "date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": "Gym Member",
            "fieldname": "gym_member",
            "fieldtype": "Link",
            "options": "Gym Member",
            "width": 180
        },
        {
            "label": "Weight",
            "fieldname": "weight",
            "fieldtype": "Float",
            "width": 120
        },
        {
            "label": "Calories Burned",
            "fieldname": "calories_burned",
            "fieldtype": "Int",
            "width": 150
        },
        {
            "label": "Calories Intake",
            "fieldname": "calories_intake",
            "fieldtype": "Int",
            "width": 150
        }
    ]

    conditions = {}

    if filters.get("gym_member"):
        conditions["gym_member"] = filters.get("gym_member")

    data = frappe.get_all(
        "Fitness Metrics",
        filters=conditions,
        fields=[
            "date",
            "gym_member",
            "weight",
            "calories_burned",
            "calories_intake"
        ]
    )

    chart = {
        "data": {
            "labels": [d["date"] for d in data],
            "datasets": [
                {
                    "name": "Weight",
                    "values": [d["weight"] for d in data]
                }
            ]
        },
        "type": "line",
    }

    return columns, data, None, chart
