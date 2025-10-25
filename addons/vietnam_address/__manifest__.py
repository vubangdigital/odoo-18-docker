# -*- coding: utf-8 -*-
{
    'name': 'Vietnam Address',
    'summary': """The Vietnam Address""",
    'author': 'Vũ Tiến Linh',
    'license': 'LGPL-3',
    'category': 'Extra Tools',
    'version': '18.0.1.0',
    'support': 'vutienlinh412001@gmail.com',
    'depends': ['base','crm','contacts','mail','web_enterprise'],
    'data': [
        'security/ir.model.access.csv',
        'data/res.country.province.csv',
        'data/res.country.ward.csv',
        'views/res_country_province_views.xml',
        'views/res_country_ward_views.xml',
        'views/res_partner_views.xml',
        'views/crm_lead_views.xml',
        # 'views/res_company_views.xml',
        'views/menu_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'vietnam_address/static/src/scss/hide_send_message.css',
            # 'vietnam_address/static/src/js/rename_chatter.js',
        ],
        'web._assets_primary_variables': [
            'vietnam_address/static/src/scss/custom_primary_variables.scss',
        ],
    },
    'images': ['static/description/thumbnail.png'],
    'application': True,
    'installable': True,
}
