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
        "real_world_project": (
            "Real-World Project: LED Current-Limiting Resistor Selector\n"
            "Given a table of 5 real LED datasheets (forward voltage and rated current for each color), "
            "calculate the correct current-limiting resistor value for each one when powered from a "
            "5V Arduino pin. This exact calculation is performed by hardware engineers every time a new "
            "LED indicator is added to a product design."
        ),
        "common_mistakes": (
            "- Forgetting to convert units before calculating (mixing mA and A, or kilohms and ohms) — "
            "always convert everything to base units (volts, amps, ohms) before applying V = I x R.\n"
            "- Connecting an LED directly to a supply with NO resistor — without a current-limiting "
            "resistor, an LED draws far more current than it's rated for and burns out almost "
            "instantly.\n"
            "- Confusing voltage (the 'push') with current (the actual 'flow') — a 12V supply isn't "
            "inherently more dangerous than a 5V one; the CURRENT it can deliver through your body is "
            "what determines danger.\n"
            "- Assuming resistance is always constant — some components (like LEDs and diodes) don't "
            "obey Ohm's Law linearly; it applies cleanly only to true 'ohmic' components like resistors."
        ),
        "best_practices": (
            "- Always calculate expected current BEFORE connecting a new component to power, not "
            "after something smokes.\n"
            "- Keep a mental (or written) table of common LED forward voltages and safe currents so "
            "you can quickly size resistors in the field.\n"
            "- Double-check units at every step of a calculation — this is the single most common "
            "source of real-world Ohm's Law errors.\n"
            "- When in doubt, err toward a HIGHER resistor value first (less current, dimmer LED) "
            "rather than lower (risking component damage) — you can always decrease resistance after "
            "confirming safety."
        ),
        "interview_questions": (
            "1. State Ohm's Law and explain what each variable represents physically.\n"
            "2. Why does an LED need a current-limiting resistor even though it's rated for a specific "
            "voltage?\n"
            "3. If you double the resistance in a circuit while keeping voltage constant, what happens "
            "to the current?\n"
            "4. Why is current, not voltage alone, generally the more dangerous factor in electrical "
            "shock?\n"
            "5. Give an example of a component that does NOT follow Ohm's Law linearly, and explain why."
        ),
        "assignment": (
            "Assignment: Resistor Sizing Worksheet\n"
            "Given 5 different LED + supply voltage combinations (varying forward voltage and desired "
            "current), calculate the correct current-limiting resistor value for each, showing your "
            "work step by step (subtract LED forward voltage from supply, then apply Ohm's Law)."
        ),
        "challenge": (
            "Challenge: Multi-LED Resistor Network\n"
            "Design a circuit powering 3 LEDs of different colors (different forward voltages) from a "
            "single 9V supply, each with its own correctly-sized series resistor, ensuring every LED "
            "receives its rated current without exceeding it."
        ),
        "summary": (
            "Ohm's Law (V = I x R) is the foundational equation of electronics, relating voltage "
            "(electrical 'pressure'), current (rate of charge flow), and resistance (opposition to "
            "flow). It's used constantly to size current-limiting resistors, predict circuit behavior, "
            "and avoid damaging components — though it only applies linearly to true ohmic components "
            "like resistors, not to LEDs or diodes."
        ),
        "lesson_references": (
            "- All About Circuits: 'Ohm's Law' tutorial (allaboutcircuits.com)\n"
            "- SparkFun: 'Voltage, Current, Resistance, and Ohm's Law' guide\n"
            "- Adafruit: 'LED current limiting resistor calculator' tool and explanation\n"
            "- Khan Academy: 'Circuits' physics module"
        ),
        "next_lesson_preview": (
            "Next up: Core Components — Resistors, Capacitors, Diodes, and LEDs. You'll learn to "
            "identify and understand the building blocks you'll use in every circuit from here on, "
            "including how to read a resistor's value from its color bands."
        ),
                "assignment": (
            "Assignment: Component Rating Lookup\n"
            "Find the datasheet for 3 real components (any resistor, any LED, any small DC motor). "
            "For each, identify its voltage and current ratings, then calculate the maximum safe "
            "power (P = V x I) it can handle before overheating."
        ),
        "challenge": (
            "Challenge: Voltage Divider Design\n"
            "Using only Ohm's Law and two resistors in series, design a voltage divider that takes a "
            "9V supply and outputs approximately 3.3V for a sensor that requires that voltage. Show "
            "your calculation and verify with a multimeter if you have one."
        ),
        "summary": (
            "Voltage (V) is electrical pressure, current (I) is the rate of charge flow, and "
            "resistance (R) opposes that flow. Ohm's Law (V = I x R) connects all three and is the "
            "single most important formula in electronics, used constantly to size resistors and "
            "predict safe current levels before connecting any component to power."
        ),
        "lesson_references": (
            "- All About Circuits: 'Ohm's Law' tutorial series\n"
            "- SparkFun: 'Voltage, Current, Resistance, and Ohm's Law' tutorial\n"
            "- Any component datasheet's 'Absolute Maximum Ratings' section (practice reading one)"
        ),
        "next_lesson_preview": (
            "Next up: Core Components — resistors, capacitors, diodes, and LEDs. You'll learn how "
            "each behaves in a circuit and how to read their markings and datasheets."
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
        "real_world_project": (
            "Real-World Project: Component Bill of Materials (BOM)\n"
            "Given a simple project brief ('blinking LED indicator with a manual reset button'), write "
            "a proper Bill of Materials listing every component needed (resistor values, capacitor "
            "values if needed, diode/LED part types), with quantities and a one-line justification for "
            "each — the exact document hardware engineers produce before ordering parts for a build."
        ),
        "common_mistakes": (
            "- Inserting an electrolytic capacitor or diode backward — unlike resistors, these "
            "components are polarized and can fail or even be damaged if reversed; always check the "
            "marked polarity band/leg length.\n"
            "- Misreading resistor color bands, especially confusing similar colors (red/orange, "
            "blue/violet) under poor lighting — when in doubt, verify with a multimeter.\n"
            "- Treating a capacitor as if it behaves like a resistor — capacitors block DC once "
            "charged and pass AC, a fundamentally different behavior worth understanding conceptually "
            "even before deep-diving into AC circuit theory.\n"
            "- Buying the wrong LED color/type without checking its forward voltage, leading to "
            "incorrect resistor calculations from Lesson 1."
        ),
        "best_practices": (
            "- Keep a labeled parts organizer or bags for resistor values — color-band misreading is a "
            "common, avoidable source of circuit bugs.\n"
            "- Always verify a diode or electrolytic capacitor's polarity with the datasheet or "
            "physical markings before soldering it in — desoldering polarized components is much more "
            "annoying than double-checking first.\n"
            "- Keep a small multimeter handy to verify unknown or unlabeled resistor values rather than "
            "guessing from faded color bands.\n"
            "- Build a personal reference sheet of common component symbols (resistor, capacitor, "
            "diode, LED) for quickly reading circuit diagrams."
        ),
        "interview_questions": (
            "1. What is the practical difference in behavior between a resistor and a capacitor in a "
            "DC circuit?\n"
            "2. Why do diodes and LEDs need to be inserted in a specific orientation, unlike "
            "resistors?\n"
            "3. How would you determine a resistor's value if its color bands were worn off or "
            "unreadable?\n"
            "4. What does a capacitor's voltage rating tell you, and why does exceeding it matter?\n"
            "5. Why might a hardware engineer prepare a formal Bill of Materials before starting a "
            "build?"
        ),
        "assignment": (
            "Assignment: Color Code Decoder\n"
            "Given 8 resistors described only by their color band sequences, decode each one's "
            "resistance value and tolerance by hand using the standard resistor color code chart, then "
            "verify your answers using a multimeter or online calculator."
        ),
        "challenge": (
            "Challenge: Component Substitution Analysis\n"
            "Given a circuit design calling for a specific resistor and capacitor value that aren't "
            "available in your kit, determine safe substitute values (e.g. combining two resistors in "
            "series/parallel) that achieve an equivalent result, and explain your reasoning."
        ),
        "summary": (
            "Resistors limit current (unpolarized, read via color bands), capacitors store and release "
            "electrical energy (some polarized, some not, blocking DC once charged), diodes allow "
            "current in only one direction (polarized), and LEDs are light-emitting diodes with a "
            "specific forward voltage. Correctly identifying and orienting these components is "
            "foundational to building any working circuit."
        ),
        "lesson_references": (
            "- SparkFun: 'Resistors', 'Capacitors', and 'Diodes' tutorials\n"
            "- All About Circuits: 'Resistor Color Codes' reference chart\n"
            "- Adafruit: 'Component identification' learning guides\n"
            "- Digi-Key: component datasheets (for real-world part specifications)"
        ),
        "next_lesson_preview": (
            "Next up: The Breadboard and Building Your First Circuit. You'll learn how a breadboard's "
            "internal connections work and build your first real, physical circuit — lighting an LED "
            "using the resistor calculations from Lesson 1 and the components from this lesson."
        ),
                "assignment": (
            "Assignment: Component Identification\n"
            "Given photos or descriptions of 5 unlabeled components (a resistor with color bands, a "
            "ceramic capacitor, an electrolytic capacitor, a diode, and an LED), identify each one and "
            "explain the visual cue that gave it away (band colors, polarity marking, physical shape)."
        ),
        "challenge": (
            "Challenge: Decode a Resistor Color Code\n"
            "Without using an online calculator, manually decode the resistance value of 5 resistors "
            "given their color bands, then verify your answers with a multimeter or calculator."
        ),
        "summary": (
            "Resistors limit current, capacitors store and release charge (useful for smoothing and "
            "timing), diodes allow current in only one direction, and LEDs are light-emitting diodes "
            "that must be inserted with correct polarity and protected by a current-limiting resistor."
        ),
        "lesson_references": (
            "- SparkFun: 'Resistors', 'Capacitors', and 'Diodes' tutorials\n"
            "- All About Circuits: 'Electronic Components' reference volume\n"
            "- Digi-Key: Resistor color code calculator (for verification, after manual practice)"
        ),
        "next_lesson_preview": (
            "Next up: The Breadboard and Building Your First Circuit. You'll learn how breadboards "
            "are internally wired and build your first real physical circuit."
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
        "real_world_project": (
            "Real-World Project: Breadboard Layout Planning\n"
            "Before building, sketch (on paper or in a drawing tool) a planned breadboard layout for a "
            "circuit with 2 LEDs, 2 resistors, and one button, minimizing wire crossings and keeping "
            "power/ground rails clean — professional hardware engineers always plan layout before "
            "wiring to avoid costly rework."
        ),
        "common_mistakes": (
            "- Misunderstanding breadboard row connectivity — the 5 holes in each row of the main "
            "section are internally connected, but the two halves of the board (split by the center "
            "gap) are NOT connected to each other.\n"
            "- Confusing the power rails' internal connectivity — the top and bottom power rails are "
            "usually separate strips (also split down the middle on most boards), not one continuous "
            "rail across the whole board.\n"
            "- Forgetting a current-limiting resistor when testing a circuit for 'just a second' — "
            "even brief direct connection can damage an LED.\n"
            "- Loose connections from bent or too-short component legs not making solid contact with "
            "the breadboard's internal spring clips, causing intermittent circuit behavior."
        ),
        "best_practices": (
            "- Always trace and verify your breadboard's rail connectivity with a multimeter's "
            "continuity mode before assuming a layout, since board designs vary slightly.\n"
            "- Build circuits incrementally: connect power, then test with a multimeter BEFORE adding "
            "the next component, catching wiring mistakes early rather than after full assembly.\n"
            "- Keep wires reasonably short and color-coded consistently (e.g. red for power, black for "
            "ground) for easier debugging later.\n"
            "- Double-check polarized components (LEDs, capacitors, diodes) one more time right before "
            "powering on, since this is the most common real-world circuit-building mistake."
        ),
        "interview_questions": (
            "1. Explain how the main row connectivity works on a standard breadboard.\n"
            "2. Why are the two halves of a breadboard (split by the center gap) typically NOT "
            "electrically connected?\n"
            "3. What's a good debugging strategy when a freshly-built breadboard circuit doesn't work "
            "as expected?\n"
            "4. Why should you test circuit sections incrementally rather than building the entire "
            "circuit before powering it on for the first time?\n"
            "5. What tool would you use to verify breadboard connectivity, and how?"
        ),
        "assignment": (
            "Assignment: Breadboard Continuity Map\n"
            "Using a multimeter's continuity mode (or careful visual inspection if unavailable), test "
            "and diagram which holes on your breadboard are electrically connected to which, "
            "confirming or correcting your assumptions about row and rail connectivity."
        ),
        "challenge": (
            "Challenge: Two-LED Independent Control Circuit\n"
            "Build a circuit with 2 LEDs, each with its own resistor and independent push-button "
            "control, sharing a single power source, requiring careful breadboard layout planning to "
            "avoid unintended connections between the two LED circuits."
        ),
        "summary": (
            "A breadboard lets you build circuits without soldering, using internally-connected rows "
            "(usually 5 holes per row, split into two halves) and separate power rails along the "
            "edges. Understanding exactly which holes are connected is essential to avoid wiring "
            "mistakes. Building and testing incrementally, verifying with a multimeter, catches "
            "problems early before they compound."
        ),
        "lesson_references": (
            "- SparkFun: 'How to Use a Breadboard' tutorial\n"
            "- Adafruit: 'Breadboards for Beginners' guide\n"
            "- All About Circuits: 'Breadboard basics' reference\n"
            "- Arduino official documentation: 'Getting Started' breadboard diagrams"
        ),
        "next_lesson_preview": (
            "Next up: Introduction to Arduino and Digital Output. You'll move from purely passive "
            "circuits to programmable ones, writing your first Arduino sketch to control an LED "
            "through code instead of a physical switch."
        ),
                "assignment": (
            "Assignment: Breadboard Wiring Diagram\n"
            "Given a simple circuit schematic (an LED, resistor, and battery in series), draw a "
            "breadboard wiring diagram showing exactly which rows/columns each component would occupy, "
            "before building it physically."
        ),
        "challenge": (
            "Challenge: Two-LED Circuit\n"
            "Build a breadboard circuit with two LEDs (different colors) that light up independently "
            "from two separate buttons, sharing a single power rail. Verify both work correctly and "
            "that neither is damaged (measure current if a multimeter is available)."
        ),
        "summary": (
            "A breadboard's rows are electrically connected in groups (usually 5-pin rows on each "
            "side of the center gap), letting you build circuits without soldering. Power rails run "
            "along the edges. Understanding this internal connectivity is essential for building any "
            "physical circuit correctly and debugging one that doesn't work."
        ),
        "lesson_references": (
            "- SparkFun: 'How to Use a Breadboard' tutorial\n"
            "- Adafruit: 'Breadboards for Beginners' guide\n"
            "- All About Circuits: 'Prototyping Techniques' chapter"
        ),
        "next_lesson_preview": (
            "Next up: Introduction to Arduino and Digital Output. You'll write your first Arduino "
            "sketch and control an LED entirely through code instead of just wiring."
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
        "real_world_project": (
            "Real-World Project: Configurable Status Indicator\n"
            "Build an Arduino sketch controlling a single LED that blinks in different patterns "
            "(solid on, slow blink, fast blink) to represent different 'system states' (idle, "
            "working, error) — the exact pattern used by real embedded devices (routers, printers, "
            "industrial equipment) to communicate status via a single indicator LED."
        ),
        "common_mistakes": (
            "- Forgetting pinMode(pin, OUTPUT) in setup() — without declaring a pin as output, "
            "digitalWrite() calls on it won't behave as expected.\n"
            "- Using delay() for everything, which completely blocks the microcontroller — this "
            "becomes a real problem once you need to do multiple things 'simultaneously' (covered in "
            "later, more advanced non-blocking timing techniques).\n"
            "- Uploading a sketch without selecting the correct board and port in the Arduino IDE, "
            "causing a cryptic upload failure unrelated to the code itself.\n"
            "- Confusing pin numbering between the digital pins and the analog pins (A0-A5), which are "
            "used differently."
        ),
        "best_practices": (
            "- Always set pinMode() explicitly for every pin you use in setup(), even though some "
            "pins have defaults — explicit code is clearer and avoids subtle bugs.\n"
            "- Use meaningful named constants (e.g. const int LED_PIN = 13;) instead of bare numbers "
            "scattered through your code, making sketches much easier to read and modify.\n"
            "- Keep setup() for one-time configuration and loop() for repeating logic — resist the "
            "urge to put initialization code inside loop() by mistake.\n"
            "- Test one small piece of functionality at a time (blink one LED) before combining "
            "multiple behaviors into a more complex sketch."
        ),
        "interview_questions": (
            "1. What is the purpose of the setup() and loop() functions in an Arduino sketch, and how "
            "do they differ?\n"
            "2. What does pinMode(pin, OUTPUT) do, and what happens if you forget it?\n"
            "3. Why might excessive use of delay() become a problem in more complex embedded "
            "projects?\n"
            "4. What's the benefit of using named constants for pin numbers instead of hardcoded "
            "numbers?\n"
            "5. Describe how you would debug an Arduino sketch that uploads successfully but doesn't "
            "behave as expected."
        ),
        "assignment": (
            "Assignment: LED Pattern Library\n"
            "Write 4 separate Arduino sketches, each producing a different LED blink pattern (steady "
            "blink, SOS morse code pattern, fade-like rapid pulsing, random flicker), documenting the "
            "timing logic used in each."
        ),
        "challenge": (
            "Challenge: Multi-LED Sequential Chase\n"
            "Using at least 4 LEDs, write a sketch creating a 'chase' or 'Knight Rider' style effect "
            "where light appears to move across the LEDs in sequence, then reverses direction, using "
            "only digitalWrite() and delay() (non-blocking versions come in a later, more advanced "
            "lesson)."
        ),
        "summary": (
            "Every Arduino sketch has setup() (runs once, for configuration like pinMode()) and "
            "loop() (runs repeatedly, for your main logic). digitalWrite(pin, HIGH/LOW) controls "
            "digital output pins, commonly used to drive LEDs. Using named constants for pins and "
            "testing incrementally are foundational good habits for embedded programming."
        ),
        "lesson_references": (
            "- Arduino official documentation: 'Language Reference' (docs.arduino.cc)\n"
            "- Arduino official 'Getting Started' guide\n"
            "- SparkFun: 'Arduino Comparison Guide' and beginner tutorials\n"
            "- Adafruit: 'Arduino Lesson 0/1' beginner series"
        ),
        "next_lesson_preview": (
            "Next up: Digital Input — Buttons and Pull-up Resistors. You'll learn how to read input "
            "from the physical world (a button press) into your Arduino sketch, including the "
            "important concept of pull-up/pull-down resistors to avoid 'floating' pin readings."
        ),
                "assignment": (
            "Assignment: Blink Pattern Designer\n"
            "Modify the classic Blink sketch to create 3 different LED patterns (e.g. slow-slow-fast, "
            "SOS morse code, a fade-like rapid blink) using only delay() and digitalWrite()."
        ),
        "challenge": (
            "Challenge: Traffic Light Simulator\n"
            "Using 3 LEDs (red, yellow, green) and digitalWrite()/delay(), build a working traffic "
            "light sequence: green for 4 seconds, yellow for 1 second, red for 4 seconds, repeating."
        ),
        "summary": (
            "Arduino sketches have two required functions: setup() (runs once) and loop() (runs "
            "repeatedly). pinMode() configures a pin as INPUT or OUTPUT, and digitalWrite() sets an "
            "output pin HIGH or LOW. This simple model is the foundation for controlling any digital "
            "output, from a single LED to complex multi-component projects."
        ),
        "lesson_references": (
            "- Arduino official documentation: 'Language Reference' and 'Built-in Examples'\n"
            "- SparkFun: 'Installing Arduino IDE' and 'Blink an LED' tutorials\n"
            "- Arduino official: 'Digital Pins' reference"
        ),
        "next_lesson_preview": (
            "Next up: Digital Input — Buttons and Pull-up Resistors. You'll learn to read input from "
            "the physical world, not just control outputs, using buttons and understanding why "
            "'floating' pins cause unreliable readings."
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
        "real_world_project": (
            "Real-World Project: Multi-Button Menu Navigator\n"
            "Build a circuit and sketch with 3 buttons (Up, Down, Select) that navigate through a "
            "list of 4 'menu items' printed to the Serial Monitor, properly debounced — the exact "
            "input pattern used in real embedded device menus (microwave ovens, thermostats, printer "
            "control panels)."
        ),
        "common_mistakes": (
            "- Leaving a digital input pin 'floating' (not connected to a defined HIGH or LOW through "
            "a pull-up/pull-down resistor) — a floating pin reads random, unstable values due to "
            "electrical noise.\n"
            "- Ignoring button 'bounce' — mechanical buttons rapidly flicker between states for a few "
            "milliseconds when pressed, causing a single physical press to register as multiple "
            "presses without debounce logic.\n"
            "- Confusing INPUT_PULLUP logic — with an internal pull-up enabled, the pin reads HIGH "
            "when NOT pressed and LOW when pressed, which is the opposite of many beginners' "
            "intuition.\n"
            "- Wiring a button without any resistor and without using INPUT_PULLUP, leaving the pin "
            "floating when the button is open."
        ),
        "best_practices": (
            "- Prefer Arduino's built-in INPUT_PULLUP mode over external pull-up resistors when "
            "possible — it's simpler wiring and one less component that can fail.\n"
            "- Always implement debounce logic (even simple delay-based debounce) for any button-"
            "driven logic that counts or triggers actions.\n"
            "- Clearly comment your code about whether a pin's logic is active-HIGH or active-LOW, "
            "since this flips depending on pull-up vs pull-down wiring.\n"
            "- Test button input behavior via the Serial Monitor BEFORE building more complex logic "
            "on top of it, isolating input bugs early."
        ),
        "interview_questions": (
            "1. What does it mean for a digital input pin to be 'floating,' and why is it a "
            "problem?\n"
            "2. Explain how INPUT_PULLUP mode changes the logic level read when a button is pressed "
            "versus not pressed.\n"
            "3. What is 'button bounce,' and why does it require debounce logic to handle correctly?\n"
            "4. Describe a simple debounce strategy using delay() or millis().\n"
            "5. Why might a hardware engineer prefer INPUT_PULLUP over wiring an external pull-up "
            "resistor?"
        ),
        "assignment": (
            "Assignment: Debounce Comparison\n"
            "Write two versions of a button-counting sketch: one WITHOUT debounce logic and one WITH "
            "it. Test both physically (or in simulation) and document the difference in counted "
            "presses for the same 10 physical button presses."
        ),
        "challenge": (
            "Challenge: Long-Press vs Short-Press Detection\n"
            "Write a sketch that distinguishes between a short button press (under 500ms) and a long "
            "press (500ms or more), triggering different Serial Monitor messages for each — a common "
            "real embedded UI pattern (e.g. short press = next, long press = menu)."
        ),
        "summary": (
            "Digital input pins read HIGH or LOW signals from the physical world, like button "
            "presses. A 'floating' pin (no defined pull-up/pull-down) gives unreliable readings; "
            "INPUT_PULLUP mode (with active-LOW logic) is the simplest, most common solution. "
            "Mechanical buttons 'bounce,' requiring debounce logic to avoid miscounting a single "
            "press as several."
        ),
        "lesson_references": (
            "- Arduino official documentation: 'Digital Pins' and 'InputPullupSerial' example\n"
            "- SparkFun: 'Pull-up Resistors' tutorial\n"
            "- Arduino official 'Debounce' example sketch\n"
            "- All About Circuits: 'Switch Debounce' reference"
        ),
        "next_lesson_preview": (
            "Next up: Analog Input, PWM, and Servo Control. You'll move beyond simple on/off signals "
            "to reading a continuous range of values (like a potentiometer's position) and outputting "
            "variable signals to control brightness, speed, or a servo motor's angle."
        ),
                "assignment": (
            "Assignment: Button-Controlled LED Toggle\n"
            "Build a circuit where pressing a button once turns an LED on, and pressing it again turns "
            "it off (a toggle, not just 'on while held') — this requires tracking state in your "
            "sketch's variables, not just reading the pin directly."
        ),
        "challenge": (
            "Challenge: Debounced Button Counter\n"
            "Build a circuit that counts button presses and prints the count to the Serial Monitor, "
            "correctly handling 'debouncing' (a single physical press sometimes registers as multiple "
            "electrical transitions) so each press counts exactly once."
        ),
        "summary": (
            "A digital input pin without a defined connection ('floating') reads unpredictable noise. "
            "INPUT_PULLUP mode uses the microcontroller's internal resistor to hold the pin HIGH by "
            "default, reading LOW only when a button connects it to ground — a clean, reliable way to "
            "read button presses without external components."
        ),
        "lesson_references": (
            "- Arduino official: 'Digital Read Serial' and 'Input Pullup Serial' examples\n"
            "- SparkFun: 'Pull-up Resistors' tutorial\n"
            "- Arduino official: 'Debounce' example sketch"
        ),
        "next_lesson_preview": (
            "Next up: Analog Input, PWM, and Servo Control. You'll move beyond simple on/off signals "
            "to reading continuous analog values and generating variable 'analog-like' output."
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
