# -*- coding: utf-8 -*-
##############################################################################
#
#	ENAPPS Canada
#    Copyright (C) 2013 http://enapps.ca
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'ITC submission for Canada',
    'version': '1.0',
    'category': 'Accounting',
    'description': """
Submit your GST/HST and ITC's to Canadian Revenue Agency (CRA)
========================================================

A .tx file is generated, then based on your CRA information you can
submit the output directly to the CRA.

""",
    'author': 'ENAPPS Canada',
    'website': 'http://www.enapps.ca',
    'images': ['images/comething.jpeg'],
    'depends': ['account', 'l10n_ca'],
    'data': [
            'account_itc_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
