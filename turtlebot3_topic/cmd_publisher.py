import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CmdPublisher(Node):
    def __init__(self):
        super().__init__('cmd_publisher')
        self.pub=self.create_publisher( Twist,
                                       'custom_cmd',
                                       10, 
                                       )
        timer_period=0.5
        self.timer=self.create_timer(timer_period,self.publish_cmd)
        

    def publish_cmd(self):
        msg=Twist()
        msg.linear.x=0.2
        msg.angular.z=0.4
        self.pub.publish(msg)
        self.get_logger().info("Command sent")

def main():
    rclpy.init()
    node=CmdPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown