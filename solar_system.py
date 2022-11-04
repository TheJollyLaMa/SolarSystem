from ursina import *
import numpy as np

app = Ursina()
def update():
    global t
    t = t+0.02
    angle = np.pi*40/180
    # rotate camera around the sun
    camera.position = (0, 0, 0)
    camera.position += (0.5, -0.5, -30)
    camera.rotation_x = 2
    camera.rotation_y = -2
    camera.rotation_z = -2
    # rotate the planets around the sun
    sun.x = 0
    sun.z = 0
    sun.y = 0

    radius_1 = 1
    mercury.x = radius_1*np.cos(t)
    mercury.z = radius_1*np.sin(t)

    radius_2 = 1.4
    venus.x = radius_2*np.cos(t+angle)
    venus.z = radius_2*np.sin(t+angle)

    radius_3 = 1.8
    earth.x = radius_3*np.cos(t+2*angle)
    earth.z = radius_3*np.sin(t+2*angle)

    radius_4 = 2.2
    mars.x = radius_4*np.cos(t+3*angle)
    mars.z = radius_4*np.sin(t+3*angle)

    radius_5 = 2.6
    jupiter.x = radius_5*np.cos(t+4*angle)
    jupiter.z = radius_5*np.sin(t+4*angle)

    radius_6 = 3
    saturn.x = radius_6*np.cos(t+5*angle)
    saturn.z = radius_6*np.sin(t+5*angle)

    radius_7 = 3.4
    uranus.x = radius_7*np.cos(t+6*angle)
    uranus.z = radius_7*np.sin(t+6*angle)

    radius_8 = 3.8
    neptune.x = radius_8*np.cos(t+7*angle)
    neptune.z = radius_8*np.sin(t+7*angle)
    
    # rotate the moon around the earth
    radius_moon = 0.8
    moon.x = earth.x + radius_moon*np.cos(t)
    moon.z = earth.z + radius_moon*np.sin(t)

# create a list of textures for the sun
sun_texture = [load_texture('textures/sun/sun{}.jpeg'.format(i)) for i in range(1, 5)]
# randomly select a texture for the sun
sun_texture = random.choice(sun_texture)
# create the sun
sun = Entity(model='sphere', texture=sun_texture, scale=1.5, double_sided=True)
# create a list of textures for mercury
mercury_texture = [load_texture('textures/mercury/mercury{}.jpeg'.format(i)) for i in range(1, 5)]
# randomly select a texture for mercury
mercury_texture = random.choice(mercury_texture)
# create mercury
mercury = Entity(model='sphere', texture=mercury_texture, scale=0.2, double_sided=True, parent=sun)

# create a list of textures for venus
venus_texture = [load_texture('textures/venus/venus{}.jpeg'.format(i)) for i in range(1, 5)]
# randomly select a texture for venus
venus_texture = random.choice(venus_texture)
# create venus
venus = Entity(model='sphere', texture=venus_texture, color=color.orange, scale=0.3, double_sided=True)

# earth texture
earth_texture = load_texture('textures/earth/earth.jpeg')
# create earth
earth = Entity(model='sphere', texture=earth_texture, color=color.blue, scale=0.4, double_sided=True)

# moon texture
moon_texture = load_texture('textures/moon/moon.jpeg')
# create moon
moon = Entity(model='sphere', texture=moon_texture, scale=0.1, double_sided=True, parent=earth)

# create a list of textures for mars
mars_texture = [load_texture('textures/mars/mars{}.jpeg'.format(i)) for i in range(1, 5)]
# randomly select a texture for mars
mars_texture = random.choice(mars_texture)
# create mars
mars = Entity(model='sphere', texture=mars_texture, color=color.red, scale=0.2, double_sided=True)

# create a list of textures for jupiter
jupiter_texture = [load_texture('textures/jupiter/jupiter{}.jpeg'.format(i)) for i in range(1, 5)]
# randomly select a texture for jupiter
jupiter_texture = random.choice(jupiter_texture)
# create jupiter
jupiter = Entity(model='sphere', texture=jupiter_texture, color=color.red, scale=0.8, double_sided=True)

# create a list of textures for saturn
saturn_texture = [load_texture('textures/saturn/saturn{}.jpeg'.format(i)) for i in range(1, 5)]
# randomly select a texture for saturn
saturn_texture = random.choice(saturn_texture)
# create saturn
saturn = Entity(model='sphere', texture=saturn_texture, color=color.brown, scale=0.7, double_sided=True)

# create a list of textures for uranus
uranus_texture = [load_texture('textures/uranus/uranus{}.jpeg'.format(i)) for i in range(1, 5)]
# randomly select a texture for uranus
uranus_texture = random.choice(uranus_texture)
# create uranus
uranus = Entity(model='sphere', texture=uranus_texture, color=color.cyan , scale=0.6, double_sided=True)

# create a list of textures for neptune
neptune_texture = [load_texture('textures/neptune/neptune{}.jpeg'.format(i)) for i in range(1, 5)]
# randomly select a texture for neptune
neptune_texture = random.choice(neptune_texture)
# create neptune
neptune = Entity(model='sphere', texture=neptune_texture, color=color.blue, scale=0.5, double_sided=True)



t = np.pi

app.run()

