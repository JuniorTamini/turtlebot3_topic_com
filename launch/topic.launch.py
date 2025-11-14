from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='turtlebot3_topic',
             executable='cmd_publisher'),
        Node(package='turtlebot3_topic',
             executable='cmd_subscriber'),
        #Node(package='turtlebot3_smart_controller',
             #executable='odom_listener'),
        #Node(package='turtlebot3_smart_controller',
             #executable='laser_listener'),
    ])