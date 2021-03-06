# -*- coding: utf-8 -*-
#############################################################################
#
#
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': 'Purchase Changes',
    'category': 'Purcase',
    'summary': "Vendor creation Approval level, and GRN approval level",
    'depends': ['stock','purchase','stock_landed_costs','odoo_multi_channel_sale'],
    'data': [
        'views/pr_view.xml',
        'data/pro_data.xml',
        'wizard/land_cost.xml',
        'security/ir.model.access.csv',
        'security/security_view.xml',

    ],
    'demo': [
    ],
    'license': 'AGPL-3',
    'application': True,
    'installable': True,
    'auto_install': False,
}
