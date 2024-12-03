import pexpect

def start_mininet(password):
    """Avvia Mininet e ritorna l'oggetto pexpect."""
    print("Avviando Mininet...")
    mn_command = "sudo mn --topo tree,2 --controller remote"
    mn_process = pexpect.spawn(mn_command, timeout=None)  # Attendi indefinitamente

    # Gestisci richiesta della password
    index = mn_process.expect(["[Pp]assword", r"[Mm]ininet>"])
    if index == 0:  # Password richiesta
        mn_process.sendline(password)
        mn_process.expect(r"[Mm]ininet>", timeout=None)

    print("Mininet avviato con successo!")
    return mn_process


def handle_link(mn_process, action):
    """Gestisci disattivazione o attivazione di un link."""
    src = input("Inserisci il nome del primo switch (es. s1): ")
    dst = input("Inserisci il nome del secondo switch (es. s2): ")
    command = f"link {src} {dst} {action}"
    print(f"Eseguo comando: {command}")
    mn_process.sendline(command)
    mn_process.expect(r"[Mm]ininet>", timeout=None)  # Aspetta indefinitamente


def add_switch(mn_process):                                                 #NON VA
    """Aggiungi uno switch alla topologia."""
    new_switch = input("Inserisci il nome del nuovo switch (es. s4): ")
    existing_switch = input("A quale switch esistente vuoi connettere il nuovo switch? (es. s1): ")

    # Aggiungi il nuovo switch
    command = f"addSwitch {new_switch}"
    print(f"Eseguo comando: {command}")
    mn_process.sendline(command)
    mn_process.expect(r"[Mm]ininet>", timeout=None)

    # Connetti il nuovo switch a uno switch esistente
    command = f"addLink {new_switch} {existing_switch}"
    print(f"Eseguo comando: {command}")
    mn_process.sendline(command)
    mn_process.expect(r"[Mm]ininet>", timeout=None)

    # Chiedi il numero di host da connettere al nuovo switch
    num_hosts = int(input(f"Quanti host vuoi connettere a {new_switch}? "))
    for i in range(1, num_hosts + 1):
        host_name = f"h{len(new_switch) + i}"  # Crea un nome unico per l'host
        print(f"Aggiungo host {host_name} e lo connetto a {new_switch}...")
        mn_process.sendline(f"addHost {host_name}")
        mn_process.expect(r"[Mm]ininet>", timeout=None)
        mn_process.sendline(f"addLink {host_name} {new_switch}")
        mn_process.expect(r"[Mm]ininet>", timeout=None)


def main():
    password = input("Inserisci la password di amministratore: ")
    mn_process = start_mininet(password)

    try:
        while True:
            print("\n--- MENU ---")
            print("1. Disattiva un link (link A B down)")
            print("2. Attiva un link (link A B up)")
            print("3. Aggiungi uno switch")                 #NON VA
            print("4. Esci")
            choice = input("Scegli un'opzione: ")

            if choice == "1":
                handle_link(mn_process, "down")
            elif choice == "2":
                handle_link(mn_process, "up")
            elif choice == "3":
                add_switch(mn_process)
            elif choice == "4":
                print("Arresto di Mininet...")
                mn_process.sendline("exit")
                mn_process.expect(pexpect.EOF)
                print("Mininet arrestato.")
                break
            else:
                print("Scelta non valida. Riprova.")
    except KeyboardInterrupt:
        print("\nInterruzione manuale. Arresto di Mininet...")
        mn_process.sendline("exit")
        mn_process.expect(pexpect.EOF)
        print("Mininet arrestato.")


if __name__ == "__main__":
    main()