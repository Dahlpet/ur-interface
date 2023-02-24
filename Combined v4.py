import Leap, sys, URBasic, URBasic.urScript, time, socket

#host = '169.254.226.180'
host = '192.168.81.128'
HOST="169.254.226.180" #replace by the IP address of the UR robot
PORT=63352 #PORT used by robotiq gripper

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #open the socket
    s.connect((HOST, PORT))
    s.sendall(b'GET POS\n')
    #s.sendall(b'SET POS 100')
    data = s.recv(2**10)


robotModle = URBasic.robotModel.RobotModel()
robot = URBasic.urScriptExt.UrScriptExt(host=host,robotModel=robotModle)
robot.reset_error()

class SampleListener(Leap.Listener):

    

    def on_frame(self, controller):

        frame = controller.frame()
        time.sleep(1)
        for hand in frame.hands:

            x, y, z = (hand.palm_position[0]/500, hand.palm_position[1]/1000, hand.palm_position[2]/500)
            robot.movej(pose=[z,x,y, -0,3.14,0], a=5000, v=5000)
            time.sleep(0.1)
            print(x, y, z, frame)
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
