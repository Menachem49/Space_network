

from satellite import *
from error_magement import *
a = SpaceNetwork(level=1)


s1 = Satellite("Sat1",100)
s2 = Satellite("Sat2",200)

new_mess = Packet("hello",s1,s2)
# a.send(new_mess)

b = SpaceNetwork(level=2)

attempt_transmission(new_mess,b)


