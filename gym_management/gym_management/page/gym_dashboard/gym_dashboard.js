frappe.pages['gym-dashboard'].on_page_load = function(wrapper) {

    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Gym Dashboard',
        single_column: true
    });

    frappe.call({

        method: "gym_management.api.get_dashboard_data",

        callback: function(r) {

            let data = r.message;

            $(page.body).html(`

                <div style="padding:20px">

                    <h2>Total Members: ${data.total_members}</h2>

                    <h2>Revenue: ₹${data.total_revenue}</h2>

                    <h2>Active Trainers: ${data.active_trainers}</h2>

                    <h2>Today's Classes: ${data.todays_classes}</h2>

                </div>

            `);
        }
    });
}
