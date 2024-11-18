# HandWave: Gesture-Controlled Robotic Arm

**Overview**

This project enables you to control a robotic arm using hand gestures detected by a webcam. The system integrates OpenCV, MediaPipe, ROS, and an Arduino-controlled robotic arm. The hand gestures captured by the webcam (such as "left," "right," "up," "down," and "center") are interpreted and used to send control signals to the robotic arm, providing a touchless, intuitive user interface.


**Features**

Hand Gesture Recognition: Uses MediaPipe to detect and interpret hand gestures in real-time via webcam.

Robotic Arm Control: Uses ROS to communicate with a robotic arm controlled by an Arduino.

Real-Time Feedback: The webcam feed displays visual feedback, including bounding boxes around detected hands and directional indicators.

Arduino Integration: The robotic arm is controlled via Arduino and servo motors for smooth movement based on detected gestures.

**Technologies Used**

Hand Gesture Recognition: The webcam captures hand movements, and MediaPipe processes the video feed to detect hand landmarks. The system calculates the hand's relative position to the center of the screen to determine gestures such as "left," "right," "up," "down," and "center."

Arduino-Controlled Robotic Arm: The detected hand gestures are mapped to commands that control the robotic arm's movement. The Arduino receives these commands and adjusts the servo positions to move the robotic arm accordingly.

Real-Time Communication: The ROS framework is used to communicate between the gesture recognition system and the robotic arm, enabling seamless control in real time.

Visual Feedback: The system provides a colored bounding box around the hand, as well as directional text (e.g., "left," "right") for real-time feedback.

**Components**


Webcam: Captures the hand gestures.

Arduino: Controls the robotic arm's servos.

Servos: Physical actuators that move the robotic arm.

Computer: Runs the hand gesture recognition software using OpenCV and MediaPipe, and sends commands to the Arduino via ROS.

**Arduino Code Overview**



The Arduino code controls a robotic arm with three servos (base, shoulder, and elbow) based on commands received through ROS. The hand gesture system sends directional commands (e.g., "left," "right") to the Arduino, which moves the corresponding servos accordingly.

Base Servo: Controls the arm’s base, allowing rotation.

Shoulder Servo: Controls the arm’s shoulder joint.

Elbow Servo: Controls the arm’s elbow joint.

ROS Communication: The Arduino receives commands via ROS and moves the servos based on those commands.
