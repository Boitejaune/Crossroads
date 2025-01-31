import time
import os
import signal

# Définition des différents handlers pour chaque signal
def handler_sigusr1(signum, frame):
    print("Signal SIGUSR1 reçu")
    # Ajoutez ici le code pour gérer le signal SIGUSR1

def handler_sigusr2(signum, frame):
    print("Signal SIGUSR2 reçu")
    # Ajoutez ici le code pour gérer le signal SIGUSR2

def handler_sigterm(signum, frame):
    print("Signal SIGTERM reçu")
    # Ajoutez ici le code pour gérer le signal SIGTERM

def handler_sigint(signum, frame):
    print("Signal SIGINT reçu")
    # Ajoutez ici le code pour gérer le signal SIGINT



# Processus de gestion des feux avec alternance simple
# Gérer les feux de circulation avec alternance toutes les 5 secondes, met à jour les états dans la queue (light_queue
def lights_process(light_queue):
    current_ns = "RED"
    current_we = "GREEN"

    while True:
        time.sleep(5)  # Intervalle de 5 secondes pour changer les feux
            # Alternance des feux
        
        # Enregistrement des handlers pour différents signaux
        signal.signal(signal.SIGUSR1, handler_sigusr1)
        signal.signal(signal.SIGUSR2, handler_sigusr2)
        signal.signal(signal.SIGTERM, handler_sigterm)
        signal.signal(signal.SIGINT, handler_sigint)

        if current_ns == "RED":
            current_ns = "GREEN"
            current_we = "RED"
        else:
            current_ns = "RED"
            current_we = "GREEN"
        # Mettre à jour les feux dans la queue
        print(current_ns,current_we)
        light_queue.put(current_ns)
        light_queue.put(current_we)
