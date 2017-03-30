import myhdl as mhd
import design 

def bench(stimulus, verification, circuit_parameters):
    signals = design.CircuitPorts(circuit_parameters)
    dut = design.circuit(signals)
    f_estimulo = stimulus(signals)
    f_verifica = verification(signals)
    return dut, f_estimulo, f_verifica

def test_initial_state():
    '''
        É importante deixarmos claro qual o objetivo do teste. Isso nos ajuda a
        recordar ou descobrir o que motivou as escolhas do desenvolvedor no
        passado.

        Esse primeiro teste valida que no início o display mostrará o valor
        zero.
    '''

    # Nessa declaração inicial temos os parâmetros do circuito sob teste
    circuit_param = design.Parameters(nleds=8)
    def stimulus(signals):
        '''
            Dado que o processo de inicialização é interno não precisamos de
            estímulo ao circuito digital nesse ponto.abs
        '''
        yield mhd.delay(1)

    def verification(signals):
        assert signals.leds == 1, 'The display must show Zero'
        yield mhd.delay(1)

    simulator = mhd.Simulation(bench(stimulus, verification, circuit_param))
    simulator.run(10)
