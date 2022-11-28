"""
Class based view to fetch the required data from Attck() object
"""

from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from django.http import JsonResponse
from pyattck import Attck
from datetime import date
import json
import os
# from api.serializers import YourSerializer

"""
pyattck is a python package to interact with the MITRE ATT&CK Framework
This package extracts details from the MITRE Enterprise, PRE-ATT&CK, Mobile, and ICS Frameworks.
The below code basically uses the pyattck package and fetches data based on the requirements.
"""
class MyAttckView(views.APIView):
	"""
	View to fetch the necessary data and store it in a JSON file to reduce time taken to
	search the Mitre ATT&CK database
	"""
	def get(self, request):
		attack = Attck()
		import pdb; pdb.set_trace()
		result_dict = {}
		for technique in attack.enterprise.techniques:
			# print(technique.last_updated)
			import pdb; pdb.set_trace()
			tech_dict = {}
			tech_dict["technique_mitre_id"] = technique.technique_id
			for subtechnique in technique.techniques:
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

		# result = json.dumps(result_dict, indent=4)
		# serializer_class = YourSerializer(result, many=True)
		# import pdb; pdb.set_trace()

		file = 'data_output.json'

		isFile = os.path.isfile(file)
		if isFile: 
			os.remove("data_output.json")
		with open("data_output.json", "w") as outfile:
			json.dump(result_dict, outfile, indent=4)
		return Response(result_dict)


class MitreAttck(views.APIView):
	"""
	View to get the data stored in JSON format created by the previous API and return the searched data
	"""
	def get(self, request):
		id = request.GET['id'].split(',')
		data = open('data_output.json')

		raw = json.load(data)

		# data_set = [raw.get(i) for i in id]
		data_set = []
		for i in id:
			data_set.append(raw.get(i))

		return Response(data_set)

	def post(self, request):
		malware = request.POST['malware_name']
		mitigation = request.POST['mitigation']

		# import pdb; pdb.set_trace()
		if malware:
			param = malware
		else:
			param = mitigation
		data = open('data_output.json')

		raw = json.load(data)
		
		result_list = []
		for value in raw:
			if param in raw[value].values():
				result_list.append(raw[value])

		return Response(result_list)