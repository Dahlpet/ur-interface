################################################################################
# Copyright (C) 2012-2016 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import Leap, sys, time


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']

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

        #print("Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % (
         #     frame.id, frame.timestamp, len(frame.hands), len(frame.fingers)))

        # Get hands
        for hand in frame.hands:

            #handType = "Left hand" if hand.is_left else "Right hand"

            #print("  %s, id %d, position: %s" % (
            print(hand.palm_position)

            # Get fingers
            for finger in hand.fingers:

                #print("    %s finger"% (
                    #self.finger_names[finger.type]))
                
                bone = finger.bone(3)
                y= bone.prev_joint
                #print("Bone: %s, start: %s, end: %s" % (
                    #self.bone_names[bone.type],
                    #bone.prev_joint,
                    #bone.next_joint))
            y = hand.fingers[0].bone(bone.type).next_joint
            g = hand.fingers[1].bone(bone.type).next_joint
            print("Fingertips " + str(y) + str(g))

        if not frame.hands.is_empty:
            pass

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
