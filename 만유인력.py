from vpython import *

#Creating Objects
Earth = sphere(pos = vector(0,0,0), radius = 6400000, texture = textures.earth) 
Moon = sphere(pos = vector(385000e3,0,0), radius = 1737000, make_trail = True)

sf = 6 
#scailing factor 
Earth.radius = sf*Earth.radius 
Moon.radius = sf*Moon.radius

#Physical Properties
G = 6.67e-11 
Earth.mass = 5.972e24 
Moon.mass = 7.347e22 
Earth.v = vec(0,0,0) 
Moon.v = vec(0,0,0)

#time
t = 0
dt = 60

scene.waitfor('click')
#Simulation Loop 
while True:
    rate(5000)

    #Forces
    r = Earth.pos - Moon.pos
    Moon.f = G*Earth.mass*Moon.mass/mag(r)**2*norm(r) 
    Earth.f= -Moon.f

    #Time Integration
    Moon.v = Moon.v + Moon.f/Moon.mass*dt 
    Earth.v = Earth.v + Earth.f/Earth.mass*dt 
    
    Moon.pos = Moon.pos + Moon.v*dt 
    Earth.pos = Earth.pos + Earth.v*dt

    t = t + dt

    #Collision Check
    if Earth.radius + Moon.radius > mag(r):
        print("Collision!")
        print( t/60/60/24, "days") 
        break