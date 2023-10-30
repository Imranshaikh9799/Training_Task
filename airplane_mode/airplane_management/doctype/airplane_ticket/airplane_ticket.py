# Copyright (c) 2023, Imran Shaikh and contributors
# For license information, please see license.txt

import random
import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):
	#pass
	def before_save(self):
		TotalAmount=0;
		for item in self.add_ons:
			TotalAmount+=item.Amount
		self.total_amount=TotalAmount+self.flight_price

	def before_submit(self):
		if self.status!="Borded":
			frappe.throw("You can not submit document before boarded");

	def before_validate(self):
		itemList=[]
		for itemvar in self.add_ons:
			if itemvar.item not in itemList:
				itemList.append(itemvar.item)
			else:
				self.add_ons.remove(itemvar)

			

	def on_submit(self):
		number=random.randint(1,100)
		string=("ABCDE")
		seat=random.sample(string,1)
		self.seat=f'{number}{seat[0]}'

