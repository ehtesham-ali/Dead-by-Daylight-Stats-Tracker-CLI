# Dead-by-Daylight-Stats-Tracker-CLI
### Introduction

The DBD Stats Tracker CLI is a small project that enables users to keep track of what killers and survivors they have faced in a simple and convenient manner. This is useful and simple to quickly add how many Trapper's you've faced against, for example. **The CLI is updated to Dead by Daylight version 5.1.1.** Features include:

- A simple and intuitive CLI interface that keeps track of what killers and survivors you have faced
- Light on system resources, so you can keep on running this in any terminal while waiting for a lobby!
- Simple commands that are easy to memorize
- All data is stored into a neat JSON file named "characters.json" if you prefer to manually update it

---

### How to Use Dead by Daylight Stats Tracker CLI

Using this CLI is super simple:

First, you need to change the directory of your powershell (or any other terminal) to where the python file "dbd_stats.py" is located.

- To see stats of a killer/survivor:

    `dbd_stats.py show *name of killer/survivor*`

- To see ALL stats:

    `dbd_stats.py show all`

- To change value of a killer/survivor:

    `dbd_stats.py edit *name of killer/survivor* --val *integer*`

    The integer can be a negative number if you made an error (-1 to remove 1, +1 to add 1)

- To change how many rounds this data is accurate to:

    `dbd_stats.py edit *name of killer/survivor* --val *integer* --match_number *integer*`

    The integer can be a negative number if you made an error (-1 to remove 1, +1 to add 1)

Example addition to database:

Say you faced a Wraith alongside a Nancy, Kate, and Nea in 1 game. This is how you would make an addition to the database:

1. First, you would `cd` into the directory where the python file is located
2. in the terminal, you would write the following statements and hit enter:
    1. `dbd_stats.py edit Wraith --val +1`
    2. `dbd_stats.py edit Nancy --val +1`
    3. `dbd_stats.py edit Kate --val +1`
    4. `dbd_stats.py edit Nea --val +1 --match_number +1`
3. To see if the changes have taken place, you would write `dbd_stats.py show all`

---

### Dependencies

This project has no dependencies; all libraries are native to python!

---

### Future Updates

At this moment no future updates are being considered.

---

**[Notion](https://knowing-letter-85f.notion.site/Dead-by-Daylight-Stats-Tracker-CLI-6d4a38bb2825466397b8cfdac06b0ad0) | [Website](https://ali-ehtesham.carrd.co/)**
