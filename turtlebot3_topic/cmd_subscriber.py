import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CmdSubscriber(Node):
    def __init__(self):
        super().__init__('cmdsubscriber')
        self.sub=self.create_subscription( Twist,
                                           'custom_cmd',
                                            self.callback,
                                            10)
        self.cm_pub=self.create_publisher(Twist,
                                          '/cmd_vel',
                                          10)
        
        
    def callback(self,msg):
        self.cm_pub.publish(msg)
        self.get_logger().info(f"Command sent to the robot: v={msg.linear.x}, w={msg.angular.z}")

def main():
    rclpy.init()
    node=CmdSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()