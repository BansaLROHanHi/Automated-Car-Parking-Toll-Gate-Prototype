# Car Parking Toll Gate Prototype

This is a prototype of a car parking toll gate system created as an electrical minor project. The project utilizes Arduino, IR sensors, LED lights, servo motor, touch sensors, and buzzers to control the flow of vehicles in and out of a parking area.

## Features

1. **Toll Bar Operation**:
   - The toll bar opens when a car passes over the first IR sensor embedded in the road.
   - The toll bar closes only when the car passes over the second IR sensor to avoid any accidents.

2. **Touch Sensor and Buzzer**:
   - If a person rushes the car into the gate, the touch sensor recognizes this and activates a buzzer to alert the driver.

3. **Traffic Lights**:
   - Traffic lights (green, yellow, red) are used to direct the flow of vehicles.

4. **Parking Capacity Monitoring**:
   - The system keeps track of the number of cars inside the parking area.
   - When the maximum capacity is reached, the red light is turned on, and no incoming cars are allowed.
   - Cars can leave the parking area at any time.

## Hardware Components

- Arduino board
- 2 IR sensors
- 1 touch sensor
- 3 LED lights (green, yellow, red)
- 1 buzzer
- 1 servo motor for the toll bar

## Code Explanation

The code provided in the project uses the following key functions:

1. `setup()`: Initializes the Arduino pins and sets the initial state of the system.
2. `loop()`: Continuously monitors the sensor inputs and controls the toll bar, traffic lights, and buzzer accordingly.
3. The code checks the following conditions:
   - If the maximum capacity is reached, the red light is turned on, and no incoming cars are allowed.
   - When the first IR sensor is triggered, the toll bar opens.
   - When the second IR sensor is triggered, the toll bar closes, and the car count is incremented.
   - If the touch sensor is triggered, the red light is turned on, and the buzzer is activated.

## Future Enhancements

1. Implement a display to show the current number of cars in the parking area.
2. Add a timer to automatically close the toll bar after a certain time delay.
3. Integrate a payment system for the parking toll.
4. Expand the system to include multiple entry and exit points.
