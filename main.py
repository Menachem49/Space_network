

from satellite import *
from error_magement import *
# a = SpaceNetwork(level=1)


# s1 = Satellite("Sat1",100)
# s2 = Satellite("Sat2",200)

# new_mess = Packet("hello",s1,s2)
# a.send(new_mess)

# b = SpaceNetwork(level=2)

# attempt_transmission(new_mess,b)



# c = SpaceNetwork(level=3)
# try :
#     attempt_transmission(new_mess,c)
# except BrokenConnectionError:
#     print("Transmission failed")




d  = SpaceNetwork(level=4)
earth = Satellite('earth',0,d)
s1 = Satellite("Sat1",100)
s2 = Satellite("Sat2",200)

p_final = Packet("hello from earth !!",s1,s2)
p_earth_to_s1 = RelayPacket(p_final,earth,s1)


try :
   earth.receive_signal(p_earth_to_s1)
except BrokenConnectionError:
    print("Transmission failed")



