# hyperskill.org
class coffee:
	water = 400
	milk = 540
	beans = 120
	cups = 9
	money = 550
		
	def machine(self):
		while True:
			self.user = input("Write action (buy, fill, take, remaining, exit): ")
			
			if self.user == "buy":
				self.user = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
				
				if self.user == "1":
					if coffee.water >= 250 and coffee.beans >= 16:
						print("I have enough resources, making you a coffee!")
						coffee.water -= 250
						coffee.beans -= 16
						coffee.money += 4
						coffee.cups -= 1
					elif coffee.water < 250:
						print("Sorry, not enough water")
					elif coffee.beans < 16:
						print("Sorry, not enough beans")
				
				elif self.user == "2":
					if coffee.water >= 350 and coffee.milk >= 75 and coffee.beans >= 20:
						print("I have enough resources, making you a coffee!")
						coffee.water -= 350
						coffee.milk -= 75
						coffee.beans -= 20
						coffee.money += 7
						coffee.cups -= 1
					elif coffee.water < 350:
						print("Sorry, not enough water")
					elif coffee.milk < 75:
						print("Sorry, not enough milk")
					elif coffee.beans < 20:
						print("Sorry, not enough beans")
				
				elif self.user == "3":
					if coffee.water >= 200 and coffee.beans >= 12 and coffee.milk >= 100:
						print("I have enough resources, making you a coffee!")
						coffee.water -= 200
						coffee.milk -= 100
						coffee.beans -= 12
						coffee.money += 6
						coffee.cups -= 1
					elif coffee.water < 200:
						print("Sorry, not enough water")
					elif coffee.milk < 100:
						print("Sorry, not enough milk")
					elif coffee.beans < 12:
						print("Sorry, not enough beans")
			
			elif self.user == "fill":
				coffee.water += int(input("Write how many ml of water do you want to add: "))
				coffee.milk += int(input("Write how many ml of milk do you want to add: "))
				coffee.beans += int(input("Write how many grams of coffee beans do you want to add: "))
				coffee.cups += int(input("Write how many disposable cups of coffee do you want to add: "))

			elif self.user == "take":
				print("I gave you $", coffee.money)
				coffee.money = 0
				
			elif self.user == "remaining":
				print(f"""The coffee machine has:
		{coffee.water} of water
		{coffee.milk} of milk
		{coffee.beans} of coffee beans
		{coffee.cups} of disposable cups
		{coffee.money} of money""")
			
			elif self.user == "exit":
				break

user = coffee()
print(user.machine())
