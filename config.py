import json

class Config:
	def __init__(self):

		self.hardware = {}
		self.software = {}
		self.water = {}

		print("Construct Config Object")
		with open("/etc/little-genesis.json") as jsonfile:
			tmp =  json.load(jsonfile)
			self.hardware = tmp["hardware"]
			self.software = tmp["software"]
			self.water = tmp["water"]
