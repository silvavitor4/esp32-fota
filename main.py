import wifi
import update
import time


SSID = "MEO-36E830"
PASSWORD = "186fb5330d"

URL_BASE = "https://raw.githubusercontent.com/silvavitor4/esp32-fota/refs/heads/main"

print("🟡 A iniciar main.py")

# Liga à internet
print("📡 A ligar ao Wi-Fi...")
wifi.liga_wifi(SSID, PASSWORD)

# Loop principal do programa (exemplo)
contador = 0
while True:
    print(f"⚙️  Programa principal a correr... contador: {contador}")
    contador += 1

    # A cada 10 ciclos, verifica se há nova versão
    if contador % 10 == 0:
        print("🕵️ A verificar versões...")

        versao_remota = update.obter_versao_remota(f"{URL_BASE}/version.txt")
        versao_local = update.obter_versao_local()

        print(f"🔢 Versão local: {versao_local}")
        print(f"🌐 Versão remota: {versao_remota}")

        if versao_remota and update.ha_update(versao_remota, versao_local):
            print("🚀 Nova versão encontrada! A atualizar...")
            update.atualizar_e_reiniciar(versao_remota, URL_BASE)
        else:
            print("✅ Já está atualizado.")

 print("✅ NEW VERSION.")

    time.sleep(1)

