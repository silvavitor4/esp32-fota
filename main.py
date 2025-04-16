import wifi
import update
import time

SSID = "MEO-36E830"
PASSWORD = "186fb5330d"

URL_BASE = "https://raw.githubusercontent.com/TEU_UTILIZADOR/esp32-fota/main"

# Liga à internet
wifi.liga_wifi(SSID, PASSWORD)

# Loop principal do programa (exemplo)
contador = 0
while True:
    print("A correr programa principal... contador:", contador)
    contador += 1

    # A cada X ciclos, verificar se há nova versão
    if contador % 10 == 0:
        print("🕵️ A verificar se há nova versão...")
        versao_remota = update.obter_versao_remota(f"{URL_BASE}/version.txt")
        versao_local = update.obter_versao_local()

        if versao_remota and update.ha_update(versao_remota, versao_local):
            print("🚀 Nova versão disponível!")
            update.atualizar_e_reiniciar(versao_remota, URL_BASE)

    time.sleep(1)
