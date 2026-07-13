from space_network_lib  import *






class Satellite(SpaceEntity):
    
 def receive_signal(self, packet: Packet):
        print(self.name ,  "Received:", {packet})

a = SpaceNetwork(level=1)


s1 = Satellite("Sat1",100)
s2 = Satellite("Sat2",200)

new_mess = Packet("hello",s1,s2)
a.send(new_mess)