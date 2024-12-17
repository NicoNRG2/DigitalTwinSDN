from flask import Flask, jsonify, render_template, request
import requests
import threading
import time

app = Flask(__name__)

# Variabile globale per la topologia
network_topology = {"switches": [], "hosts": [], "links": []}

def fetch_topology():
    global network_topology
    while True:
        try:
            switches = requests.get('http://localhost:8080/v1.0/topology/switches').json()
            hosts = requests.get('http://localhost:8080/v1.0/topology/hosts').json()
            links = requests.get('http://localhost:8080/v1.0/topology/links').json()

            # Filtra i link duplicati
            unique_links = []
            seen_links = set()
            for link in links:
                src = link['src']['dpid'] + link['src']['port_no']
                dst = link['dst']['dpid'] + link['dst']['port_no']
                if (dst, src) not in seen_links:
                    seen_links.add((src, dst))
                    unique_links.append(link)

            # Aggiungi i link dagli host agli switch
            host_links = []
            for host in hosts:
                host_link = {
                    "src": {"id": host["mac"]},
                    "dst": {
                        "id": host["port"]["dpid"],
                        "port_no": host["port"]["port_no"]
                    }
                }
                host_links.append(host_link)

            # Combina link switch-switch e host-switch
            all_links = unique_links + host_links

            network_topology = {
                "switches": switches,
                "hosts": hosts,
                "links": all_links
            }
        except Exception as e:
            print(f"Errore nel recupero della topologia: {e}")

        time.sleep(5)  # Aggiorna ogni 5 secondi

# Endpoint per il frontend
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint API
@app.route('/api/topology', methods=['GET'])
def get_topology():
    return jsonify(network_topology)

@app.route('/api/traffic_stats', methods=['GET'])
def get_traffic_stats():
    try:
        # Recupera la lista degli switch
        switches = requests.get('http://localhost:8080/v1.0/topology/switches').json()
        
        traffic_stats = {}
        for switch in switches:
            dpid = switch['dpid']
            response = requests.get(f'http://localhost:8080/stats/port/{dpid}')
            if response.status_code == 200:
                traffic_stats[dpid] = response.json().get(str(dpid), [])
            else:
                traffic_stats[dpid] = []
        
        return jsonify(traffic_stats)
    except Exception as e:
        return jsonify({'error': f'Failed to fetch traffic stats: {str(e)}'}), 500

if __name__ == '__main__':
    # Thread separato per aggiornare la topologia
    threading.Thread(target=fetch_topology, daemon=True).start()
    app.run(debug=True, host='0.0.0.0', port=5000)