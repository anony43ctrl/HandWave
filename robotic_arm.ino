#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Float64.h>
#include <Servo.h>

// Define servo pins
#define SERVO1_PIN 8
#define SERVO2_PIN 9
#define SERVO3_PIN 10

// Define servo objects
Servo servo1; // Base servo
Servo servo2; // Shoulder servo
Servo servo3; // Elbow servo

// Define initial servo positions
int pos1 = 90; // Initial position for servo1 (base)
int pos2 = 90; // Initial position for servo2 (shoulder)
int pos3 = 90; // Initial position for servo3 (elbow)

// Define threshold for servo movement
const int threshold = 180;

// Define ROS node handle
ros::NodeHandle nh;

// Define callback function for input command
void commandCallback(const std_msgs::String& msg) {
  String command = msg.data;

  if (command == "left") {
    moveServo(&servo1, -1); // Move servo1 (base) left
  } else if (command == "right") {
    moveServo(&servo1, 1);  // Move servo1 (base) right
  } else if (command == "up") {
    moveServo(&servo2, -1); // Move servo2 (shoulder) up
  } else if (command == "down") {
    moveServo(&servo2, 1);  // Move servo2 (shoulder) down
  } else if (command == "forward") {
    moveServo(&servo3, -1); // Move servo3 (elbow) forward
  } else if (command == "backward") {
    moveServo(&servo3, 1);  // Move servo3 (elbow) backward
  }
}

// Function to move servo
void moveServo(Servo *servo, int direction) {
  int newPos = servo->read() + direction; // Calculate new position

  // Ensure the new position is within the servo's threshold
  if (newPos >= 0 && newPos <= threshold) {
    servo->write(newPos); // Move servo to the new position

    // Publish the new position to the same topic
    std_msgs::Float64 posMsg;
    posMsg.data = newPos;
    servo->getPositionPub().publish(&posMsg);
  }
}

// Define ROS subscriber
ros::Subscriber<std_msgs::String> sub("input_command", &commandCallback);

void setup() {
  // Initialize ROS
  nh.initNode();
  nh.subscribe(sub);

  // Attach servo pins
  servo1.attach(SERVO1_PIN);
  servo2.attach(SERVO2_PIN);
  servo3.attach(SERVO3_PIN);

  // Set initial servo positions
  servo1.write(pos1);
  servo2.write(pos2);
  servo3.write(pos3);
}

void loop() {
  // Handle ROS communication
  nh.spinOnce();
}
