import json
import os
# Set main directory
maindir = os.path.dirname(os.path.abspath(__file__))
os.chdir(maindir)


def parse_and_save_files():
    for filename in os.listdir(maindir + "/stats"):
        # open in readonly mode
        with open(maindir + "/stats/" + filename, 'r') as f:
            data = json.load(f)

        # Make directory for sorted player data
        playerPath = maindir + "/Players/" + filename.replace(".json", "")
        try:
            os.mkdir(playerPath)
        except OSError:
            pass

        # Create a file for each statistic category (i.e. blocks mined, crafted..)
        for stat_category in data['stats']:
            statArray = []
            # Add each entry to 2D statArray
            for stat in data['stats'][stat_category]:
                statArray.append([stat.replace("minecraft:", ""), int(
                    data['stats'][stat_category][stat])])

            # Sort statistics from highest value to lowest
            try:
                statArray = sorted(statArray, key=lambda l: l[1], reverse=True)
            except IndexError:
                pass

            # Save statistic category to file
            with open(playerPath + "/" + stat_category.replace("minecraft:", "") + ".csv", "a") as f:
                for i in range(len(statArray)):
                    f.write(str(statArray[i][0]))
                    f.write(",")
                    f.write(str(statArray[i][1]))
                    f.write("\n")

# Start program
print("Starting..")
parse_and_save_files()
print("Saved statistics in the 'Players' folder")
