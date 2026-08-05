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
