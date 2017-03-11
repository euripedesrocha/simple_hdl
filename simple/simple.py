'''
    This is a simple led sequencer to show how to use a full myhdl flow for
    development
'''
import myhdl as hdl

class Simple(object):
    '''
        This class define our simple digital circuit
    '''

    class CircuitPorts(object):
        '''
            This is the place where we declare the circuit ports
        '''
        def __init__(self):
            self.leds = hdl.Signal(hdl.intbv(val=0, min=0, max=255))


    def __init__(self):
        self.port = Simple.CircuitPorts()

    def top_circuit(self, signals):
        pass
