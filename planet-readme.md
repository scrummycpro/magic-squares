# Planetary Hours and Astronomical Data Script

## Overview
This Python script calculates and displays **planetary hours**, **moon phase and visibility**, **Orion visibility**, and **visible planets** for a given location. The script is flexible and provides detailed outputs based on user-specified command-line arguments.

### Features
1. **Planetary Hours**:
   - Displays the current planetary hour and the next three.
   - Provides a detailed list of all 24 planetary hours for the day.
2. **Moon Information**:
   - Displays the moon phase and percentage illumination.
   - Shows the moon’s altitude, azimuth, and zodiac sign.
   - Provides moonrise, transit, and moonset times.
3. **Orion Visibility**:
   - Displays rise, transit, and set times for the constellation Orion.
4. **Visible Planets**:
   - Lists visible planets along with their altitude, azimuth, zodiac sign, and rise, transit, and set times.
5. **Comprehensive Output**:
   - The `--all` flag combines all the above information into one detailed output.

---

## Requirements

### Python Libraries
Ensure the following libraries are installed:
- `ephem`
- `astral`
- `pytz`

Install them using pip:
```bash
pip install ephem astral pytz
```

---

## Usage

### Running the Script
Execute the script using Python and specify the desired flags for the output.

#### Basic Command:
```bash
python script.py [flags]
```

### Flags
1. `--planetary_hours`:
   - Displays the current planetary hour, the next three hours, and a detailed list of all 24 planetary hours for the day.

   Example:
   ```bash
   python script.py --planetary_hours
   ```

2. `--moon`:
   - Displays detailed moon information including phase, illumination, position, zodiac sign, and visibility times.

   Example:
   ```bash
   python script.py --moon
   ```

3. `--orion`:
   - Displays Orion’s rise, transit, and set times.

   Example:
   ```bash
   python script.py --orion
   ```

4. `--planets`:
   - Lists all visible planets along with their position, zodiac sign, and visibility times.

   Example:
   ```bash
   python script.py --planets
   ```

5. `--all`:
   - Combines all outputs into one detailed report, including planetary hours, moon information, Orion visibility, and visible planets.

   Example:
   ```bash
   python script.py --all
   ```

---

## Outputs

### Example Output for `--all`
```plaintext
Current Time: 07:20 PM
Planetary Day: Saturn
Planetary Hour: Saturn
Next Three Hours: Jupiter, Mars, Sun

Planetary hours for Atlanta, USA on 2023-12-07:
17:30 - Saturn
18:25 - Jupiter
19:20 - Mars
20:15 - Sun
21:10 - Venus
22:05 - Mercury
23:00 - Moon
23:55 - Saturn
00:50 - Jupiter
01:45 - Mars
02:40 - Sun
03:35 - Venus
07:00 - Mercury
08:00 - Moon
09:00 - Saturn
10:00 - Jupiter
11:00 - Mars
12:00 - Sun
13:00 - Venus
14:00 - Mercury
15:00 - Moon
16:00 - Saturn
17:00 - Jupiter

Moon Phase: 85.45%
Moon Illumination: 85.45%
Moon Position: Altitude = 12.34°, Azimuth = 180.56°
Moon Rise: 05:10 PM | Transit: 11:35 PM | Set: 06:15 AM
Moon is in the zodiac sign of Aquarius

Orion Rise: 07:10 PM | Transit: 12:45 AM | Set: 05:30 AM

Visible Planets:
Mars - Altitude: 35.23°, Azimuth: 160.45°, Zodiac: Scorpio | Rise: 06:45 PM | Transit: 10:30 PM | Set: 02:15 AM
Jupiter - Altitude: 25.45°, Azimuth: 210.33°, Zodiac: Pisces | Rise: 05:30 PM | Transit: 09:15 PM | Set: 01:00 AM
```

---

## How It Works

### Planetary Hours
- The script calculates planetary hours based on the Chaldean Order and the time of sunrise and sunset.
- Each planetary day starts with the planet ruling that day and continues in a fixed sequence.

### Moon Information
- Uses the `ephem` library to calculate the moon’s phase, illumination, and position.
- Determines zodiac sign based on the moon’s current location in the sky.

### Orion Visibility
- Uses fixed RA/Dec coordinates to track Orion’s rise, transit, and set times.

### Visible Planets
- Checks if a planet is above the horizon and calculates its visibility times and zodiac sign.

---

## Customization

### Changing Location
Update the `LocationInfo` object with your desired location:
```python
location = LocationInfo("Your City", "Your Country", "Your Timezone", latitude, longitude)
```

### Timezone Adjustments
Ensure the correct timezone is set by updating:
```python
tz = pytz.timezone("Your Timezone")
```

---

## Troubleshooting

### Common Issues
1. **Naive vs. Aware Datetimes**:
   - Ensure `current_time`, `sunrise`, and `sunset` are all timezone-aware.

2. **Library Not Installed**:
   - Install missing libraries using pip:
     ```bash
     pip install ephem astral pytz
     ```

### Debugging
Use print statements to check intermediate values, such as planetary hours or object positions, if results seem incorrect.

---

## Future Enhancements
- Add visualization of planetary positions using libraries like `matplotlib`.
- Support for additional celestial objects.
- Option to export results to a file (e.g., JSON or CSV).

---

## License
This script is open-source and free to use under the MIT License.

---

## Author


