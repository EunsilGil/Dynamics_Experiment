from vpython import *

#Creating Objects & Scene Setting
water = box(pos = vec(0,0,0), size=vec(10,10,10), color = color.blue, opacity = 0.5)
wood = box(pos = vec(0,10,0), size=vec(2,2,2), texture = textures.wood)
scene.background = color.white

# Initial Setting 
wood.v = vec(0,0,0)
wood.rho = 1000 # 나무토막의 밀도
wood.volume = wood.size.x*wood.size.y*wood.size.z
wood.volume_im = 0 # 잠긴 부피
wood.m = wood.rho*wood.volume # 질량
water.rho = 1000 # 물의 밀도
air_rho = 1.2 # 공기 밀도
rho = air_rho # 초기 밀도 (처음엔 완전 공기)
Cd = 1.06 # 저항 계수
g = vec(0,-9.8,0) # 중력 가속도
t=0
dt = 0.001

def collision_with_bottom(pBox,pbox):
    col_check = (pbox.pos.y - 0.5*pbox.size.y) - (pBox.pos.y - 0.5*pBox.size.y) 
    if col_check < 0:
        return True
    else:
        return False

def calc_im(pBox,pbox): ##Calculation of immersed volume and effective rho 
    float_height = (pbox.pos.y + 0.5*pbox.size.y) - (pBox.pos.y + 0.5*pBox.size.y)
    if float_height < 0:
        pbox.volume_im = pbox.volume
    else:
        pbox.volume_im = max(0, pbox.volume - float_height*pbox.size.x*pbox.size.z) 
        
    if pbox.volume_im > 0:
        rho = water.rho 
    else:
        rho = air_rho

    return pbox.volume_im, rho

scene.waitfor('click')
while t < 100: 
    rate(1/dt)
    #collision
    if collision_with_bottom(water, wood): 
        print("collision!")
        break

    wood.volume_im, rho = calc_im(water, wood)
    #force
    grav = wood.m*g
    bouy = -water.rho*wood.volume_im*g
    drag = -0.5*rho*Cd*(wood.size.x*wood.size.y)*mag(wood.v)**2*norm(wood.v)
    wood.f = grav + bouy + drag # 알짜힘

    #time integration
    wood.v = wood.v + wood.f/wood.m*dt
    wood.pos = wood.pos + wood.v*dt 
    
    #time update
    t = t + dt