
import URBasic, time


#host = '192.168.81.128' #Lenovo
host = '192.168.12.128' #Lenovo
acc = 10
vel = 10


def ExampleurScript():

    robotModle = URBasic.robotModel.RobotModel()
    robot = URBasic.urScriptExt.UrScriptExt(host=host,robotModel=robotModle)
    robot.reset_error()
    #print('movel with joint specification')
    #robot.movej(q=[-3.14,-1.,0.5, -1.,-1.5,0], r=0.2)
    a = 0
    while a < 100 :
        print('movel with pose specification')
        robot.movej(pose=[0.3,0.3,0.3, 0,3.14,0], a=acc, v=vel)
        a = a+1
    
    print('movel with pose specification')
    robot.movel(pose=[0.3,-0.3,0.3, 0,3.14,0], a=acc, v=vel)
    
    """           
    print('forcs_mode')
    robot.force_mode(task_frame=[0., 0., 0.,  0., 0., 0.], selection_vector=[0,0,1,0,0,0], wrench=[0., 0., -20.,  0., 0., 0.], f_type=2, limits=[2, 2, 1.5, 1, 1, 1])
    """
    #time.sleep(1)
    robot.end_force_mode()
    robot.close()

def ExampleExtendedFunctions():

    robotModle = URBasic.robotModel.RobotModel()
    robot = URBasic.urScriptExt.UrScriptExt(host=host,robotModel=robotModle)

    print('forcs_remote')
    robot.set_force_remote(task_frame=[0., 0., 0.,  0., 0., 0.], selection_vector=[0,0,1,0,0,0], wrench=[0., 0., 20.,  0., 0., 0.], f_type=2, limits=[2, 2, 1.5, 1, 1, 1])
    robot.reset_error()
    a = 0
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

    robotModle = URBasic.robotModel.RobotModel()
    robot = URBasic.urScriptExt.UrScriptExt(host=host,robotModel=robotModle,hasForceTorque=True)

    print(robotModle.dataDir['urPlus_force_torque_sensor'])
    time.sleep(1)
    print(robotModle.dataDir['urPlus_force_torque_sensor'])
    robot.close()
        

if __name__ == '__main__':

    ExampleurScript()
    ##ExampleExtendedFunctions()
    print("Completed!!!!!!")
 