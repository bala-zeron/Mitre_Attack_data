"""
Class based view to fetch the required data from Attck() object
"""

from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from datetime import date, datetime

from api import load_mitre_attck

class MitreAttckView(views.APIView):
	def get(self, request, mitre_id):

		starttime = datetime.now()

		global result_dict
		if 'result_dict' not in globals():
			result_dict = load_mitre_attck()

		if mitre_id not in result_dict:
			raise APIException({"message": f"Cannot find the mitre id `{mitre_id}`"})

		result = result_dict[mitre_id]
		data = {
			mitre_id: {
				"name": result.name,
				"description": result.description,
				"permissions": result.permissions,
				"platforms": result.platforms,

				# "tactics": dict([
				# 	(tactic.id , tactic.name)  for tactic in result.tactics
				# ]),
				# "subtechnique": dict([
				# 	(subtechnique.id , subtechnique.name)  for subtechnique in result.subtechnique
				# ]),

				"wiki": result.wiki,
			}
		}
		endtime = datetime.now()

		print(f'Time taken to load data : ', endtime - starttime)


		return Response(data)
