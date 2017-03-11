'''
    This is a simple led sequencer to show how to use a full myhdl flow for
    development
'''
import myhdl

class Simple(object):
    '''
        This class define our simple digital
    '''
    
    class CircuitPorts(object):
        '''
            This is the place where we declare the circuit ports
        '''
        def __init__(self):
            pass


    def __init__(self):
        self.port = Simple.CircuitPorts()

    def top_circuit(self, signals):
        pass
