# Variabili
RYU_CMD = ryu-manager ryu.app.rest_topology ryu.app.ofctl_rest ryu.app.simple_switch_13 --observe-links
APP_CMD = python3 app.py
CLI_CMD = python3 cli.py

.PHONY: all clean run stop

# Regola principale
all: clean run

# Pulizia di Mininet
clean:
	sudo mn -c

# Avvio dei processi in background e CLI in primo piano
run:
	@echo "Avvio Ryu in background..."
	$(RYU_CMD) > /dev/null 2>&1 & echo $$! > ryu.pid
	@echo "Avvio app.py in background..."
	$(APP_CMD) > /dev/null 2>&1 & echo $$! > app.pid
	@echo "Avvio CLI..."
	$(CLI_CMD)

# Arresto dei processi
stop:
	@echo "Interrompo Ryu..."
	@if [ -f ryu.pid ]; then kill $$(cat ryu.pid) && rm ryu.pid; fi
	@echo "Interrompo app.py..."
	@if [ -f app.pid ]; then kill $$(cat app.pid) && rm app.pid; fi
