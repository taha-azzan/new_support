# -*- coding: utf-8 -*-
# Copyright (c) 2021, Partner Team and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class OperationOrder(Document):
	pass

@frappe.whitelist()
def make_material_request(source_name, target_doc=None):
	from frappe.model.mapper import get_mapped_doc, map_child_doc

	def _update_links(source_doc, target_doc, source_parent):
		target_doc.prevdoc_doctype = source_parent.doctype
		target_doc.prevdoc_docname = source_parent.name

	visit = frappe.db.sql("""select t1.name
		from `tabMaterial Request` t1, `tabOperation Order Item` t2
		where t2.parent=t1.name and t2.prevdoc_docname=%s """, source_name)

	if not visit:
		target_doc = get_mapped_doc("Operation Order", source_name, {
			"Operation Order": {
				"doctype": "Material Request",
				"field_map": {}
			}
		}, target_doc)

		source_doc = frappe.get_doc("Operation Order", source_name)
		if source_doc.get("item_code"):
			table_map = {
				"doctype": "Operation Order Item",
				"postprocess": _update_links
			}
			map_child_doc(source_doc, target_doc, table_map, source_doc)

		return target_doc