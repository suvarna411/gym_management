frappe.pages['member-profile'].on_page_load = function(wrapper) {

    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Member Profile',
        single_column: true
    });

    frappe.call({
        method: "gym_management.api.get_member_profile",

        callback: function(r) {

            let data = r.message;

            $(page.body).html(`
                <h3>Active Plan: ${data.plan}</h3>
                <h3>Remaining Days: ${data.remaining_days}</h3>
                <h3>Trainer: ${data.trainer}</h3>
                <h3>Past Plans: ${data.past_plans}</h3>
            `);
        }
    });
}