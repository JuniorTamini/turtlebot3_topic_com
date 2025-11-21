import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class laser_listener(Node):
    def __init__(self):
        super().__init__('laser_listener')
        self.sub = self.create_subscription(LaserScan, '/scan', self.callback, 10)

    def callback(self, msg: LaserScan):
        ranges = msg.ranges

        # Angle 0 = devant. Pour TurtleBot3, on prend un cône frontal.
        front_indices = range(-5, 5)  # environ 10 points au centre
        front_distances = [ranges[i] for i in front_indices if ranges[i] > 0.0]

        if front_distances:
            min_front = min(front_distances)

            if min_front < 0.3:
                self.get_logger().warn(f" Obstacle proche à {min_front:.2f} m")
            else:
                self.get_logger().info(f"Zone frontale dégagée : {min_front:.2f} m")
        else:
            self.get_logger().info("Aucune mesure laser valide devant")

def main():
    rclpy.init()
    node = laser_listener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()