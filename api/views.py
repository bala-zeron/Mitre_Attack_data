"""
Class based view to fetch the required data from Attck() object
"""

from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from django.http import JsonResponse
from pyattck import Attck
import json
# from api.serializers import YourSerializer

"""
pyattck is a python package to interact with the MITRE ATT&CK Framework
This package extracts details from the MITRE Enterprise, PRE-ATT&CK, Mobile, and ICS Frameworks.
The below code basically uses the pyattck package and fetches data based on the requirements.
"""
class MyAttckView(views.APIView):
	def get(self, request):
		attack = Attck()

		result_dict = {}
		for technique in attack.enterprise.techniques:
			# print(technique.last_updated)
			tech_dict = {}
			for subtechnique in technique.techniques:
				# print(subtechnique.id)
				# print(subtechnique.name)
				tech_dict["technique_name"] = subtechnique.name
				tech_dict["created"] = subtechnique.created
				tech_dict["modified"] = subtechnique.modified
				tech_dict["type"] = subtechnique.type
				for actor in subtechnique.actors:
					tech_dict["actor_name"] = actor.name
					tech_dict["actor_aliases"] = actor.aliases
				for malware in subtechnique.malwares:
					tech_dict["malware_name"] = malware.name
				for mitigation in subtechnique.mitigations:
					tech_dict["mitigation"] = mitigation.name
					
			result_dict[technique.technique_id] = tech_dict

		result = json.dumps(result_dict, indent=4)
		# serializer_class = YourSerializer(result, many=True)
		# import pdb; pdb.set_trace()
		return JsonResponse(result, safe=False)