"""
Seed data for the Electronics & Arduino/ESP32 course — Part 1 (Lessons 1-5).

Covers electrical fundamentals through digital I/O on Arduino, laying the
foundation for the ESP32/IoT lessons in Part 2.
"""

ELECTRONICS_LESSONS_PART1 = [
    {
        "slug": "elec-01-electricity-basics",
        "title": "1. Voltage, Current, and Ohm's Law",
        "level": "beginner",
        "explanation": (
            "Electricity is the flow of electric charge. Voltage (V, measured in volts) is the "
            "'pressure' pushing charge through a circuit. Current (I, measured in amps) is the rate "
            "of charge flow. Resistance (R, measured in ohms) opposes that flow. Ohm's Law ties them "
            "together: V = I x R. This single equation lets you calculate any one value if you know "
            "the other two, and it is the most important formula in all of electronics — you will use "
            "it to size resistors, predict current draw, and avoid burning out components."
        ),
        "examples": (
            "V = I x R\n"
            "I = V / R\n"
            "R = V / I\n\n"
            "Example: A 9V battery connected to a 450 ohm resistor.\n"
            "I = V / R = 9 / 450 = 0.02 A = 20 mA\n"
        ),
        "practice": (
            "1. A 5V supply is connected to a 220 ohm resistor. Calculate the current in mA.\n"
            "2. An LED circuit draws 15 mA from a 3.3V supply through a resistor. Calculate the "
            "resistor's value if the LED itself drops 2V (hint: subtract the LED drop from the "
            "supply voltage first).\n"
            "3. Explain in your own words why a wire with very low resistance connected directly "
            "across a battery (a short circuit) causes a dangerously high current."
        ),
        "mini_project": (
            "Mini Project: Ohm's Law Calculator\n"
            "Write a small script (Python, or use the built-in Electronics Calculator tool once "
            "available) that takes any two of V, I, R and computes the third. Test it against the "
            "practice problems above."
        ),
        "quiz": {
            "title": "Voltage, Current, and Ohm's Law Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does Ohm's Law state?",
                    "option_a": "V = I / R",
                    "option_b": "V = I x R",
                    "option_c": "I = V x R",
                    "option_d": "R = I x V",
                    "correct_option": "b",
                    "explanation": "Ohm's Law is V = I x R, relating voltage, current, and resistance.",
                },
                {
                    "text": "What is the unit of electrical current?",
                    "option_a": "Volt",
                    "option_b": "Ohm",
                    "option_c": "Amp",
                    "option_d": "Watt",
                    "correct_option": "c",
                    "explanation": "Current is measured in amperes (amps), symbol A.",
                },
                {
                    "text": "A 12V supply drives current through a 1000 ohm resistor. What is the current?",
                    "option_a": "12 mA",
                    "option_b": "1.2 A",
                    "option_c": "120 mA",
                    "option_d": "0.012 mA",
                    "correct_option": "a",
                    "explanation": "I = V/R = 12/1000 = 0.012 A = 12 mA.",
                },
            ],
        },
    },
    {
        "slug": "elec-02-components",
        "title": "2. Core Components: Resistors, Capacitors, Diodes, LEDs",
        "level": "beginner",
        "explanation": (
            "Resistors limit current and are color-coded to show their value in ohms. Capacitors "
            "store energy in an electric field and are used for filtering and timing; their value is "
            "measured in farads (usually microfarads, uF). Diodes allow current to flow in only one "
            "direction, protecting circuits from reversed polarity. LEDs (Light Emitting Diodes) are "
            "diodes that emit light when current flows through them in the correct direction, and "
            "they always need a current-limiting resistor in series to avoid burning out."
        ),
        "examples": (
            "Common resistor color bands: Brown-Black-Red = 1000 ohm (1k)\n"
            "Typical LED forward voltage: red/green ~2V, blue/white ~3.2V\n"
            "LED resistor formula: R = (Vsupply - Vled) / Iled\n"
            "Example: 5V supply, red LED (2V drop), want 10mA: R = (5-2)/0.01 = 300 ohm\n"
        ),
        "practice": (
            "1. Look up (or use the reference library) the color bands for a 4.7k ohm resistor.\n"
            "2. Calculate the correct resistor for a blue LED (3.2V drop) run from a 5V supply at 15mA.\n"
            "3. Explain why connecting an LED backwards (reverse polarity) simply results in no light, "
            "while connecting it with no resistor at all can destroy it."
        ),
        "mini_project": (
            "Mini Project: Component Identification Sheet\n"
            "Using the component database/pinout reference, create a table listing 5 resistor values, "
            "their color codes, and a matching LED resistor calculation for each, as if sizing them "
            "for a 5V Arduino circuit."
        ),
        "quiz": {
            "title": "Core Components Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does a resistor do in a circuit?",
                    "option_a": "Stores energy in a magnetic field",
                    "option_b": "Limits current flow",
                    "option_c": "Converts AC to DC",
                    "option_d": "Amplifies voltage",
                    "correct_option": "b",
                    "explanation": "Resistors oppose (limit) current flow according to Ohm's Law.",
                },
                {
                    "text": "Why does an LED need a series resistor?",
                    "option_a": "To make it brighter",
                    "option_b": "To change its color",
                    "option_c": "To limit current and prevent it from burning out",
                    "option_d": "LEDs never need a resistor",
                    "correct_option": "c",
                    "explanation": "Without a current-limiting resistor, an LED draws excessive current and fails.",
                },
                {
                    "text": "What happens if a diode is connected in reverse (against its allowed direction)?",
                    "option_a": "It blocks current flow",
                    "option_b": "It doubles the voltage",
                    "option_c": "It always explodes",
                    "option_d": "Nothing changes",
                    "correct_option": "a",
                    "explanation": "Diodes only conduct in one direction (forward bias); reverse-biased, they block current.",
                },
            ],
        },
    },
    {
        "slug": "elec-03-breadboard",
        "title": "3. The Breadboard and Building Your First Circuit",
        "level": "beginner",
        "explanation": (
            "A breadboard lets you build circuits without soldering. The two outer rows on each side "
            "(marked + and -) are power rails, connected horizontally along their full length. The "
            "central rows are split into groups of 5 holes, connected vertically in short columns, "
            "with a gap down the middle separating the two halves — this gap is designed to fit an IC "
            "chip. Components plugged into the same column of 5 holes are electrically connected to "
            "each other."
        ),
        "examples": (
            "Basic LED circuit on a breadboard:\n"
            "1. Connect breadboard + rail to Arduino 5V, - rail to Arduino GND\n"
            "2. Place LED with long leg (anode) in one column, short leg (cathode) in another\n"
            "3. Connect a 220 ohm resistor from the anode column to the + rail\n"
            "4. Connect a wire from the cathode column to the - rail\n"
            "5. The LED lights up immediately, no code required\n"
        ),
        "practice": (
            "1. Sketch (on paper or in the circuit simulator) the LED circuit described above.\n"
            "2. Identify which breadboard holes are electrically connected to which in a standard "
            "half-size breadboard.\n"
            "3. Modify the circuit to add a push-button in series with the LED so it only lights while "
            "pressed."
        ),
        "mini_project": (
            "Mini Project: First Working Circuit\n"
            "Build (physically, or in the breadboard simulator) a circuit with one LED, one 220 ohm "
            "resistor, one push-button, and a coin-cell or 3xAA battery pack, so the LED only lights "
            "while the button is held down. Take a photo or screenshot of the finished circuit."
        ),
        "quiz": {
            "title": "Breadboard Basics Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "On a standard breadboard, how are the central rows grouped?",
                    "option_a": "All connected together across the whole board",
                    "option_b": "In short vertical columns of 5 holes",
                    "option_c": "Not connected to anything",
                    "option_d": "Only the top row is connected",
                    "correct_option": "b",
                    "explanation": "Central breadboard rows are split into columns of 5 connected holes, with a center gap.",
                },
                {
                    "text": "What are the outer + and - rails used for?",
                    "option_a": "Distributing power along the whole board",
                    "option_b": "Holding ICs",
                    "option_c": "Nothing, they are decorative",
                    "option_d": "Only for resistors",
                    "correct_option": "a",
                    "explanation": "The power rails run the length of the board and are used to distribute supply voltage and ground.",
                },
                {
                    "text": "Which LED leg (pin) is the anode, needing the more positive voltage?",
                    "option_a": "The shorter leg",
                    "option_b": "The longer leg",
                    "option_c": "Both legs are identical",
                    "option_d": "It depends on the resistor",
                    "correct_option": "b",
                    "explanation": "The longer leg of an LED is the anode (+); the shorter leg is the cathode (-).",
                },
            ],
        },
    },
    {
        "slug": "elec-04-arduino-intro",
        "title": "4. Introduction to Arduino and Digital Output",
        "level": "beginner",
        "explanation": (
            "Arduino is a microcontroller board that runs simple C/C++ code (called a 'sketch') to "
            "control real-world hardware. Every sketch has two required functions: setup(), which "
            "runs once to configure pins, and loop(), which runs repeatedly forever. Digital pins can "
            "be set as OUTPUT to drive a signal high (5V/3.3V) or low (0V) — enough to switch an LED "
            "on and off directly."
        ),
        "examples": (
            "// Blink an LED on pin 13\n"
            "void setup() {\n"
            "  pinMode(13, OUTPUT);\n"
            "}\n\n"
            "void loop() {\n"
            "  digitalWrite(13, HIGH);  // LED on\n"
            "  delay(1000);             // wait 1 second\n"
            "  digitalWrite(13, LOW);   // LED off\n"
            "  delay(1000);\n"
            "}\n"
        ),
        "practice": (
            "1. Wire an LED with a 220 ohm resistor to Arduino pin 9 and GND.\n"
            "2. Modify the blink sketch above to blink on pin 9 instead of 13.\n"
            "3. Change the timing so the LED is on for 200ms and off for 800ms — a quick flash pattern."
        ),
        "mini_project": (
            "Mini Project: Traffic Light Simulator\n"
            "Using 3 LEDs (red, yellow, green) each with its own resistor, write a sketch that cycles "
            "them like a real traffic light: green for 4s, yellow for 1s, red for 4s, repeating."
        ),
        "quiz": {
            "title": "Arduino Intro Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which function in an Arduino sketch runs repeatedly forever?",
                    "option_a": "setup()",
                    "option_b": "main()",
                    "option_c": "loop()",
                    "option_d": "run()",
                    "correct_option": "c",
                    "explanation": "loop() runs continuously after setup() has run once.",
                },
                {
                    "text": "What does digitalWrite(pin, HIGH) do?",
                    "option_a": "Reads a sensor value",
                    "option_b": "Sets the pin's output voltage to logic high (on)",
                    "option_c": "Deletes the pin configuration",
                    "option_d": "Sets the pin to input mode",
                    "correct_option": "b",
                    "explanation": "digitalWrite with HIGH drives the pin to its supply voltage (logic 1).",
                },
                {
                    "text": "What must be called before using a pin as an output?",
                    "option_a": "pinMode(pin, OUTPUT) in setup()",
                    "option_b": "Nothing, all pins are outputs by default",
                    "option_c": "digitalRead(pin)",
                    "option_d": "delay(pin)",
                    "correct_option": "a",
                    "explanation": "pinMode() configures whether a pin behaves as INPUT or OUTPUT, and should be set in setup().",
                },
            ],
        },
    },
    {
        "slug": "elec-05-digital-input",
        "title": "5. Digital Input: Buttons and Pull-up Resistors",
        "level": "beginner",
        "explanation": (
            "Reading a button requires a digital INPUT pin. Without a defined resting state, an "
            "unconnected input 'floats' and reads random noise. A pull-up resistor connects the pin "
            "to 5V by default, so it reads HIGH when the button is not pressed, and LOW when the "
            "button connects the pin to GND. Most microcontrollers, including Arduino, have a built-in "
            "pull-up you can enable in software with INPUT_PULLUP, removing the need for an external "
            "resistor."
        ),
        "examples": (
            "// Read a button using the internal pull-up resistor\n"
            "const int buttonPin = 2;\n"
            "const int ledPin = 13;\n\n"
            "void setup() {\n"
            "  pinMode(buttonPin, INPUT_PULLUP);\n"
            "  pinMode(ledPin, OUTPUT);\n"
            "}\n\n"
            "void loop() {\n"
            "  int state = digitalRead(buttonPin);\n"
            "  if (state == LOW) {       // pressed pulls the pin to GND\n"
            "    digitalWrite(ledPin, HIGH);\n"
            "  } else {\n"
            "    digitalWrite(ledPin, LOW);\n"
            "  }\n"
            "}\n"
        ),
        "practice": (
            "1. Wire a push-button between pin 2 and GND (no external resistor needed with "
            "INPUT_PULLUP).\n"
            "2. Upload the example sketch and confirm the LED lights only while the button is held.\n"
            "3. Modify the sketch to toggle the LED on each press (stay on after release, turn off on "
            "the next press) instead of only lighting while held."
        ),
        "mini_project": (
            "Mini Project: Button-Controlled Counter\n"
            "Write a sketch that counts button presses and prints the count to the Serial Monitor "
            "each time the button is pressed, using simple debounce logic (ignore repeated triggers "
            "within 200ms) so a single press isn't counted multiple times."
        ),
        "quiz": {
            "title": "Digital Input Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Why does a floating (unconnected) digital input read unreliable values?",
                    "option_a": "Because Arduino pins are always broken",
                    "option_b": "Because it has no defined voltage and picks up electrical noise",
                    "option_c": "Because floating pins are illegal in code",
                    "option_d": "It doesn't — floating inputs are always stable",
                    "correct_option": "b",
                    "explanation": "A floating pin has no fixed reference and can read HIGH or LOW unpredictably from noise.",
                },
                {
                    "text": "With INPUT_PULLUP, what does the pin read when the button is NOT pressed?",
                    "option_a": "LOW",
                    "option_b": "HIGH",
                    "option_c": "Random",
                    "option_d": "It reads 2.5V exactly",
                    "correct_option": "b",
                    "explanation": "The internal pull-up holds the pin HIGH until the button connects it to GND.",
                },
                {
                    "text": "What is 'debouncing' used for?",
                    "option_a": "Making the LED brighter",
                    "option_b": "Preventing a single physical press from being read as multiple presses",
                    "option_c": "Increasing the button's voltage",
                    "option_d": "Speeding up the microcontroller clock",
                    "correct_option": "b",
                    "explanation": "Mechanical button contacts can bounce, causing multiple rapid HIGH/LOW transitions from one press; debouncing filters that out.",
                },
            ],
        },
    },
]
