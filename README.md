# Dead-by-Daylight-Stats-Tracker-CLI
### Introduction

The DBD Stats Tracker CLI is a small project that enables users to keep track of what killers and survivors they have faced in a simple and convenient manner. This is useful and simple to quickly add how many Trapper's you've faced against, for example. The CLI is updated to Dead by Daylight version 5.1.1. ****Features include:

- A simple and intuitive CLI interface that keeps track of what killers and survivors you have faced
- Light on system resources, so you can keep on running this in any terminal while waiting for a lobby!
- Simple commands that are easy to memorize
- All data is stored into a neat JSON file named "characters.json" if you prefer to manually update it

---

### How to Use Dead by Daylight Stats Tracker CLI

Using this CLI is super simple:

First, you need to change the directory of your powershell (or any other terminal) to where the python file "dbd_stats.py" is located. (Note that the Python and JSON file MUST be in the same working directory, preferably in a folder with nothing else in it)

- To see how many times you've killed a survivor:

    `python3 stats.py show killer Nea`

- To see how many times you've faced a killer:

    `python3 stats.py show survivor Wraith`

- To see all killer stats:

    `python3 stats.py show killer all`

- To see all survivor stats:

    `python3 stats.py show survivor all`

- To add a value to how many times you've faced a killer:

    `python3 stats.py edit survivor Wraith --val +1`

- To add a value to how many times you've hunted a survivor:

    `python3 stats.py edit killer Nea --val +1`

- To add a killer match to make data accurate:

    `python3 stats.py edit killer Nea --val +1 --match_number +1`

### Example addition to database:

Say you faced a Wraith in a game. This is how you would make an addition to the database:

1. First, you would `cd` into the directory where the python file is located
2. in the terminal, you would write the following statements and hit enter:
    1. `python3 stats.py edit survivor Wraith --val +1 --match_number +1`
3. To confirm the changes have taken place, you would write `python3 dbd_stats.py survivor show all`

### Example addition to database (pt. 2):

Say you hunted a Nancy, Kate, and Nea in a game. This is how you would make an addition to the database:

1. First, you would `cd` into the directory where the python file is located
2. In the terminal, you would write the following statements and hit enter:
    1. `python3 stats.py edit killer Nancy --val +1`
    2. `python3 stats.py edit killer Kate --val +1`
    3. `python3 stats.py edit killer Nea --val +1 --match_number +1`
3. To confirm the changes have taken place, you would write `python3 stats.py show killer all`

---

### Dependencies

This project has no dependencies; all libraries are native to python!

---

### Future Updates

At this moment no future updates are being considered.

---
**[Notion](https://knowing-letter-85f.notion.site/Dead-by-Daylight-Stats-Tracker-CLI-6d4a38bb2825466397b8cfdac06b0ad0) | [Website](https://ali-ehtesham.carrd.co/)**
