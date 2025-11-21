from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='turtlebot3_topic',
             executable='cmd_publisher'),
        Node(package='turtlebot3_topic',
             executable='cmd_subscriber'),
        Node(package='turtlebot3_topic',
             executable='odom_listener'),
        Node(package='turtlebot3_topic',
             executable='laser_listener'),
    ])