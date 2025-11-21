from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'turtlebot3_topic'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name),glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='junior',
    maintainer_email='junior@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'cmd_publisher=turtlebot3_topic.cmd_publisher:main',
            'cmd_subscriber=turtlebot3_topic.cmd_subscriber:main',
            'odom_listener=turtlebot3_topic.odom_listener:main',
            'laser_listener=turtlebot3_topic.laser_listener:main',

        ],
    },
)
