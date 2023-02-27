import Leap, sys, time, math

class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    last_print_time = 0.0
    print_interval = 1.0 # Print once per second

    def on_init(self, controller):
        pass

    def on_connect(self, controller):
        pass

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        pass

    def on_exit(self, controller):
        pass

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        # Get hands
        for hand in frame.hands:
            # Only print information to the screen once per second
            if (time.time() - self.last_print_time) > self.print_interval:
                self.last_print_time = time.time()

                handType = "Left hand" if hand.is_left else "Right hand"

                print("  %s, id %d, position: %s" % (
                    handType, hand.id, hand.palm_position))

                # Get the hand's normal vector and direction
                normal = hand.palm_normal
                direction = hand.direction

                # Calculate the hand's pitch, roll, and yaw angles
                print("  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
                    direction.pitch * Leap.RAD_TO_DEG,
                    normal.roll * Leap.RAD_TO_DEG,
                    direction.yaw * Leap.RAD_TO_DEG))

                # Get arm bone
                arm = hand.arm
                print("  Arm direction: %s, wrist position: %s, elbow position: %s" % (
                    arm.direction,
                    arm.wrist_position,
                    arm.elbow_position))

                # Get fingers
                for finger in hand.fingers:

                    print("    %s finger, id: %d, length: %fmm, width: %fmm" % (
                        self.finger_names[finger.type],
                        finger.id,
                        finger.length,
                        finger.width))

                    # Get bones
                    for b in range(0, 4):
                        bone = finger.bone(b)
                        print("      Bone: %s, start: %s, end: %s, direction: %s" % (
                            self.bone_names[bone.type],
                            bone.prev_joint,
                            bone.next_joint,
                            bone.direction))
                        
                t = hand.fingers[0].bone(bone.type).next_joint
                i = hand.fingers[1].bone(bone.type).next_joint
            #diff = t - i
                d = math.sqrt(((i[0]-t[0])**2 + (i[1]-t[1])**2 + (i[2]-t[2])**2))
                if d > 120:
                    d = 120
                if d < 15:
                    d = 15

            #print("Fingertips " + str(t) + str(i))
            #print(diff)
                print(round(d,0))

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print("Press Enter to quit...")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()
