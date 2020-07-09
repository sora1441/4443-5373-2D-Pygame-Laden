# Import needed files
import tkinter as tk
import json

# Read in player-info json file into a python dictionary
with open("player-info.json") as player_info:
    data_dict = json.load(player_info)

# List Player Attributes
player_attributes = ["First","Last","Rank","Email","Power-boost","Available-boosts"]

# Create window and pass in title
window = tk.Tk()
window.title("Player: "+ data_dict["screen_name"])

# Loop through new dictionary and format player info
index = 0
for key,value in data_dict.items():
    if(key != "screen_name" and key != "available-boosts"):
        label = tk.Label(text = player_attributes[index] + "\t" + ":  " + str(data_dict[key]))
        label.pack(anchor = "nw")
        index = index + 1
    if(key == "available-boosts"):
        value = ",  ".join(value)
        label = tk.Label(text = player_attributes[5] + "\t" + ":  " + str(value))
        label.pack(anchor = "nw")

window.mainloop()