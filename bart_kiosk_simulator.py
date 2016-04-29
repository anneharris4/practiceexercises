def load_card (ones,fives,tens,twenties):
	return (1*ones) + (5*fives) + (10*tens) + (20 * twenties)

x = int(raw_input("How many ones?"))
y = int(raw_input("How many five?"))
z = int(raw_input("how many tens?"))
v = int(raw_input("How many twenties?"))


print load_card(x, y, z, v)
