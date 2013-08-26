# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

import time

from openerp.osv import fields, osv
from openerp.tools.translate import _

class account_itc_config(osv.osv):
    _name = "account.itc.config"
    _description = "Accounting ITC Tax Configuration"
    _columns = {
        'software_code' : fields.char('Software Verification Code', size=128, required=True),
        'transaction_set_id' : fields.char('Transaction Set Id', size=128, required=True),
        'business_number' : fields.char('Business Number', size=20, required=True),
    }
account_itc_config()

class account_itc_return(osv.osv):
    _name = "account.itc.return"
    _description = "Accounting ITC Tax Submission"
    _columns = {
        'name' : fields.char('Name', size=128, required=True),
        'reporting_period_start' : fields.date('Reporting Period Start', required=True, help="The start date of this ITC return"),
        'reporting_period_end' : fields.date('Reporting Period END', required=True, help="The end date of this ITC return"),
        'line_101' : fields.float('Sales & Revenue', digits=[12,2], required=True),
        'line_105' : fields.float('Total GST/HST', digits=[12,2], required=True),
        'line_108' : fields.float('Total ITC\'s & adj', digits=[12,2], required=True),
        'line_109' : fields.float('Net Tax', digits=[12,2], required=True),
        'line_110' : fields.float('Installments & Revenue', digits=[12,2], required=True),
        'line_111' : fields.float('Rebates', digits=[12,2], required=True),
        'line_205' : fields.float('GST/HST due to aquisition of property', digits=[12,2], required=True),
        'line_405' : fields.float('Other GST/HST', digits=[12,2], required=True),
        'line_114' : fields.float('Refund Claimed', digits=[12,2], required=True),
        'line_115' : fields.float('Amount Owing', digits=[12,2], required=True),
        'line_135' : fields.float('Total GST New housing Rebates', digits=[12,2], required=True),
        'line_136' : fields.float('Deduction for Pension', digits=[12,2], required=True),
    }

account_itc_return()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
