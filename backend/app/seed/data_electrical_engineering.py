"""
Seed data for the Electrical Engineering course — complete (Lessons 1-10).

Covers: DC Circuits, AC Circuits, Transformers, Electric Motors, Generators,
Inverters, UPS Systems, Solar Systems, Battery Management, Power Distribution
& Protection Systems.
"""

ELECTRICAL_ENGINEERING_LESSONS = [
    {
        "slug": "elec-eng-01-dc-circuits",
        "title": "1. DC Circuits",
        "level": "beginner",
        "explanation": (
            "A DC (Direct Current) circuit is one where current flows in a single, constant "
            "direction, unlike AC which reverses direction periodically. Every DC circuit is built "
            "from three quantities related by Ohm's Law: Voltage (V, in volts) is the electrical "
            "pressure pushing current, Current (I, in amps) is the rate of charge flow, and "
            "Resistance (R, in ohms) opposes that flow. Ohm's Law states V = I x R. Circuits are "
            "either series (one path, current is the same everywhere, voltages add up) or parallel "
            "(multiple paths, voltage is the same across each branch, currents add up). Kirchhoff's "
            "Voltage Law says the sum of voltage drops around any closed loop equals zero. "
            "Kirchhoff's Current Law says the current entering a junction equals the current leaving it."
        ),
        "examples": (
            "Example: A 12V battery connected to a 4-ohm resistor.\n"
            "I = V / R = 12 / 4 = 3 amps\n\n"
            "Series resistors: R_total = R1 + R2 + R3 (add directly)\n"
            "Parallel resistors: 1/R_total = 1/R1 + 1/R2 + 1/R3\n\n"
            "Two 6-ohm resistors in parallel: 1/R = 1/6 + 1/6 = 1/3, so R_total = 3 ohms\n"
        ),
        "practice": (
            "1. A 9V battery is connected across a 3-ohm resistor. Find the current.\n"
            "2. Two resistors of 10 ohms and 20 ohms are in series across a 12V supply. Find the total "
            "resistance and the current.\n"
            "3. The same two resistors are now in parallel across the same 12V supply. Find the total "
            "resistance and the total current drawn from the battery."
        ),
        "mini_project": (
            "Mini Project: Resistor Network Calculator\n"
            "Write a short program (or work by hand) that takes a list of resistor values and a mode "
            "(series or parallel) and computes the total resistance, then the current drawn from a "
            "given supply voltage using Ohm's Law."
        ),
                "real_world_project": (
            "Real-World Project: Battery-Powered Circuit Design\n"
            "Design (on paper first, then build if you have components) a simple DC circuit powering "
            "3 LEDs from a 9V battery, each with a correctly calculated series resistor, showing your "
            "Ohm's Law calculations for every resistor value chosen."
        ),
        "common_mistakes": (
            "- Confusing series and parallel circuit behavior -- in series, current is the same "
            "everywhere and voltage divides; in parallel, voltage is the same across branches and "
            "current divides. Mixing these up leads to wrong calculations.\n"
            "- Forgetting a current-limiting resistor when powering an LED directly from a battery, "
            "which can destroy the LED almost instantly.\n"
            "- Miscalculating total resistance in parallel circuits by simply adding resistances "
            "(which only works for series) instead of using the parallel resistance formula.\n"
            "- Ignoring a component's power rating (P = IV or I²R) and burning out a resistor rated "
            "for less power than the circuit actually dissipates through it."
        ),
        "best_practices": (
            "- Always calculate expected current BEFORE connecting a circuit to power, using Ohm's "
            "Law, to catch dangerous mistakes on paper first.\n"
            "- Double-check whether components are wired in series or parallel before applying "
            "formulas -- draw the circuit if it's not obvious.\n"
            "- Check power ratings (not just voltage/current) on every component, especially "
            "resistors, to avoid overheating failures.\n"
            "- Use a multimeter to verify actual voltage/current in a real circuit and compare against "
            "your calculated predictions -- discrepancies reveal wiring mistakes."
        ),
        "interview_questions": (
            "1. State Ohm's Law and explain what each variable represents.\n"
            "2. What's the key difference in how voltage and current behave in series versus parallel "
            "circuits?\n"
            "3. How do you calculate total resistance for resistors in parallel?\n"
            "4. Why is a current-limiting resistor necessary when powering an LED?\n"
            "5. How would you calculate the power dissipated by a resistor, and why does that matter "
            "practically?"
        ),
        "assignment": (
            "Assignment: Series vs Parallel Calculation Set\n"
            "Given 2 circuits (one with 3 resistors in series, one with the same 3 resistors in "
            "parallel, both at 12V), calculate total resistance, total current, and the voltage/"
            "current through each individual resistor for both configurations."
        ),
        "challenge": (
            "Challenge: LED Array Power Budget\n"
            "Design a circuit powering 6 LEDs from a single 9V battery (mixing series and parallel "
            "groupings as needed), calculating appropriate resistor values for each LED and verifying "
            "the total current draw stays within a reasonable battery capacity."
        ),
        "summary": (
            "DC circuits have current flowing in one constant direction, governed by Ohm's Law "
            "(V = IR). Series circuits share the same current with voltage dividing across "
            "components; parallel circuits share the same voltage with current dividing across "
            "branches. Correctly identifying circuit topology and respecting component power ratings "
            "are essential for safe, working circuits."
        ),
        "lesson_references": (
            "- All About Circuits: 'DC Circuits' textbook volume (free online)\n"
            "- Khan Academy: 'Circuits' physics course\n"
            "- SparkFun: 'Series and Parallel Circuits' tutorial"
        ),
        "next_lesson_preview": (
            "Next up: AC Circuits. You'll learn how alternating current differs fundamentally from DC, "
            "including frequency, RMS values, and why household power uses AC instead of DC."
        ),
"quiz": {
            "title": "DC Circuits Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What formula relates voltage, current, and resistance?",
                    "option_a": "V = I / R",
                    "option_b": "V = I x R",
                    "option_c": "V = R / I",
                    "option_d": "I = V x R",
                    "correct_option": "b",
                    "explanation": "Ohm's Law: V = I x R.",
                },
                {
                    "text": "In a series circuit, what stays the same through every component?",
                    "option_a": "Voltage",
                    "option_b": "Resistance",
                    "option_c": "Current",
                    "option_d": "Power",
                    "correct_option": "c",
                    "explanation": "Series circuits have a single path, so current is identical everywhere in the loop.",
                },
                {
                    "text": "In a parallel circuit, what stays the same across every branch?",
                    "option_a": "Current",
                    "option_b": "Voltage",
                    "option_c": "Resistance",
                    "option_d": "Power only",
                    "correct_option": "b",
                    "explanation": "All branches of a parallel circuit share the same two connection nodes, so voltage across each branch is equal.",
                },
            ],
        },
    },
    {
        "slug": "elec-eng-02-ac-circuits",
        "title": "2. AC Circuits",
        "level": "beginner",
        "explanation": (
            "AC (Alternating Current) periodically reverses direction, typically following a sine "
            "wave, and is described by frequency (Hz — cycles per second, e.g. 50Hz or 60Hz mains "
            "power) and amplitude. Because AC voltage/current constantly changes, we describe its "
            "'effective' value using RMS (Root Mean Square), which is the DC-equivalent value that "
            "would deliver the same power. For a sine wave, RMS = Peak / sqrt(2) (~0.707 x Peak). "
            "AC circuits also involve reactance from capacitors and inductors, which oppose current "
            "changes and shift the timing (phase) between voltage and current — together resistance "
            "and reactance form impedance (Z), measured in ohms."
        ),
        "examples": (
            "Nigerian/most-of-world mains: 230V RMS, 50Hz\n"
            "Peak voltage = RMS x sqrt(2) = 230 x 1.414 = ~325V\n\n"
            "Impedance combines resistance (R) and reactance (X): Z = sqrt(R^2 + X^2)\n"
        ),
        "practice": (
            "1. If mains supply is 230V RMS, what is the peak voltage?\n"
            "2. A circuit has 50Hz frequency. How many complete cycles occur in 2 seconds?\n"
            "3. Explain in your own words why RMS is used instead of peak or average voltage to rate "
            "household appliances."
        ),
        "mini_project": (
            "Mini Project: AC Waveform Sketch\n"
            "By hand or in code, generate 20 sample points of one full cycle of a sine wave with peak "
            "value 325V and frequency 50Hz, and calculate the RMS from your samples to confirm it is "
            "close to 230V."
        ),
                "real_world_project": (
            "Real-World Project: Household Appliance Power Audit\n"
            "Look up (or read from) the power rating labels of 5 household appliances. For each, "
            "identify its rated voltage, current, and power, calculate whether the stated numbers are "
            "consistent (P = VI), and note whether it runs on single-phase mains power."
        ),
        "common_mistakes": (
            "- Confusing peak voltage with RMS voltage -- household '230V' or '120V' mains ratings are "
            "RMS values, not peak; the actual peak voltage is significantly higher (RMS x sqrt(2)).\n"
            "- Assuming AC circuit calculations work exactly like DC -- reactive components "
            "(capacitors/inductors) introduce phase differences that pure resistive DC math doesn't "
            "capture.\n"
            "- Forgetting that frequency (50Hz vs 60Hz) varies by country/region, which matters when "
            "importing or using equipment across regions.\n"
            "- Treating AC power as inherently more dangerous or less dangerous than DC without "
            "understanding both can be lethal at sufficient voltage/current -- respect BOTH equally."
        ),
        "best_practices": (
            "- Always use RMS values (not peak) when working with standard AC voltage/current "
            "ratings, since that's the industry convention for describing 'effective' power.\n"
            "- Check equipment's rated frequency (50Hz/60Hz) compatibility before using it in a "
            "different region.\n"
            "- Treat any AC mains-connected circuit work with extreme caution and proper safety "
            "practices -- this is not a 'learn by trial and error with live power' subject.\n"
            "- Use a proper AC-rated multimeter setting when measuring mains voltage, never a DC "
            "setting."
        ),
        "interview_questions": (
            "1. What does RMS voltage represent, and why is it used instead of peak voltage for rating "
            "AC equipment?\n"
            "2. Why does household power use AC instead of DC?\n"
            "3. What is frequency in the context of AC power, and what are the two common standard "
            "values worldwide?\n"
            "4. Why can't you always apply simple DC Ohm's Law math directly to AC circuits with "
            "capacitors or inductors?\n"
            "5. Why is mains AC power dangerous even though its RMS voltage may seem 'not that high' "
            "compared to peak values?"
        ),
        "assignment": (
            "Assignment: RMS Calculation Practice\n"
            "Given 4 different peak AC voltage values, calculate the corresponding RMS voltage for "
            "each, and explain in one sentence why RMS is the more practically useful number for rating "
            "equipment."
        ),
        "challenge": (
            "Challenge: 50Hz vs 60Hz Research\n"
            "Research which countries use 50Hz versus 60Hz mains power, and explain one practical "
            "consequence for someone traveling internationally with electronic equipment (beyond just "
            "the voltage difference)."
        ),
        "summary": (
            "AC (Alternating Current) periodically reverses direction following a sine wave, described "
            "by frequency (Hz) and RMS voltage/current (the 'effective' value used for standard "
            "ratings, distinct from peak). Household power uses AC due to efficient long-distance "
            "transmission via transformers. AC circuit analysis requires accounting for phase "
            "differences introduced by reactive components."
        ),
        "lesson_references": (
            "- All About Circuits: 'AC Circuits' textbook volume\n"
            "- Khan Academy: 'AC Circuit Analysis'\n"
            "- Fluke: 'RMS vs Peak Voltage' explainer"
        ),
        "next_lesson_preview": (
            "Next up: Transformers. You'll learn how AC's ability to change voltage via "
            "electromagnetic induction makes long-distance power transmission and household voltage "
            "conversion possible."
        ),
"quiz": {
            "title": "AC Circuits Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does RMS stand for?",
                    "option_a": "Rated Maximum Supply",
                    "option_b": "Root Mean Square",
                    "option_c": "Reactive Mean Signal",
                    "option_d": "Real Measured Sine",
                    "correct_option": "b",
                    "explanation": "RMS (Root Mean Square) gives the DC-equivalent effective value of an AC waveform.",
                },
                {
                    "text": "What is the standard mains frequency in most of the world (including Nigeria)?",
                    "option_a": "50Hz",
                    "option_b": "100Hz",
                    "option_c": "12Hz",
                    "option_d": "220Hz",
                    "correct_option": "a",
                    "explanation": "Most countries, including Nigeria, use 50Hz mains frequency (North America mainly uses 60Hz).",
                },
                {
                    "text": "What is impedance?",
                    "option_a": "Only the resistance in a circuit",
                    "option_b": "The combined opposition to AC current from resistance and reactance",
                    "option_c": "The peak voltage of a signal",
                    "option_d": "The frequency of a signal",
                    "correct_option": "b",
                    "explanation": "Impedance (Z) combines resistance and reactance: Z = sqrt(R^2 + X^2).",
                },
            ],
        },
    },
    {
        "slug": "elec-eng-03-transformers",
        "title": "3. Transformers",
        "level": "beginner",
        "explanation": (
            "A transformer transfers AC electrical energy between two circuits through "
            "electromagnetic induction, changing voltage while (ideally) keeping power constant. It "
            "has a primary winding (input) and secondary winding (output) wrapped around a shared "
            "iron core. The turns ratio determines the voltage change: Vs/Vp = Ns/Np, where N is the "
            "number of turns. A step-up transformer increases voltage (fewer primary turns than "
            "secondary); a step-down transformer decreases voltage. Since ideal power in equals power "
            "out (Vp x Ip = Vs x Is), a step-up transformer decreases current as it increases voltage."
        ),
        "examples": (
            "Step-down transformer: Np = 1000 turns, Ns = 100 turns, Vp = 230V\n"
            "Vs = Vp x (Ns/Np) = 230 x (100/1000) = 23V\n\n"
            "Power conservation: if Vp x Ip = Vs x Is, and Vs is 10x smaller, Is is 10x larger than Ip.\n"
        ),
        "practice": (
            "1. A transformer has 500 primary turns and 50 secondary turns, with 230V on the primary. "
            "Find the secondary voltage and state whether this is step-up or step-down.\n"
            "2. If the same transformer draws 2A on the primary, what current flows on the secondary "
            "(assume ideal, lossless transformer)?\n"
            "3. Why do transformers only work with AC and not DC?"
        ),
        "mini_project": (
            "Mini Project: Transformer Ratio Table\n"
            "Build a small table (on paper or in code) showing secondary voltage and current for a "
            "230V, 2A primary supply across turns ratios of 1:1, 2:1, 10:1, and 1:10."
        ),
                "real_world_project": (
            "Real-World Project: Transformer Ratio Investigation\n"
            "Find (or read the label of) any real wall-wart/phone charger transformer. Identify its "
            "input and output voltage ratings, calculate the implied turns ratio, and explain whether "
            "it's a step-up or step-down transformer."
        ),
        "common_mistakes": (
            "- Assuming a transformer can step up voltage 'for free' without any tradeoff -- power is "
            "approximately conserved (P = VI), so stepping up voltage proportionally steps DOWN "
            "current, not a free lunch.\n"
            "- Trying to use a transformer with DC input -- transformers rely on CHANGING magnetic "
            "flux (from AC) to induce a secondary voltage; DC produces no induction after the initial "
            "transient.\n"
            "- Ignoring transformer efficiency losses (core losses, winding resistance) and assuming "
            "100% ideal behavior in real calculations.\n"
            "- Confusing turns ratio direction -- more turns on the secondary means step-UP, fewer "
            "turns means step-DOWN; it's easy to get this backward."
        ),
        "best_practices": (
            "- Always calculate both voltage AND current using the turns ratio (they move in opposite "
            "directions) rather than only tracking voltage.\n"
            "- Remember transformers only work with AC, never DC, due to the electromagnetic induction "
            "principle they rely on.\n"
            "- Account for real-world efficiency losses (typically 90-99% for well-designed "
            "transformers) rather than assuming ideal 100% power transfer in practical estimates.\n"
            "- Check a transformer's power (VA) rating, not just its voltage ratio, before using it "
            "for a specific load."
        ),
        "interview_questions": (
            "1. Why do transformers only work with AC, not DC?\n"
            "2. If a transformer steps voltage UP, what necessarily happens to current, and why?\n"
            "3. What determines whether a transformer is 'step-up' or 'step-down'?\n"
            "4. Why is long-distance power transmission done at very high voltage using step-up "
            "transformers?\n"
            "5. What's the difference between an ideal transformer and a real one in terms of "
            "efficiency?"
        ),
        "assignment": (
            "Assignment: Turns Ratio Calculations\n"
            "Given 4 different transformer scenarios (primary turns, secondary turns, and input "
            "voltage), calculate the output voltage for each, and identify whether each is step-up or "
            "step-down."
        ),
        "challenge": (
            "Challenge: Power Transmission Explainer\n"
            "Write a short explanation (with calculations) of why power is transmitted over long "
            "distances at very high voltage (using step-up transformers) and stepped back down near "
            "consumers, in terms of reducing transmission line current and resulting energy loss."
        ),
        "summary": (
            "Transformers transfer AC power between circuits via electromagnetic induction, changing "
            "voltage according to the turns ratio between primary and secondary windings, while "
            "current changes inversely (approximately conserving power). They only work with AC (not "
            "DC) and are essential for efficient long-distance power transmission and voltage "
            "conversion for everyday devices."
        ),
        "lesson_references": (
            "- All About Circuits: 'Transformers' textbook volume\n"
            "- Khan Academy: 'Transformers' physics lesson\n"
            "- IEEE Spectrum: articles on power transmission grid design"
        ),
        "next_lesson_preview": (
            "Next up: Electric Motors. You'll learn how electrical energy is converted into mechanical "
            "rotation, the reverse process of what you'll see in the following Generators lesson."
        ),
"quiz": {
            "title": "Transformers Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What principle allows a transformer to transfer energy between windings?",
                    "option_a": "Chemical reaction",
                    "option_b": "Electromagnetic induction",
                    "option_c": "Direct wire connection",
                    "option_d": "Capacitive coupling",
                    "correct_option": "b",
                    "explanation": "Transformers work by electromagnetic induction between the primary and secondary windings via a shared core.",
                },
                {
                    "text": "In an ideal step-down transformer, what happens to current on the secondary side?",
                    "option_a": "It decreases",
                    "option_b": "It increases",
                    "option_c": "It stays exactly the same",
                    "option_d": "It becomes zero",
                    "correct_option": "b",
                    "explanation": "Since power is conserved (Vp x Ip = Vs x Is), a lower secondary voltage means a higher secondary current.",
                },
                {
                    "text": "Why don't transformers work with DC?",
                    "option_a": "DC has too much current",
                    "option_b": "DC voltage is always too low",
                    "option_c": "A constant DC current produces no changing magnetic field needed for induction",
                    "option_d": "Transformers are only rated for AC by law",
                    "correct_option": "c",
                    "explanation": "Induction requires a changing magnetic field; steady DC produces no change, so no voltage is induced in the secondary.",
                },
            ],
        },
    },
    {
        "slug": "elec-eng-04-electric-motors",
        "title": "4. Electric Motors",
        "level": "intermediate",
        "explanation": (
            "Electric motors convert electrical energy into mechanical rotation using magnetic "
            "fields. DC motors use a magnetic field and current-carrying coil (armature) — force on "
            "the coil (F = BIL) causes rotation, with a commutator reversing current direction each "
            "half-turn to keep the motor spinning. AC induction motors (the most common industrial "
            "motor) use a rotating magnetic field created by AC current in stator windings, which "
            "induces current in the rotor and causes it to follow the field. Key motor concepts: "
            "torque (rotational force), RPM (speed), and starting current (which is much higher than "
            "running current, requiring protection)."
        ),
        "examples": (
            "Basic DC motor force: F = B x I x L (B = magnetic flux density, I = current, L = wire length)\n"
            "Synchronous speed of an AC induction motor: Ns = (120 x f) / P\n"
            "  where f = supply frequency (Hz), P = number of poles\n"
            "  Example: 50Hz, 4-pole motor -> Ns = (120 x 50) / 4 = 1500 RPM\n"
        ),
        "practice": (
            "1. Calculate the synchronous speed of a 50Hz, 2-pole induction motor.\n"
            "2. Explain the role of the commutator in a brushed DC motor.\n"
            "3. Why is starting current on an induction motor much higher than its running current, "
            "and why does this matter for circuit protection?"
        ),
        "mini_project": (
            "Mini Project: Motor Selection Sheet\n"
            "For three example applications (a ceiling fan, a water pump, and a robot wheel), list "
            "which motor type (DC brushed, DC brushless, AC induction, or servo/stepper) you would "
            "choose and justify your reasoning based on speed control, cost, and torque needs."
        ),
                "real_world_project": (
            "Real-World Project: Motor Type Comparison Chart\n"
            "Research 3 different real applications (an electric fan, an electric vehicle drive motor, "
            "a robotics servo) and identify which motor type each likely uses (DC brushed, brushless "
            "DC, stepper, etc.), explaining why that type suits the application's requirements."
        ),
        "common_mistakes": (
            "- Assuming all electric motors work identically -- DC brushed, brushless DC, stepper, and "
            "AC induction motors have meaningfully different control requirements and use cases.\n"
            "- Underestimating motor starting current (inrush current), which is often several times "
            "higher than running current and must be accounted for when sizing power supplies/"
            "protection.\n"
            "- Ignoring motor direction/polarity when a specific rotation direction matters for the "
            "application, especially with simple DC motors.\n"
            "- Not accounting for back-EMF (the motor itself generates a voltage opposing its own "
            "supply as it spins), which affects both control circuitry design and understanding motor "
            "behavior under load."
        ),
        "best_practices": (
            "- Choose motor type based on actual application needs: DC brushed for simple/cheap "
            "control, brushless DC for efficiency/longevity, stepper for precise positioning.\n"
            "- Size power supplies and protection devices for a motor's STARTING current, not just its "
            "running current.\n"
            "- Use a flyback diode when switching a DC motor with a transistor/relay to protect "
            "against voltage spikes from back-EMF when the motor turns off.\n"
            "- Consult a motor's datasheet for stall current and torque curves before designing a "
            "control circuit around it."
        ),
        "interview_questions": (
            "1. Explain the basic principle (F = BIL) behind how a DC motor produces rotational "
            "force.\n"
            "2. What is back-EMF, and why does it matter for motor control circuit design?\n"
            "3. Why is a motor's starting (inrush) current typically much higher than its running "
            "current?\n"
            "4. What's the practical difference between a brushed and brushless DC motor?\n"
            "5. Why would you use a flyback diode when switching a DC motor with a transistor?"
        ),
        "assignment": (
            "Assignment: Motor Selection Justification\n"
            "Given 3 project scenarios (a simple toy car, a 3D printer's precise axis movement, a "
            "cooling fan), select the most appropriate motor type for each and justify your choice "
            "based on cost, precision, and control complexity tradeoffs."
        ),
        "challenge": (
            "Challenge: Motor Protection Circuit Design\n"
            "Design (on paper) a transistor-switched DC motor control circuit including a "
            "current-limiting consideration and a flyback diode, explaining the purpose of each "
            "component in your design."
        ),
        "summary": (
            "Electric motors convert electrical energy into mechanical rotation using magnetic fields "
            "and current-carrying conductors (F = BIL for DC motors). Different motor types (brushed "
            "DC, brushless DC, stepper) suit different applications based on cost, control complexity, "
            "and precision needs. Starting current, back-EMF, and proper switching protection "
            "(flyback diodes) are essential practical considerations."
        ),
        "lesson_references": (
            "- All About Circuits: 'DC Motors' textbook volume\n"
            "- SparkFun: 'Motors and Selecting the Right One' tutorial\n"
            "- Digi-Key: 'Brushed vs Brushless DC Motors' article"
        ),
        "next_lesson_preview": (
            "Next up: Generators -- the reverse process of motors, converting mechanical energy back "
            "into electrical energy via electromagnetic induction."
        ),
"quiz": {
            "title": "Electric Motors Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does the commutator do in a brushed DC motor?",
                    "option_a": "Converts AC to DC",
                    "option_b": "Reverses current direction in the coil to keep it rotating",
                    "option_c": "Increases the motor's voltage rating",
                    "option_d": "Cools the motor",
                    "correct_option": "b",
                    "explanation": "The commutator switches current direction in the armature every half-turn, maintaining continuous rotation.",
                },
                {
                    "text": "What creates rotation in an AC induction motor?",
                    "option_a": "A physical crank",
                    "option_b": "A rotating magnetic field induced by the stator windings",
                    "option_c": "Direct current only",
                    "option_d": "A commutator",
                    "correct_option": "b",
                    "explanation": "AC in the stator windings produces a rotating magnetic field, which induces current in the rotor and drives rotation.",
                },
                {
                    "text": "Compared to running current, an induction motor's starting current is typically:",
                    "option_a": "Much lower",
                    "option_b": "Exactly the same",
                    "option_c": "Much higher",
                    "option_d": "Zero",
                    "correct_option": "c",
                    "explanation": "Starting current can be several times the running current, which is why motor circuits need appropriately rated protection.",
                },
            ],
        },
    },
    {
        "slug": "elec-eng-05-generators",
        "title": "5. Generators",
        "level": "intermediate",
        "explanation": (
            "Generators do the reverse of motors: they convert mechanical energy into electrical "
            "energy using electromagnetic induction (Faraday's Law) — moving a conductor through a "
            "magnetic field (or a magnetic field through a conductor) induces a voltage. AC "
            "generators (alternators) rotate a coil within a magnetic field, or a magnetic field "
            "within a fixed coil (as in most modern designs), producing sinusoidal AC output. DC "
            "generators use a commutator to convert the internally generated AC into DC output, "
            "similarly to how a DC motor's commutator works in reverse. In practice, small portable "
            "'generators' (like the petrol/diesel gensets common for backup power) are AC alternators "
            "driven by an internal combustion engine, often paired with a voltage regulator (AVR) to "
            "keep output steady as load changes."
        ),
        "examples": (
            "Faraday's Law (magnitude): induced EMF is proportional to the rate of change of magnetic "
            "flux through the coil: EMF proportional to (change in flux) / (change in time)\n\n"
            "A genset rated 5kVA at 230V can supply roughly:\n"
            "I = S / V = 5000 / 230 = ~21.7A maximum\n"
        ),
        "practice": (
            "1. Explain, in your own words, the difference between a motor and a generator in terms "
            "of energy conversion direction.\n"
            "2. A generator is rated 3.5kVA at 230V. What is its maximum rated current?\n"
            "3. Why does a generator's output voltage tend to sag under heavy load, and what "
            "component is used to counteract this?"
        ),
        "mini_project": (
            "Mini Project: Genset Sizing Worksheet\n"
            "List the appliances in a small household (fridge, TV, fans, lights, etc.) with their "
            "wattage, sum the total load with a safety margin, and determine what size (kVA) "
            "generator would be appropriate."
        ),
                "real_world_project": (
            "Real-World Project: Power Generation Method Comparison\n"
            "Research 3 real electricity generation methods (hydroelectric, wind turbine, diesel "
            "generator) and explain, for each, what provides the mechanical energy that turns the "
            "generator, connecting back to Faraday's Law of induction."
        ),
        "common_mistakes": (
            "- Confusing motors and generators as entirely different devices -- structurally they're "
            "often nearly identical, differing mainly in whether electrical or mechanical energy is "
            "the input.\n"
            "- Forgetting that generator output voltage depends on rotation speed -- an "
            "under-speed generator produces lower voltage/frequency than rated, which can damage "
            "connected equipment.\n"
            "- Not accounting for a generator's load -- an unloaded generator behaves very differently "
            "electrically (and mechanically, in terms of required driving torque) than a loaded one.\n"
            "- Assuming all generators produce clean, stable AC -- small/cheap generators can produce "
            "significant voltage fluctuation or harmonic distortion unsuitable for sensitive "
            "electronics without additional regulation."
        ),
        "best_practices": (
            "- Understand that motors and generators are two directions of the same underlying "
            "electromagnetic principle -- this connection deepens intuition for both.\n"
            "- Check a generator's rated speed (RPM) and frequency output requirements before "
            "connecting it to a specific mechanical power source.\n"
            "- For sensitive electronics, use an inverter generator (which regulates output "
            "electronically) rather than a basic generator with raw, less stable AC output.\n"
            "- Always consider generator loading -- match capacity to actual expected load, with "
            "reasonable headroom for starting currents of connected equipment (like motors)."
        ),
        "interview_questions": (
            "1. Explain the relationship between motors and generators in terms of energy conversion "
            "direction.\n"
            "2. What is Faraday's Law, and how does it explain how a generator produces voltage?\n"
            "3. Why does a generator's rotation speed affect its output voltage and frequency?\n"
            "4. Why might a basic generator be unsuitable for powering sensitive electronics compared "
            "to an inverter generator?\n"
            "5. Name a real-world power generation method and explain what supplies its mechanical "
            "energy input."
        ),
        "assignment": (
            "Assignment: Generator Sizing Estimate\n"
            "Given a list of 5 household appliances with their power ratings, calculate the total "
            "power needed and recommend a generator capacity (with reasonable headroom for starting "
            "currents), explaining your reasoning."
        ),
        "challenge": (
            "Challenge: Motor-Generator Duality Explainer\n"
            "Write a clear explanation, with a simple diagram description, of how the SAME physical "
            "device structure can function as either a motor or a generator, depending on which energy "
            "form is the input versus the output."
        ),
        "summary": (
            "Generators convert mechanical energy into electrical energy via electromagnetic induction "
            "(Faraday's Law) -- the structural reverse of a motor. Output voltage and frequency depend "
            "on rotation speed, and generator behavior differs significantly under load versus "
            "unloaded. Real-world generation methods (hydro, wind, diesel) all supply mechanical "
            "energy to spin a generator."
        ),
        "lesson_references": (
            "- All About Circuits: 'Generators' and 'Electromagnetic Induction' volumes\n"
            "- Khan Academy: 'Faraday's Law' physics lesson\n"
            "- U.S. Energy Information Administration: 'How electricity is generated' overview"
        ),
        "next_lesson_preview": (
            "Next up: Inverters. You'll learn how DC power (from batteries or solar panels) is "
            "converted into usable AC power for standard household appliances."
        ),
"quiz": {
            "title": "Generators Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Generators convert which form of energy into electrical energy?",
                    "option_a": "Chemical",
                    "option_b": "Mechanical",
                    "option_c": "Thermal only",
                    "option_d": "Nuclear",
                    "correct_option": "b",
                    "explanation": "Generators convert mechanical rotational energy into electrical energy via electromagnetic induction.",
                },
                {
                    "text": "Which law describes the induction of voltage in a generator?",
                    "option_a": "Ohm's Law",
                    "option_b": "Faraday's Law",
                    "option_c": "Newton's Third Law",
                    "option_d": "Boyle's Law",
                    "correct_option": "b",
                    "explanation": "Faraday's Law of electromagnetic induction explains how a changing magnetic field induces voltage.",
                },
                {
                    "text": "What component helps keep a generator's output voltage steady under varying load?",
                    "option_a": "A commutator only",
                    "option_b": "An automatic voltage regulator (AVR)",
                    "option_c": "A transformer only",
                    "option_d": "A capacitor bank always",
                    "correct_option": "b",
                    "explanation": "An AVR adjusts the field excitation to keep output voltage stable as load changes.",
                },
            ],
        },
    },
    {
        "slug": "elec-eng-06-inverters",
        "title": "6. Inverters",
        "level": "intermediate",
        "explanation": (
            "An inverter converts DC power (from batteries or solar panels) into AC power for "
            "running standard household appliances. It uses electronic switches (transistors/MOSFETs "
            "or IGBTs) to rapidly switch DC current on and off in a pattern that approximates a sine "
            "wave. Inverter output quality falls into tiers: square wave (cheapest, roughest, can "
            "damage sensitive electronics), modified sine wave (a stepped approximation, works for "
            "most basic loads), and pure sine wave (matches mains-quality AC, safe for all "
            "appliances including motors and sensitive electronics). Key inverter specs are continuous "
            "power rating (watts), surge/peak rating (for motor start-up spikes), and input DC voltage "
            "(commonly 12V, 24V, or 48V systems)."
        ),
        "examples": (
            "A 24V, 2000W pure sine wave inverter running a 500W load draws roughly:\n"
            "I = P / V = 500 / 24 = ~20.8A from the battery bank\n\n"
            "Surge rating matters for loads with motors (fridges, pumps) which can draw 3-6x their "
            "running wattage for a brief moment at startup.\n"
        ),
        "practice": (
            "1. Explain the difference between modified sine wave and pure sine wave inverter output.\n"
            "2. A 12V inverter is running a 240W load. What current is it drawing from the battery?\n"
            "3. Why is the surge rating of an inverter important when sizing it for a fridge or water "
            "pump?"
        ),
        "mini_project": (
            "Mini Project: Inverter Sizing Exercise\n"
            "List 5 household devices with wattage, mark which have motors (higher surge), sum "
            "continuous wattage, and pick an inverter continuous + surge rating with a reasonable "
            "safety margin."
        ),
                "real_world_project": (
            "Real-World Project: Home Backup Load Assessment\n"
            "List 5 essential appliances you'd want powered during an outage (lights, fan, router, "
            "phone charger, small fridge). Sum their wattages, add 20% headroom, and determine what "
            "inverter power rating (VA/W) would be required to run them simultaneously."
        ),
        "common_mistakes": (
            "- Sizing an inverter only for running (steady-state) load and ignoring surge/starting "
            "load -- motors (fridges, fans, pumps) can draw 2-6x their running current momentarily at "
            "startup, which can trip or damage an undersized inverter.\n"
            "- Confusing modified sine wave and pure sine wave inverter output -- some sensitive "
            "electronics (certain motors, medical equipment, audio gear) require pure sine wave and "
            "may malfunction or run hot on modified sine wave.\n"
            "- Ignoring inverter efficiency losses when sizing battery capacity -- some energy is lost "
            "as heat during DC-to-AC conversion, so battery capacity must exceed the raw load "
            "calculation.\n"
            "- Overlooking continuous vs peak power ratings on an inverter's spec sheet -- a unit's "
            "peak rating is only sustainable briefly, not for continuous heavy loads."
        ),
        "best_practices": (
            "- Always size an inverter for the SURGE load of your most demanding connected appliance, "
            "not just the sum of running wattages.\n"
            "- Choose pure sine wave inverters for sensitive electronics, even at higher cost, to avoid "
            "compatibility issues.\n"
            "- Factor inverter efficiency (typically 85-95%) into battery capacity calculations, not "
            "just raw load wattage.\n"
            "- Check both continuous and peak/surge power ratings before purchasing, matching them to "
            "your actual expected load profile."
        ),
        "interview_questions": (
            "1. What is the fundamental job of an inverter, and what components does it typically use "
            "to perform DC-to-AC conversion?\n"
            "2. Why does surge/starting load matter more than running load when sizing an inverter?\n"
            "3. What's the practical difference between modified sine wave and pure sine wave "
            "inverter output?\n"
            "4. Why does inverter efficiency matter when calculating required battery capacity?\n"
            "5. What's the difference between an inverter's continuous and peak power rating?"
        ),
        "assignment": (
            "Assignment: Inverter Sizing Calculation\n"
            "Given a list of 4 appliances with both running and starting wattage figures, calculate "
            "the minimum inverter surge rating required to start the largest one while the others are "
            "already running."
        ),
        "challenge": (
            "Challenge: Pure vs Modified Sine Wave Research\n"
            "Research and document 3 specific types of equipment that require pure sine wave power and "
            "explain, in engineering terms, why modified sine wave can cause problems for each."
        ),
        "summary": (
            "Inverters convert DC (from batteries/solar) into usable AC power using rapidly switching "
            "transistors/MOSFETs/IGBTs. Correct sizing requires accounting for surge/starting current "
            "(not just running load), inverter efficiency losses, and choosing pure sine wave output "
            "for sensitive electronics. Continuous and peak power ratings both matter when selecting a "
            "unit."
        ),
        "lesson_references": (
            "- Victron Energy: 'Inverter Sizing' technical guide\n"
            "- All About Circuits: 'Inverters' textbook volume\n"
            "- Renewable Energy World: 'Pure Sine Wave vs Modified Sine Wave' explainer"
        ),
        "next_lesson_preview": (
            "Next up: UPS Systems. You'll learn how uninterruptible power supplies provide near-instant "
            "backup power and the three main UPS architectures used in real installations."
        ),
"quiz": {
            "title": "Inverters Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does an inverter convert?",
                    "option_a": "AC to DC",
                    "option_b": "DC to AC",
                    "option_c": "AC to AC at a different frequency only",
                    "option_d": "Mechanical energy to electrical",
                    "correct_option": "b",
                    "explanation": "An inverter converts DC input (e.g. from batteries) into AC output for standard appliances.",
                },
                {
                    "text": "Which inverter output type is safest and cleanest for all appliances, including motors?",
                    "option_a": "Square wave",
                    "option_b": "Modified sine wave",
                    "option_c": "Pure sine wave",
                    "option_d": "DC output",
                    "correct_option": "c",
                    "explanation": "Pure sine wave inverters closely match mains AC quality, safe for all load types.",
                },
                {
                    "text": "Why does a fridge or pump need an inverter with a high surge rating?",
                    "option_a": "They use more power once the compressor motor is spinning steadily",
                    "option_b": "Motor-driven loads draw a brief high current spike at startup",
                    "option_c": "They require DC power directly",
                    "option_d": "Surge rating only matters for LED lighting",
                    "correct_option": "b",
                    "explanation": "Motors draw several times their running current for a moment at startup, which the inverter's surge rating must cover.",
                },
            ],
        },
    },
    {
        "slug": "elec-eng-07-ups-systems",
        "title": "7. UPS Systems",
        "level": "intermediate",
        "explanation": (
            "A UPS (Uninterruptible Power Supply) provides near-instant backup power when mains "
            "supply fails, protecting connected equipment from sudden shutdown and, in higher-end "
            "units, from voltage spikes/sags. There are three main types: Standby (Offline) UPS — "
            "switches to battery only when mains fails, with a brief switchover delay, cheapest and "
            "common for basic computer backup; Line-Interactive UPS — regulates minor voltage "
            "fluctuations without switching to battery, faster switchover, good general-purpose "
            "choice; Online (Double-Conversion) UPS — continuously converts incoming AC to DC then "
            "back to AC, so there is zero switchover time and the cleanest possible output, used for "
            "servers and critical equipment. UPS runtime depends on its battery capacity (VA/Wh) "
            "versus the connected load."
        ),
        "examples": (
            "A UPS rated 1000VA with a power factor of 0.6 supports about 600W of real load.\n"
            "Runtime estimate: Runtime (hours) roughly = Battery Wh / Load W\n"
            "  A 240Wh battery running a 60W load lasts roughly 4 hours (ignoring inverter losses).\n"
        ),
        "practice": (
            "1. Explain the key difference between a standby UPS and an online (double-conversion) "
            "UPS.\n"
            "2. A UPS is rated 1500VA at power factor 0.7. What real wattage load can it support?\n"
            "3. Why might a data center choose an online UPS over a cheaper standby UPS despite the "
            "extra cost?"
        ),
        "mini_project": (
            "Mini Project: UPS Runtime Estimator\n"
            "Given a battery capacity in Wh and a list of loads in watts, calculate estimated backup "
            "runtime, and identify at what load the UPS could only last 10 minutes."
        ),
                "real_world_project": (
            "Real-World Project: UPS Selection for a Home Office\n"
            "List the equipment in a typical home office setup (computer, monitor, router, modem). "
            "Calculate total load, research an appropriately sized UPS (VA rating) for it, and specify "
            "which UPS type (standby, line-interactive, or online) best fits based on how critical "
            "uninterrupted power is for that equipment."
        ),
        "common_mistakes": (
            "- Choosing UPS capacity based only on connected equipment's wattage without accounting "
            "for how LONG backup power is needed (runtime), which depends on battery capacity, not "
            "just VA rating.\n"
            "- Confusing VA (volt-amps) and W (watts) ratings -- due to power factor, VA rating is "
            "typically higher than the actual usable wattage, and sizing purely on VA can overestimate "
            "real capacity.\n"
            "- Using a basic standby UPS for equipment that's highly sensitive to the brief switchover "
            "delay, when a line-interactive or online UPS would provide more seamless protection.\n"
            "- Neglecting periodic battery testing/replacement -- UPS batteries degrade over years and "
            "a 'working' UPS with a dead battery provides zero actual backup protection."
        ),
        "best_practices": (
            "- Size UPS capacity based on BOTH load wattage and desired runtime, checking the "
            "manufacturer's runtime chart at your specific load level.\n"
            "- Use watts (not just VA) for accurate capacity planning, understanding the power factor "
            "relationship between them.\n"
            "- Match UPS type to criticality: standby for basic protection, line-interactive for "
            "improved voltage regulation, online (double-conversion) for zero-transfer-time critical "
            "systems.\n"
            "- Test UPS batteries periodically (many units support self-test) and replace on the "
            "manufacturer's recommended schedule, not just when they visibly fail."
        ),
        "interview_questions": (
            "1. What's the practical difference between standby, line-interactive, and online UPS "
            "architectures?\n"
            "2. Why is VA rating not the same as usable wattage, and why does that matter for sizing?\n"
            "3. Why does UPS runtime depend on more than just its power rating?\n"
            "4. Why might a data center choose an online (double-conversion) UPS despite its higher "
            "cost and lower efficiency compared to standby?\n"
            "5. Why is periodic UPS battery testing important even when the UPS 'seems fine'?"
        ),
        "assignment": (
            "Assignment: UPS Type Selection Matrix\n"
            "Given 4 scenarios (a home router, a hospital ventilator, a home computer, a server room), "
            "select the most appropriate UPS type for each and justify your choice based on how "
            "critical zero-interruption power is."
        ),
        "challenge": (
            "Challenge: Runtime vs Capacity Tradeoff\n"
            "Research how UPS runtime changes as connected load increases (using any real UPS "
            "manufacturer's runtime chart), and explain the relationship you observe between load "
            "percentage and available backup time."
        ),
        "summary": (
            "A UPS provides near-instant backup power during mains failure, in three main "
            "architectures: standby (basic, brief switchover), line-interactive (improved regulation), "
            "and online/double-conversion (zero transfer time, for critical loads). Correct sizing "
            "requires considering both wattage and desired runtime, and batteries need periodic "
            "testing since UPS reliability depends entirely on battery health."
        ),
        "lesson_references": (
            "- APC by Schneider Electric: 'UPS Types and Topologies' technical guide\n"
            "- Eaton: 'UPS Sizing Calculator' and sizing methodology guide\n"
            "- All About Circuits: 'Uninterruptible Power Supplies' overview"
        ),
        "next_lesson_preview": (
            "Next up: Solar Power Systems. You'll learn how photovoltaic panels, charge controllers, "
            "batteries, and inverters combine into a complete solar power system."
        ),
"quiz": {
            "title": "UPS Systems Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which UPS type has zero switchover time because it continuously converts AC to DC to AC?",
                    "option_a": "Standby UPS",
                    "option_b": "Line-Interactive UPS",
                    "option_c": "Online (double-conversion) UPS",
                    "option_d": "None of these",
                    "correct_option": "c",
                    "explanation": "Online UPS continuously runs power through conversion, so there's no switching delay when mains fails.",
                },
                {
                    "text": "What does VA measure on a UPS rating?",
                    "option_a": "Voltage only",
                    "option_b": "Apparent power (volts x amps)",
                    "option_c": "Battery weight",
                    "option_d": "Frequency",
                    "correct_option": "b",
                    "explanation": "VA (Volt-Amps) is apparent power; real power (watts) is VA multiplied by the power factor.",
                },
                {
                    "text": "A standby UPS's main drawback compared to an online UPS is:",
                    "option_a": "It costs more",
                    "option_b": "A brief switchover delay when mains fails",
                    "option_c": "It cannot run any equipment",
                    "option_d": "It has no battery",
                    "correct_option": "b",
                    "explanation": "Standby UPS units switch to battery only after detecting mains failure, causing a short delay.",
                },
            ],
        },
    },
    {
        "slug": "elec-eng-08-solar-systems",
        "title": "8. Solar Systems",
        "level": "intermediate",
        "explanation": (
            "A solar power system converts sunlight into usable electricity using photovoltaic (PV) "
            "panels, and typically includes: Solar Panels (rated in watts peak, Wp, under standard "
            "test conditions), a Charge Controller (regulates power from the panels into the "
            "battery, either simpler PWM or more efficient MPPT which tracks the panel's maximum "
            "power point), a Battery Bank (stores energy for use at night/low sun), and an Inverter "
            "(converts stored DC to usable AC). Systems are either off-grid (fully independent), "
            "grid-tied (feeds excess power to the utility grid, no batteries needed), or hybrid "
            "(grid-tied with battery backup). Panel output depends on irradiance, temperature, angle, "
            "and shading."
        ),
        "examples": (
            "A 300W panel receiving good sun for 5 peak-sun-hours can produce roughly:\n"
            "Energy = 300W x 5h = 1500Wh (1.5kWh) per day (real-world derates apply)\n\n"
            "MPPT controllers are typically 20-30% more efficient than PWM controllers, especially "
            "when panel voltage is much higher than battery voltage.\n"
        ),
        "practice": (
            "1. List the four main components of an off-grid solar system and what each one does.\n"
            "2. A home needs 3kWh per day and the location gets 5 peak sun hours daily. Roughly what "
            "total panel wattage is needed (ignoring losses)?\n"
            "3. Explain the difference between a PWM and an MPPT charge controller."
        ),
        "mini_project": (
            "Mini Project: Basic Solar System Sizing\n"
            "Given a daily energy requirement (kWh) and average peak sun hours for a location, "
            "calculate the required panel wattage, then size a battery bank to cover 1 day of "
            "autonomy at a chosen system voltage (12V/24V/48V)."
        ),
                "real_world_project": (
            "Real-World Project: Basic Solar System Sizing\n"
            "For a small household load (e.g. lights, fan, phone charging -- estimate total daily "
            "watt-hours), size a basic off-grid solar system: panel wattage needed (accounting for "
            "average sun hours in your region), battery capacity for one day of autonomy, and an "
            "appropriately rated charge controller."
        ),
        "common_mistakes": (
            "- Sizing solar panels based on their rated wattage without accounting for real-world "
            "derating factors (temperature, dust, angle, inverter/charge controller efficiency) -- "
            "actual output is typically 70-80% of the panel's rated peak wattage in practice.\n"
            "- Undersizing battery capacity for the desired days of autonomy (backup during cloudy "
            "days), leading to a system that works great on sunny days but fails during a cloudy "
            "stretch.\n"
            "- Using a PWM charge controller with a panel voltage significantly higher than the "
            "battery voltage, wasting the available power that an MPPT controller could have "
            "captured.\n"
            "- Ignoring local average 'sun hours' (not daylight hours) when sizing panels -- this "
            "region-specific figure is essential for accurate energy production estimates."
        ),
        "best_practices": (
            "- Apply a realistic derating factor (commonly ~75-80%) to a solar panel's rated wattage "
            "when estimating actual daily energy production.\n"
            "- Size battery capacity for at least 1-2 days of autonomy (more for critical loads) to "
            "handle cloudy weather without excessive load shedding.\n"
            "- Use an MPPT charge controller rather than PWM when panel voltage significantly exceeds "
            "battery voltage, to capture more available power.\n"
            "- Use your specific region's average daily 'sun hours' (a standardized solar resource "
            "figure, not raw daylight hours) for accurate sizing calculations."
        ),
        "interview_questions": (
            "1. Why is a solar panel's actual real-world output typically lower than its rated peak "
            "wattage?\n"
            "2. What is the difference between a PWM and an MPPT charge controller, and when does the "
            "difference matter most?\n"
            "3. What does 'sun hours' mean in solar system sizing, and why isn't it the same as "
            "daylight hours?\n"
            "4. Why does a solar system need battery storage rather than only powering loads directly "
            "during daylight?\n"
            "5. What factors would you consider when deciding how many days of battery autonomy a "
            "solar system needs?"
        ),
        "assignment": (
            "Assignment: Panel Wattage Estimation\n"
            "Given a daily energy requirement (in watt-hours) and an average of 5 sun hours per day for "
            "a given location, calculate the minimum panel wattage needed, applying a reasonable "
            "derating factor to your calculation."
        ),
        "challenge": (
            "Challenge: MPPT vs PWM Efficiency Comparison\n"
            "Research and document a specific numeric example (with real or realistic panel/battery "
            "voltages) showing how much more usable power an MPPT controller could capture compared to "
            "a PWM controller in that scenario."
        ),
        "summary": (
            "A solar power system combines PV panels (rated in Wp), a charge controller (PWM or the "
            "more efficient MPPT) regulating power to batteries, batteries for storage, and an "
            "inverter for AC output. Correct sizing accounts for real-world panel derating, "
            "region-specific sun hours, and sufficient battery autonomy for cloudy-day reliability."
        ),
        "lesson_references": (
            "- Victron Energy: 'Solar System Design' technical guides\n"
            "- NREL (National Renewable Energy Laboratory): solar resource data and sizing tools\n"
            "- SparkFun: 'Solar Power for Beginners' tutorial"
        ),
        "next_lesson_preview": (
            "Next up: Battery Management. You'll go deeper into capacity, state of charge, charge/"
            "discharge rates, and how to safely manage the batteries that store solar and backup "
            "power."
        ),
"quiz": {
            "title": "Solar Systems Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does an MPPT charge controller do?",
                    "option_a": "Converts AC to DC only",
                    "option_b": "Tracks the panel's maximum power point for more efficient charging",
                    "option_c": "Stores energy directly without a battery",
                    "option_d": "Measures sunlight hours",
                    "correct_option": "b",
                    "explanation": "MPPT (Maximum Power Point Tracking) continuously adjusts to extract the most power available from the panel.",
                },
                {
                    "text": "In a grid-tied solar system without batteries, what happens to excess power?",
                    "option_a": "It is wasted with no destination",
                    "option_b": "It is fed back into the utility grid",
                    "option_c": "It automatically shuts the panels off",
                    "option_d": "It charges a non-existent battery",
                    "correct_option": "b",
                    "explanation": "Grid-tied systems (without batteries) export surplus power to the grid, often for credit depending on local policy.",
                },
                {
                    "text": "Panel output in watts-peak (Wp) is measured under:",
                    "option_a": "Any random conditions",
                    "option_b": "Standard Test Conditions (specific irradiance and temperature)",
                    "option_c": "Nighttime conditions",
                    "option_d": "Only cloudy conditions",
                    "correct_option": "b",
                    "explanation": "Wp ratings are measured under Standard Test Conditions (STC), so real-world output varies with actual sun and temperature.",
                },
            ],
        },
    },
    {
        "slug": "elec-eng-09-battery-management",
        "title": "9. Battery Management",
        "level": "intermediate",
        "explanation": (
            "Battery management covers safely charging, discharging, and monitoring batteries to "
            "maximize life and prevent damage or hazards. Key concepts: Capacity (Ah — amp-hours; a "
            "100Ah battery can theoretically supply 100A for 1 hour, or 5A for 20 hours), State of "
            "Charge (SoC — percentage of capacity remaining), Depth of Discharge (DoD — how much has "
            "been used; deeper discharge cycles shorten most battery lifespans), and C-rate "
            "(charge/discharge rate relative to capacity — a 1C rate on a 100Ah battery is 100A). "
            "Common chemistries: Lead-acid (cheap, heavy, shorter cycle life, ~50% usable DoD), "
            "Lithium-ion/LiFePO4 (lighter, longer cycle life, higher usable DoD ~80-100%, needs a "
            "Battery Management System (BMS) to prevent over-charge/over-discharge and balance "
            "individual cells)."
        ),
        "examples": (
            "A 100Ah, 12V lead-acid battery at 50% usable DoD gives ~50Ah usable = 600Wh usable energy.\n"
            "A 100Ah, 12V LiFePO4 battery at 90% usable DoD gives ~90Ah usable = 1080Wh usable energy.\n\n"
            "Charging current example: charging a 100Ah battery at 0.2C = 20A charge current.\n"
        ),
        "practice": (
            "1. Define Ah (amp-hours) and explain what a 200Ah battery theoretically means for current "
            "over time.\n"
            "2. Why does a lithium battery typically deliver more usable energy than a lead-acid "
            "battery of the same rated Ah?\n"
            "3. What is the role of a BMS on a lithium battery pack?"
        ),
        "mini_project": (
            "Mini Project: Battery Bank Comparison\n"
            "For a 2kWh backup requirement, calculate the required battery bank size in Ah at 24V for "
            "both lead-acid (50% DoD) and LiFePO4 (90% DoD), and compare the total usable capacity "
            "each would need to be rated at."
        ),
                "real_world_project": (
            "Real-World Project: Battery Bank Runtime Calculator\n"
            "For a battery bank of a given capacity (Ah) and voltage, and a specified load (watts), "
            "calculate the theoretical runtime, then apply a realistic depth-of-discharge limit "
            "(e.g. 50% for lead-acid, 80-90% for lithium) to determine the SAFE usable runtime."
        ),
        "common_mistakes": (
            "- Fully discharging lead-acid batteries regularly -- this dramatically shortens their "
            "lifespan; lead-acid batteries should typically not be discharged below 50% depth of "
            "discharge for reasonable longevity.\n"
            "- Treating all battery chemistries (lead-acid, lithium-ion, LiFePO4) as interchangeable "
            "in terms of safe discharge depth, charging voltage, and charging behavior -- each has "
            "distinctly different characteristics.\n"
            "- Mixing old and new batteries, or different capacity batteries, in the same bank -- this "
            "causes uneven charging/discharging that stresses and shortens the life of the weaker "
            "units.\n"
            "- Ignoring temperature effects on battery capacity and charging -- both very hot and very "
            "cold conditions significantly affect real usable capacity and safe charge rates."
        ),
        "best_practices": (
            "- Respect chemistry-specific depth-of-discharge limits: roughly 50% for lead-acid, "
            "80-90%+ for quality lithium/LiFePO4 batteries, to maximize battery lifespan.\n"
            "- Never mix batteries of different age, capacity, or chemistry within the same bank.\n"
            "- Use a charge controller/BMS (Battery Management System) appropriate for your specific "
            "battery chemistry, since charging profiles differ significantly.\n"
            "- Monitor battery temperature in extreme climates and adjust charging behavior "
            "accordingly, following the manufacturer's temperature compensation guidance."
        ),
        "interview_questions": (
            "1. What does Ah (amp-hour) capacity mean, and how do you calculate theoretical runtime "
            "from it?\n"
            "2. Why does depth of discharge matter for battery lifespan, and how does the safe limit "
            "differ between lead-acid and lithium batteries?\n"
            "3. Why shouldn't you mix old and new batteries, or different capacities, in the same "
            "bank?\n"
            "4. What is a BMS (Battery Management System), and why is it especially important for "
            "lithium battery banks?\n"
            "5. How does temperature affect battery capacity and charging safety?"
        ),
        "assignment": (
            "Assignment: Chemistry Comparison Table\n"
            "Build a comparison table for lead-acid, lithium-ion, and LiFePO4 batteries covering: "
            "typical safe depth of discharge, approximate cycle life, and one key safety consideration "
            "for each chemistry."
        ),
        "challenge": (
            "Challenge: Battery Bank Design\n"
            "Design a battery bank (chemistry, total Ah capacity, voltage configuration) to reliably "
            "power a 200W continuous load for 8 hours, respecting your chosen chemistry's safe depth "
            "of discharge limit in your capacity calculation."
        ),
        "summary": (
            "Battery capacity (Ah) determines theoretical runtime at a given load, but SAFE usable "
            "capacity is limited by chemistry-specific depth-of-discharge guidelines (lead-acid ~50%, "
            "lithium 80-90%+). Proper battery management includes avoiding mixed battery banks, using "
            "chemistry-appropriate charging (often via a BMS for lithium), and accounting for "
            "temperature effects."
        ),
        "lesson_references": (
            "- Battery University (batteryuniversity.com): comprehensive battery chemistry guides\n"
            "- Victron Energy: 'Battery Types and Depth of Discharge' technical guide\n"
            "- NREL: battery storage technical reports"
        ),
        "next_lesson_preview": (
            "Next up: Power Distribution & Protection Systems -- the final lesson of this course. "
            "You'll learn how electricity is safely distributed within a building and protected "
            "against electrical faults."
        ),
"quiz": {
            "title": "Battery Management Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does Ah (amp-hours) measure?",
                    "option_a": "Voltage rating",
                    "option_b": "A battery's charge capacity over time",
                    "option_c": "Power in watts",
                    "option_d": "Battery weight",
                    "correct_option": "b",
                    "explanation": "Amp-hours describe how much current a battery can theoretically supply over one hour (or equivalent).",
                },
                {
                    "text": "What is the main role of a Battery Management System (BMS) on a lithium pack?",
                    "option_a": "Increase the battery's physical size",
                    "option_b": "Prevent over-charge/over-discharge and balance individual cells",
                    "option_c": "Convert DC to AC",
                    "option_d": "Generate solar power",
                    "correct_option": "b",
                    "explanation": "A BMS protects lithium cells from unsafe conditions and keeps cells balanced for longer pack life.",
                },
                {
                    "text": "Compared to lead-acid, lithium (LiFePO4) batteries typically allow:",
                    "option_a": "Lower usable depth of discharge",
                    "option_b": "Higher usable depth of discharge and longer cycle life",
                    "option_c": "No charging at all",
                    "option_d": "Only AC charging",
                    "correct_option": "b",
                    "explanation": "LiFePO4 batteries typically tolerate deeper discharge and more charge cycles than lead-acid.",
                },
            ],
        },
    },
    {
        "slug": "elec-eng-10-power-distribution-protection",
        "title": "10. Power Distribution & Protection Systems",
        "level": "advanced",
        "explanation": (
            "Power distribution moves electricity from source to load safely and efficiently, while "
            "protection systems prevent damage from faults. A distribution board (consumer unit) "
            "splits incoming supply into circuits, each protected by a breaker sized for that "
            "circuit's wiring and load. Key protection devices: Fuses (a wire that melts to break the "
            "circuit on overcurrent, one-time use), Circuit Breakers (MCBs — mechanically trip on "
            "overcurrent and can be reset), Earth Leakage / Residual Current Devices (RCCB/ELCB/GFCI "
            "— trip on current imbalance indicating a leak to earth, protecting against electric "
            "shock), and Surge Protection Devices (SPDs — protect against voltage spikes from "
            "lightning or switching events). Proper earthing (grounding) gives fault current a safe "
            "path back to source, allowing protection devices to trip quickly and safely."
        ),
        "examples": (
            "A circuit wired with 2.5mm^2 cable is typically protected with a 20A breaker; wiring "
            "gauge and breaker rating must be matched so the breaker trips before the wire overheats.\n\n"
            "An RCCB rated 30mA is a common sensitivity used for shock protection on socket circuits.\n"
        ),
        "practice": (
            "1. Explain the difference between a fuse and a circuit breaker.\n"
            "2. What does an RCCB/ELCB protect against that a standard MCB does not?\n"
            "3. Why must a breaker's current rating be matched to the wire gauge it protects, rather "
            "than sized as large as possible?"
        ),
        "mini_project": (
            "Mini Project: Home Distribution Board Plan\n"
            "Sketch a simple distribution board layout for a small home with lighting circuits, socket "
            "circuits, and a kitchen/high-load circuit, choosing appropriate breaker ratings for each "
            "and noting where RCCB protection should be applied."
        ),
                "real_world_project": (
            "Real-World Project: Home Circuit Breaker Audit\n"
            "If safely possible, examine (without touching internals) a real household distribution "
            "board. Document how many circuits it has, and for 3 circuits, note their labeled breaker "
            "rating and identify what that circuit likely powers based on the rating (e.g. a "
            "high-rated breaker likely serves a kitchen/high-power circuit)."
        ),
        "common_mistakes": (
            "- Using a breaker rated too high for the wire gauge it protects -- the breaker must "
            "protect the WIRE from overheating, so an oversized breaker on thin wiring defeats its "
            "safety purpose.\n"
            "- Confusing overcurrent protection (breakers/fuses, which protect against overload/short "
            "circuit) with ground fault protection (GFCI/RCD, which protects against electric shock "
            "from current leaking to ground) -- they serve different safety purposes and neither "
            "substitutes for the other.\n"
            "- Treating all electrical protection work as a DIY task -- distribution board and mains "
            "wiring work carries serious electrocution and fire risk and, in most jurisdictions, "
            "legally requires a licensed electrician.\n"
            "- Overloading a single circuit with too many high-draw devices, causing nuisance tripping "
            "or, in poorly protected systems, overheating."
        ),
        "best_practices": (
            "- Always match breaker rating to the wire gauge it protects, following relevant wiring "
            "regulations/standards for your region.\n"
            "- Use GFCI/RCD protection on circuits near water (kitchens, bathrooms, outdoor outlets) "
            "specifically for shock protection, in addition to standard overcurrent breakers.\n"
            "- Treat any actual mains wiring or distribution board work as licensed-electrician "
            "territory -- understanding the theory is valuable, but hands-on live work requires proper "
            "training and certification.\n"
            "- Distribute high-power appliances across multiple circuits rather than overloading a "
            "single one, following the practical rule of not regularly running a circuit near its "
            "rated maximum."
        ),
        "interview_questions": (
            "1. What is the fundamental job of a circuit breaker, and what does it protect against?\n"
            "2. What's the difference between overcurrent protection (breakers) and ground fault "
            "protection (GFCI/RCD)?\n"
            "3. Why must a breaker's rating be matched to the wire gauge it protects, rather than just "
            "chosen for convenience?\n"
            "4. Why is a GFCI/RCD specifically important in kitchens and bathrooms?\n"
            "5. Why should mains-level electrical work generally be left to a licensed electrician "
            "even by someone who understands the underlying theory?"
        ),
        "assignment": (
            "Assignment: Protection Device Selection\n"
            "Given 4 scenarios (a bathroom outlet, a kitchen high-power circuit, a bedroom lighting "
            "circuit, an outdoor garden outlet), identify what protection device(s) -- breaker rating "
            "considerations plus GFCI/RCD where relevant -- each would need and why."
        ),
        "challenge": (
            "Challenge: Distribution Board Documentation\n"
            "Create a labeled diagram (described in text if you can't draw one) of a hypothetical "
            "household distribution board with 8 circuits, assigning a sensible breaker rating to "
            "each based on what it powers, and noting which circuits need GFCI/RCD protection."
        ),
        "summary": (
            "Power distribution safely routes electricity from source to load via a distribution "
            "board splitting supply into individually protected circuits. Circuit breakers protect "
            "wiring from overcurrent/short circuits, while GFCI/RCD devices protect people from shock "
            "via ground faults -- these are complementary, not interchangeable, protections. Breaker "
            "ratings must match wire gauge, and actual mains wiring work requires licensed "
            "professionals. This completes the Electrical Engineering course."
        ),
        "lesson_references": (
            "- National Electrical Code (NEC) or your region's equivalent wiring standard "
            "(overview/summary resources)\n"
            "- All About Circuits: 'Circuit Protection' textbook volume\n"
            "- Electrical Safety Foundation International: GFCI/RCD safety guides"
        ),
        "next_lesson_preview": (
            "You've completed the Electrical Engineering course! This, combined with the Electronics "
            "& Arduino/ESP32 course, gives you a solid foundation across both the software and "
            "hardware sides of engineering covered by Kabiru AI Tutor."
        ),
"quiz": {
            "title": "Power Distribution & Protection Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does an RCCB (or ELCB/GFCI) primarily protect against?",
                    "option_a": "Overheating of the main transformer",
                    "option_b": "Electric shock from current leaking to earth",
                    "option_c": "Low voltage only",
                    "option_d": "Excess water in a device",
                    "correct_option": "b",
                    "explanation": "RCCBs detect current imbalance (a sign of leakage to earth, e.g. through a person) and trip to prevent shock.",
                },
                {
                    "text": "Unlike a fuse, a circuit breaker can:",
                    "option_a": "Only be used once and then discarded",
                    "option_b": "Be reset and reused after tripping",
                    "option_c": "Never trip on overcurrent",
                    "option_d": "Only work on DC circuits",
                    "correct_option": "b",
                    "explanation": "Circuit breakers mechanically trip and can be manually reset, unlike a fuse which must be replaced.",
                },
                {
                    "text": "Why must breaker rating match the wire gauge it protects?",
                    "option_a": "So the wire overheats before the breaker trips",
                    "option_b": "So the breaker trips before the wire is overloaded and overheats",
                    "option_c": "It doesn't matter as long as the breaker is large",
                    "option_d": "To reduce the cost of the wire only",
                    "correct_option": "b",
                    "explanation": "The breaker must trip at a current the wire can safely handle, or the wire could overheat before protection activates.",
                },
            ],
        },
    },
]
