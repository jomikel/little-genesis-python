import json

class Config:
	def __init__(self):

		self.hardware = {}
		self.hardware.pins = {}
		self.hardware.pins.light = {}
		self.software = {}
		self.water = {}

		print("Construct Config Object")
		with open("/etc/little-genesis.json") as jsonfile:
			tmp =  json.load(jsonfile)
			
			if tmp["hardware"]:
				if tmp["hardware"]["pins"]:
					if tmp["hardware"]["pins"]["water"]:
						self.hardware.pins.water = tmp["hardware"]["pins"]["water"]
					if tmp["hardware"]["pins"]["light"]:
						if tmp["hardware"]["pins"]["light"]["red"]:
							self.hardware.pins.light.red = tmp["hardware"]["pins"]["light"]["red"]
						if tmp["hardware"]["pins"]["light"]["green"]:
							self.hardware.pins.light.green = tmp["hardware"]["pins"]["light"]["green"]
						if tmp["hardware"]["pins"]["light"]["blue"]:
							self.hardware.pins.light.green = tmp["hardware"]["pins"]["light"]["blue"]
						
			# self.hardware = tmp["hardware"]
			self.software = tmp["software"]
			self.water = tmp["water"]
		
		if !self.hardware.pins.water:
			print("Error: No Pin for watering given!")
		
		if !self.hardware.pins.light.red:
			print("Error: No Pin for red lights given!")
		if !self.hardware.pins.light.green:
			print("Error: No Pin for green lights given!")
		if !self.hardware.pins.light.blue:
			print("Error: No Pin for blue lights given!")
			
