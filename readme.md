# Bird Bouncer
 This handy machine makes it so chickens do not make your nice cement pad turn into the poop deck. The innovative machine tracks chickens, and detects if they go on your precious cement pad, and if they do, the 'Bird Bouncer' will soak them, making them regret their decision to ever go on the cement pad. 

![Picture of the turret](./Images/Image1.jpg)

## How The Bird Bouncer works:
So my code works by first, seeing is there is a chicken detected, and if there is, it will get the middle of the detected box, does some math to convert that to angles for the servo, and tells the arduino the angles, and wether to turn the gun on

## Running this project

1. Install python 3.9, on the jetson nano you have to compile it yourself
2. install the following libraries :
flask
cv2
roboflow
supervision
3. Run the provided python code (make sure to put your own roboflow API key in the respetive variable)

![Demo](./Images/output.gif)





No chickens were harmed in the making of this video.
