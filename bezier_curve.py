bezier = [
  {
    'A': {'x': 0,  'y': 0},
    'B': {'x': 1,  'y': 0},
    'C': {'x': 2, 'y': 1},
    'D': {'x': 3, 'y': 1},
  }, {
    'A': {'x': 120, 'y': 160},
    'B': {'x': 35, 'y': 200},
    'C': {'x': 220, 'y': 260},
    'D': {'x':220, 'y': 40},
  }
]

x = []
y = []
label = ['A','B','C','D']
for i in range(0,2):
    for j in  label:
      x.append(bezier[i][j]['x'])
      y.append(bezier[i][j]['y'])
print(x,y)

import matplotlib.pyplot as plt
plt.plot(x[4:8],y[4:8],label='seg2')

def beziercurve(t,p1,p2,p3,p4):
  P = (p1*((1-t)**3))+(3*t*(((1-t)**2)*p2))+((3*(1-t))*((t**2)*p3))+((t**3)*p4)
  return P
  
print(beziercurve(0.02,bezier[0]['A']['x'],bezier[0]['B']['x'],bezier[0]['C']['x'],bezier[0]['D']['x']))


t = 0.2
x_bezier = []
y_bezier = []
for i in range(1,6):
  x_bezier.append(beziercurve(t*i,bezier[0]['A']['x'],bezier[0]['B']['x'],bezier[0]['C']['x'],bezier[0]['D']['x']))
  y_bezier.append(beziercurve(t*i,bezier[0]['A']['y'],bezier[0]['B']['y'],bezier[0]['C']['y'],bezier[0]['D']['y']))
print(x_bezier)

t = 0.02
x_bezier1 = []
y_bezier1 = []
for i in range(1,51):
  x_bezier1.append(beziercurve(t*i,bezier[1]['A']['x'],bezier[1]['B']['x'],bezier[1]['C']['x'],bezier[1]['D']['x']))
  y_bezier1.append(beziercurve(t*i,bezier[1]['A']['y'],bezier[1]['B']['y'],bezier[1]['C']['y'],bezier[1]['D']['y']))


plt.plot(x[4:8],y[4:8],label='line1')
plt.plot(x_bezier1,y_bezier1,label='line2')

	