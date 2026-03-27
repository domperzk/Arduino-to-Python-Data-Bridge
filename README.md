# Arduino to Python Data Bridge

## 💡 What is this?
This is a "Hello World" style project for the world of Hardware + Software. I wanted to see if I could make an LED react to light in the real world and then send that data to my Mac to be graphed live.

## 🛠️ How it works
1. **The Hardware:** An Arduino reads a photoresistor. If it gets dark, the Arduino automatically dims or brightens an LED using PWM.
2. **The Bridge:** The Arduino sends the light level numbers over the USB cable (Serial).
3. **The Visuals:** A Python script picks up those numbers and uses `Matplotlib` to draw a live moving graph of the light levels.

## 🧱 Parts List
- Arduino Uno
- LED & Photoresistor
- Resistors (220Ω and 10kΩ)
- Breadboard & Wires

## 💻 Tech Stack
- **C++ / Arduino:** For the sensor logic and LED control.
- **Python:** For the data processing.
- **Libraries:** `pyserial` (to talk to the Arduino), `matplotlib` (for the graph), and `numpy` (to handle the data).

## 📝 What I Learned
- How to debug a hardware circuit (and that LEDs only work in one direction!).
- How to set up a Python Virtual Environment (`venv`) on a Mac.
- How to map different scales of numbers (0-1023 sensor values to 0-255 LED values).
