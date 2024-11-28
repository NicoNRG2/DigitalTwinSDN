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


def main():
    password = input("Inserisci la password di amministratore: ")
    mn_process = start_mininet(password)

    try:
        while True:
            print("\n--- MENU ---")
            print("1. Disattiva un link (link A B down)")
            print("2. Attiva un link (link A B up)")
            print("3. Esci")
            choice = input("Scegli un'opzione: ")

            if choice == "1":
                handle_link(mn_process, "down")
            elif choice == "2":
                handle_link(mn_process, "up")
            elif choice == "3":
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
