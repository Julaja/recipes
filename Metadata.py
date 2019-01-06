#	recipes - Python-based HTML5 generation for cooking recipes
#	Copyright (C) 2019-2019 Johannes Bauer
#
#	This file is part of recipes.
#
#	recipes is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; this program is ONLY licensed under
#	version 3 of the License, later versions are explicitly excluded.
#
#	recipes is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with recipes; if not, write to the Free Software
#	Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#	Johannes Bauer <JohannesBauer@gmx.de>

import json

class Metadata():
	def __init__(self, conversion_file, ingredient_file):
		with open(conversion_file) as f:
			self._conversion = json.load(f)
		with open(ingredient_file) as f:
			self._ingredient = json.load(f)

	def getingredientname(self, cid):
		ingredient = self._ingredient["ingredients"].get(cid)
		if ingredient is None:
			return cid
		return ingredient["name"]

	def getunitname(self, unit_id):
		return self._ingredient["units"].get(unit_id, unit_id)