


import typer
import time
from uuid import uuid4
import random



i = 0

while i < 10000000000000:

	a = uuid4()
	b = uuid4()
	c = uuid4()
	e = uuid4()
		


	col = ["green", "green", "green", "green", "red", "white", "green", "white", "green", "red", 'green', 'green', 'green']
	color = random.choice(col)
	d = [2, 3, 4, 2, 4, 4, 3, 1, 0]
	
	if color == "green":
		f = random.choice(d)
		if f == 0:
			print("\n")
		elif f == 1:
			print(typer.style(f"{a}", fg=typer.colors.GREEN))
		
		elif f == 2:
			print(typer.style(f"{a}-{b}", fg=typer.colors.GREEN))

		elif f == 3:
			print(typer.style(f"{a}-{b}-{c}", fg=typer.colors.GREEN))

		elif f == 4:
			print(typer.style(f"{a}-{b}-{c}-{e}", fg=typer.colors.GREEN))


#
#	elif color == "blue":
#		x = [2, 3, 2, 3, 2, 2, 2, 3, 2, 2 ]
#		f = random.choice(x)
#		if f == 2:  
#			print(typer.style(f"{a}-{b}", fg=typer.colors.BLUE))
#
#		elif f == 3:
#			print(typer.style(f"{a}-{b}-{c}", fg=typer.colors.BLUE))
#



	elif color == "red":
		
		f = random.choice(d)
		if f == 0:
			print("\n")
		elif f == 2:  
			print(typer.style(f"{a}-{b}", fg=typer.colors.RED))
		
		elif f == 3:
			print(typer.style(f"{a}-{b}-{c}", fg=typer.colors.RED))

		elif f == 4:
			print(typer.style(f"{a}-{b}-{c}-{e}", fg=typer.colors.RED))





	else:
		p = [2, 3, 2, 2, 3, 2, 2, 1]
		f = random.choice(p)
		if f == 1:
			print(a)
		elif f == 2:
			print(f"{a}-{b}")
			
		elif f == 3:
			print(f"{a}-{b}-{c}")



	time.sleep(0.02)

