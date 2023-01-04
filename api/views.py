"""
Class based view to fetch the required data from Attck() object
"""

from django.shortcuts import render
from rest_framework import views
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from datetime import date, datetime

from api import load_mitre_attck_techniques, load_mitre_attck_tactics

def get_sub_fields(field, all_fields):
	map_str = f"{field}."

	result = []
	for f in all_fields:
		if f.startswith(map_str):
			result += [ f[len(map_str):] ]
	if len(result):
		return result
	else:
		return all_fields

def fetch_fields(object, fields):
	result = {}
	for field in fields:
		if '.' in field:
			# Has sub-fields
			base_class = field.split('.')[0]
			if not hasattr(object, field):
				# Set null, if field not exists object
				result[field] = None
				continue

			element = getattr(object, base_class)
			if type(element) in [list, ]:
				sub_fields = get_sub_fields(base_class, fields)
				result[base_class] = [ fetch_fields(e, sub_fields) for e in element ]
			elif type(element) in [dict, ]:
				sub_fields = get_sub_fields(base_class, fields)
				result[base_class] = { k: fetch_fields(v, sub_fields) for k, v in element.items() }
		else:
			# Does not have sub-fields
			if not hasattr(object, field):
				# Set null, if field not exists object
				result[field] = None
				continue

			element = getattr(object, field)
			if type(element) in [str, int, float, bool, ]:
				result[field] = element

	return result

def get_element(id_list, type='technique', fields=['id', 'name', 'description']):
	result = {}

	if type == "technique":
		result_dict = load_mitre_attck_techniques()
	if type == "tactic":
		result_dict = load_mitre_attck_tactics()

	for id in id_list:
		if id not in result_dict:
			result[id] = f"{type.capitalize()} {id} not found."
		else:
			result[id] = fetch_fields(result_dict[id], fields=fields)

	return result

class MitreDataView(viewsets.GenericViewSet):
	def get_queryset(self):
		return super().get_queryset()

	def get_throttles(self):
		return super().get_throttles()

	def get_paginated_response(self, data):
		return super().get_paginated_response(data)

	def list(self, request):
		result = {}

		fields = request.query_params.get('fields', "").split(',')
		data = request.data

		if 'technique' in data:
			result = get_element(data['technique'], type="technique", fields=fields)

		if 'tactic' in data:
			result = get_element(data['tactic'], type="tactic", fields=fields)

		return Response(result)
