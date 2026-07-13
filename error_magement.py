class BrokenConnectionError(Exception):
    pass

from satellite import *
import time
def attempt_transmission(new_mess,space_net):
    try :
        space_net.send(new_mess)
        return
    except DataCorruptedError as e:
        print(e)
        attempt_transmission(new_mess,space_net)
    except TemporalInterferenceError as e :
        print(e)
        time.sleep(2)
        attempt_transmission(new_mess,space_net)
        
    except OutOfRangeError :
        print("Target out of range")
        raise BrokenConnectionError
    except LinkTerminatedError :
        print("Link lost")
        raise BrokenConnectionError
            
