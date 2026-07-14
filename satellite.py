from space_network_lib  import *
from relay_packet import *
from error_magement import attempt_transmission




class Satellite(SpaceEntity):
 def __init__(self, name, distance_from_earth , space_net = None ):
      super().__init__(name, distance_from_earth)
      self.space_net = space_net
    
 def receive_signal(self, packet: Packet):
        if isinstance(packet,RelayPacket):
                print(f'Unwrapping and forwarding to {packet.receiver}')
                packet = packet.data
                attempt_transmission(packet,self.space_net)
        else : print(self.name ,  "Received:", {packet})
