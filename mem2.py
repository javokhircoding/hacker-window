#!usr/bin/python


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
	print(typer.style(f"{c}-{a}-{b}-{e}", fg=typer.colors.GREEN))
