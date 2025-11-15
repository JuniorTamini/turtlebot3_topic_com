import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class OdomListener(Node):
    def __init__(self):
        super().__init__('odom_listener')
        self.sub=self.create_subscription(Odometry,
                                          '/odom',
                                          self.callback,
                                          10)
        
    def callback(self,msg):
        x=msg.pose.pose.position.x
        y=msg.pose.pose.position.y
        self.get_logger().info(f"Odom → x={x:.2f}, y={y:.2f}")

def main():
    rclpy.init()
    node=OdomListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()