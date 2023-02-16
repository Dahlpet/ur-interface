import Leap, sys, URBasic, URBasic.urScript, time

host = '192.168.12.128'

robotModle = URBasic.robotModel.RobotModel()
robot = URBasic.urScriptExt.UrScriptExt(host=host,robotModel=robotModle)

class SampleListener(Leap.Listener):

    def on_frame(self, controller):

        frame = controller.frame()
        for hand in frame.hands:

            x, y, z = (hand.palm_position[0]/500, hand.palm_position[1]/1000, hand.palm_position[2]/500)
            print(x, y, z, frame)
            robot.movej(pose=[z,x,y, -0,3.14,0], a=5000, v=5000)
        time.sleep(0.1)    
   
   
def ExampleurScriptLEAP():

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
            robot.close()
        SampleListener.frame = 0

if __name__ == '__main__':
    ExampleurScriptLEAP()