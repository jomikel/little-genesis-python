import json

class Config:
	def __init__(self):
		self.water = {}
		print("Construct Config Object")
		with open("params.json") as jsonfile:
			tmp =  json.load(jsonfile)
			self.water = tmp["water"]
