# -*- coding: utf-8 -*-
{
    'name': "Courses",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Kirollos Noshy",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'contacts', 'website'],
    'application': True,
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/course_room_info_view.xml',
        'views/course_course_info_view.xml',
        'views/course_lesson_info_view.xml',
        'views/courses_person_view.xml',
        'views/courses_display_view.xml',
        'views/menu_items.xml',
        'views/templates.xml',
        'reports/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
