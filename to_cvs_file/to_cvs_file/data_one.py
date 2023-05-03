import rclpy
from rclpy.node import Node
from geometry_msgs.msg import WrenchStamped 
import message_filters
from std_msgs.msg import String
from message_filters import Cache, Subscriber 
from rclpy.time import Time 
from rclpy.clock import ClockType 
from rclpy.clock import ROSClock
from rclpy.duration import Duration 
import numpy as np 
import time 
import pandas as pd 
import os 
import unittest 

# ########################### CSV Createion ############################################
path = '/home/pranav/needle_steering/src/test/to_cvs_file/data/'
name = input('SPecify the file name: ')
csvname = name + ".csv"
csvFileName = os.path.join(path, csvname)

########################### METRICS VARIABLE #######################################

force_x = []
force_y = []
force_z = []
torque_x = []
torque_y = []
torque_z = []
timestamp = []
frame_id = []
g_node = None

##################################################################################

def toCSV(): 

    df_timeStamp = pd.DataFrame(timestamp, columns = ['Time'])
    df_frame_id = pd.DataFrame(frame_id, columns = ['Frame ID'])
    df_force_x = pd.DataFrame(force_x, columns = ['Force x'])
    df_force_y = pd.DataFrame(force_y, columns = ['Force y'])
    df_force_z =  pd.DataFrame(force_z, columns = ['Force z'])
    df_torque_x = pd.DataFrame(torque_x, columns=['Torque x'])
    df_torque_y = pd.DataFrame(torque_y, columns=['Torque y'])
    df_torque_z = pd.DataFrame(torque_z, columns=['Torque z'])

    df = pd.concat([df_timeStamp, df_frame_id, df_force_x, df_force_y, df_force_z, df_torque_x, df_torque_y, df_torque_z])

    df.to_csv(csvFileName, index = True)
    print('\n ...Saved metrics to CSV file...\n')


    
class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        # self.subscription = self.create_subscription(WrenchStamped,'/ati', self.listener_callback, 10)
        # self.subscription 
        # self.raw_force_sub = message_filters.Subscriber("/ati", WrenchStamped)

        # tss = message_filters.ApproximateTimeSynchronizer([self.force_sub],5, 0.1,allow_headerless=True)
        # tss.registerCallback(self.listener_callback)

        self.subcription = self.create_subscription(WrenchStamped, '/ati', self.listener_callback, 10)
        self.subcription  


    def listener_callback(self, msg1):

        force_x.append(msg1.wrench.force.x)
        force_y.append(msg1.wrench.force.y)
        force_z.append(msg1.wrench.force.z)
        torque_x.append(msg1.wrench.torque.x)
        torque_y.append(msg1.wrench.torque.y)
        torque_z.append(msg1.wrench.torque.z)
        timestamp.append(msg1.header.stamp)
        frame_id.append(msg1.header.frame_id)
        
        self.get_logger().info('I heard: "%f"'%msg1.wrench.force.y)




class TestShutdown():
    def on_shutdown_method(self):
        toCSV()

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    test_class = TestShutdown()
    rclpy.get_default_context().on_shutdown(test_class.on_shutdown_method)


    try: 
        rclpy.spin(minimal_subscriber)
    except:
        print("Exception occoured")
    
    minimal_subscriber.destroy_node()
    rclpy.shutdown()  
    
    

if __name__ == '__main__':
    main() 
  
    