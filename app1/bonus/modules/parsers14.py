def parse(feet_inches):
    feet_inches = feet_inches.split()
    feet = float(feet_inches[0])
    inches = float(feet_inches[1])
    return {"feet": feet, "inches": inches}
