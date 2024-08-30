"""
from machine import ADC, Pin
from time import *

ldr = ADC(Pin(34, Pin.IN))               # crée un objet ADC sur la broche 34
ldr.atten(ADC.ATTN_11DB)         # étendue totale : 3.3V

while True:
    photoresistance = ldr.read()        # conversion analogique-numérique 0-4095
    print("Valeur de la photorésistance = ", photoresistance)     # affichage sur la console REPL de la valeur numérique
    sleep_ms(100)

"""
from machine import ADC, Pin, PWM
from time import *

ldr = ADC(Pin(34, Pin.IN))
ldr.atten(ADC.ATTN_11DB)
pwm_led = PWM(Pin(2,mode=Pin.OUT))
pwm_led.freq(1_000)

while True:
    photoresistance = ldr.read()
    print("Valeur de la photorésistance = ", photoresistance)
    pwm_value = (photoresistance / 4095) * 1023
    pwm_led.duty(int(pwm_value))
    sleep_ms(100)
