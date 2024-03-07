G = 6.67e-11  
MEarth = 6.0e24 
mMoon = 7.34e22  
r = 3.84e8  

grav_force = G * (MEarth * mMoon) / (r**2)

print("Gravitational Force between Earth and the Moon:", grav_force, "N")