import Leap, sys, URBasic, URBasic.urScript, time, socket

#host = '169.254.226.180'
host = '192.168.81.128'


robotModle = URBasic.robotModel.RobotModel()
robot = URBasic.urScriptExt.UrScriptExt(host=host,robotModel=robotModle)
robot.reset_error()

class SampleListener(Leap.Listener):

    def on_frame(self, controller):

        frame = controller.frame()
        
        #while hand in frame:




        for hand in frame.hands:

            x, y, z = (hand.palm_position[0]/500, hand.palm_position[1]/1000, hand.palm_position[2]/500)

            normal = hand.palm_normal
            direction = hand.direction
            rx, ry, rz = direction.pitch, (1.3*normal.roll + 2.9), direction.yaw
            while hand in frame.hands:
            
                robot.movej(pose=[z,x,y, -0,ry,0], a=0.8, v=5000)
            print(round(x, 3), round(y, 3), round(z, 3), round(rx, 3), round(ry, 3), round(rz, 3), frame)
            

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