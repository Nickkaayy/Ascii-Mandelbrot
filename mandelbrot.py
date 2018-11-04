import math
import sys
from os import system


###initializing

width = 100;
height = 20;
cont = 1;


w = 6.5
h = (w * height)/width;
xmin = (-w/2 + 2)*1.1;
ymin = -h/2-0.2;
maxiterations = 300;
xmax = xmin + w;
ymax = ymin + h;
dx = ((xmax - xmin) / width) / (w/2)
dy = ((ymax - ymin) / height)/(w/8)
initx = dx
inity = dy

while(cont == 1):


	print dx
	print dy
	y = ymin;
	for j in range(height):
		x = xmin;
		for i in range(width):
			a = x;
			b = y;
			n = 0;
			cont = 0;
			while (n < maxiterations):
				aa = a * a;
				bb = b * b;
				twoab = 2.0*a*b;
				a = aa-bb+x;
				b = twoab+y;

				if (math.sqrt((0-aa)**2 + (0-bb)**2) > 4.0):
					break;
				n+=1;
			

			if (n==maxiterations):
				sys.stdout.write('#')
				sys.stdout.flush()
			elif (n<maxiterations/3):
				sys.stdout.write('~')
				sys.stdout.flush()
			elif (n<maxiterations/2.5):
				sys.stdout.write('@')
				sys.stdout.flush()
			elif (n<maxiterations/2):
				sys.stdout.write('-')
				sys.stdout.flush()
			elif (n<maxiterations/1.8):
				sys.stdout.write('(')
				sys.stdout.flush()
			elif (n<maxiterations/1.6):
				sys.stdout.write(')')
				sys.stdout.flush()
			elif (n<maxiterations/1.4):
				sys.stdout.write('$')
				sys.stdout.flush()
			elif (n<maxiterations/1.1):
				sys.stdout.write('!')
				sys.stdout.flush()
			elif (math.sqrt((0-aa)**2 + (0-bb)**2) > 4.0):
				sys.stdout.write('.')
				sys.stdout.flush()
				
			x +=dx;
		y +=dy;
		print "\n"

	##controls!!! apolagies for the difficult controls!!!

	action = input()
	if action == 1: #move left!
		xmin *=1+(dx/initx * 0.5)
	if action == 2: #move right!
		xmin /=1+(dx/initx * 0.5)
	if action == 3: #move up!
		ymin *=1+(dy/inity * 0.8)
	if action == 4: #move down!
		ymin /=1+(dy/inity * 0.8)
	
	if action == 6: #zoom out!
		dx *=1.3;
		dy *=1.3;
	elif action == 7: #zoom in!
		dx /=1.3;
		dy /=1.3;

	cont = 1;





























