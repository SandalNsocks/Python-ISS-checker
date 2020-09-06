import json
import turtle
import urllib.request

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)


print('People in space: ', result['number'])

people = result['people']
for p in people:
    print(p['name'] + " in " + p['craft'])
    
url = 'http://api.open-notify.org/iss-now.json?lat=29.5502&lon=-95.097'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print(result)






screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.png')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('latitude: ', lat)
print('longitude: ', lon)

iss.penup()
iss.goto(float(lon), float(lat))

# space Center houston
lat1 = 29.5502
lon1 = -95.097

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon1,lat1)
location.dot(5)
location.hideturtle()


