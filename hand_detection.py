'''
import cv2
import mediapipe as mp

# Initialize MediaPipe Hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Function to get the direction based on hand position relative to the center
def get_direction(hand_landmarks, screen_center, screen_width, screen_height):
    if hand_landmarks is not None:
        hand_center = (
            int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * screen_width),
            int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * screen_height)
        )

        x_diff = hand_center[0] - screen_center[0]
        y_diff = hand_center[1] - screen_center[1]

        if abs(x_diff) > abs(y_diff):
            if x_diff > 0:
                return "left"
            else:
                return "right"
        else:
            if y_diff > 0:
                return "Bottom"
            else:
                return "Top"
    else:
        return "No hand detected"

# Main function for hand detection and direction prediction
def main():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Get the screen dimensions
    screen_width = int(cap.get(3))
    screen_height = int(cap.get(4))
    screen_center = (screen_width // 2, screen_height // 2)

    while True:
        # Read frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect hands in the frame
        results = hands.process(rgb_frame)

        # Get hand landmarks and direction
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                direction = get_direction(hand_landmarks, screen_center, screen_width, screen_height)
                print(direction)

        # Display the frame
        cv2.imshow("Frame", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

    '''



'''
v2


import cv2
import mediapipe as mp
import time

# Initialize MediaPipe Hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Function to get the direction based on hand position relative to the center
def get_direction(hand_landmarks, screen_center, screen_width, screen_height):
    if hand_landmarks is not None:
        hand_center = (
            int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * screen_width),
            int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * screen_height)
        )

        x_diff = hand_center[0] - screen_center[0]
        y_diff = hand_center[1] - screen_center[1]

        if abs(x_diff) > abs(y_diff):
            if x_diff > 0:
                return "left"
            else:
                return "right"
        else:
            if y_diff > 0:
                return "bottom"
            else:
                return "top"
    else:
        return "No hand detected"

# Main function for hand detection and direction prediction
def main():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Get the screen dimensions
    screen_width = int(cap.get(3))
    screen_height = int(cap.get(4))
    screen_center = (screen_width // 2, screen_height // 2)

    # Variables for delay in detection
    last_detection_time = 0
    detection_interval = 2  # 2 seconds

    while True:
        # Read frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect hands in the frame
        results = hands.process(rgb_frame)

        # Get hand landmarks and direction
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                direction = get_direction(hand_landmarks, screen_center, screen_width, screen_height)
                print(direction)

                # Calculate bounding box coordinates
                x_min, y_min = screen_width, screen_height
                x_max, y_max = 0, 0
                for landmark in hand_landmarks.landmark:
                    x, y = int(landmark.x * screen_width), int(landmark.y * screen_height)
                    if x < x_min:
                        x_min = x
                    if x > x_max:
                        x_max = x
                    if y < y_min:
                        y_min = y
                    if y > y_max:
                        y_max = y

                # Draw a green box around the detected hand
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

        # Display the frame
        cv2.imshow("Frame", frame)

        # Check if it's time to detect again
        current_time = time.time()
        if current_time - last_detection_time >= detection_interval:
            last_detection_time = current_time

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

'''

'''
v3

import cv2
import mediapipe as mp
import time
import math

# Initialize MediaPipe Hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Function to get the direction based on hand position relative to the center
def get_direction(hand_landmarks, screen_center, screen_width, screen_height):
    if hand_landmarks is not None:
        hand_center = (
            int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * screen_width),
            int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * screen_height)
        )

        # Calculate distance between hand center and screen center
        distance = math.sqrt((hand_center[0] - screen_center[0])**2 + (hand_center[1] - screen_center[1])**2)
        center_threshold = min(screen_width, screen_height) * 0.1  # Adjust this threshold as needed

        if distance < center_threshold:
            return "centre"
        else:
            x_diff = hand_center[0] - screen_center[0]
            y_diff = hand_center[1] - screen_center[1]

            if abs(x_diff) > abs(y_diff):
                if x_diff > 0:
                    return "left"
                else:
                    return "right"
            else:
                if y_diff > 0:
                    return "bottom"
                else:
                    return "top"
    else:
        return "No hand detected"

# Main function for hand detection and direction prediction
def main():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Get the screen dimensions
    screen_width = int(cap.get(3))
    screen_height = int(cap.get(4))
    screen_center = (screen_width // 2, screen_height // 2)

    # Variables for delay in detection
    last_detection_time = 0
    detection_interval = 2  # 2 seconds

    while True:
        # Read frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect hands in the frame
        results = hands.process(rgb_frame)

        # Get hand landmarks and direction
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                direction = get_direction(hand_landmarks, screen_center, screen_width, screen_height)
                print(direction)

                # Calculate bounding box coordinates
                x_min, y_min = screen_width, screen_height
                x_max, y_max = 0, 0
                for landmark in hand_landmarks.landmark:
                    x, y = int(landmark.x * screen_width), int(landmark.y * screen_height)
                    if x < x_min:
                        x_min = x
                    if x > x_max:
                        x_max = x
                    if y < y_min:
                        y_min = y
                    if y > y_max:
                        y_max = y

                # Draw a green box around the detected hand
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

        # Display the frame
        cv2.imshow("Frame", frame)

        # Check if it's time to detect again
        current_time = time.time()
        if current_time - last_detection_time >= detection_interval:
            last_detection_time = current_time

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
'''
'''
v4

import cv2
import mediapipe as mp
import time
import math

# Initialize MediaPipe Hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Function to get the direction based on hand position relative to the center
def get_direction(hand_landmarks, screen_center, screen_width, screen_height):
    if hand_landmarks is not None:
        hand_center = (
            int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * screen_width),
            int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * screen_height)
        )

        # Calculate distance between hand center and screen center
        distance = math.sqrt((hand_center[0] - screen_center[0])**2 + (hand_center[1] - screen_center[1])**2)
        center_threshold = min(screen_width, screen_height) * 0.1  # Adjust this threshold as needed

        if distance < center_threshold:
            return "centre", (0, 255, 0)  # Green color for center
        else:
            x_diff = hand_center[0] - screen_center[0]
            y_diff = hand_center[1] - screen_center[1]

            if abs(x_diff) > abs(y_diff):
                if x_diff > 0:
                    return "right", (0, 0, 255)  # Red color for right
                else:
                    return "left", (255, 0, 0)   # Blue color for left
            else:
                if y_diff > 0:
                    return "bottom", (0, 255, 255)  # Yellow color for bottom
                else:
                    return "top", (255, 255, 0)     # Cyan color for top
    else:
        return "No hand detected", (0, 0, 0)  # Black color for no detection

# Main function for hand detection and direction prediction
def main():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Get the screen dimensions
    screen_width = int(cap.get(3))
    screen_height = int(cap.get(4))
    screen_center = (screen_width // 2, screen_height // 2)

    # Variables for delay in detection
    last_detection_time = 0
    detection_interval = 2  # 2 seconds

    while True:
        # Read frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect hands in the frame
        results = hands.process(rgb_frame)

        # Get hand landmarks and direction
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                direction, color = get_direction(hand_landmarks, screen_center, screen_width, screen_height)
                print(direction)

                # Calculate bounding box coordinates
                x_min, y_min = screen_width, screen_height
                x_max, y_max = 0, 0
                for landmark in hand_landmarks.landmark:
                    x, y = int(landmark.x * screen_width), int(landmark.y * screen_height)
                    if x < x_min:
                        x_min = x
                    if x > x_max:
                        x_max = x
                    if y < y_min:
                        y_min = y
                    if y > y_max:
                        y_max = y

                # Draw a green box around the detected hand
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), color, 2)

                # Draw directional indicators on the frame
                cv2.putText(frame, direction, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Display the frame
        cv2.imshow("Frame", frame)

        # Check if it's time to detect again
        current_time = time.time()
        if current_time - last_detection_time >= detection_interval:
            last_detection_time = current_time

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
'''

'''

import cv2
import mediapipe as mp
import time
import math

# Initialize MediaPipe Hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Function to calculate distance between two landmarks
def calculate_distance(landmark1, landmark2, screen_width, screen_height):
    x1, y1 = int(landmark1.x * screen_width), int(landmark1.y * screen_height)
    x2, y2 = int(landmark2.x * screen_width), int(landmark2.y * screen_height)
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to get the direction based on hand position relative to the center
def get_direction(hand_landmarks, screen_center, screen_width, screen_height):
    if hand_landmarks is not None:
        # Calculate hand center
        hand_center = (
            int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * screen_width),
            int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * screen_height)
        )

        # Calculate distance between thumb tip and index finger tip
        thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        hand_status = "open" if calculate_distance(thumb_tip, index_tip, screen_width, screen_height) > screen_width * 0.1 else "closed"

        # Calculate distance between hand center and screen center
        distance = math.sqrt((hand_center[0] - screen_center[0])**2 + (hand_center[1] - screen_center[1])**2)
        center_threshold = min(screen_width, screen_height) * 0.1  # Adjust this threshold as needed

        if distance < center_threshold:
            direction = "centre"
            color = (0, 255, 0)  # Green color for center
        else:
            x_diff = hand_center[0] - screen_center[0]
            y_diff = hand_center[1] - screen_center[1]

            if abs(x_diff) > abs(y_diff):
                if x_diff > 0:
                    direction = "right"
                    color = (0, 0, 255)  # Red color for right
                else:
                    direction = "left"
                    color = (255, 0, 0)   # Blue color for left
            else:
                if y_diff > 0:
                    direction = "bottom"
                    color = (0, 255, 255)  # Yellow color for bottom
                else:
                    direction = "top"
                    color = (255, 255, 0)     # Cyan color for top

        return direction, color, hand_status

    else:
        return "No hand detected", (0, 0, 0), "unknown"

# Main function for hand detection and direction prediction
def main():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Get the screen dimensions
    screen_width = int(cap.get(3))
    screen_height = int(cap.get(4))
    screen_center = (screen_width // 2, screen_height // 2)

    # Variables for delay in detection
    last_detection_time = 0
    detection_interval = 2  # 2 seconds

    while True:
        # Read frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect hands in the frame
        results = hands.process(rgb_frame)

        # Get hand landmarks, direction, and hand status
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                direction, color, hand_status = get_direction(hand_landmarks, screen_center, screen_width, screen_height)
                print(f"Direction: {direction}, Status: {hand_status}")

                # Calculate bounding box coordinates
                x_min, y_min = screen_width, screen_height
                x_max, y_max = 0, 0
                for landmark in hand_landmarks.landmark:
                    x, y = int(landmark.x * screen_width), int(landmark.y * screen_height)
                    if x < x_min:
                        x_min = x
                    if x > x_max:
                        x_max = x
                    if y < y_min:
                        y_min = y
                    if y > y_max:
                        y_max = y

                # Draw a green box around the detected hand
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), color, 2)

                # Draw directional indicators on the frame
                cv2.putText(frame, f"{direction}, {hand_status}", (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Display the frame
        cv2.imshow("Frame", frame)

        # Check if it's time to detect again
        current_time = time.time()
        if current_time - last_detection_time >= detection_interval:
            last_detection_time = current_time

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
'''


import cv2
import mediapipe as mp
import time
import math

# Initialize MediaPipe Hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Function to calculate distance between two landmarks
def calculate_distance(landmark1, landmark2, screen_width, screen_height):
    x1, y1 = int(landmark1.x * screen_width), int(landmark1.y * screen_height)
    x2, y2 = int(landmark2.x * screen_width), int(landmark2.y * screen_height)
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to get the direction based on hand position relative to the center
def get_direction(hand_landmarks, screen_center, screen_width, screen_height):
    if hand_landmarks is not None:
        # Calculate hand center
        hand_center = (
            int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * screen_width),
            int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * screen_height)
        )

        # Calculate distance between thumb tip and index finger tip
        thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        hand_status = "open" if calculate_distance(thumb_tip, index_tip, screen_width, screen_height) > screen_width * 0.1 else "closed"

        # Calculate distance between hand center and screen center
        distance = math.sqrt((hand_center[0] - screen_center[0])**2 + (hand_center[1] - screen_center[1])**2)
        center_threshold = min(screen_width, screen_height) * 0.1  # Adjust this threshold as needed

        if distance < center_threshold:
            direction = "centre"
            color = (0, 255, 0)  # Green color for center
        else:
            x_diff = hand_center[0] - screen_center[0]
            y_diff = hand_center[1] - screen_center[1]

            if abs(x_diff) > abs(y_diff):
                if x_diff > 0:
                    direction = "right"
                    color = (0, 0, 255)  # Red color for right
                else:
                    direction = "left"
                    color = (255, 0, 0)   # Blue color for left
            else:
                if y_diff > 0:
                    direction = "bottom"
                    color = (0, 255, 255)  # Yellow color for bottom
                else:
                    direction = "top"
                    color = (255, 255, 0)     # Cyan color for top

        return direction, color, hand_status

    else:
        return "No hand detected", (0, 0, 0), "unknown"

# Main function for hand detection and direction prediction
def main():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Get the screen dimensions
    screen_width = int(cap.get(3))
    screen_height = int(cap.get(4))
    screen_center = (screen_width // 2, screen_height // 2)

    # Variables for delay in detection
    last_detection_time = 0
    detection_interval = 2  # 2 seconds

    while True:
        # Read frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect hands in the frame
        results = hands.process(rgb_frame)

        # Get hand landmarks, direction, and hand status
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                direction, color, hand_status = get_direction(hand_landmarks, screen_center, screen_width, screen_height)

                # Print direction and hand status every 2 seconds
                current_time = time.time()
                if current_time - last_detection_time >= detection_interval:
                    print(f"Direction: {direction}, Status: {hand_status}")
                    last_detection_time = current_time

                # Calculate bounding box coordinates
                x_min, y_min = screen_width, screen_height
                x_max, y_max = 0, 0
                for landmark in hand_landmarks.landmark:
                    x, y = int(landmark.x * screen_width), int(landmark.y * screen_height)
                    if x < x_min:
                        x_min = x
                    if x > x_max:
                        x_max = x
                    if y < y_min:
                        y_min = y
                    if y > y_max:
                        y_max = y

                # Draw a green box around the detected hand
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), color, 2)

                # Draw directional indicators on the frame
                cv2.putText(frame, f"{direction}, {hand_status}", (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Display the frame
        cv2.imshow("Frame", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
