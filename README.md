# TurtleBot3 Exemple 

**Projet ROS2 – Publisher / Subscriber / LaserScan / Odom / CmdVel/ pour TurtleBot3**

---

## Description

Ce projet permet de contrôler un TurtleBot3 en ROS2 en utilisant des nodes `Publisher` et `Subscriber`.  
Il inclut :
- Commandes manuelles via un node `cmd_publisher`  
- Node `cmd_subscriber` qui relaie les commandes vers `/cmd_vel`  
- Node `odom_listener` pour écouter les informations de position  
- Node `laser_listener` pour traiter les données LaserScan  
- Possibilité de simulation avec Gazebo ou contrôle du robot réel

---

## Architecture ROS2

+--------------------+
| cmd_publisher |
| (Publisher) |
+--------------------+
|
v
custom_cmd
|
v
+--------------------+
| cmd_subscriber |
| (Subscriber -> Publisher) |
+--------------------+
|
v
/cmd_vel topic
|
v
+--------------------+
| TurtleBot3 |
| (Simulation / réel)|


Pour ceux qui n'aiment pas les graphes 🙃

- `cmd_publisher` → envoie des commandes linéaires et angulaires sur `custom_cmd`
- `cmd_subscriber` → reçoit `custom_cmd`, puis publie sur `/cmd_vel` pour le robot
- `odom_listener` → écoute `/odom` pour la position du robot
- `laser_listener` → écoute `/scan` pour détecter obstacles

---

##Installation

1. Clone ton workspace ROS2 :

bash
    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws/src
    git clone https://github.com/TON_UTILISATEUR/turtlebot3_topic_com.git


2. Installer les dépendances ROS2 si nécessaire :
bash
    sudo apt update
    sudo apt install ros-humble-turtlebot3-gazebo ros-humble-geometry-msgs ros-humble-sensor-msgs

3. Retour au workspace et build :
    cd ~/ros2_ws
    colcon build
    source install/setup.bash


## Lancer le projet

Simulation avec Gazebo

bash
    export TURTLEBOT3_MODEL=burger
    ros2 launch turtlebot3_gazebo empty_world.launch.py
    ros2 run turtlebot3_smart_controller cmd_publisher
    ros2 run turtlebot3_smart_controller cmd_subscriber
    ros2 run turtlebot3_smart_controller odom_listener
    ros2 run turtlebot3_smart_controller laser_listener


📦 Structure du projet

    turtlebot3_topic/
    ├── launch/       # fichiers launch pour simulation et nodes
    ├── turtlebot3_smart_controller/
    │   ├── __init__.py
    │   ├── cmd_publisher.py
    │   ├── robot_controller.py
    │   ├── odom_listener.py
    │   └── laser_listener.py
    ├── package.xml
    └── setup.py


🎥 Démo