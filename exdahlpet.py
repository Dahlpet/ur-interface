import URBasic
import time


host = '192.168.56.101'   #E.g. a Universal Robot offline simulator, please adjust to match your IP
acc = 10
vel = 10


def ExampleurScript():
    robotModle = URBasic.robotModel.RobotModel()
    robot = URBasic.urScriptExt.UrScriptExt(host=host,robotModel=robotModle)
    robot.reset_error()
    print('movej with joint specification')
    robot.movej(q=[-3.14,-1.,0.5, -1.,-1.5,0], a=acc, v=vel)
    
    print('movej with pose specification')
    robot.movej(pose=[0.3,0.3,0.3, 0,3.14,0], a=1.2, v=vel)
    
    print('movel with pose specification')
    robot.movel(pose=[0.3,-0.3,0.3, 0,3.14,0], a=1.2, v=vel)
                
    print('forcs_mode')
    robot.force_mode(task_frame=[0., 0., 0.,  0., 0., 0.], selection_vector=[0,0,1,0,0,0], wrench=[0., 0., -20.,  0., 0., 0.], f_type=2, limits=[2, 2, 1.5, 1, 1, 1])
    time.sleep(1)
    robot.end_force_mode()
    robot.close()
  
def ExampleExtendedFunctions():
    '''
    This is an example of an extension to the Universal Robot script library. 
    How to update the force parameters remote via the RTDE interface, 
    hence without sending new programs to the controller.
    This enables to update force "realtime" (125Hz)  
    '''
    robotModle = URBasic.robotModel.RobotModel()
    robot = URBasic.urScriptExt.UrScriptExt(host=host,robotModel=robotModle)

    print('forcs_remote')
    robot.set_force_remote(task_frame=[0., 0., 0.,  0., 0., 0.], selection_vector=[0,0,1,0,0,0], wrench=[0., 0., 20.,  0., 0., 0.], f_type=2, limits=[2, 2, 1.5, 1, 1, 1])
    robot.reset_error()
    a = 5
    upFlag = True
    while a<3:
        pose = robot.get_actual_tcp_pose()
        if pose[2]>0.1 and upFlag:
            print('Move Down')
            robot.set_force_remote(task_frame=[0., 0., 0.,  0., 0., 0.], selection_vector=[0,0,1,0,0,0], wrench=[0., 0., -20.,  0., 0., 0.], f_type=2, limits=[2, 2, 1.5, 1, 1, 1])
            a +=1
            upFlag = False
        if pose[2]<0.0 and not upFlag:
            print('Move Up')
            robot.set_force_remote(task_frame=[0., 0., 0.,  0., 0., 0.], selection_vector=[0,0,1,0,0,0], wrench=[0., 0., 20.,  0., 0., 0.], f_type=2, limits=[2, 2, 1.5, 1, 1, 1])
            upFlag = True    
    robot.end_force_mode()
    robot.reset_error()
    robot.close()
 

def ExampleFT_sensor():
    '''
    This is a small example of how to connect to a Robotiq FORCE TORQUE SENSOR and read data from the sensor.
    To run this part comment in the function call in the main call below.

    '''
    robotModle = URBasic.robotModel.RobotModel()
    robot = URBasic.urScriptExt.UrScriptExt(host=host,robotModel=robotModle,hasForceTorque=True)

    print(robotModle.dataDir['urPlus_force_torque_sensor'])
    time.sleep(1)
    print(robotModle.dataDir['urPlus_force_torque_sensor'])
    robot.close()
        

if __name__ == '__main__':
    ExampleurScript()
    ExampleExtendedFunctions()
    #ExampleFT_sensor()
    