# Arduino to Python Data Bridge

## Project Overview
This project serves as a foundational study in hardware-to-software data pipelines. It establishes a real-time, unidirectional serial bridge between an embedded microcontroller (Arduino UNO) and a host machine (macOS) to visualise physical sensor data dynamically.

## System Pipeline
1.  **Data Acquisition:** The Arduino continuously polls an analogue photoresistor (LDR) to measure ambient light intensity.
2.  **Hardware Feedback Loop:** A simple proportional control logic running on the microcontroller automatically adjusts the PWM duty cycle of an LED to inversely match the ambient light.
3.  **Serial Transmission:** The raw 10-bit ADC values are transmitted over UART to the host computer.
4.  **Data Visualisation:** A Python script operating within a virtual environment intercepts the serial stream and utilises `matplotlib` to render a live, moving time-series graph of the environmental data.

## Hardware Components
* Arduino UNO R3
* Photoresistor (LDR)
* Standard 5mm LED
* Resistors (220Ω for LED current limiting, 10kΩ for LDR voltage divider)

## Technologies Used
* **C++ / Arduino:** Embedded sensor polling, PWM actuation, and UART transmission.
* **Python:** Serial port interfacing and data handling (`pyserial`, `numpy`).
* **Matplotlib:** Real-time data rendering and UI updates.

## Technical Takeaways
* Implementing hardware-in-the-loop debugging and understanding diode polarity.
* Managing Python virtual environments (`venv`) for isolated dependency management on macOS.
* Applying linear mapping to scale 10-bit ADC resolution (0-1023) to 8-bit PWM resolution (0-255).
