import Leap, sys, URBasic, time

host = '192.168.12.128'  #Stasjonær
#host = '192.168.81.128' #Lenovo
acc = 5000
vel = 50

class SampleListener(Leap.Listener):

    def on_init(self, controller):
        pass

    def on_connect(self, controller):
        pass

    def on_disconnect(self, controller):
        pass

    def on_exit(self, controller):
        pass

    def on_frame(self, controller):

        frame = controller.frame()

        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

            print("position: %s" %(hand.palm_position))


        if not frame.hands.is_empty:
            pass

def ExampleurScript():

    robotModle = URBasic.robotModel.RobotModel()
    robot = URBasic.urScriptExt.UrScriptExt(host=host,robotModel=robotModle)
    robot.reset_error()
    print('movej with joint specification')
    robot.movej(q=[-3.14,-1.,0.5, -1.,-1.5,0], a=acc, v=vel)
    
    print('movej with pose specification')
    robot.movej(pose=[0.3,0.3,0.3, 0,3.14,0], a=acc, v=vel)
    
    robot.end_force_mode()
    robot.close()

def main():

    listener = SampleListener()
    controller = Leap.Controller()
    controller.add_listener(listener)

    print("Press Enter to quit...")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:

        controller.remove_listener(listener)    

if __name__ == '__main__':
    ExampleurScript()
    main()