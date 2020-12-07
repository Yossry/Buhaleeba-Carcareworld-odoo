# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#    See LICENSE file for full copyright and licensing details.
##########H#########Y#########P#########N#########O#########S###################
import logging
_logger = logging.getLogger(__name__)
from odoo import api, fields, models
from odoo.exceptions import UserError

class ExportWoocommercebrand(models.TransientModel):
    _name = 'export.woocommerce.brand'
    _inherit = "export.operation"
    _description  = "Export Woocommerce brand"

    def export_brand(self, attribute):
        woocommerce = self._context.get("woocommerce")
        channel = self._context.get("channel_id")
        vals_list = []
        is_attribute_mapped = self.env['channel.brand.mappings'].search([
            ('odoo_brand_id', '=', attribute.id),
            ('channel_id', '=', channel.id)])
        if not is_attribute_mapped:
            attribute_dict = {
                "name"			: attribute.name,
                # "type"			: "select",
                # "order_by"		: "menu_order",
                # "has_archives"	: True
            }
            return_dict = woocommerce.post(
                'products/attributes/3/terms', attribute_dict).json()
            if 'message' in return_dict:
                raise UserError('Error in Creating Brands :' +
                                str(return_dict['message']))
            store_attribute_id = return_dict['id']
            channel.create_attribute_mapping(attribute, store_attribute_id,store_attribute_name = attribute.name)
        else:
            attribute_dict = {
                "name"			: attribute.name,
                # "type"			: "select",
                # "order_by"		: "menu_order",
                # "has_archives"	: True
            }
            url = "products/attributes/3/terms/%s"% (is_attribute_mapped.store_brand_id)
            return_dict = woocommerce.put(
                url, attribute_dict).json()
            if 'message' in return_dict:
                raise UserError('Error in Updating Brands :' +
                                str(return_dict['message']))
            store_attribute_id = is_attribute_mapped.store_brand_id
        # for attribute_value in attribute_values:
        #     vals = self.export_attribute_values(
        #         woocommerce, channel, attribute_value, store_attribute_id)
        # _logger.info("Attribute with Id(%r) and its values %r are exported/updated to Woocommerce." % (
        #     attribute.id, vals))
        return [True, store_attribute_id]

    def export_attribute_values(self, woocommerce, channel, attribute_value, store_attribute_id):
        is_attribute_value_mapped = self.env['channel.attribute.value.mappings'].search([
            ("channel_id", '=', channel.id),
            ("attribute_value_name", '=', attribute_value.id)
        ])
        if not is_attribute_value_mapped:
            attribute_value_dict = {
                "name": attribute_value.name,
            }
            return_dict = woocommerce.post('products/attributes/' +
                                           str(store_attribute_id)+"/terms", attribute_value_dict).json()
            if 'message' in return_dict:
                raise UserError('Error in Creating terms ' +
                                str(return_dict['message']))
            channel.create_attribute_value_mapping(
                attribute_value,return_dict["id"],store_attribute_value_name = attribute_value.name)
        else:
            attribute_value_dict = {
                "name": attribute_value.name,
            }
            url = "products/attributes/{}/terms/{}".format(store_attribute_id,is_attribute_value_mapped.store_attribute_value_id)
            return_dict = woocommerce.put(url, attribute_value_dict).json()
            if 'message' in return_dict:
                raise UserError('Error in Updating terms ' +
                                str(return_dict['message']))
          
        return attribute_value.id