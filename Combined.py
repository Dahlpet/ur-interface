import Leap, sys, URBasic, URBasic.urScript

#host = '169.254.226.180'
host = '192.168.81.128'

robotModle = URBasic.robotModel.RobotModel()
robot = URBasic.urScriptExt.UrScriptExt(host=host,robotModel=robotModle)

class SampleListener(Leap.Listener):

    def on_frame(self, controller):
 
        frame = controller.frame()
        for hand in frame.hands:

            x, y, z = (format(hand.palm_position[0]/500, '.3f'), format(hand.palm_position[1]/1000, '.3f'), format(hand.palm_position[2]/500, '.3f'))
            print(z, x, y)
     
def ExampleurScriptLEAP():

        listener = SampleListener()
        controller = Leap.Controller()
        controller.add_listener(listener)

        robot.movel(pose=[0.6,0.2,0.4, -0,3.14,0], a=5, v=500)
        robot.movel(pose=[0.3,-0.3,0.3, 0,3.14,0], a=5, v=500)
        robot.close()
     
        print("Press Enter to quit...")
        try:
            sys.stdin.readline()
        except KeyboardInterrupt:
            pass
        finally:
            controller.remove_listener(listener)
        SampleListener.frame = 0

if __name__ == '__main__':
    ExampleurScriptLEAP()
