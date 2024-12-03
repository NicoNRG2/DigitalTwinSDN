# DigitalTwinSDN



Run on one shell:


Run on another shell:
python3 app.py


Run on another shell:
python3 cli.py



/////////////////////////////////////////////////////////

# DigitalTwin SDN
![Topology](/images/topo2.png) 


## Index
- [Project Description](#Project-Description)
- [Link](#Link)
- [Implementation Details](#Implementation-Details)
- [Project Layout](#Project-Layout)
- [Installation](#Installation)
- [Demo](#Demo)
- [Contacts](#Contacts)

## Project Description

This is the project of the Softwarized and Virtualized Mobile Networks course of the University of Trento.
The main goal of this project is to build a script that, using the RYU Northbound RestAPI and retrieving the topology anche the traffic informations, allows to generate the Digital Twin of a  SDN network.
This procedure has to be completely automated: runtime, changes to the Physical Twin are reproduced automatically to the Digital Twin


[Back to the index](#Index)


## Link

[**Presentation Link**](https://)

[**Demo Link**](https://) 

[Back to the index](#Index)

## Implementation Details
**ENVIRONMENT:**

This project makes substantial use of ComNetsEmu and Mininet. ComNetsEmu is a tested and network emulator designed for the NFV/SDN teaching book "Computing in Communication Networks: From Theory to Practice". The design focuses on emulating all the applications on a single computer. ComNetsEmu extends the famous Mininet network emulator. Mininet creates a realistic virtual network, running real kernel, switch and application code, on a single machine. The programming language used is Python. The project was developed in a dedicated virtual machine with Linux operating system.

**NETWORK DESCRIPTION:**

The phisical network is defined in the script CLI.PY, by default it is a tree topology with a root switch and 2 switch connected to it. The last 2 switch has 2 hosts connected. It is possibile to change this topology by modifying the specific line of code and the system will continue to work properly.


**CLI:**

The user can interact with the system with a Command Line Interface, trrough which he can activate/deactivate the links. 
Mininet considers links only the connection between swithes, so we can't affect links that connect switches and hosts.


**NETWORK VISUALIZATION:**


the Digital Twin of the Phisical Twin can be viewed via a web page.
Every time the user activate/deactivate a link, the topology of the Digital Twin is automatically updated, according to the changes made.

Every time the user changes mode, a web server is automatically started which graphically displays the network topology and active slices.

![Topology](/images/server.png) 



[Back to the index](#Index)


## Project Layout
![Project Layout](/images/tree.png)


**app.py:** spiegare

**index.html:** allows to view the active topology via the web.

**cli.py:** script for interacting with the system



[Back to the index](#Index)


## Installation
You can run this project by following this steps:
1. Install comnetsemu using VirtualBox (option A) at this [link](https://www.granelli-lab.org/researches/relevant-projects/comnetsemu-labs)

2. download this project via git commands. Then, open 3 terminals in this directory:

```
cd /home/comnetsemu/comnetsemu/app/DigitalTwinSDN
```

3. In the first terminal, start the controller:

```
ryu-manager ryu.app.rest_topology ryu.app.ofctl_rest ryu.app.simple_switch_13 --observe-links
```


4. In the second terminal, start the application:

```
python3 app.py
```
Now it's possible to view the digital twin topology via web at
```
http://localhost:5000
```

5. In the third terminal, start the CLI:

```
python3 cli.py
```
If required, insert the password, by default is ``` comnetsemu ```
A menù will appear. The user can follow the istruction to activate/deactivate a link.

[Back to the index](#Index)

## Demo

This section will explain a complete usage example of this application.
It is based on the demo video in the "Link" section.
Suppose you have already done the installation and have 2 open terminals (as explained in the previous section).

| Firts terminal                                                                     | Second terminal                                     |
|------------------------------------------------------------------------------------|-----------------------------------------------------|
|  1. Run: ```make```                                   |  2. Run: ```python3 run.py```. The CLI will appear  ![menu](/images/menu.png)
|  4. Run diagnostic commands, such as ```pingall``` or ```iperf h1 h4```                                                |  3. Choose a mode, for example:   ```1```. A web browser will appear to graphically display the active slices based on the chosen mode                                                           |
|  ![ping](/images/ping1.png)  ![iperf](/images/iperf1.png)        |    ![topo](/images/topo1.png)         |       
|5. Repeat steps 3 and 4 to test all modes|      |                                          
|6. Close mininet: ```exit``` | Close the CLI with the option:  ```4``` |
       

Note 1: The ```iperf <host1> <host2>``` command will not give any results if executed with two hosts which, based on the active slices and the network topology, cannot communicate with each other. You will need to stop it manually with ```Ctrl+C```

Note 2: ```pingall``` wastes time trying to get all hosts to communicate with each other: the following command is an alternative to test communication between 2 hosts:
```<host1> ping <host2>```

[Back to the index](#Index)

## Contacts

Riccardo Zannoni - riccardo.zannoni@studenti.unitn.it

[Back to the index](#Index)

