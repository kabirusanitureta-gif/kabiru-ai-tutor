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
                "real_world_project": (
            "Real-World Project: Light-Controlled Dimmer\n"
            "Wire a photoresistor (LDR) to an analog input and an LED to a PWM output. Write code so "
            "the LED gets brighter as the room gets darker (an automatic night light), mapping the "
            "analogRead() range to an appropriate PWM output range using the map() function."
        ),
        "common_mistakes": (
            "- Trying to use analogWrite() (PWM) on a pin that doesn't support it -- only specific "
            "pins (usually marked with a ~ on the board) support PWM; check your board's pinout.\n"
            "- Forgetting that analogRead() returns 0-1023 while analogWrite() expects 0-255 -- these "
            "ranges must be converted (often with map()), not used interchangeably.\n"
            "- Powering a servo directly from the Arduino's 5V pin for anything beyond a single small "
            "servo -- servos can draw more current than the board can safely supply, requiring an "
            "external power source for multiple or larger servos.\n"
            "- Assuming PWM output is a 'real' analog voltage -- it's actually a fast digital on/off "
            "switching that averages out to an apparent analog effect, which matters for some "
            "sensitive analog applications."
        ),
        "best_practices": (
            "- Always use map() to convert between analogRead()'s 0-1023 range and analogWrite()'s "
            "0-255 range rather than guessing a scaling factor.\n"
            "- Check your specific board's datasheet/pinout diagram to confirm which pins support PWM "
            "before wiring a dimming or motor-speed circuit.\n"
            "- Power servos and motors from an appropriate external supply, not directly from the "
            "microcontroller's regulator, for anything beyond the smallest test servo.\n"
            "- Add a small delay or smoothing when reading noisy analog sensors, since raw ADC "
            "readings can jitter slightly even with a stable input."
        ),
        "interview_questions": (
            "1. How does PWM simulate an analog output using only digital HIGH/LOW switching?\n"
            "2. What is the practical range difference between analogRead() and analogWrite(), and "
            "why does that matter?\n"
            "3. Why might a servo motor need an external power supply instead of power from the "
            "microcontroller directly?\n"
            "4. What does an Analog-to-Digital Converter (ADC) actually do?\n"
            "5. Name one real project where PWM is essential rather than just convenient."
        ),
        "assignment": (
            "Assignment: PWM Fade Sweep\n"
            "Write a sketch that smoothly fades an LED from fully off to fully on and back, using a "
            "for loop and analogWrite(), with a short delay() between each brightness step to make the "
            "fade visible."
        ),
        "challenge": (
            "Challenge: Potentiometer-Controlled Servo\n"
            "Wire a potentiometer to an analog input and a servo to a PWM-capable pin. Use "
            "analogRead() and map() so turning the potentiometer smoothly sweeps the servo's angle "
            "from 0 to 180 degrees in real time."
        ),
        "summary": (
            "analogRead() reads a continuous voltage (0-1023) via the ADC on analog-capable pins. "
            "PWM (via analogWrite(), 0-255) simulates analog output on specific digital pins by rapid "
            "switching. The map() function converts between these differing ranges. Servos are "
            "controlled with a dedicated Servo library rather than raw PWM, and often need external "
            "power beyond a single small unit."
        ),
        "lesson_references": (
            "- Arduino official: 'Analog Input', 'PWM', and 'Servo' library references\n"
            "- SparkFun: 'Pulse Width Modulation' tutorial\n"
            "- Arduino official: 'map()' function reference"
        ),
        "next_lesson_preview": (
            "Next up: Working with Sensors -- temperature, distance, and light. You'll integrate real "
            "sensor modules and libraries into your projects, moving beyond basic buttons and "
            "potentiometers."
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
                "real_world_project": (
            "Real-World Project: Environmental Monitor\n"
            "Build a small station that reads temperature (DHT11/DHT22 or TMP36), light level (LDR), "
            "and displays both readings on the Serial Monitor every 2 seconds, formatted clearly with "
            "labels and units -- the foundational pattern behind real weather stations and smart home "
            "sensors."
        ),
        "common_mistakes": (
            "- Reading a digital sensor library (like DHT) too frequently -- most have a minimum "
            "sampling interval (often ~2 seconds for DHT sensors) and will return garbage or stale "
            "data if polled faster.\n"
            "- Not accounting for sensor tolerance/noise -- a single analog reading can be inaccurate; "
            "averaging several readings over a short window often gives more reliable results.\n"
            "- Wiring analog sensors without checking whether they need a pull-up/pull-down resistor "
            "or voltage divider to produce a meaningful reading.\n"
            "- Forgetting to install a sensor's specific library (e.g. DHT library) before attempting "
            "to use its functions, resulting in confusing compile errors."
        ),
        "best_practices": (
            "- Always check a sensor's datasheet for its required sampling interval, operating "
            "voltage, and any needed supporting components before wiring it.\n"
            "- Average multiple readings for noisy analog sensors rather than trusting a single "
            "sample.\n"
            "- Print sensor readings with clear units (e.g. 'Temp: 24.5 C') during development -- raw "
            "unlabeled numbers are hard to debug later.\n"
            "- Handle sensor read failures gracefully (many libraries return NaN or a sentinel value "
            "on failure) rather than assuming every reading succeeds."
        ),
        "interview_questions": (
            "1. Why do digital sensors like the DHT11/DHT22 have a minimum polling interval?\n"
            "2. What's the benefit of averaging multiple analog sensor readings instead of using a "
            "single sample?\n"
            "3. What is a voltage divider, and why might a sensor need one?\n"
            "4. How would you handle a sensor read failure gracefully in your code?\n"
            "5. What's the difference between an analog sensor (like an LDR) and a digital sensor "
            "(like a DHT22) in terms of how you read them?"
        ),
        "assignment": (
            "Assignment: Multi-Sensor Data Logger\n"
            "Wire 2 different sensors (one analog, one digital) and print both readings to the Serial "
            "Monitor every second with clear labels, running continuously for at least 2 minutes to "
            "observe how the readings change over time."
        ),
        "challenge": (
            "Challenge: Threshold Alert System\n"
            "Build a system that reads a temperature sensor continuously and lights a red LED (plus "
            "prints a warning) whenever the temperature exceeds a threshold you define, and a green "
            "LED otherwise -- the basic pattern behind real environmental alert systems."
        ),
        "summary": (
            "Sensors convert physical quantities (temperature, light, distance) into electrical "
            "signals. Analog sensors are read directly with analogRead(); digital sensors typically "
            "need a specific library and have a minimum polling interval. Averaging readings and "
            "checking datasheets for wiring/timing requirements are essential for reliable sensor "
            "data."
        ),
        "lesson_references": (
            "- Adafruit: DHT11/DHT22 sensor library and wiring guide\n"
            "- SparkFun: 'Sensors' tutorial hub (temperature, light, distance)\n"
            "- Arduino official: 'AnalogReadSerial' and library examples"
        ),
        "next_lesson_preview": (
            "Next up: Communication Protocols -- UART, I2C, and SPI. You'll learn how microcontrollers "
            "talk to other chips and modules, essential for displays, more advanced sensors, and "
            "multi-device projects."
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
                "real_world_project": (
            "Real-World Project: I2C Device Scanner\n"
            "Write a sketch using the Wire library that scans all possible I2C addresses (0 to 127) "
            "and prints which ones respond -- a genuinely useful diagnostic tool used constantly in "
            "real embedded development to identify unknown or misconfigured I2C devices."
        ),
        "common_mistakes": (
            "- Forgetting I2C pull-up resistors -- SDA/SCL lines need pull-up resistors (many modules "
            "include them, but bare sensors often don't) or communication becomes unreliable.\n"
            "- Connecting SPI's MISO/MOSI backward between devices -- unlike I2C's shared bus, SPI "
            "wiring must be directional and correct, or nothing will communicate.\n"
            "- Using the same UART pins for Serial Monitor debugging AND a wired UART module "
            "simultaneously -- they conflict since Arduino's main UART (pins 0/1) is shared with USB "
            "programming/debugging.\n"
            "- Not matching baud rates between two UART devices -- both ends must agree on the exact "
            "same speed or received data will be garbled."
        ),
        "best_practices": (
            "- Use I2C when you have several sensors on a shared bus and don't need extremely high "
            "speed; use SPI when you need high-speed communication (like a display) with a device "
            "that supports it.\n"
            "- Always double-check pull-up resistor requirements for I2C devices without built-in "
            "breakout board support.\n"
            "- Reserve hardware UART (pins 0/1) for USB debugging where possible, and use "
            "SoftwareSerial or a second hardware UART (on boards that have one) for external UART "
            "modules.\n"
            "- Keep a mental checklist when a new I2C/SPI device doesn't respond: power, ground, "
            "pull-ups (I2C), correct MISO/MOSI orientation (SPI), and correct address/library."
        ),
        "interview_questions": (
            "1. What's the key structural difference between I2C and SPI in terms of wiring?\n"
            "2. Why can multiple I2C devices share the same two wires without interfering with each "
            "other?\n"
            "3. What happens if two UART devices are configured with different baud rates?\n"
            "4. Why do I2C buses typically need pull-up resistors?\n"
            "5. When would you choose SPI over I2C for a project?"
        ),
        "assignment": (
            "Assignment: Protocol Selection Matrix\n"
            "Given 5 different scenarios (a single GPS module, 6 temperature sensors on one bus, a "
            "high-refresh-rate display, a simple 2-device debug link, an SD card reader), identify "
            "which protocol (UART/I2C/SPI) best fits each and justify your choice in one sentence."
        ),
        "challenge": (
            "Challenge: Multi-Device I2C Bus\n"
            "Wire 2 different I2C devices (e.g. an OLED display and a sensor) on the same SDA/SCL bus, "
            "confirm both have different addresses using an I2C scanner sketch, and read/display data "
            "from both without conflicts."
        ),
        "summary": (
            "UART is simple point-to-point serial communication (used for debugging and GPS modules). "
            "I2C uses two shared wires (SDA/SCL) letting multiple addressed devices share one bus, "
            "ideal for several sensors. SPI uses more wires but achieves higher speed, common for "
            "displays and SD cards. Choosing the right protocol depends on speed needs, device count, "
            "and available pins."
        ),
        "lesson_references": (
            "- Arduino official: 'Wire' (I2C) and 'SPI' library references\n"
            "- SparkFun: 'I2C' and 'Serial Peripheral Interface (SPI)' tutorials\n"
            "- Adafruit: 'I2C Addresses' reference list"
        ),
        "next_lesson_preview": (
            "Next up: Introduction to ESP32 -- WiFi and IoT Basics. You'll move from wired "
            "communication to wireless, connecting a microcontroller directly to the internet."
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
                "real_world_project": (
            "Real-World Project: Remote LED Control Web Server\n"
            "Program an ESP32 to host a simple web page (served directly from the chip) with a button "
            "that turns an onboard/external LED on and off when clicked from any browser on the same "
            "WiFi network -- the foundational pattern behind countless real IoT control panels."
        ),
        "common_mistakes": (
            "- Hardcoding WiFi credentials directly in committed source code -- for any real/shared "
            "project, credentials should be kept out of version control (e.g. in a separate "
            "gitignored config file).\n"
            "- Not handling WiFi connection failures -- a sketch that assumes WiFi.begin() always "
            "succeeds immediately will hang or behave unpredictably on a weak/unavailable network.\n"
            "- Forgetting that ESP32 pin numbering and available pins differ from classic Arduino "
            "boards -- copying pin numbers directly from Arduino Uno tutorials can target the wrong "
            "or non-existent pins.\n"
            "- Blocking the main loop with long delay() calls in a networked sketch, which prevents "
            "the ESP32 from responding to incoming web requests promptly."
        ),
        "best_practices": (
            "- Keep WiFi credentials out of shared/committed code; use a separate config file or "
            "environment-style approach.\n"
            "- Always check WiFi.status() and handle the 'still connecting' state gracefully rather "
            "than assuming instant connection.\n"
            "- Consult the specific ESP32 board's pinout diagram rather than assuming Arduino Uno pin "
            "numbers apply.\n"
            "- Avoid long blocking delay() calls in networked sketches; use millis()-based timing so "
            "the chip stays responsive to network events."
        ),
        "interview_questions": (
            "1. Why shouldn't WiFi credentials be hardcoded into shared or committed source code?\n"
            "2. What could go wrong if a sketch assumes WiFi.begin() connects instantly?\n"
            "3. Why is the ESP32 commonly chosen over a classic Arduino Uno for IoT projects?\n"
            "4. Why does blocking delay() usage cause problems in a networked/web-server sketch?\n"
            "5. What's the basic idea behind an ESP32 serving its own web page?"
        ),
        "assignment": (
            "Assignment: WiFi Connection Status Reporter\n"
            "Write an ESP32 sketch that attempts to connect to WiFi, prints connection progress to "
            "Serial, and once connected prints its assigned local IP address -- the essential first "
            "step of nearly every ESP32 IoT project."
        ),
        "challenge": (
            "Challenge: Sensor Data Web Page\n"
            "Combine this lesson with Lesson 7: have the ESP32 read a sensor (temperature or light) "
            "and serve a web page showing the LIVE current reading, refreshing when the page is "
            "reloaded."
        ),
        "summary": (
            "The ESP32 adds built-in WiFi/Bluetooth to the same programming model as classic Arduino "
            "(setup()/loop()). WiFi.begin() connects to a network, and the ESP32 can both make "
            "outbound requests and serve its own web pages, forming the basis of most DIY IoT "
            "projects. Credentials should be kept out of shared code, and blocking delay() calls "
            "should be avoided in networked sketches."
        ),
        "lesson_references": (
            "- Espressif official: ESP32 Arduino core documentation\n"
            "- Random Nerd Tutorials: 'ESP32 Web Server' guide\n"
            "- Arduino official: 'WiFi' library reference (ESP32 core)"
        ),
        "next_lesson_preview": (
            "Next up: the Capstone Project -- an IoT Temperature & Humidity Dashboard, combining "
            "sensors, wiring, and ESP32 WiFi into one complete, real project."
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
                "real_world_project": (
            "Real-World Project: Deployed IoT Dashboard\n"
            "Complete the full capstone: wire a DHT22 to an ESP32, read temperature and humidity, and "
            "serve a live-updating web dashboard on your local network. Document your wiring diagram, "
            "code, and a photo/description of the working setup as a portfolio piece -- exactly the "
            "kind of project real IoT job applications and freelance gigs expect to see demonstrated."
        ),
        "common_mistakes": (
            "- Powering the DHT22 and ESP32 from mismatched or insufficient power sources, causing "
            "unreliable readings or resets under WiFi load.\n"
            "- Not adding a small delay/retry when a DHT sensor read fails intermittently (common with "
            "these sensors) -- a single missed reading shouldn't crash the whole dashboard.\n"
            "- Serving raw, unformatted sensor data with no error state shown to the user if the "
            "sensor or WiFi temporarily fails.\n"
            "- Forgetting to test the dashboard from a genuinely different device on the network "
            "(not just the same computer used for programming), which is the actual real-world use "
            "case."
        ),
        "best_practices": (
            "- Design for graceful degradation: show 'Sensor Error' on the dashboard rather than "
            "crashing or showing garbage data when a read fails.\n"
            "- Test the final dashboard from a phone or another computer on the same network, not just "
            "the development machine.\n"
            "- Document your project (wiring diagram, code, photos) as you build it -- this capstone "
            "is portfolio-quality work worth presenting professionally.\n"
            "- Consider what you'd add next (data logging, alerts, a nicer UI) to think like a "
            "product engineer, not just someone finishing an assignment."
        ),
        "interview_questions": (
            "1. Walk through the full data flow of this capstone project, from physical sensor to "
            "displayed dashboard.\n"
            "2. How would you handle a temporary sensor read failure without crashing the whole "
            "system?\n"
            "3. What would you need to change to make this dashboard accessible over the internet, "
            "not just the local network?\n"
            "4. What's one feature you would add to make this project genuinely useful day-to-day "
            "(e.g. alerts, logging, historical graphs)?\n"
            "5. How does this capstone project demonstrate skills across the whole course (wiring, "
            "sensors, protocols, and networking)?"
        ),
        "assignment": (
            "Assignment: Project Documentation\n"
            "Write a short README-style document for your completed capstone: what it does, the "
            "wiring diagram (described or sketched), how to run it, and one limitation you'd want to "
            "fix with more time -- the kind of documentation every real engineering project needs."
        ),
        "challenge": (
            "Challenge: Add Historical Logging\n"
            "Extend the capstone to store the last 20 sensor readings in memory (an array) and display "
            "them as a simple list or basic chart on the dashboard, so a visitor can see recent trends, "
            "not just the current instantaneous reading."
        ),
        "summary": (
            "This capstone integrates the entire Electronics & Arduino/ESP32 course: correct sensor "
            "wiring and power, reading a DHT22 with its library, connecting an ESP32 to WiFi, and "
            "serving live data as a web dashboard. Graceful error handling and testing from a real "
            "separate device are what separate a working demo from a genuinely reliable IoT project."
        ),
        "lesson_references": (
            "- Random Nerd Tutorials: 'ESP32 DHT22 Web Server' complete project guide\n"
            "- Adafruit: DHT sensor library documentation\n"
            "- Espressif: ESP32 Arduino core WiFi and WebServer examples"
        ),
        "next_lesson_preview": (
            "You've completed the Electronics & Arduino/ESP32 course! Continue with the Electrical "
            "Engineering course to build a deeper foundation in circuits, power systems, and the "
            "principles underlying everything you've just built."
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
