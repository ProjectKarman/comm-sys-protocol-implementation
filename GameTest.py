import pygame

#execfile('C:\Users\duggy_000\Documents\Homework\RocketClub\Karman\GameTest.py')

pygame.init()

display_width = 1500
display_height = 1000

#color definitions

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

temperature=[]
accelx = []
accely=[]
accelz=[]
gyrox=[]
gyroy=[]
gyroz=[]
magnx=[]
magny=[]
magnz=[]
pressure=[]


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Graphs Hopefully')
clock = pygame.time.Clock()

def getData():
	#get array of packets and iterate through?
	#packetType = unkown.packetType
	#value = unkown.value
	if(packetType == "t"):
		temperature.append(value)
	elif(packetType == "ax"):
		accelx.append(value)
	elif(packetType == "ay"):
		accely.append(value)
	elif(packetType == "az"):
		accelz.append(value)
	elif(packetType == "gx"):
		gyrox.append(value)
	elif(packetType =="gy"):
		gyroy.append(value)
	elif(packetType == "gz"):
		gyroz.append(value)
	elif(packetType =="mx"):
		magnx.append(value)
	elif(packetType == "my"):
		magny.append(value)
	elif(packetType == "mz"):
		magnz.append(value)
	elif(packetType == "p"):
		pressure.append(value)


def init():
	myfont = pygame.font.SysFont("monospace", 15)

	tempx = 150
	tempy = 250

	temp = myfont.render("Temperature", 1, black)
	gameDisplay.blit(temp, (tempx+25, tempy-210))
	
	#temperature
	pygame.draw.line(gameDisplay, black, [tempx,tempy-200], [tempx, tempy])
	pygame.draw.line(gameDisplay, black, [tempx,tempy], [tempx+200, tempy])

	acxx = 500
	acxy = 250
	acx = myfont.render("X Acceleration", 1, black)
	gameDisplay.blit(acx, (acxx+25, acxy-210))

	#accelx
	pygame.draw.line(gameDisplay, black, [acxx, acxy], [acxx, acxy-200])
	pygame.draw.line(gameDisplay, black, [acxx, acxy], [acxx+200, acxy])

	acyzx = 850
	acyzy = 250
	acx = myfont.render("Y and Z Acceleration", 1, black)
	gameDisplay.blit(acx, (acyzx + 25, acyzy-210))

	#accely and accelz
	pygame.draw.line(gameDisplay, black, [acyzx, acyzy], [acyzx, acyzy-200])
	pygame.draw.line(gameDisplay, black, [acyzx, acxy], [acyzx+200, acyzy])


	gyrox = 150
	gyroy = 750

	gyro = myfont.render("Gyroscope X, Y, Z", 1, black)
	gameDisplay.blit(gyro, (gyrox+25, gyroy-210))
	
	#temperature
	pygame.draw.line(gameDisplay, black, [gyrox,gyroy-200], [gyrox, gyroy])
	pygame.draw.line(gameDisplay, black, [gyrox,gyroy], [gyrox+200, gyroy])

	magnx = 500
	magny = 750
	acx = myfont.render("X, Y, Z Magnetometer", 1, black)
	gameDisplay.blit(acx, (magnx+25, magny-210))

	#accelx
	pygame.draw.line(gameDisplay, black, [magnx, magny], [magnx, magny-200])
	pygame.draw.line(gameDisplay, black, [magnx, magny], [magnx+200, magny])

	presx = 850
	presy = 750
	press = myfont.render("Pressure", 1, black)
	gameDisplay.blit(press, (presx + 25, presy-210))

	#accely and accelz
	pygame.draw.line(gameDisplay, black, [presx, presy], [presx, presy-200])
	pygame.draw.line(gameDisplay, black, [presx, presy], [presx+200, presy])


def graphAll():
	#Graph Temperature
	tempx = 150
	tempy = 250
	for i in range(0, len(temperature)):
		dot(tempx + i, tempy - temperature[i], green)


def dot(dotx, doty, color):
	pygame.draw.circle(gameDisplay, color, [dotx, doty], 1, 0)

def game_loop():

	crashed = False

	while not crashed:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True

		gameDisplay.fill(white)
		#getData()
		init()

		dot(50, 250, red) # origin graph1
		graphAll()
		pygame.display.update()
		clock.tick(60)


game_loop()
pygame.quit()
quit()

