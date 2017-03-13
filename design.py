'''
    This is a simple led sequencer to show how to use a full myhdl flow for
    development
'''
from collections import namedtuple
import myhdl as hdl

Parameters = namedtuple('Parameters', 'nleds')

class CircuitPorts(object):
    '''
        This is the place where we declare the circuit ports
    '''
    def __init__(self, parameters):
        assert parameters.nleds <= 8, 'You should use until 8 leds'
        self.leds = hdl.Signal(hdl.intbv(val=0,
                                         min=0,
                                         max=(2**parameters.nleds)-1))
        self.select = hdl.Signal(False)


def circuit(port):

    @hdl.always_comb
    def implementation():
        if port.select == 1:
            port.leds.next = 25
        else:
            port.leds.next = 0

    return implementation
