import machine
import time

def main():
    wdt = machine.WDT(timeout=10000)  # watchdog: 10 segundos
    led = machine.Pin(2, machine.Pin.OUT)
    start_time = time.time()
    
    print("Novo firmware: a correr...")
    
    while True:
        led.value(not led.value())
        wdt.feed()
        print("Novo firmware ativo... uptime:", int(time.time() - start_time), "s")
        time.sleep(1)
        
        # CRASH controlado após 5 segundos
        if time.time() - start_time > 5:
            print("Simular crash!")
            raise Exception("Crash simulado no firmware novo!")
            
if __name__ == "__main__":
    main()
