import Leap, sys, URBasic, URBasic.urScript, time, socket

host = '169.254.226.180'
#host ='192.168.12.128'
port=63352 #PORT used by robotiq gripper

robotModle = URBasic.robotModel.RobotModel()
robot = URBasic.urScriptExt.UrScriptExt(host=host,robotModel=robotModle)
robot.reset_error()


class SampleListener(Leap.Listener):

    

    def on_frame(self, controller):

        frame = controller.frame()

        for hand in frame.hands:

            x, y, z = (hand.palm_position[0]/500, hand.palm_position[1]/1000, hand.palm_position[2]/500)
            #robot.movej(pose=[z,x,y, -0,3.14,0], a=50, v=50)
            
            print(x, y, z, frame)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))
                #s.sendall(b'SET ACT 1\n')
                #time.sleep(4)
                s.sendall(b'SET SPE 200\n')
                if x > -0.34:
                    s.sendall(b'SET POS 0\n')
                elif x <= -0.34:
                    s.sendall(b'SET POS 226\n')
                s.sendall(b'GET POS\n')
                data = s.recv(2**10)
                #time.sleep(1)
            print('Gripper finger position is: ', data)

def ExampleurScriptLEAP(controller):

        listener = SampleListener()
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
    controller = Leap.Controller()
    ExampleurScriptLEAP(controller)
