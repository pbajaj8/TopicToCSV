import rclpy
from rclpy.node import Node
from geometry_msgs.msg import WrenchStamped 
import message_filters
from std_msgs.msg import String
from sensor_msgs.msg import JointState 
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
from tf2_ros import TransformException 
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

# ########################### CSV Createion ############################################
path = '/home/pranav/needle_steering/src/test/to_cvs_file/data/'
name = input('SPecify the file name: ')
csvname = name + ".csv"
csvFileName = os.path.join(path, csvname)

########################### METRICS VARIABLE #######################################

timestamp = []
timestamp_nano_sec = []
force_x = []
force_y = []
force_z = []
torque_x = []
torque_y = []
torque_z = []

force_x_raw = []
force_y_raw = []
force_z_raw = []
torque_x_raw = []
torque_y_raw = []
torque_z_raw = []

zaber_pos = []
zaber_vel = []

tip_trans_x = []
tip_trans_y = []
tip_trans_z = []
tip_rot_x = []
tip_rot_y = []
tip_rot_z = []
tip_rot_w = []

template_trans_x = []
template_trans_y = []
template_trans_z = []
template_rot_x = []
template_rot_y = []
template_rot_z = []
template_rot_w = []

handle_trans_x = []
handle_trans_y = []
handle_trans_z = []
handle_rot_x = []
handle_rot_y = []
handle_rot_z = []
handle_rot_w = []
##################################################################################

def toCSV(): 

    df_timeStamp = pd.DataFrame(timestamp, columns = ['Time'])
    df_timeStampNanoSec = pd.DataFrame(timestamp_nano_sec, columns = ['Time nanosec'])
    # df_force_x = pd.DataFrame(force_x, columns = ['Force x'])
    # df_force_y = pd.DataFrame(force_y, columns = ['Force y'])
    # df_force_z =  pd.DataFrame(force_z, columns = ['Force z'])
    # df_torque_x = pd.DataFrame(torque_x, columns=['Torque x'])
    # df_torque_y = pd.DataFrame(torque_y, columns=['Torque y'])
    # df_torque_z = pd.DataFrame(torque_z, columns=['Torque z'])

    # df_force_x_raw = pd.DataFrame(force_x_raw, columns = ['Force x (Raw)'])
    # df_force_y_raw = pd.DataFrame(force_y_raw, columns = ['Force y (Raw)'])
    # df_force_z_raw =  pd.DataFrame(force_z_raw, columns = ['Force z (Raw)'])
    # df_torque_x_raw = pd.DataFrame(torque_x_raw, columns=['Torque x (Raw)'])
    # df_torque_y_raw = pd.DataFrame(torque_y_raw, columns=['Torque y (Raw)'])
    # df_torque_z_raw = pd.DataFrame(torque_z_raw, columns=['Torque z (Raw)'])

    df_zaber_pos = pd.DataFrame(zaber_pos, columns=['Zaber pos'])
    df_zaber_vel = pd.DataFrame(zaber_vel, columns=['Zaber vel']) 

    df_tip_trans_x = pd.DataFrame(tip_trans_x, columns = ['Tip trans x'])
    df_tip_trans_y = pd.DataFrame(tip_trans_y, columns = ['Tip trans y'])
    df_tip_trans_z = pd.DataFrame(tip_trans_z, columns = ['Tip trans z'])
    df_tip_rot_x = pd.DataFrame(tip_rot_x, columns = ['Tip rot x'])
    df_tip_rot_y = pd.DataFrame(tip_rot_y, columns = ['Tip rot y'])
    df_tip_rot_z = pd.DataFrame(tip_rot_z, columns = ['Tip rot z'])
    df_tip_rot_w = pd.DataFrame(tip_rot_w, columns = ['Tip rot w'])

    # df_template_trans_x = pd.DataFrame(template_trans_x, columns = ['Template trans x'])
    # df_template_trans_y = pd.DataFrame(template_trans_y, columns = ['Template trans y'])
    # df_template_trans_z = pd.DataFrame(template_trans_z, columns = ['Template trans z'])
    # df_template_rot_x = pd.DataFrame(template_rot_x, columns = ['Template rot x'])
    # df_template_rot_y = pd.DataFrame(template_rot_y, columns = ['Template rot y'])
    # df_template_rot_z = pd.DataFrame(template_rot_z, columns = ['Template rot z'])
    # df_template_rot_w = pd.DataFrame(template_rot_w, columns = ['Template rot w'])

    df_handle_trans_x = pd.DataFrame(handle_trans_x, columns = ['Handle trans x'])
    df_handle_trans_y = pd.DataFrame(handle_trans_y, columns = ['Handle trans y'])
    df_handle_trans_z = pd.DataFrame(handle_trans_z, columns = ['Handle trans z'])
    df_handle_rot_x = pd.DataFrame(handle_rot_x, columns = ['Handle rot x'])
    df_handle_rot_y = pd.DataFrame(handle_rot_y, columns = ['Handle rot y'])
    df_handle_rot_z = pd.DataFrame(handle_rot_z, columns = ['Handle rot z'])
    df_handle_rot_w = pd.DataFrame(handle_rot_w, columns = ['Handle rot w'])



    # df = pd.concat([df_timeStamp, df_force_x, df_force_y, df_force_z, df_torque_x, df_torque_y, df_torque_z, df_force_x_raw, df_force_y_raw, df_force_z_raw,
    #                 df_torque_x_raw, df_torque_y_raw, df_torque_z_raw, df_zaber_pos, df_zaber_vel, df_tip_trans_x,df_tip_trans_y,df_tip_trans_z,df_tip_rot_x,
    #                 df_tip_rot_y,df_tip_rot_z,df_tip_rot_w, df_template_trans_x,df_template_trans_y,df_template_trans_z,df_template_rot_x,df_template_rot_y,
    #                 df_template_rot_z,df_template_rot_w, df_handle_trans_x,df_handle_trans_y,df_handle_trans_z,df_handle_rot_x, df_handle_rot_y,
    #                 df_handle_rot_z, df_handle_rot_w],axis=1,sort=False)

    df = pd.concat([df_timeStamp, df_timeStampNanoSec, df_zaber_pos, df_zaber_vel, df_tip_trans_x,df_tip_trans_y,df_tip_trans_z,df_tip_rot_x,
                     df_tip_rot_y,df_tip_rot_z,df_tip_rot_w, df_handle_trans_x,df_handle_trans_y,df_handle_trans_z,df_handle_rot_x, df_handle_rot_y,
                     df_handle_rot_z, df_handle_rot_w],axis=1,sort=False)

    df.to_csv(csvFileName, index = True)
    print('\n ...Saved metrics to CSV file...\n')


    
class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')

        #self.force_sub = message_filters.Subscriber(self, WrenchStamped,"/ati")
        #self.force_raw_sub = message_filters.Subscriber(self, WrenchStamped, "/ati_raw")
        self.joint_state = message_filters.Subscriber(self, JointState, "/joint_state")
        
        
        ## ts = message_filters.ApproximateTimeSynchronizer([self.force_sub, self.force_raw_sub, self.joint_state],1,0.1,allow_headerless=True)
        ts = message_filters.ApproximateTimeSynchronizer([self.joint_state],1,0.1,allow_headerless=True)
        
        ts.registerCallback(self.listener_callback)

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)






    #def listener_callback(self, msg1, msg2, msg3):

    def listener_callback(self, msg3):
        #ati
        # force_x.append(msg1.wrench.force.x)
        # force_y.append(msg1.wrench.force.y)
        # force_z.append(msg1.wrench.force.z)
        # torque_x.append(msg1.wrench.torque.x)
        # torque_y.append(msg1.wrench.torque.y)
        # torque_z.append(msg1.wrench.torque.z)
        # timestamp.append(msg1.header.stamp)
        #ati_raw
        # force_x_raw.append(msg2.wrench.force.x)
        # force_y_raw.append(msg2.wrench.force.y)
        # force_z_raw.append(msg2.wrench.force.z)
        # torque_x_raw.append(msg2.wrench.torque.x)
        # torque_y_raw.append(msg2.wrench.torque.y)
        # torque_z_raw.append(msg2.wrench.torque.z)
        #Zaber 

        

        #tip
        try: 
            t = self.tf_buffer.lookup_transform("base", "tip", rclpy.time.Time())

            try: 
                t2 = self.tf_buffer.lookup_transform("base", "handle", rclpy.time.Time())

                tip_trans_x.append(t.transform.translation.x)
                tip_trans_y.append(t.transform.translation.y)
                tip_trans_z.append(t.transform.translation.z)
                tip_rot_x.append(t.transform.rotation.x)
                tip_rot_y.append(t.transform.rotation.y)
                tip_rot_z.append(t.transform.rotation.z)
                tip_rot_w.append(t.transform.rotation.w)

                zaber_pos.append(msg3.position[0])
                zaber_vel.append(msg3.velocity[0])
                timestamp.append(msg3.header.stamp.sec) 
                timestamp_nano_sec.append(msg3.header.stamp.nanosec) 

                handle_trans_x.append(t2.transform.translation.x)
                handle_trans_y.append(t2.transform.translation.y)
                handle_trans_z.append(t2.transform.translation.z)
                handle_rot_x.append(t2.transform.rotation.x)
                handle_rot_y.append(t2.transform.rotation.y)
                handle_rot_z.append(t2.transform.rotation.z)
                handle_rot_w.append(t2.transform.rotation.w)

            
            except: 
                self.get_logger().info('Could not find the handle transform')
                return

        except TransformException as ex: 
            self.get_logger().info('Could not find the tip transform')
            return

        


        #template
        # try: 
        #     t1 = self.tf_buffer.lookup_transform("base", "template", rclpy.time.Time())
        # except TransformException as ex: 
        #     self.get_logger().info('Could not find the template transform')
        #     return

        # template_trans_x.append(t1.transform.translation.x)
        # template_trans_y.append(t1.transform.translation.y)
        # template_trans_z.append(t1.transform.translation.z)
        # template_rot_x.append(t1.transform.rotation.x)
        # template_rot_y.append(t1.transform.rotation.y)
        # template_rot_z.append(t1.transform.rotation.z)
        # template_rot_w.append(t1.transform.rotation.w)


        #handle
        # try: 
        #     t2 = self.tf_buffer.lookup_transform("base", "handle", rclpy.time.Time())
        # except TransformException as ex: 
        #     self.get_logger().info('Could not find the handle transform')
        #     return

        # handle_trans_x.append(t2.transform.translation.x)
        # handle_trans_y.append(t2.transform.translation.y)
        # handle_trans_z.append(t2.transform.translation.z)
        # handle_rot_x.append(t2.transform.rotation.x)
        # handle_rot_y.append(t2.transform.rotation.y)
        # handle_rot_z.append(t2.transform.rotation.z)
        # handle_rot_w.append(t2.transform.rotation.w)

        # self.get_logger().info('Tip position: "%f"'%t2.transform.translation.x)

        self.get_logger().info('Recording the data')





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
  
    