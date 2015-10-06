# -*- encoding: utf-8 -*-
##############################################################################
#
#    Bista Solutions Pvt. Ltd
#    Copyright (C) 2012 (http://www.bistasolutions.com)
#
##############################################################################

{
    'name': 'Advance multi-level navigation',
    'version': '1.2',
    'description': """
        1. Default vertical navigation bar is hidden on installation of module
         and this can be accessed using the left nav menu.
        2. Ease of access to all the Odoo functionality through
        the horizontal navigation bar.
            1. Each menus of the horizontal bar consist of sub menus
            of the particular module.
        3. On this version improved form view screen size.
    """,
    'author': 'Bista Solutions Pvt. Ltd',
    'website': 'http://www.bistasolutions.com',
    'depends': ['base'],
    'category': 'Bista Solutions',
    'data': ['views/webclient_templates.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
