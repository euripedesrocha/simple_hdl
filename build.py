import myhdl

import design

def generate():
    circuit_param = design.Parameters(nleds=9999999991)
    circuit_ports = design.CircuitPorts(circuit_param)
    myhdl.toVerilog(design.circuit, circuit_ports)

def synthesize():
    generate()

if __name__ == '__main__':
    synthesize()
