"""
Seed data for the Electronics & Arduino/ESP32 course — Part 2 (Lessons 6-10).

Covers analog I/O, PWM, communication protocols, sensors, and a first
ESP32 WiFi/IoT project, building on the digital I/O basics from Part 1.
"""

ELECTRONICS_LESSONS_PART2 = [
    {
        "slug": "elec-06-analog-pwm",
        "title": "6. Analog Input, PWM, and Servo Control",
        "level": "intermediate",
        "explanation": (
            "Analog input pins (labeled A0-A5 on most Arduinos) read a continuous voltage between 0 "
            "and 5V as a number from 0-1023, using a built-in Analog-to-Digital Converter (ADC). "
            "Going the other way, digital pins can't output a true analog voltage, but PWM (Pulse "
            "Width Modulation) simulates one by rapidly switching HIGH/LOW and varying the fraction of "
            "time spent HIGH (the 'duty cycle') — this is how analogWrite() dims an LED or controls "
            "the position of a servo motor, which reads pulse width to decide its angle."
        ),
        "examples": (
            "// Read a potentiometer and use it to set brightness and a servo angle\n"
            "#include <Servo.h>\n"
            "Servo myServo;\n"
            "const int potPin = A0;\n"
            "const int ledPin = 9;   // must be a PWM-capable pin (~)\n\n"
            "void setup() {\n"
            "  myServo.attach(10);\n"
            "  pinMode(ledPin, OUTPUT);\n"
            "}\n\n"
            "void loop() {\n"
            "  int raw = analogRead(potPin);        // 0-1023\n"
            "  int brightness = map(raw, 0, 1023, 0, 255);\n"
            "  int angle = map(raw, 0, 1023, 0, 180);\n"
            "  analogWrite(ledPin, brightness);\n"
            "  myServo.write(angle);\n"
            "  delay(20);\n"
            "}\n"
        ),
        "practice": (
            "1. Wire a potentiometer to A0 and an LED (with resistor) to pin 9.\n"
            "2. Upload the example and confirm turning the pot smoothly dims the LED.\n"
            "3. Add a second LED on another PWM pin that dims in the opposite direction (brightest "
            "when the first is dimmest), using 255 - brightness."
        ),
        "mini_project": (
            "Mini Project: Servo-Controlled Pointer Gauge\n"
            "Build a simple analog gauge: a servo with a paper pointer taped to its horn, controlled "
            "by a potentiometer so turning the knob sweeps the pointer across a 0-180 degree scale "
            "you draw on paper."
        ),
        "quiz": {
            "title": "Analog I/O and PWM Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What range of values does analogRead() typically return on a standard Arduino?",
                    "option_a": "0 to 5",
                    "option_b": "0 to 255",
                    "option_c": "0 to 1023",
                    "option_d": "-1023 to 1023",
                    "correct_option": "c",
                    "explanation": "The standard 10-bit ADC on most Arduinos returns values from 0 to 1023.",
                },
                {
                    "text": "How does PWM simulate an analog voltage on a digital pin?",
                    "option_a": "By outputting a true variable voltage",
                    "option_b": "By rapidly switching on/off and varying the duty cycle",
                    "option_c": "By reducing the clock speed",
                    "option_d": "It cannot simulate analog voltage",
                    "correct_option": "b",
                    "explanation": "PWM rapidly toggles the pin, and the fraction of time spent HIGH (duty cycle) determines the average effective voltage.",
                },
                {
                    "text": "What does a servo motor use to determine its target angle?",
                    "option_a": "The color of the wire",
                    "option_b": "Pulse width of the control signal",
                    "option_c": "The battery voltage only",
                    "option_d": "Serial text commands only",
                    "correct_option": "b",
                    "explanation": "Standard hobby servos read the width of a repeating pulse (typically 1-2ms) to set their shaft angle.",
                },
            ],
        },
    },
    {
        "slug": "elec-07-sensors",
        "title": "7. Working with Sensors (Temperature, Distance, Light)",
        "level": "intermediate",
        "explanation": (
            "Sensors convert a physical quantity into an electrical signal a microcontroller can "
            "read. Simple analog sensors like an LDR (light-dependent resistor) or a TMP36 "
            "temperature sensor output a variable voltage read directly with analogRead(). Digital "
            "sensors like the DHT11/DHT22 (temperature+humidity) or HC-SR04 (ultrasonic distance) "
            "send data using a specific timed protocol and usually need a library to decode correctly. "
            "Always check a sensor's datasheet for its supply voltage, pinout, and interface type "
            "before wiring it."
        ),
        "examples": (
            "// HC-SR04 ultrasonic distance sensor\n"
            "const int trigPin = 7;\n"
            "const int echoPin = 8;\n\n"
            "void setup() {\n"
            "  pinMode(trigPin, OUTPUT);\n"
            "  pinMode(echoPin, INPUT);\n"
            "  Serial.begin(9600);\n"
            "}\n\n"
            "void loop() {\n"
            "  digitalWrite(trigPin, LOW); delayMicroseconds(2);\n"
            "  digitalWrite(trigPin, HIGH); delayMicroseconds(10);\n"
            "  digitalWrite(trigPin, LOW);\n"
            "  long duration = pulseIn(echoPin, HIGH);\n"
            "  float distanceCm = duration * 0.034 / 2;\n"
            "  Serial.println(distanceCm);\n"
            "  delay(200);\n"
            "}\n"
        ),
        "practice": (
            "1. Wire an HC-SR04 sensor and confirm it reports roughly correct distances to a nearby "
            "wall.\n"
            "2. Wire an LDR in a voltage divider with a fixed resistor to A0, and print analogRead() "
            "values in bright vs. dim light.\n"
            "3. Explain, from the datasheet-style behavior above, why the HC-SR04 needs a trigger "
            "pulse before it can measure — what physical process is it timing?"
        ),
        "mini_project": (
            "Mini Project: Parking Sensor\n"
            "Using the HC-SR04 and an LED (or buzzer), build a simple parking-assist alert: LED off "
            "when distance > 30cm, blinking slowly between 15-30cm, and solid on/fast beep under 15cm."
        ),
        "quiz": {
            "title": "Working with Sensors Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does the HC-SR04 sensor measure?",
                    "option_a": "Temperature",
                    "option_b": "Distance, using ultrasonic pulses",
                    "option_c": "Light intensity",
                    "option_d": "Air pressure",
                    "correct_option": "b",
                    "explanation": "The HC-SR04 emits an ultrasonic pulse and times the echo to calculate distance.",
                },
                {
                    "text": "Why should you check a sensor's datasheet before wiring it?",
                    "option_a": "Datasheets are optional and rarely useful",
                    "option_b": "To confirm supply voltage, pinout, and interface type",
                    "option_c": "Only to find the price",
                    "option_d": "Sensors are universally standardized so it's not needed",
                    "correct_option": "b",
                    "explanation": "Wiring a sensor to the wrong voltage or pins can damage it; the datasheet specifies correct usage.",
                },
                {
                    "text": "What kind of signal does a simple LDR (light sensor) typically produce?",
                    "option_a": "A digital I2C data stream",
                    "option_b": "A varying analog voltage, readable with analogRead()",
                    "option_c": "A fixed 5V output",
                    "option_d": "A radio signal",
                    "correct_option": "b",
                    "explanation": "An LDR changes resistance with light, producing a variable analog voltage when used in a voltage divider.",
                },
            ],
        },
    },
    {
        "slug": "elec-08-communication-protocols",
        "title": "8. Communication Protocols: UART, I2C, and SPI",
        "level": "intermediate",
        "explanation": (
            "Microcontrollers talk to other chips using standard protocols. UART (Serial) is simple "
            "point-to-point communication over TX/RX wires, used for Serial Monitor debugging and "
            "modules like GPS. I2C uses just two shared wires (SDA for data, SCL for clock) and lets "
            "many devices share the same bus, each identified by a unique address — common for "
            "sensors and OLED displays. SPI uses four wires (MOSI, MISO, SCK, CS) and is faster than "
            "I2C, commonly used for SD cards and displays that need high data throughput."
        ),
        "examples": (
            "// I2C scanner sketch — finds addresses of connected I2C devices\n"
            "#include <Wire.h>\n\n"
            "void setup() {\n"
            "  Wire.begin();\n"
            "  Serial.begin(9600);\n"
            "  for (byte addr = 1; addr < 127; addr++) {\n"
            "    Wire.beginTransmission(addr);\n"
            "    if (Wire.endTransmission() == 0) {\n"
            "      Serial.print(\"Found device at 0x\");\n"
            "      Serial.println(addr, HEX);\n"
            "    }\n"
            "  }\n"
            "}\n\n"
            "void loop() {}\n"
        ),
        "practice": (
            "1. Wire an I2C device (e.g. an SSD1306 OLED display) to the Arduino's SDA/SCL pins and "
            "run the I2C scanner sketch to confirm you can see its address.\n"
            "2. Compare, in your own words, when you would choose UART vs I2C vs SPI for a new "
            "project.\n"
            "3. List which pins on your specific Arduino board are the hardware SDA/SCL and MOSI/"
            "MISO/SCK pins, using the pinout reference."
        ),
        "mini_project": (
            "Mini Project: I2C Bus Explorer\n"
            "Connect two different I2C devices (for example an OLED display and a real-time clock "
            "module) to the same SDA/SCL bus, run the scanner to confirm both addresses appear, then "
            "write to the display using its library."
        ),
        "quiz": {
            "title": "Communication Protocols Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "How many shared data/clock wires does I2C use for communication?",
                    "option_a": "1",
                    "option_b": "2 (SDA and SCL)",
                    "option_c": "4",
                    "option_d": "8",
                    "correct_option": "b",
                    "explanation": "I2C uses two wires: SDA (data) and SCL (clock), shared by all devices on the bus.",
                },
                {
                    "text": "What distinguishes SPI from I2C?",
                    "option_a": "SPI uses only one wire total",
                    "option_b": "SPI uses more wires but is typically faster",
                    "option_c": "SPI cannot connect to sensors",
                    "option_d": "There is no difference",
                    "correct_option": "b",
                    "explanation": "SPI uses four lines (MOSI, MISO, SCK, CS) and generally achieves higher data rates than I2C.",
                },
                {
                    "text": "What is UART commonly used for on Arduino?",
                    "option_a": "Powering the board",
                    "option_b": "Simple point-to-point serial communication, like the Serial Monitor",
                    "option_c": "Connecting many devices on one shared bus",
                    "option_d": "Reading analog voltages",
                    "correct_option": "b",
                    "explanation": "UART is a simple two-wire (TX/RX) serial link, used for debugging output and simple modules like GPS.",
                },
            ],
        },
    },
    {
        "slug": "elec-09-esp32-wifi",
        "title": "9. Introduction to ESP32: WiFi and IoT Basics",
        "level": "intermediate",
        "explanation": (
            "The ESP32 is a low-cost microcontroller with built-in WiFi and Bluetooth, making it the "
            "standard choice for IoT projects. It is programmed the same way as Arduino (setup()/"
            "loop(), digitalWrite(), analogRead()) using the Arduino IDE with the ESP32 board package "
            "installed, but adds networking libraries like WiFi.h. A typical IoT project connects to a "
            "WiFi network, then either serves a small web page, sends data to a server, or listens for "
            "commands, letting you control hardware remotely."
        ),
        "examples": (
            "// ESP32 connects to WiFi and prints its IP address\n"
            "#include <WiFi.h>\n\n"
            "const char* ssid = \"YourNetworkName\";\n"
            "const char* password = \"YourPassword\";\n\n"
            "void setup() {\n"
            "  Serial.begin(115200);\n"
            "  WiFi.begin(ssid, password);\n"
            "  while (WiFi.status() != WL_CONNECTED) {\n"
            "    delay(500);\n"
            "    Serial.print(\".\");\n"
            "  }\n"
            "  Serial.println(\"\\nConnected! IP address: \");\n"
            "  Serial.println(WiFi.localIP());\n"
            "}\n\n"
            "void loop() {}\n"
        ),
        "practice": (
            "1. Install the ESP32 board package in the Arduino IDE (or use PlatformIO) and upload the "
            "example sketch with your own WiFi credentials.\n"
            "2. Confirm you can see the assigned IP address in the Serial Monitor.\n"
            "3. Research and note the difference between the ESP32's GPIO voltage (3.3V logic) and a "
            "classic Arduino Uno's (5V logic) — why does this matter when reusing 5V sensors?"
        ),
        "mini_project": (
            "Mini Project: WiFi-Controlled LED Web Server\n"
            "Using the ESP32 WebServer library, build a tiny web page with ON/OFF buttons that, when "
            "clicked from any device on the same WiFi network, turns an LED connected to the ESP32 on "
            "or off."
        ),
        "quiz": {
            "title": "ESP32 and WiFi Basics Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What key feature does the ESP32 have that a basic Arduino Uno does not?",
                    "option_a": "More analog pins only",
                    "option_b": "Built-in WiFi and Bluetooth",
                    "option_c": "It cannot run C/C++ code",
                    "option_d": "It has no GPIO pins",
                    "correct_option": "b",
                    "explanation": "The ESP32's defining feature is integrated WiFi and Bluetooth, ideal for IoT projects.",
                },
                {
                    "text": "What logic voltage do ESP32 GPIO pins use?",
                    "option_a": "5V",
                    "option_b": "3.3V",
                    "option_c": "12V",
                    "option_d": "1V",
                    "correct_option": "b",
                    "explanation": "ESP32 GPIO pins operate at 3.3V logic, and are generally not 5V-tolerant.",
                },
                {
                    "text": "What does WiFi.localIP() return after a successful connection?",
                    "option_a": "The router's WiFi password",
                    "option_b": "The IP address assigned to the ESP32 on the network",
                    "option_c": "The MAC address of the router",
                    "option_d": "The signal strength in dB",
                    "correct_option": "b",
                    "explanation": "WiFi.localIP() returns the local network IP address assigned to the device.",
                },
            ],
        },
    },
    {
        "slug": "elec-10-iot-capstone",
        "title": "10. Capstone: IoT Temperature & Humidity Dashboard",
        "level": "advanced",
        "explanation": (
            "This capstone combines everything from the course: wiring and powering a sensor "
            "correctly (DHT22 temperature/humidity), reading it with a library, connecting an ESP32 "
            "to WiFi, and serving the live readings on a simple web dashboard anyone on the network "
            "can open in a browser. This is the same pattern used in real smart-home and industrial "
            "monitoring systems — a sensor feeding a network-accessible endpoint."
        ),
        "examples": (
            "// Simplified structure of the capstone sketch\n"
            "#include <WiFi.h>\n"
            "#include <WebServer.h>\n"
            "#include <DHT.h>\n\n"
            "DHT dht(4, DHT22);          // data pin 4\n"
            "WebServer server(80);\n\n"
            "void handleRoot() {\n"
            "  float t = dht.readTemperature();\n"
            "  float h = dht.readHumidity();\n"
            "  String page = \"<h1>Temp: \" + String(t) + \"C</h1><h1>Humidity: \" + String(h) + \"%</h1>\";\n"
            "  server.send(200, \"text/html\", page);\n"
            "}\n\n"
            "void setup() {\n"
            "  dht.begin();\n"
            "  WiFi.begin(\"ssid\", \"password\");\n"
            "  while (WiFi.status() != WL_CONNECTED) delay(500);\n"
            "  server.on(\"/\", handleRoot);\n"
            "  server.begin();\n"
            "}\n\n"
            "void loop() {\n"
            "  server.handleClient();\n"
            "}\n"
        ),
        "practice": (
            "1. Wire a DHT22 sensor to an ESP32 (data pin, VCC, GND, plus a 10k pull-up resistor on "
            "the data line if your module doesn't already include one).\n"
            "2. Build the sketch above piece by piece: first confirm readings in the Serial Monitor, "
            "then add the web server.\n"
            "3. Open the ESP32's IP address in a browser from another device on the same WiFi network "
            "and confirm the live readings update on refresh."
        ),
        "mini_project": (
            "Final Project: Full IoT Environment Dashboard\n"
            "Extend the capstone into a complete mini dashboard: auto-refresh the page every 5 "
            "seconds using a small HTML meta-refresh tag, add a second sensor of your choice (light or "
            "distance), and add a simple threshold alert (e.g. an LED that turns on if temperature "
            "exceeds a set value) — combining digital output, analog/digital sensing, and networking "
            "in one finished IoT project."
        ),
        "quiz": {
            "title": "IoT Capstone Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "In the capstone project, what is the role of the ESP32 WebServer library?",
                    "option_a": "It reads the temperature directly without a sensor",
                    "option_b": "It serves the sensor readings as a web page over the network",
                    "option_c": "It replaces the need for WiFi",
                    "option_d": "It only works over Bluetooth",
                    "correct_option": "b",
                    "explanation": "WebServer lets the ESP32 respond to HTTP requests, serving live sensor data as a web page.",
                },
                {
                    "text": "Why might a DHT22 need a pull-up resistor on its data line?",
                    "option_a": "To increase the temperature reading",
                    "option_b": "To hold the data line at a stable default state, similar to a button's pull-up",
                    "option_c": "To power the WiFi module",
                    "option_d": "It never needs one under any circumstance",
                    "correct_option": "b",
                    "explanation": "Like a floating digital input, the DHT's single-wire data line needs a defined resting state, provided by a pull-up.",
                },
                {
                    "text": "Which skill areas does this capstone combine?",
                    "option_a": "Only digital output",
                    "option_b": "Sensor wiring/reading, WiFi networking, and serving data over HTTP",
                    "option_c": "Only breadboard wiring, with no code",
                    "option_d": "Only SPI communication",
                    "correct_option": "b",
                    "explanation": "The capstone brings together sensor reading, WiFi connectivity, and a basic web server — the full stack of a simple IoT device.",
                },
            ],
        },
    },
]
