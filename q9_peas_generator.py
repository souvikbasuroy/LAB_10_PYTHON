# Q9: PEAS description generator

PEAS_DB = {
    "vacuum cleaner agent": {
        "Performance Measure": ["Cleanliness of floor", "Time taken", "Energy/battery used", "Noise produced"],
        "Environment": ["Rooms", "Floor (carpet/tiles)", "Dirt", "Furniture & obstacles"],
        "Actuators": ["Wheels", "Brushes", "Suction motor", "Dust bin"],
        "Sensors": ["Dirt sensor", "Bump sensor", "Cliff sensor", "Wheel encoder", "Battery sensor"],
    },
    "self-driving car": {
        "Performance Measure": ["Safety", "Travel time", "Legal compliance", "Passenger comfort", "Fuel efficiency"],
        "Environment": ["Roads", "Traffic", "Pedestrians", "Weather", "Traffic signals"],
        "Actuators": ["Steering", "Accelerator", "Brake", "Indicators", "Horn"],
        "Sensors": ["Cameras", "LIDAR", "Radar", "GPS", "Speedometer", "Odometer"],
    },
    "medical diagnosis system": {
        "Performance Measure": ["Correct diagnosis", "Patient health", "Treatment cost"],
        "Environment": ["Patient", "Hospital", "Medical staff"],
        "Actuators": ["Display of questions/tests", "Diagnosis & treatment report"],
        "Sensors": ["Keyboard entry of symptoms", "Lab test results", "Patient answers"],
    },
    "chess player": {
        "Performance Measure": ["Win/loss/draw", "Moves/time used"],
        "Environment": ["Chess board", "Opponent"],
        "Actuators": ["Move piece (output of move)"],
        "Sensors": ["Board state", "Opponent's move"],
    },
    "navigation agent": {
        "Performance Measure": ["Path cost", "Nodes explored", "Execution time", "Reaching goal"],
        "Environment": ["Grid map", "Walls/obstacles", "Start & goal cells"],
        "Actuators": ["Move up/down/left/right"],
        "Sensors": ["Current position", "Obstacle detection", "Goal location"],
    },
}

def print_peas(task):
    key = task.strip().lower()
    if key not in PEAS_DB:
        print(f"'{task}' not in database.")
        print("Let's create it:")
        PEAS_DB[key] = {}
        for comp in ["Performance Measure", "Environment", "Actuators", "Sensors"]:
            PEAS_DB[key][comp] = [x.strip() for x in input(f"  {comp} (comma separated): ").split(",") if x.strip()]
    peas = PEAS_DB[key]
    print("\n" + "=" * 50)
    print(f"PEAS DESCRIPTION : {key.title()}")
    print("=" * 50)
    for comp, items in peas.items():
        print(f"\n{comp}:")
        for it in items:
            print("   -", it)
    print("=" * 50)

if __name__ == "__main__":
    print("available tasks:", ", ".join(PEAS_DB))
    while True:
        t = input("\nenter AI application (or 'quit'): ")
        if t.lower() in ("quit", "q", ""): break
        print_peas(t)
