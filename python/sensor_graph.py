import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# 1. SETUP THE USB CONNECTION
# Replace the string below with your EXACT Mac port name from the Arduino IDE
arduino_port = '/dev/cu.usbmodem21101' 
baud_rate = 9600

# Open the serial port
ser = serial.Serial(arduino_port, baud_rate)

# 2. SETUP THE GRAPH
# Create an empty list to store our incoming numbers
data_points = []
max_data_points = 50 # We only want to show the last 50 readings on screen

# Create the figure and axis for Matplotlib
fig, ax = plt.subplots()
ax.set_ylim(0, 1023) # The Y-axis matches our 0 to 1023 sensor range
ax.set_title("Live Photoresistor Data")
ax.set_ylabel("Light Level")
line, = ax.plot(data_points)

# 3. THE ANIMATION LOOP
# This function runs over and over, grabbing new data and updating the graph
def update_graph(frame):
    # Check if there is data waiting in the USB buffer
    if ser.in_waiting > 0:
        # Read the line, decode the bytes into a string, and strip invisible characters
        raw_data = ser.readline().decode('utf-8').strip()
        
        try:
            # Convert the text into an integer
            light_level = int(raw_data)
            
            # Add the new number to our list
            data_points.append(light_level)
            
            # If the list gets too long, chop off the oldest number
            if len(data_points) > max_data_points:
                data_points.pop(0)
            
            # Update the line on the graph with the new list of numbers
            line.set_ydata(data_points)
            line.set_xdata(np.arange(len(data_points))) # NumPy creates our X-axis time steps
            ax.set_xlim(0, len(data_points))
            
        except ValueError:
            # Sometimes the first reading is corrupted, so we just ignore errors
            pass
            
    return line,

# 4. START THE SHOW
# Tell Matplotlib to run the update function every 50 milliseconds
ani = animation.FuncAnimation(fig, update_graph, interval=50)

plt.show()