frappe.pages['my-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'My Page',
		single_column: true
	});

	page.set_indicator("Inactive","orange");
}