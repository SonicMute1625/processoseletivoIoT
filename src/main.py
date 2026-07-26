from machine import Pin, ADC
import time

LDR_PIN = 34
BTN_PIN = 15

LUX_LIVRE_LIMIAR = 500
LUX_BLOQUEIO_LIMIAR = 100

MICROPARADA_LIMIAR_MS = 5000
DEBOUNCE_MS = 50

ldr = ADC(Pin(LDR_PIN))
ldr.atten(ADC.ATTN_11DB)

btn = Pin(BTN_PIN, Pin.IN, Pin.PULL_DOWN)

estado_esteira = "LIVRE"

total_pecas = 0

inicio_bloqueio_ms = None

alerta_microparada_emitido = False

estado_botao_anterior = 0
ultimo_evento_botao_ms = 0


def ler_lux():
    GAMMA = 0.7
    RL10 = 50
    R_FIXO = 10000
    VCC = 3.3

    valor_bruto = ldr.read()
    if valor_bruto <= 0:
        valor_bruto = 1

    v_ao = (valor_bruto / 4095) * VCC

    if v_ao >= VCC:
        v_ao = VCC - 0.001

    r_ldr = R_FIXO * (VCC - v_ao) / v_ao
    lux = 10 * (r_ldr / (RL10 * 1000)) ** (-1 / GAMMA)

    return lux


def resetar_turno():
    global total_pecas, inicio_bloqueio_ms, alerta_microparada_emitido, estado_esteira

    total_pecas = 0
    inicio_bloqueio_ms = None
    alerta_microparada_emitido = False
    estado_esteira = "LIVRE"

    print("Turno resetado com sucesso. Contadores zerados.")


def processar_botao_reset():
    global estado_botao_anterior, ultimo_evento_botao_ms

    agora = time.ticks_ms()
    leitura_atual = btn.value()

    if leitura_atual != estado_botao_anterior:
        if time.ticks_diff(agora, ultimo_evento_botao_ms) > DEBOUNCE_MS:
            ultimo_evento_botao_ms = agora
            estado_botao_anterior = leitura_atual

            if leitura_atual == 1:
                resetar_turno()


def processar_sensor_lux():
    global estado_esteira, total_pecas, inicio_bloqueio_ms, alerta_microparada_emitido

    lux = ler_lux()
    agora = time.ticks_ms()

    if estado_esteira == "LIVRE":
        if lux < LUX_BLOQUEIO_LIMIAR:
            estado_esteira = "BLOQUEADO"
            inicio_bloqueio_ms = agora
            alerta_microparada_emitido = False

    elif estado_esteira == "BLOQUEADO":
        if lux > LUX_LIVRE_LIMIAR:
            total_pecas += 1
            print("Peca detectada! Total: {}".format(total_pecas))

            estado_esteira = "LIVRE"
            inicio_bloqueio_ms = None
            alerta_microparada_emitido = False
        else:
            if inicio_bloqueio_ms is not None and not alerta_microparada_emitido:
                duracao_bloqueio = time.ticks_diff(agora, inicio_bloqueio_ms)
                if duracao_bloqueio >= MICROPARADA_LIMIAR_MS:
                    print("Alerta: Micro-parada detectada!")
                    alerta_microparada_emitido = True


def main():
    print("Contador de Producao Inicializado")

    while True:
        processar_sensor_lux()
        processar_botao_reset()
        time.sleep_ms(10)


if __name__ == "__main__":
    main()
