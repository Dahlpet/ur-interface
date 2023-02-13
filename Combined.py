import Leap, sys, URBasic, URBasic.urScript

host = '192.168.12.128'

class SampleListener(Leap.Listener):

    def on_frame(self, controller):
        x = [None]
        y = [None]
        z = [None]
        frame = [None]
    

        frame = controller.frame()
        for hand in frame.hands:

            a=500
            x, y, z =(format(hand.palm_position[0]/a, '.3f'), format(hand.palm_position[1]/a, '.3f'), format(hand.palm_position[2]/a, '.3f'))
            print(frame, x, y, z)

    """
    def val(self, frame, x, z, y):
        self.frame = frameNR
        self.pos = pos
        print(frameNR, pos)
    """

def ExampleurScriptLEAP():

        robotModle = URBasic.robotModel.RobotModel()
        robot = URBasic.urScriptExt.UrScriptExt(host=host,robotModel=robotModle)
        robot.reset_error()

        listener = SampleListener()
        controller = Leap.Controller()
        controller.add_listener(listener)

        robot.movel(pose=[0.6,0.2,0.4, -0,3.14,0], a=5, v=5)
        robot.movel(pose=[0.3,-0.3,0.3, 0,3.14,0], a=5, v=5)
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