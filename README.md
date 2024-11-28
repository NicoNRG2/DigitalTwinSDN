# DigitalTwinSDN

Digital Twin for SDN networks
• GOAL: To buid a script that allows to generate the Digital Twin of an SDN network
• Exploit RYU Northbound RestAPI to retrieve the topology- and traffic-related information
• The procedure should be completely automated
• Runtime, changes to the Physical Twin are reproduced automatically to the Digital Twin

Run on one shell:
ryu-manager ryu.app.rest_topology ryu.app.ofctl_rest ryu.app.simple_switch_13 --observe-links

Run on another shell:
sudo mn --topo tree,2 --controller remote

Run on another shell:
python3 app.py
