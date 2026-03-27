import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Serial setup ---
port = '/dev/cu.usbmodem21101'
baud = 9600

ser = serial.Serial(port, baud)

# --- Data storage ---
values = []
max_points = 50  # only keep last 50 readings

# --- Graph setup ---
fig, ax = plt.subplots()
ax.set_title("Light Sensor Readings")
ax.set_ylim(0, 1023)

line, = ax.plot([])

# --- Update function ---
def update(frame):
    if ser.in_waiting:
        raw = ser.readline().decode().strip()

        try:
            num = int(raw)
            values.append(num)

            # keep list size under control
            if len(values) > max_points:
                values.pop(0)

            # update graph
            line.set_data(range(len(values)), values)
            ax.set_xlim(0, len(values))

        except:
            # ignore bad readings
            pass

    return line,

# --- Run animation ---
ani = animation.FuncAnimation(fig, update, interval=100)

plt.show()
