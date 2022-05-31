# Octobotics Coding Assignment

This Github repository provides a base inverted pendulum simulation to be used as-is for the purposes of this assignment.

![](src/inverted_pendulum_sim/media/inverted_pendulum_sim.png)

# [Problem Statements](https://github.com/maanvisingh/Octobotics_Coding_Assignment/blob/main/Robotics%20Engineer%20Coding%20Assignment.pdf)
- Goal 1: Creating a controller package
- Goal 2: Send control input to the pendulum
- Goal 3: Balance the inverted pendulum

# My Solution
All the scripts I created are a part of the [inverted_pendulum_controller](https://github.com/maanvisingh/Octobotics_Coding_Assignment/tree/main/src/inverted_pendulum_controller) package.
- You can find the report for the same [here](https://github.com/maanvisingh/Octobotics_Coding_Assignment/blob/main/Octobotics_Report.pdf).

# To Run the tasks:

## Task 1:
```
roslaunch inverted_pendulum_controller task1.launch  
```
- [Video Output](https://github.com/maanvisingh/Octobotics_Coding_Assignment/blob/main/Videos/task1.webm)

## Task 2:
```
roslaunch inverted_pendulum_controller task2.launch  
```
- [Video Output](https://github.com/maanvisingh/Octobotics_Coding_Assignment/blob/main/Videos/task2_part1.webm)

- [Video Output with Increased Frequency](https://github.com/maanvisingh/Octobotics_Coding_Assignment/blob/main/Videos/task2_part2_increasedFrequency.webm)

- [Video Output with Incresed Amplitude](https://github.com/maanvisingh/Octobotics_Coding_Assignment/blob/main/Videos/task2_part3_increaseAmplitude.webm)

## Task 3:
```
roslaunch inverted_pendulum_controller task3.launch  
```
- [Video Output](https://github.com/maanvisingh/Octobotics_Coding_Assignment/blob/main/Videos/task3.webm)


### Dependencies

- [`pygame`](https://pypi.org/project/pygame/)

```bash
pip install pygame
```

- [`rospy`](http://wiki.ros.org/rospy)
- [`catkin_tools`](https://catkin-tools.readthedocs.io/en/latest/installing.html)

```bash
sudo apt-get install python3-catkin-tools
```

### Usage

- clone the repository

```bash
git clone git@github.com:octobotics/Octobotics_Coding_Assignment.git
```

- navigate to the repository directory

```bash
cd Octobotics_Coding_Assignment
```

- build the project

```bash
catkin build
```
- source the workspace

```bash
source devel/setup.bash
```

- launch the simulation using roslaunch

```bash
roslaunch inverted_pendulum_sim inverted_pendulum_sim.launch
```

### Published Topics
- /inverted_pendulum/current_state ([inverted_pendulum_sim/CurrentState](https://github.com/octobotics/Octobotics_Coding_Assignment/blob/main/src/inverted_pendulum_sim/msg/CurrentState.msg)) - Publishes the current state of the inverted pendulum at 100 Hz
 
### Subscribed Topics
- /inverted_pendulum/control_force ([inverted_pendulum_sim/ControlForce](https://github.com/octobotics/Octobotics_Coding_Assignment/blob/main/src/inverted_pendulum_sim/msg/ControlForce.msg)) - Subscribes to the control force input to the inverted pendulum

### Services
- /inverted_pendulum/set_params ([inverted_pendulum_sim/SetParams](https://github.com/octobotics/Octobotics_Coding_Assignment/tree/main/src/inverted_pendulum_sim/src) - Sets the parameters and initial conditions of the inverted pendulum
