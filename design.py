import myhdl

from simple.simple import Simple

def generate():
    simple_circuit = Simple()
    myhdl.toVerilog(simple_circuit.top_circuit, simple_circuit.port)

def synthesize():
    generate()

if __name__ == '__main__':
    synthesize()
