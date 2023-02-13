import URBasic

host = '192.168.12.128'
acc, vel = 5, 5

def Testing():

    robotModle = URBasic.robotModel.RobotModel()
    robot = URBasic.urScriptExt.UrScriptExt(host=host,robotModel=robotModle)
    robot.reset_error()
    robot.close()

if __name__ == '__main__':
    Testing()