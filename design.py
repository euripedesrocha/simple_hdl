import myhdl

from simple import simple

def generate():
    circuit_ports = simple.SocInterface()
    myhdl.toVerilog(simple.top_circuit, circuit_ports)

def synthesize():
    generate()

if __name__ == '__main__':
    synthesize()
