import ephem
from astral import LocationInfo
from astral.sun import sun
from datetime import datetime, timedelta
import pytz
import argparse

# Setup observer location
location = LocationInfo("Atlanta", "USA", "US/Eastern", 33.84, -84.38)
observer = ephem.Observer()
observer.lat, observer.lon = str(location.latitude), str(location.longitude)
observer.elevation = 320
observer.date = datetime.utcnow()

# Chaldean planetary order and day rulers
chaldean_order = ["Saturn", "Jupiter", "Mars", "Sun", "Venus", "Mercury", "Moon"]
planetary_days = {0: "Sun", 1: "Moon", 2: "Mars", 3: "Mercury", 4: "Jupiter", 5: "Venus", 6: "Saturn"}

# Get sunrise and sunset times
s = sun(location.observer, date=datetime.now())
sunrise = s["sunrise"]
sunset = s["sunset"]
day_duration = (sunset - sunrise) / 12
night_duration = ((sunrise + timedelta(days=1)) - sunset) / 12

# Ensure sunrise, sunset, and current time are timezone-aware
tz = pytz.timezone(location.timezone)
current_time = datetime.now(tz)
sunrise = sunrise.astimezone(tz)
sunset = sunset.astimezone(tz)

# Function to calculate planetary hours for the day
def calculate_planetary_hours():
    planetary_hours = []
    current_ruler_index = chaldean_order.index(planetary_days[datetime.now().weekday()])
    
    # Night hours (start at sunset)
    current = sunset
    for _ in range(12):
        planetary_hours.append((current, chaldean_order[current_ruler_index]))
        current += night_duration
        current_ruler_index = (current_ruler_index + 1) % 7

    # Day hours (start at sunrise)
    current = sunrise
    for _ in range(12):
        planetary_hours.append((current, chaldean_order[current_ruler_index]))
        current += day_duration
        current_ruler_index = (current_ruler_index + 1) % 7

    return planetary_hours

# Function to display planetary hours
def display_planetary_hours():
    planetary_hours = calculate_planetary_hours()
    print(f"\nPlanetary hours for {location.name}, {location.region} on {datetime.now().date()}:")
    for hour, ruler in planetary_hours:
        print(f"{hour.strftime('%H:%M')} - {ruler}")

# Function to get current planetary hour and the next three
def get_planetary_hour_and_next_three():
    planetary_hours = calculate_planetary_hours()

    # Determine current planetary hour
    for i in range(len(planetary_hours) - 1):
        if planetary_hours[i][0] <= current_time < planetary_hours[i + 1][0]:
            current_hour = planetary_hours[i][1]
            next_hours = [
                planetary_hours[i + 1][1],
                planetary_hours[i + 2][1],
                planetary_hours[i + 3][1]
            ]
            return current_hour, next_hours

# Function to calculate moon info
def moon_info():
    moon = ephem.Moon(observer)
    moon_phase = moon.phase
    moon_illumination = moon.phase / 100
    moon_alt = moon.alt * 57.2958
    moon_az = moon.az * 57.2958
    moon_rise = observer.next_rising(moon).datetime().astimezone(tz)
    moon_transit = observer.next_transit(moon).datetime().astimezone(tz)
    moon_set = observer.next_setting(moon).datetime().astimezone(tz)
    moon_constellation = ephem.constellation(moon)[1]
    return {
        "phase": moon_phase,
        "illumination": moon_illumination,
        "altitude": moon_alt,
        "azimuth": moon_az,
        "rise": moon_rise,
        "transit": moon_transit,
        "set": moon_set,
        "constellation": moon_constellation
    }

# Function to calculate Orion visibility
def orion_visibility():
    orion = ephem.FixedBody()
    orion._ra, orion._dec = "5:35:17.3", "-5:23:28"
    orion.compute(observer)
    orion_rise = observer.next_rising(orion).datetime().astimezone(tz)
    orion_transit = observer.next_transit(orion).datetime().astimezone(tz)
    orion_set = observer.next_setting(orion).datetime().astimezone(tz)
    return {
        "rise": orion_rise,
        "transit": orion_transit,
        "set": orion_set
    }

# Function to calculate visible planets
def visible_planets():
    planets = [ephem.Sun(), ephem.Mercury(), ephem.Venus(), ephem.Mars(), ephem.Jupiter(), ephem.Saturn()]
    visible = []
    for planet in planets:
        planet.compute(observer)
        if planet.alt > 0:  # Visible above the horizon
            planet_rise = observer.next_rising(planet).datetime().astimezone(tz)
            planet_transit = observer.next_transit(planet).datetime().astimezone(tz)
            planet_set = observer.next_setting(planet).datetime().astimezone(tz)
            planet_constellation = ephem.constellation(planet)[1]
            visible.append({
                "name": planet.name,
                "altitude": planet.alt * 57.2958,
                "azimuth": planet.az * 57.2958,
                "zodiac": planet_constellation,
                "rise": planet_rise,
                "transit": planet_transit,
                "set": planet_set
            })
    return visible

# Command-line arguments for options
parser = argparse.ArgumentParser(description="Astronomical and planetary hour calculations.")
parser.add_argument("--planetary_hours", action="store_true", help="Display planetary hours and current ruling planet.")
parser.add_argument("--moon", action="store_true", help="Display moon phase, position, and visibility times.")
parser.add_argument("--orion", action="store_true", help="Display Orion's rise, transit, and set times.")
parser.add_argument("--planets", action="store_true", help="Display visible planets and their positions.")
parser.add_argument("--all", action="store_true", help="Display all information.")

args = parser.parse_args()

# Display all results if --all is specified
if args.all or args.planetary_hours:
    current_hour, next_hours = get_planetary_hour_and_next_three()
    current_day = planetary_days[datetime.now().weekday()]
    print(f"Current Time: {datetime.now().strftime('%I:%M %p')}")
    print(f"Planetary Day: {current_day}")
    print(f"Planetary Hour: {current_hour}")
    print(f"Next Three Hours: {', '.join(next_hours)}")
    display_planetary_hours()

if args.all or args.moon:
    moon_data = moon_info()
    print(f"\nMoon Phase: {moon_data['phase']:.2f}%")
    print(f"Moon Illumination: {moon_data['illumination']:.2%}")
    print(f"Moon Position: Altitude = {moon_data['altitude']:.2f}°, Azimuth = {moon_data['azimuth']:.2f}°")
    print(f"Moon Rise: {moon_data['rise'].strftime('%I:%M %p')} | Transit: {moon_data['transit'].strftime('%I:%M %p')} | Set: {moon_data['set'].strftime('%I:%M %p')}")
    print(f"Moon is in the zodiac sign of {moon_data['constellation']}")

if args.all or args.orion:
    orion_data = orion_visibility()
    print(f"\nOrion Rise: {orion_data['rise'].strftime('%I:%M %p')} | Transit: {orion_data['transit'].strftime('%I:%M %p')} | Set: {orion_data['set'].strftime('%I:%M %p')}")

if args.all or args.planets:
    planets_data = visible_planets()
    print("\nVisible Planets:")
    if planets_data:
        for planet in planets_data:
            print(f"{planet['name']} - Altitude: {planet['altitude']:.2f}°, Azimuth: {planet['azimuth']:.2f}°, "
                  f"Zodiac: {planet['zodiac']} | Rise: {planet['rise'].strftime('%I:%M %p')} | "
                  f"Transit: {planet['transit'].strftime('%I:%M %p')} | Set: {planet['set'].strftime('%I:%M %p')}")
    else:
        print("No planets are visible in the sky right now.")