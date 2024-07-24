import requests

url = "https://api.tomorrow.io/v4/weather/forecast?location=new%20york&apikey=SwyVTH07GeA5nQDa292sfDyx0HM0X0J3"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

Weather Forecast
GET
https://api.tomorrow.io/v4/weather/forecast
RECIPES
Plot Weather Forecast Trends using Node
Open Recipe
Uncover Weather and Climate Variations Over Time Using Node
Open Recipe
LOG IN TO SEE FULL REQUEST HISTORY
TIME	STATUS	USER AGENT	
Make a request to see history.
0 Requests This Month

Using the weather forecast API you can access up-to-date weather information for your location, including minute-by-minute forecasts (for premium users) for the next hour, hourly forecasts for the next 120 hours, and daily forecasts for the next 5 days.
For the location query parameter we support multiple location types:

Latitude and Longitude (Decimal degree) location=42.3478, -71.0466
City name location=new york
US zip location=10001 US(2-letter code based on ISO-3166)
UK postcode location=SW1
QUERY PARAMS
location
string
required
Defaults to new york
new york
timesteps
array of strings
Timesteps includes: hourly: "1h", daily: "1d"


ADD STRING
units
string
Unit system of the field values, either "metric" or "imperial" - see Field Descriptors

Realtime Weather
GET
https://api.tomorrow.io/v4/weather/realtime
LOG IN TO SEE FULL REQUEST HISTORY
TIME	STATUS	USER AGENT	
Make a request to see history.
0 Requests This Month

Using the Realtime Weather API you can access current weather information for your location in minute-by-minute temporal resolution.
For the location query parameter, we support multiple location types:

Latitude and Longitude (Decimal degree) location=42.3478, -71.0466
City name location=new york
US zip location=10001 US (2-letter code based on ISO-3166)
UK postcode location=SW1
QUERY PARAMS
location
string
required
Defaults to toronto
toronto
units
string
Unit system of the field values, either "metric" or "imperial" - see Field Descriptors

import requests

url = "https://api.tomorrow.io/v4/weather/realtime?location=toronto&apikey=SwyVTH07GeA5nQDa292sfDyx0HM0X0J3"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

Weather Recent History
GET
https://api.tomorrow.io/v4/weather/history/recent
LOG IN TO SEE FULL REQUEST HISTORY
TIME	STATUS	USER AGENT	
Make a request to see history.
0 Requests This Month

Using the recent history weather API you can access historical weather forecasts for your location, including hourly history for the last 24 hours, and daily history for the last day.
For the location query parameter, we support multiple location types:

Latitude and Longitude (Decimal degree) location=42.3478, -71.0466
City name location=new york
US zip location=10001 US(2-letter code based on ISO-3166)
UK postcode location=SW1
QUERY PARAMS
location
string
required
Defaults to austin
austin
timesteps
array of strings
Timesteps includes: hourly: "1h", daily: "1d"


ADD STRING
units
string
Unit system of the field values, either "metric" or "imperial" - see Field Descriptors

import requests

url = "https://api.tomorrow.io/v4/weather/history/recent?location=austin&apikey=SwyVTH07GeA5nQDa292sfDyx0HM0X0J3"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

Core
Data Fields
The Tomorrow.io REST Weather API provides the following information:

Field	Values (Metric, Imperial)	Availability
temperature

The "real" temperature measurement (at 2m)

Learn more	Celsius [-90,60]
Fahrenheit [-130,140]	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I M R
A: WW
S: ∧ ∨ ~ ⧖
P: +
temperature

temperature-si
temperature-us
temperatureApparent

The temperature equivalent perceived by humans, caused by the combined effects of air temperature, relative humidity, and wind speed (at 2m)

Also known as "feels like".

Learn more	Celsius [-90,60]
Fahrenheit [-130,140]	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I M R
A: WW
S: ∧ ∨ ~ ⧖
P: +
dewPoint

The temperature to which air must be cooled to become saturated with water vapor (at 2m)

Learn more	Celsius [0,100]
Fahrenheit [32,212]	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I M R
A: WW
S: ∧ ∨ ~ ⧖
P: +
dewpoint

dewpoint-si
dewpoint-us
humidity

The concentration of water vapor present in the air

Learn more	%	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I M R
A: WW
S: ∧ ∨ ~ ⧖
P: +
humidity

humidity
windSpeed

The fundamental atmospheric quantity caused by air moving from high to low pressure, usually due to changes in temperature (at 10m)

Learn more	m/s
mph	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]

I: T I M R
A: WW
S: ∧ ∨ ~ ⧖
P: +
wind-speed

wind-speed-si
wind-speed-us
windDirection

The direction from which it originates, measured in degrees clockwise from due north (at 10m)

Learn more	degrees or null	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I M R
A: WW
S:
P: +
wind-direction

wind-direction
windGust

The maximum brief increase in the speed of the wind, usually less than 20 seconds (at 10m)

Learn more	m/s
mph	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I M R
A: WW
S: ∧ ∨ ~ ⧖
P: +
wind-gust

wind-gust-si
wind-gust-us
pressureSurfaceLevel

The force exerted against a surface by the weight of the air above the surface (at the surface level)

Learn more	hPa
inHg	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I R
A: WW
S: ∧ ∨ ~ ⧖
P: +
pressureSeaLevel

The force exerted against a surface by the weight of the air above the surface (at the mean sea level)

Learn more	hPa
inHg	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T M R
A: WW
S: ∧ ∨ ~ ⧖
P: +
pressure

pressure-si
pressure-us
precipitationIntensity

The instantaneous precipitation rate at ground level

The measure of the intensity of precipitation by calculating the amount of precipitation that would fall over a given interval of time if the precipitation intensity were constant over that time period.

The rate is expressed in terms of length (depth) per unit time, in millimeters per hour, or inches per hour.

Learn more	mm/hr
in/hr	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I M R
A: WW
S: ∧ ∨ ~ ⧖
P: +
precip-si

precip-si
precip-us
rainIntensity

The measure of the intensity of rainfall by calculating the amount of rain that would fall over a given interval of time if the rain intensity were constant over that time period.

The rate is expressed in terms of length (depth) per unit time, in millimeters per hour, or inches per hour.

Learn more	mm/hr
in/hr	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I M R
A: WW
S: ∧ ∨ ~ ⧖
P: -
freezingRainIntensity

The measure of the intensity of freezing rain by calculating the amount of freezing rain that would fall over a given interval of time if the freezing rain intensity were constant over that time period.

The rate is expressed in terms of length (depth) per unit time, in millimeters per hour, or inches per hour.

Learn more	mm/hr
in/hr	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I M R
A: WW
S: ∧ ∨ ~ ⧖
P: -
snowIntensity

The measure of the intensity of snowfall by calculating the amount of snow that would fall over a given interval of time if the snow intensity were constant over that time period.

The rate is expressed in terms of length (depth) per unit time, in millimeters per hour, or inches per hour.

Learn more	mm/hr
in/hr	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I M R
A: WW
S: ∧ ∨ ~ ⧖
P: -
sleetIntensity

The measure of the intensity of sleet (ice pellets) by calculating the amount of sleet that would fall over a given interval of time if the sleet intensity were constant over that time period.

The rate is expressed in terms of length (depth) per unit time, in millimeters per hour, or inches per hour.

Learn more	mm/hr
in/hr	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I M R
A: WW
S: ∧ ∨ ~ ⧖
P: -
precipitationProbability

Probability of precipitation represents the chance of >0.0254 cm (0.01 in.) of liquid equivalent precipitation at a radius surrounding a point location over a specific period of time.

Learn more	%	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T R
A: WW
S: ∧ ∨ ~ ⧖
P: -
precipitationType

The various types of precipitation often include the character or phase of the precipitation which is falling to ground level (Schuur classification)

Precipitation Type indicates what type the precipitation will be if something were to precipitate out.

This will have a non-zero value regardless of the precipitation probability or intensity values

Learn more	1: Rain
2: Snow
3: Freezing Rain
4: Ice Pellets / Sleet	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I R
A: WW
S: ∧ ∨ ~ ⧖
P: -
rainAccumulation

The accumulated amount of liquid rain that has or will accumulate for the past or future hour of the requested time

Learn more	mm
in	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I
A: WW
S: ∧ ∨ ~ ⧖
P: +
snowAccumulation

The accumulated amount of new snowfall that has or will accumulate for the past or future hour of the requested time

Will always return hourly data and does not aggregate - eg. if you request snowAccumulationMax over a daily timestep, the max hourly value of that day will be returned, not the accumulation for the whole day.

Learn more	mm
in	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I
A: WW
S: ∧ ∨ ~ ⧖
P: -
snowAccumulationLwe

The liquid water equivalent of accumulated amount of new snowfall that has or will accumulate for the past or future hour of the requested time

Will always return hourly data and does not aggregate - eg. if you request snowAccumulationMax over a daily timestep, the max hourly value of that day will be returned, not the accumulation for the whole day.

Learn more	mm of LWE
in of LWE	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I
A: WW
S: ∧ ∨ ~
P: +
snowDepth

The depth of snow on the ground including both new and old snow

Learn more	cm
in	F: [-6 hours for free, up to -7 days for paying accounts, +48 hours]
I: T I M
A: US
S: ∧ ∨ ~ ⧖
P: -
sleetAccumulation

The accumulated amount of sleet (ice pellets) that has or will accumulate for the past or future hour of the requested time

Learn more	mm
in	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I
A: WW
S: ∧ ∨ ~ ⧖
P: -
sleetAccumulationLwe

The liquid water equivalent accumulated amount of sleet (ice pellets) that has or will accumulate for the past or future hour of the requested time	mm of LWE
in of LWE	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I
A: WW
S: ∧ ∨ ~
P: -
iceAccumulation

The accumulated amount of ice from freezing rain that has or will accumulate for the past or future hour of the requested time

Learn more	mm
in	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I
A: WW
S: ∧ ∨ ~ ⧖
P: -
iceAccumulationLwe

The liquid water equivalent
accumulated amount of ice from freezing rain that has or will accumulate for the past or future hour of the requested time	mm of LWE
in of LWE	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I
A: WW
S: ∧ ∨ ~
P: -
sunriseTime

The daily appearance of the Sun on the horizon due to Earth's rotation

Learn more	UTC ISO-8601	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I
A: WW
S:
P: -
sunsetTime

The daily disappearance of the Sun below the horizon due to Earth's rotation

Learn more	UTC ISO-8601	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I
A: WW
S:
P: -
visibility

The measure of the distance at which an object or light can be clearly discerned

Learn more	km
mi	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I M R
A: WW
S: ∧ ∨ ~ ⧖
P: +
visibility

visibility-si
visibility-us
cloudCover

The fraction of the sky obscured by clouds when observed from a particular location

Learn more	%	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I M R
A: WW
S: ∧ ∨ ~ ⧖
P: +
cloud-cover

cloud-cover
cloudBase

The lowest altitude of the visible portion of a cloud (above ground level)

Learn more	km or null
mi or null	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I M R
A: WW
S: ∧ ∨ ~ ⧖
P: +
cloud-base

cloud-base-si
cloud-base-us
cloudCeiling

The highest altitude of the visible portion of a cloud (above ground level)

Learn more	km or null
mi or null	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I M R
A: WW
S: ∧ ∨ ~ ⧖
P: +
cloud-ceiling

cloud-ceiling-si
cloud-ceiling-us
moonPhase

The shape of the directly sunlit portion of the Moon as viewed from Earth

Learn more	0: New (0.0625-0.9375)
1: Waxing Crescent (0.0625-0.1875)
2: First Quarter (0.1875-0.3125)
3: Waxing Gibbous (0.3125-0.4375)
4: Full (0.4375-0.5625)
5: Waning Gibbous (0.5625-0.6875)
6: Third Quarter (0.6875-0.8125)
7: Waning Crescent (0.8125-0.9375)	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T
A: WW
S:
P: -
uvIndex

Standard measurement of the strength of sunburn producing UV radiation at a particular place and time.

Learn more	0-2: Low
3-5: Moderate
6-7: High
8-10: Very High
11+: Extreme	F: [-6 hours for free, up to -7 days for paying accounts, +108 hours]
D: T
A: WW
S: ∧ ∨ ~ ⧖
P: -
uvHealthConcern

When the predicted UV index is within these numerical ranges, the recommended need for protection is indicated by the qualitative description of the values.

Learn more	0-2: Low
3-5: Moderate
6-7: High
8-10: Very High
11+: Extreme	F: [-6 hours for free, up to -7 days for paying accounts, +108 hours]
D: T
A: WW
S: ∧ ∨ ~ ⧖
P: -
gdd10To30

Growing Degree Days calculation with a temperature base of 10°C and a temperature cap of 30°C.
Typically used to determine Maize and Soybean phonological stage.

Learn more	The number of growing degree days	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T R
A: WW
P: -
gdd10To31

Growing Degree Days calculation with a temperature base of 10°C and a temperature cap of 31°C.
Typically used to determine Sunflower phonological stage.	The number of growing degree days	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T R
A: WW
P: -
gdd08To30

Growing Degree Days calculation with a temperature base of 08°C and a temperature cap of 30°C.
Typically used to determine Green Gram and Sorghum phonological stage.	The number of growing degree days	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T R
A: WW
P: -
gdd03To25

Growing Degree Days calculation with a temperature base of 03°C and a temperature cap of 25°C.
Typically used to determine Potatoes phonological stage.	The number of growing degree days	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T R
A: WW
P: -
evapotranspiration
Penman–Monteith FAO56

The combined processes by which water moves from the earth’s surface into the atmosphere.

Learn more	mm
in	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T I
A: WW
S: ∧ ∨ ~ ⧖
P: +
weatherCodeFullDay

The text description that conveys the most prominent weather condition during the day (from sunrise till next sunrise)	Weather Codes values	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T R
A: WW
S: ∧ ∨ ⧖
P: -
weatherCodeDay

The text description that conveys the most prominent weather condition during the day (from sunrise till sunset)	Weather Codes values	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T R
A: WW
S: ∧ ∨ ⧖
P: -
weatherCodeNight

The text description that conveys the most prominent weather condition during the night (from sunset till sunrise)	Weather Codes values	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T R
A: WW
S: ∧ ∨ ⧖
P: -
weatherCode

The text description that conveys the most prominent weather condition	Weather Codes values	F: [-6 hours for free, up to -7 days for paying accounts, +15 days]
I: T R
A: WW
S: ∧ ∨ ⧖
P: -
thunderstormProbability

The probability that lightning flash density exceeds 0.1 with units of (100 km^2 / hour).	%	F: [+14 days]
I: T I M
A: WW
S: ∧ ∨ ~
P: -

Updated 1 day ago

Weather Codes
🚧
weatherCode field only includes basic weather conditions i.e "clear", and does not include mixed conditions ("partly cloudy and fog").

For a complete set of daily conditions, please use the new weatherCodeFullDay (calculated from sunrise to sunrise), weatherCodeDay (calculated from sunrise to sunset), and weatherCodeNight (calculated from sunset to sunrise).

Is it foggy? Rainy? A clear day? If you need a description of what the weather is like, simply request the weather code.

As our beloved Tomorrow.io REST Weather API consumers, we provide full access to our library of weather icons. Be sure to place a “Powered by Tomorrow.io” attribution in your application if you use our icons.

Field Code	Description	Icon
weatherCode 1000
weatherCodeFullDay 1000
weatherCodeDay 10000
weatherCodeNight 10001	Clear	clear_day

clear_night
weatherCode 1100
weatherCodeFullDay 1100
weatherCodeDay 11000
weatherCodeNight 11001	Mostly Clear	mostly_clear_day

mostly_clear_night
weatherCode 1101
weatherCodeFullDay 1101
weatherCodeDay 11010
weatherCodeNight 11011	Partly Cloudy	partly_cloudy_day

partly_cloudy_night
weatherCode 1102
weatherCodeFullDay 1102
weatherCodeDay 11020
weatherCodeNight 11021	Mostly Cloudy	mostly_cloudy_day

mostly_cloudy_night
weatherCode 1001
weatherCodeFullDay 1001
weatherCodeDay 10010
weatherCodeNight 10011	Cloudy	cloudy
weatherCodeFullDay 1103
weatherCodeDay 11030
weatherCodeNight 11031	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Mostly Clear	mostly_clear_day

mostly_clear_night
weatherCode 2100
weatherCodeFullDay 2100
weatherCodeDay 21000
weatherCodeNight 21001	Light Fog	light_fog
weatherCode 2000
weatherCodeFullDay 2000
weatherCodeDay 20000
weatherCodeNight 20001	Fog	fog
weatherCodeFullDay 2101
weatherCodeDay 21010
weatherCodeNight 21011	Mixed conditions:
Condition 1: Mostly Clear
Condition 2: Light Fog	mostly_clear_light_fog_day

mostly_clear_light_fog_night
weatherCodeFullDay 2102
weatherCodeDay 21020
weatherCodeNight 21021	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Light Fog	partly_cloudy_light_fog_day

partly_cloudy_light_fog_night
weatherCodeFullDay 2103
weatherCodeDay 21030
weatherCodeNight 21031	Mixed conditions:
Condition 1: Mostly Cloudy
Condition 2: Light Fog	mostly_cloudy_light_fog_day

mostly_cloudy_light_fog_night
weatherCodeFullDay 2106
weatherCodeDay 21060
weatherCodeNight 21061	Mixed conditions:
Condition 1: Mostly Clear
Condition 2: Fog	mostly_clear_fog_day

mostly_clear_fog_night
weatherCodeFullDay 2107
weatherCodeDay 21070
weatherCodeNight 21071	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Fog	partly_cloudy_fog_day

partly_cloudy_fog_night
weatherCodeFullDay 2108
weatherCodeDay 21080
weatherCodeNight 21081	Mixed conditions:
Condition 1: Mostly Cloudy
Condition 2: Fog	mostly_cloudy_fog_day

mostly_cloudy_fog_night
weatherCode 4000
weatherCodeFullDay 4000
weatherCodeDay 40000
weatherCodeNight 40001	Drizzle	drizzle
weatherCode 4200
weatherCodeFullDay 4200
weatherCodeDay 42000
weatherCodeNight 42001	Light Rain	light_rain
weatherCode 4001
weatherCodeFullDay 4001
weatherCodeDay 40010
weatherCodeNight 40011	Rain	rain
weatherCode 4201
weatherCodeFullDay 4201
weatherCodeDay 42010
weatherCodeNight 42011	Heavy Rain	heavy_rain
weatherCodeFullDay 4203
weatherCodeDay 42030
weatherCodeNight 42031	Mixed conditions:
Condition 1: Mostly Clear
Condition 2: Drizzle	mostly_clear_drizzle_day

mostly_clear_drizzle_night
weatherCodeFullDay 4204
weatherCodeDay 42040
weatherCodeNight 42041	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Drizzle	partly_cloudy_drizzle_day

partly_cloudy_drizzle_night
weatherCodeFullDay 4205
weatherCodeDay 42050
weatherCodeNight 42051	Mixed conditions:
Condition 1: Mostly Cloudy
Condition 2: Drizzle	mostly_cloudy_drizzle_day

mostly_cloudy_drizzle_night
weatherCodeFullDay 4213
weatherCodeDay 42130
weatherCodeNight 42131	Mixed conditions:
Condition 1: Mostly Clear
Condition 2: Light Rain	mostly_clear_light_rain_day

mostly_clear_light_rain_night
weatherCodeFullDay 4214
weatherCodeDay 42140
weatherCodeNight 42141	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Light Rain	partly_cloudy_light_rain_day

partly_cloudy_light_rain_night
weatherCodeFullDay 4215
weatherCodeDay 42150
weatherCodeNight 42151	Mixed conditions:
Condition 1: Mostly Cloudy
Condition 2: Light Rain	mostly_cloudy_light_rain_day

mostly_cloudy_light_rain_night
weatherCodeFullDay 4209
weatherCodeDay 42090
weatherCodeNight 42091	Mixed conditions:
Condition 1: Mostly Clear
Condition 2: Rain	mostly_clear_rain_day

mostly_clear_rain_night
weatherCodeFullDay 4208
weatherCodeDay 42080
weatherCodeNight 42081	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Rain	partly_cloudy_rain_day

partly_cloudy_rain_night
weatherCodeFullDay 4210
weatherCodeDay 42100
weatherCodeNight 42101	Mixed conditions:
Condition 1: Mostly Cloudy
Condition 2: Rain	mostly_cloudy_rain_day

mostly_cloudy_rain_night
weatherCodeFullDay 4211
weatherCodeDay 42110
weatherCodeNight 42111	Mixed conditions:
Condition 1: Mostly Clear
Condition 2: Heavy Rain	mostly_clear_heavy_rain_day

mostly_clear_heavy_rain_night
weatherCodeFullDay 4202
weatherCodeDay 42020
weatherCodeNight 42021	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Heavy Rain	partly_cloudy_heavy_rain_day

partly_cloudy_heavy_rain_night
weatherCodeFullDay 4212
weatherCodeDay 42120
weatherCodeNight 42121	Mixed conditions:
Condition 1: Mostly Cloudy
Condition 2: Heavy Rain	mostly_cloudy_heavy_rain_day

mostly_cloudy_heavy_rain_night
weatherCode 5001
weatherCodeFullDay 5001
weatherCodeDay 50010
weatherCodeNight 50011	Flurries	flurries
weatherCode 5100
weatherCodeFullDay 5100
weatherCodeDay 51000
weatherCodeNight 51001	Light Snow	light_snow_day
weatherCode 5000
weatherCodeFullDay 5000
weatherCodeDay 50000
weatherCodeNight 50001	Snow	snow
weatherCode 5101
weatherCodeFullDay 5101
weatherCodeDay 51010
weatherCodeNight 51011	Heavy Snow	heavy_snow
weatherCodeFullDay 5115
weatherCodeDay 51150
weatherCodeNight 51151	Mixed conditions:
Condition 1: Mostly Clear
Condition 2: Flurries	mostly_clear_flurries_day

mostly_clear_flurries_night
weatherCodeFullDay 5116
weatherCodeDay 51160
weatherCodeNight 51161	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Flurries	partly_cloudy_flurries_day

partly_cloudy_flurries_night
weatherCodeFullDay 5117
weatherCodeDay 51170
weatherCodeNight 51171	Mixed conditions:
Condition 1: Mostly Cloudy
Condition 2: Flurries	mostly_cloudy_flurries_day

mostly_cloudy_flurries_night
weatherCodeFullDay 5122
weatherCodeDay 51220
weatherCodeNight 51221	Mixed conditions:
Condition 1: Drizzle
Condition 2: Light Snow	drizzle_light_snow
weatherCodeFullDay 5102
weatherCodeDay 51020
weatherCodeNight 51021	Mixed conditions:
Condition 1: Mostly Clear
Condition 2: Light Snow	mostly_clear_light_snow_day

mostly_clear_light_snow_night
weatherCodeFullDay 5103
weatherCodeDay 51030
weatherCodeNight 51031	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Light Snow	partly_cloudy_light_snow_day

partly_cloudy_light_snow_night
weatherCodeFullDay 5104
weatherCodeDay 51040
weatherCodeNight 51041	Mixed conditions:
Condition 1: Mostly Cloudy
Condition 2: Light Snow	mostly_cloudy_light_snow_day

mostly_cloudy_light_snow_night
weatherCodeFullDay 5105
weatherCodeDay 51050
weatherCodeNight 51051	Mixed conditions:
Condition 1: Mostly Clear
Condition 2: Snow	mostly_clear_snow_day

mostly_clear_snow_night
weatherCodeFullDay 5106
weatherCodeDay 51060
weatherCodeNight 51061	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Snow	partly_cloudy_snow_day

partly_cloudy_snow_night
weatherCodeFullDay 5107
weatherCodeDay 51070
weatherCodeNight 51071	Mixed conditions:
Condition 1: Mostly Cloudy
Condition 2: Snow	mostly_cloudy_snow_day

mostly_cloudy_snow_night
weatherCodeFullDay 5119
weatherCodeDay 51190
weatherCodeNight 51191	Mixed conditions:
Condition 1: Mostly Clear
Condition 2: Heavy Snow	mostly_clear_heavy_snow_day

mostly_clear_heavy_snow_night
weatherCodeFullDay 5120
weatherCodeDay 51200
weatherCodeNight 51201	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Heavy Snow	partly_cloudy_heavy_snow_day

partly_cloudy_heavy_snow_night
weatherCodeFullDay 5121
weatherCodeDay 51210
weatherCodeNight 51211	Mixed conditions:
Condition 1: Mostly Cloudy
Condition 2: Heavy Snow	mostly_cloudy_heavy_snow_day

mostly_cloudy_heavy_snow_night
weatherCodeFullDay 5110
weatherCodeDay 51100
weatherCodeNight 51101	Mixed conditions:
Condition 1: Drizzle
Condition 2: Snow	drizzle_snow
weatherCodeFullDay 5108
weatherCodeDay 51080
weatherCodeNight 51081	Mixed conditions:
Condition 1: Rain
Condition 2: Snow	rain_snow
weatherCodeFullDay 5114
weatherCodeDay 51140
weatherCodeNight 51141	Mixed conditions:
Condition 1: Snow
Condition 2: Freezing Rain	snow_freezing_rain
weatherCodeFullDay 5112
weatherCodeDay 51120
weatherCodeNight 51121	Mixed conditions:
Condition 1: Snow
Condition 2: Ice Pellets	snow_ice_pellets
weatherCode 6000
weatherCodeFullDay 6000
weatherCodeDay 60000
weatherCodeNight 60001	Freezing Drizzle	freezing_drizzle
weatherCode 6200
weatherCodeFullDay 6200
weatherCodeDay 62000
weatherCodeNight 62001	Light Freezing Drizzle	light_freezing_drizzle
weatherCode 6001
weatherCodeFullDay 6001
weatherCodeDay 60010
weatherCodeNight 60011	Freezing Rain	freezing_rain
weatherCode 6201
weatherCodeFullDay 6201
weatherCodeDay 62010
weatherCodeNight 62011	Heavy Freezing Rain	heavy_freezing_rain
weatherCodeFullDay 6003
weatherCodeDay 60030
weatherCodeNight 60031	Mixed conditions:
Condition 1: Mostly Clear
Condition 2: Freezing Drizzle	mostly_clear_freezing_drizzle_day

mostly_clear_freezing_drizzle_night
weatherCodeFullDay 6002
weatherCodeDay 60020
weatherCodeNight 60021	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Freezing Drizzle	partly_cloudy_freezing_drizzle_day

partly_cloudy_freezing_drizzle_night
weatherCodeFullDay 6004
weatherCodeDay 60040
weatherCodeNight 60041	Mixed conditions:
Condition 1: Mostly Cloudy
Condition 2: Freezing Drizzle	mostly_cloudy_freezing_drizzle_day

mostly_cloudy_freezing_drizzle_night
weatherCodeFullDay 6204
weatherCodeDay 62040
weatherCodeNight 62041	Mixed conditions:
Condition 1: Drizzle
Condition 2: Freezing Drizzle	drizzle_freezing_drizzle
weatherCodeFullDay 6206
weatherCodeDay 62060
weatherCodeNight 62061	Mixed conditions:
Condition 1: Light Rain
Condition 2: Freezing Drizzle	light_rain_freezing_drizzle
weatherCodeFullDay 6205
weatherCodeDay 62050
weatherCodeNight 62051	Mixed conditions:
Condition 1: Mostly Clear
Condition 2: Light Freezing Rain	mostly_clear_light_freezing_rain_day

mostly_clear_light_freezing_rain_night
weatherCodeFullDay 6203
weatherCodeDay 62030
weatherCodeNight 62031	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Light Freezing Rain	partly_cloudy_light_freezing_rain_day

partly_cloudy_light_freezing_rain_night
weatherCodeFullDay 6209
weatherCodeDay 62090
weatherCodeNight 62091	Mixed conditions:
Condition 1: Mostly Cloudy
Condition 2: Light Freezing Rain	mostly_cloudy_light_freezing_rain_day

mostly_cloudy_light_freezing_rain_night
weatherCodeFullDay 6213
weatherCodeDay 62130
weatherCodeNight 62131	Mixed conditions:
Condition 1: Mostly Clear
Condition 2: Freezing Rain	mostly_clear_freezing_rain_day

mostly_cloudy_freezing_rain_night
weatherCodeFullDay 6214
weatherCodeDay 62140
weatherCodeNight 62141	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Freezing Rain	partly_cloudy_freezing_rain_day

partly_cloudy_freezing_rain_night
weatherCodeFullDay 6215
weatherCodeDay 62150
weatherCodeNight 62151	Mixed conditions:
Condition 1: Mostly Cloudy
Condition 2: Freezing Rain	mostly_cloudy_freezing_rain_day

mostly_cloudy_freezing_rain_night
weatherCodeFullDay 6212
weatherCodeDay 62120
weatherCodeNight 62121	Mixed conditions:
Condition 1: Drizzle
Condition 2: Freezing Rain	drizzle_freezing_rain
weatherCodeFullDay 6220
weatherCodeDay 62200
weatherCodeNight 62201	Mixed conditions:
Condition 1: Light Rain
Condition 2: Freezing Rain	light_rain_freezing_rain
weatherCodeFullDay 6222
weatherCodeDay 62220
weatherCodeNight 62221	Mixed conditions:
Condition 1: Rain
Condition 2: Freezing Rain	rain_freezing_rain
weatherCodeFullDay 6207
weatherCodeDay 62070
weatherCodeNight 62071	Mixed conditions:
Condition 1: Mostly Clear
Condition 2: Heavy Freezing Rain	mostly_clear_heavy_freezing_rain_day

mostly_clear_heavy_freezing_rain_night
weatherCodeFullDay 6202
weatherCodeDay 62020
weatherCodeNight 62021	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Heavy Freezing Rain	partly_cloudy_heavy_freezing_rain_day

partly_cloudy_heavy_freezing_rain_night
weatherCodeFullDay 6208
weatherCodeDay 62080
weatherCodeNight 62081	Mixed conditions:
Condition 1: Mostly Cloudy
Condition 2: Heavy Freezing Rain	mostly_cloudy_heavy_freezing_rain_day

mostly_cloudy_heavy_freezing_rain_night
weatherCode 7102
weatherCodeFullDay 7102
weatherCodeDay 71020
weatherCodeNight 71021	Light Ice Pellets	light_ice_pellets
weatherCode 7000
weatherCodeFullDay 7000
weatherCodeDay 70000
weatherCodeNight 70001	Ice Pellets	ice_pellets
weatherCode 7101
weatherCodeFullDay 7101
weatherCodeDay 71010
weatherCodeNight 71011	Heavy Ice Pellets	heavy_ice_pellets
weatherCodeFullDay 7110
weatherCodeDay 71100
weatherCodeNight 71101	Mixed conditions:
Condition 1: Mostly Clear
Condition 2: Light Ice Pellets	mostly_clear_light_ice_pellets_day

mostly_clear_light_ice_pellets_day
weatherCodeFullDay 7111
weatherCodeDay 71110
weatherCodeNight 71111	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Light Ice Pellets	partly_cloudy_light_ice_pellets_day

partly_cloudy_light_ice_pellets_day
weatherCodeFullDay 7112
weatherCodeDay 71120
weatherCodeNight 71121	Mixed conditions:
Condition 1: Mostly Cloudy
Condition 2: Light Ice Pellets	mostly_cloudy_light_ice_pellets_day

mostly_cloudy_light_ice_pellets_day
weatherCodeFullDay 7108
weatherCodeDay 71080
weatherCodeNight 71081	Mixed conditions:
Condition 1: Mostly Clear
Condition 2: Ice Pellets	mostly_clear_ice_pellets_day

mostly_clear_ice_pellets_night
weatherCodeFullDay 7107
weatherCodeDay 71070
weatherCodeNight 71071	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Ice Pellets	partly_cloudy_ice_pellets_day

partly_cloudy_ice_pellets_night
weatherCodeFullDay 7109
weatherCodeDay 71090
weatherCodeNight 71091	Mixed conditions:
Condition 1: Mostly Cloudy
Condition 2: Ice Pellets	mostly_cloudy_ice_pellets_day

mostly_cloudy_ice_pellets_night
weatherCodeFullDay 7113
weatherCodeDay 71130
weatherCodeNight 71131	Mixed conditions:
Condition 1: Mostly Clear
Condition 2: Heavy Ice Pellets	mostly_clear_heavy_ice_pellets_day

mostly_clear_heavy_ice_pellets_night
weatherCodeFullDay 7114
weatherCodeDay 71140
weatherCodeNight 71141	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Heavy Ice Pellets	partly_cloudy_heavy_ice_pellets_day

partly_cloudy_heavy_ice_pellets_night
weatherCodeFullDay 7116
weatherCodeDay 71160
weatherCodeNight 71161	Mixed conditions:
Condition 1: Mostly Cloudy
Condition 2: Heavy Ice Pellets	mostly_cloudy_heavy_ice_pellets_day

mostly_cloudy_heavy_ice_pellets_night
weatherCodeFullDay 7105
weatherCodeDay 71050
weatherCodeNight 71051	Mixed conditions:
Condition 1: Drizzle
Condition 2: Ice Pellets	drizzle_ice_pellets
weatherCodeFullDay 7115
weatherCodeDay 71150
weatherCodeNight 71151	Mixed conditions:
Condition 1: Light Rain
Condition 2: Ice Pellets	light_rain_ice_pellets
weatherCodeFullDay 7117
weatherCodeDay 71170
weatherCodeNight 71171	Mixed conditions:
Condition 1: Rain
Condition 2: Ice Pellets	rain_ice_pellets
weatherCodeFullDay 7106
weatherCodeDay 71060
weatherCodeNight 71061	Mixed conditions:
Condition 1: Freezing Rain
Condition 2: Ice Pellets	freezing_rain_ice_pellets
weatherCodeFullDay 7103
weatherCodeDay 71030
weatherCodeNight 71031	Mixed conditions:
Condition 1: Freezing Rain
Condition 2: Heavy Ice Pellets	freezing_rain_heavy_ice_pellets
weatherCode 8000
weatherCodeFullDay 8000
weatherCodeDay 80000
weatherCodeNight 80001	Thunderstorm	thunderstorm
weatherCodeFullDay 8001
weatherCodeDay 80010
weatherCodeNight 80011	Mixed conditions:
Condition 1: Mostly Clear
Condition 2: Thunderstorm	mostly_clear_thunderstorm_day

mostly_clear_thunderstorm_night
weatherCodeFullDay 8003
weatherCodeDay 80030
weatherCodeNight 80031	Mixed conditions:
Condition 1: Partly Cloudy
Condition 2: Thunderstorm	partly_cloudy_thunderstorm_day

partly_cloudy_thunderstorm_night
weatherCodeFullDay 8002
weatherCodeDay 80020
weatherCodeNight 80021	Mixed conditions:
Condition 1: Mostly Cloudy
Condition 2: Thunderstorm	mostly_cloudy_thunderstorm_day

mostly_cloudy_thunderstorm_night
JSON

"weatherCode": {
      "0": "Unknown",
      "1000": "Clear, Sunny",
      "1100": "Mostly Clear",
      "1101": "Partly Cloudy",
      "1102": "Mostly Cloudy",
      "1001": "Cloudy",
      "2000": "Fog",
      "2100": "Light Fog",
      "4000": "Drizzle",
      "4001": "Rain",
      "4200": "Light Rain",
      "4201": "Heavy Rain",
      "5000": "Snow",
      "5001": "Flurries",
      "5100": "Light Snow",
      "5101": "Heavy Snow",
      "6000": "Freezing Drizzle",
      "6001": "Freezing Rain",
      "6200": "Light Freezing Rain",
      "6201": "Heavy Freezing Rain",
      "7000": "Ice Pellets",
      "7101": "Heavy Ice Pellets",
      "7102": "Light Ice Pellets",
      "8000": "Thunderstorm"
    },

    "weatherCodeFullDay": {
      "0": "Unknown",
      "1000": "Clear, Sunny",
      "1100": "Mostly Clear",
      "1101": "Partly Cloudy",
      "1102": "Mostly Cloudy",
      "1001": "Cloudy",
      "1103": "Partly Cloudy and Mostly Clear",
      "2100": "Light Fog",
      "2101": "Mostly Clear and Light Fog",
      "2102": "Partly Cloudy and Light Fog",
      "2103": "Mostly Cloudy and Light Fog",
      "2106": "Mostly Clear and Fog",
      "2107": "Partly Cloudy and Fog",
      "2108": "Mostly Cloudy and Fog",
      "2000": "Fog",
      "4204": "Partly Cloudy and Drizzle",
      "4203": "Mostly Clear and Drizzle",
      "4205": "Mostly Cloudy and Drizzle",
      "4000": "Drizzle",
      "4200": "Light Rain",
      "4213": "Mostly Clear and Light Rain",
      "4214": "Partly Cloudy and Light Rain",
      "4215": "Mostly Cloudy and Light Rain",
      "4209": "Mostly Clear and Rain",
      "4208": "Partly Cloudy and Rain",
      "4210": "Mostly Cloudy and Rain",
      "4001": "Rain",
      "4211": "Mostly Clear and Heavy Rain",
      "4202": "Partly Cloudy and Heavy Rain",
      "4212": "Mostly Cloudy and Heavy Rain",
      "4201": "Heavy Rain",
      "5115": "Mostly Clear and Flurries",
      "5116": "Partly Cloudy and Flurries",
      "5117": "Mostly Cloudy and Flurries",
      "5001": "Flurries",
      "5100": "Light Snow",
      "5102": "Mostly Clear and Light Snow",
      "5103": "Partly Cloudy and Light Snow",
      "5104": "Mostly Cloudy and Light Snow",
      "5122": "Drizzle and Light Snow",
      "5105": "Mostly Clear and Snow",
      "5106": "Partly Cloudy and Snow",
      "5107": "Mostly Cloudy and Snow",
      "5000": "Snow",
      "5101": "Heavy Snow",
      "5119": "Mostly Clear and Heavy Snow",
      "5120": "Partly Cloudy and Heavy Snow",
      "5121": "Mostly Cloudy and Heavy Snow",
      "5110": "Drizzle and Snow",
      "5108": "Rain and Snow",
      "5114": "Snow and Freezing Rain",
      "5112": "Snow and Ice Pellets",
      "6000": "Freezing Drizzle",
      "6003": "Mostly Clear and Freezing drizzle",
      "6002": "Partly Cloudy and Freezing drizzle",
      "6004": "Mostly Cloudy and Freezing drizzle",
      "6204": "Drizzle and Freezing Drizzle",
      "6206": "Light Rain and Freezing Drizzle",
      "6205": "Mostly Clear and Light Freezing Rain",
      "6203": "Partly Cloudy and Light Freezing Rain",
      "6209": "Mostly Cloudy and Light Freezing Rain",
      "6200": "Light Freezing Rain",
      "6213": "Mostly Clear and Freezing Rain",
      "6214": "Partly Cloudy and Freezing Rain",
      "6215": "Mostly Cloudy and Freezing Rain",
      "6001": "Freezing Rain",
      "6212": "Drizzle and Freezing Rain",
      "6220": "Light Rain and Freezing Rain",
      "6222": "Rain and Freezing Rain",
      "6207": "Mostly Clear and Heavy Freezing Rain",
      "6202": "Partly Cloudy and Heavy Freezing Rain",
      "6208": "Mostly Cloudy and Heavy Freezing Rain",
      "6201": "Heavy Freezing Rain",
      "7110": "Mostly Clear and Light Ice Pellets",
      "7111": "Partly Cloudy and Light Ice Pellets",
      "7112": "Mostly Cloudy and Light Ice Pellets",
      "7102": "Light Ice Pellets",
      "7108": "Mostly Clear and Ice Pellets",
      "7107": "Partly Cloudy and Ice Pellets",
      "7109": "Mostly Cloudy and Ice Pellets",
      "7000": "Ice Pellets",
      "7105": "Drizzle and Ice Pellets",
      "7106": "Freezing Rain and Ice Pellets",
      "7115": "Light Rain and Ice Pellets",
      "7117": "Rain and Ice Pellets",
      "7103": "Freezing Rain and Heavy Ice Pellets",
      "7113": "Mostly Clear and Heavy Ice Pellets",
      "7114": "Partly Cloudy and Heavy Ice Pellets",
      "7116": "Mostly Cloudy and Heavy Ice Pellets",
      "7101": "Heavy Ice Pellets",
      "8001": "Mostly Clear and Thunderstorm",
      "8003": "Partly Cloudy and Thunderstorm",
      "8002": "Mostly Cloudy and Thunderstorm",
      "8000": "Thunderstorm"
    },

    "weatherCodeDay":{
      "0": "Unknown",
      "10000": "Clear, Sunny",
      "11000": "Mostly Clear",
      "11010": "Partly Cloudy",
      "11020": "Mostly Cloudy",
      "10010": "Cloudy",
      "11030": "Partly Cloudy and Mostly Clear",
      "21000": "Light Fog",
      "21010": "Mostly Clear and Light Fog",
      "21020": "Partly Cloudy and Light Fog",
      "21030": "Mostly Cloudy and Light Fog",
      "21060": "Mostly Clear and Fog",
      "21070": "Partly Cloudy and Fog",
      "21080": "Mostly Cloudy and Fog",
      "20000": "Fog",
      "42040": "Partly Cloudy and Drizzle",
      "42030": "Mostly Clear and Drizzle",
      "42050": "Mostly Cloudy and Drizzle",
      "40000": "Drizzle",
      "42000": "Light Rain",
      "42130": "Mostly Clear and Light Rain",
      "42140": "Partly Cloudy and Light Rain",
      "42150": "Mostly Cloudy and Light Rain",
      "42090": "Mostly Clear and Rain",
      "42080": "Partly Cloudy and Rain",
      "42100": "Mostly Cloudy and Rain",
      "40010": "Rain",
      "42110": "Mostly Clear and Heavy Rain",
      "42020": "Partly Cloudy and Heavy Rain",
      "42120": "Mostly Cloudy and Heavy Rain",
      "42010": "Heavy Rain",
      "51150": "Mostly Clear and Flurries",
      "51160": "Partly Cloudy and Flurries",
      "51170": "Mostly Cloudy and Flurries",
      "50010": "Flurries",
      "51000": "Light Snow",
      "51020": "Mostly Clear and Light Snow",
      "51030": "Partly Cloudy and Light Snow",
      "51040": "Mostly Cloudy and Light Snow",
      "51220": "Drizzle and Light Snow",
      "51050": "Mostly Clear and Snow",
      "51060": "Partly Cloudy and Snow",
      "51070": "Mostly Cloudy and Snow",
      "50000": "Snow",
      "51010": "Heavy Snow",
      "51190": "Mostly Clear and Heavy Snow",
      "51200": "Partly Cloudy and Heavy Snow",
      "51210": "Mostly Cloudy and Heavy Snow",
      "51100": "Drizzle and Snow",
      "51080": "Rain and Snow",
      "51140": "Snow and Freezing Rain",
      "51120": "Snow and Ice Pellets",
      "60000": "Freezing Drizzle",
      "60030": "Mostly Clear and Freezing drizzle",
      "60020": "Partly Cloudy and Freezing drizzle",
      "60040": "Mostly Cloudy and Freezing drizzle",
      "62040": "Drizzle and Freezing Drizzle",
      "62060": "Light Rain and Freezing Drizzle",
      "62050": "Mostly Clear and Light Freezing Rain",
      "62030": "Partly Cloudy and Light Freezing Rain",
      "62090": "Mostly Cloudy and Light Freezing Rain",
      "62000": "Light Freezing Rain",
      "62130": "Mostly Clear and Freezing Rain",
      "62140": "Partly Cloudy and Freezing Rain",
      "62150": "Mostly Cloudy and Freezing Rain",
      "60010": "Freezing Rain",
      "62120": "Drizzle and Freezing Rain",
      "62200": "Light Rain and Freezing Rain",
      "62220": "Rain and Freezing Rain",
      "62070": "Mostly Clear and Heavy Freezing Rain",
      "62020": "Partly Cloudy and Heavy Freezing Rain",
      "62080": "Mostly Cloudy and Heavy Freezing Rain",
      "62010": "Heavy Freezing Rain",
      "71100": "Mostly Clear and Light Ice Pellets",
      "71110": "Partly Cloudy and Light Ice Pellets",
      "71120": "Mostly Cloudy and Light Ice Pellets",
      "71020": "Light Ice Pellets",
      "71080": "Mostly Clear and Ice Pellets",
      "71070": "Partly Cloudy and Ice Pellets",
      "71090": "Mostly Cloudy and Ice Pellets",
      "70000": "Ice Pellets",
      "71050": "Drizzle and Ice Pellets",
      "71060": "Freezing Rain and Ice Pellets",
      "71150": "Light Rain and Ice Pellets",
      "71170": "Rain and Ice Pellets",
      "71030": "Freezing Rain and Heavy Ice Pellets",
      "71130": "Mostly Clear and Heavy Ice Pellets",
      "71140": "Partly Cloudy and Heavy Ice Pellets",
      "71160": "Mostly Cloudy and Heavy Ice Pellets",
      "71010": "Heavy Ice Pellets",
      "80010": "Mostly Clear and Thunderstorm",
      "80030": "Partly Cloudy and Thunderstorm",
      "80020": "Mostly Cloudy and Thunderstorm",
      "80000": "Thunderstorm"
    },

    "weatherCodeNight": {
      "0": "Unknown",
      "10001": "Clear",
      "11001": "Mostly Clear",
      "11011": "Partly Cloudy",
      "11021": "Mostly Cloudy",
      "10011": "Cloudy",
      "11031": "Partly Cloudy and Mostly Clear",
      "21001": "Light Fog",
      "21011": "Mostly Clear and Light Fog",
      "21021": "Partly Cloudy and Light Fog",
      "21031": "Mostly Cloudy and Light Fog",
      "21061": "Mostly Clear and Fog",
      "21071": "Partly Cloudy and Fog",
      "21081": "Mostly Cloudy and Fog",
      "20001": "Fog",
      "42041": "Partly Cloudy and Drizzle",
      "42031": "Mostly Clear and Drizzle",
      "42051": "Mostly Cloudy and Drizzle",
      "40001": "Drizzle",
      "42001": "Light Rain",
      "42131": "Mostly Clear and Light Rain",
      "42141": "Partly Cloudy and Light Rain",
      "42151": "Mostly Cloudy and Light Rain",
      "42091": "Mostly Clear and Rain",
      "42081": "Partly Cloudy and Rain",
      "42101": "Mostly Cloudy and Rain",
      "40011": "Rain",
      "42111": "Mostly Clear and Heavy Rain",
      "42021": "Partly Cloudy and Heavy Rain",
      "42121": "Mostly Cloudy and Heavy Rain",
      "42011": "Heavy Rain",
      "51151": "Mostly Clear and Flurries",
      "51161": "Partly Cloudy and Flurries",
      "51171": "Mostly Cloudy and Flurries",
      "50011": "Flurries",
      "51001": "Light Snow",
      "51021": "Mostly Clear and Light Snow",
      "51031": "Partly Cloudy and Light Snow",
      "51041": "Mostly Cloudy and Light Snow",
      "51221": "Drizzle and Light Snow",
      "51051": "Mostly Clear and Snow",
      "51061": "Partly Cloudy and Snow",
      "51071": "Mostly Cloudy and Snow",
      "50001": "Snow",
      "51011": "Heavy Snow",
      "51191": "Mostly Clear and Heavy Snow",
      "51201": "Partly Cloudy and Heavy Snow",
      "51211": "Mostly Cloudy and Heavy Snow",
      "51101": "Drizzle and Snow",
      "51081": "Rain and Snow",
      "51141": "Snow and Freezing Rain",
      "51121": "Snow and Ice Pellets",
      "60001": "Freezing Drizzle",
      "60031": "Mostly Clear and Freezing drizzle",
      "60021": "Partly Cloudy and Freezing drizzle",
      "60041": "Mostly Cloudy and Freezing drizzle",
      "62041": "Drizzle and Freezing Drizzle",
      "62061": "Light Rain and Freezing Drizzle",
      "62051": "Mostly Clear and Light Freezing Rain",
      "62031": "Partly cloudy and Light Freezing Rain",
      "62091": "Mostly Cloudy and Light Freezing Rain",
      "62001": "Light Freezing Rain",
      "62131": "Mostly Clear and Freezing Rain",
      "62141": "Partly Cloudy and Freezing Rain",
      "62151": "Mostly Cloudy and Freezing Rain",
      "60011": "Freezing Rain",
      "62121": "Drizzle and Freezing Rain",
      "62201": "Light Rain and Freezing Rain",
      "62221": "Rain and Freezing Rain",
      "62071": "Mostly Clear and Heavy Freezing Rain",
      "62021": "Partly Cloudy and Heavy Freezing Rain",
      "62081": "Mostly Cloudy and Heavy Freezing Rain",
      "62011": "Heavy Freezing Rain",
      "71101": "Mostly Clear and Light Ice Pellets",
      "71111": "Partly Cloudy and Light Ice Pellets",
      "71121": "Mostly Cloudy and Light Ice Pellets",
      "71021": "Light Ice Pellets",
      "71081": "Mostly Clear and Ice Pellets",
      "71071": "Partly Cloudy and Ice Pellets",
      "71091": "Mostly Cloudy and Ice Pellets",
      "70001": "Ice Pellets",
      "71051": "Drizzle and Ice Pellets",
      "71061": "Freezing Rain and Ice Pellets",
      "71151": "Light Rain and Ice Pellets",
      "71171": "Rain and Ice Pellets",
      "71031": "Freezing Rain and Heavy Ice Pellets",
      "71131": "Mostly Clear and Heavy Ice Pellets",
      "71141": "Partly Cloudy and Heavy Ice Pellets",
      "71161": "Mostly Cloudy and Heavy Ice Pellets",
      "71011": "Heavy Ice Pellets",
      "80011": "Mostly Clear and Thunderstorm",
      "80031": "Partly Cloudy and Thunderstorm",
      "80021": "Mostly Cloudy and Thunderstorm",
      "80001": "Thunderstorm"
    }
Updated over 2 years ago

Historical
Data fields for the historical weather API:

Field	Values (Metric, Imperial)	Availability
temperature

The "real" temperature measurement (at 2m)	Celsius [-90,60]
Fahrenheit	F: January 1st 2000 till -7 days.
I: H
A: WW Land
Aggregations: Max, Min, Avg, P95, P50, P5. i.e temperatureMax
P: +
dewPoint

The temperature to which air must be cooled to become saturated with water vapor (at 2m)	Celsius [0,100]
Fahrenheit	F: January 1st 2000 till -7 days.
I: H
A: WW Land
Aggregations: Max, Min, Avg, P95, P50, P5. i.e dewPointMax
P: +
humidity

The concentration of water vapor present in the air	%	F: January 1st 2000 till -7 days.
I: H
A: WW Land
Aggregations: Max, Min, Avg, P95, P50, P5. i.e humidityMax
P: +
windSpeed

The fundamental atmospheric quantity caused by air moving from high to low pressure, usually due to changes in temperature at 10m	m/s
mph	F: January 1st 2000 till -7 days.
I: H
A: WW Land
Aggregations: Max, Min, Avg, P95, P50, P5. i.e windSpeedMax
P: +
windSpeed100

The fundamental atmospheric quantity caused by air moving from high to low pressure, usually due to changes in temperature at 100m	m/s
mph	F: January 1st 2000 till -7 days.
I: H
A: WW Land
Aggregations: Max, Min, Avg, P95, P50, P5. i.e windSpeed100Max
P: +
windDirection

The direction from which it originates, measured in degrees clockwise from due north at 10m	degrees or null	F: January 1st 2000 till -7 days.
I: H
A: WW Land
Aggregations: Avg. i.e windDirectionAvg
P: -
windDirection100

The direction from which it originates, measured in degrees clockwise from due north at 100m	degrees or null	F: January 1st 2000 till -7 days.
I: H
A: WW Land
Aggregations: Avg. i.e windDirection100Avg
P: -
windGust

The maximum brief increase in the speed of the wind, usually less than 20 seconds (at 10m)	m/s
mph	F: January 1st 2000 till -7 days.
I: H
A: WW Land
Aggregations: Max, Min, Avg, P95, P50, P5. i.e windGustMax
P:+
pressureSurfaceLevel

The force exerted against a surface by the weight of the air above the surface (at the surface level)	hPa
inHg	F: January 1st 2000 till -7 days.
I: H
A: WW Land
Aggregations: Max, Min, Avg, P95, P50, P5. i.e pressureSurfaceLevelMax
P: +
totalPrecipitationAccumulation

The total amount of precipitation that has occurred within a given timeframe.

This field will be deprecated. Use precipitationAccumulation instead. For daily sum, use precipitationAccumulationSum	mm
in	F: January 1st 2000 till -7 days.
I: H
A: WW Land
Aggregations: Max, Min, Avg, P95, P50, P5. i.e totalPrecipitationAccumulationMax
P: +
precipitationAccumulation

The amount of precipitation accumulated every hour within a given timeframe.	mm
in	F: January 1st 2000 till -7 days.
I: H
A: WW Land
Aggregations: Sum, Max, Min, Avg, P95, P50, P5. i.e precipitationAccumulationSum
P: +
et0

ET0 (evapotranspiration)
The amount of water extracted from the different soil layers.	mm
in	F: January 1st 2000 till -90 days.
I: H
A: WW Land
Aggregations: Max, Min, Avg, P95, P50, P5. i.e et0Max
P: -
snowAccumulation

The 'liquid water equivalent' of accumulated amount of new snowfall that has occurred over the last hour of the requested time

Will always return hourly data and does not aggregate - eg. if you request snowAccumulationMax over a daily timestep, the max hourly value of that day will be returned, not the accumulation for the whole day.	mm of LWE
in of LWE	F: January 1st 2000 till -7 days.
I: H
A: East Africa Land
Aggregations: Max, Min, Avg, P95, P50, P5. i.e snowAccumulationMax
P: -
potentialEvaporation

An indication of the maximum possible evaporation	mm
in	F: January 1st 2000 till -7 days.
I: H
A: WW Land
Aggregations: Sum, Max, Min, Avg, P95, P50, P5. i.e potentialEvaporationMax
P:+
evaporationFromVegetationTranspiration

The amount of evaporation from vegetation transpiration

Will be deprecated. Use evaporationVegetationTranspiration instead. For daily sum, use evaporationVegetationTranspirationSum	mm
in	F: January 1st 2000 till -90 days.
I: H
A: WW Land
Aggregations: Max, Min, Avg, P95, P50, P5. i.e `evaporationFromVegetationTranspirationMax
P: +
evaporationVegetationTranspiration

The amount of evaporation from vegetation transpiration	mm
in	F: January 1st 2000 till -90 days.
I: H
A: WW Land
Aggregations: Sum, Max, Min, Avg, P95, P50, P5. i.e evaporationVegetationTranspiration
P: +
snowAccumulationLwe

The 'liquid water equivalent' of accumulated amount of new snowfall that has occurred over the last hour of the requested time	mm of LWE
in of LWE	F: January 1st 2000 till -7 days.
I: H
A: WW Land
Aggregations: Max, Min, Avg, P95, P50, P5. i.e snowAccumulationLweMax
P: -
cloudCover

Cloud cover represents the percentage of total cloud cover present occurring at all levels throughout the atmosphere for the reanalysis grid box of which a location/or locations reside.	%	F: January 1st 2000 till -7 days.
I: H
A: WW Land
Aggregations: Max, Min, Avg, P95, P50, P5. i.e cloudCoverMax
P: +
solarGHI

The total amount of shortwave radiation received from above by a surface horizontal to the ground.	W/m^2
Btu/ft2	F: January 1st 2000 till -7 days.
I: H
A: WW
Aggregations: Max, Min, Avg
P: +
solarDNI

The diffuse (i.e., scattered) component of GHI reaching the surface of the earth at each point	W/m^2
Btu/ft2	F: January 1st 2000 till -7 days.
I: H
A: WW
Aggregations: Max, Min, Avg
P: +
solarDHI

The direct component of GHI reaching the surface of the earth at each point	W/m^2
Btu/ft2	F: January 1st 2000 till -7 days.
I: H
A: WW
Aggregations: Max, Min, Avg
P: +
Calculated daily fields:

Field	Values (Metric, Imperial)	Availability
sunriseTime

The daily appearance of the Sun on the horizon due to Earth's rotation	UTC ISO-8601	F: January 1st 2000 till -7 days.
I: H
A: WW Land
P: -
sunsetTime

The daily disappearance of the Sun below the horizon due to Earth's rotation	UTC ISO-8601	F: January 1st 2000 till -7 days.
I: H
A: WW Land
P: -
moonPhase

The shape of the directly sunlit portion of the Moon as viewed from Earth	0: New (0.0625-0.9375)
1: Waxing Crescent (0.0625-0.1875)
2: First Quarter (0.1875-0.3125)
3: Waxing Gibbous (0.3125-0.4375)
4: Full (0.4375-0.5625)
5: Waning Gibbous (0.5625-0.6875)
6: Third Quarter (0.6875-0.8125)
7: Waning Crescent (0.8125-0.9375)	F: January 1st 2000 till -7 days.
I: H
A: WW Land
P: -
Updated 6 months ago

Advanced Precipitation
The Tomorrow.io REST Weather API provides the following information:

Field	Values (Metric, Imperial)	Availability
hailBinary

The binary forecast of precipitation consisting of solid ice that forms inside thunderstorm updrafts	0/1 (boolean value)	F: [-48h, +48h]
I: T I R
A: CA, US
S: ∧ ∨ ~

Pollen
The Tomorrow.io REST Weather API provides the following information:

Field	Values (Metric, Imperial)	Availability
treeIndex

The Tomorrow.io index representing the extent of grains of overall tree pollen or mold spores in a cubic meter of the air	0: None
1: Very low
2: Low
3: Medium
4: High
5: Very High	F: [-7 days, +120 Hours]
I: T R
A: WW
S: ∧ ∨ ~
P: -
treeAcaciaIndex
treeAshIndex
treeBeechIndex
treeBirchIndex
treeCedarIndex
treeCypressIndex
treeElderIndex
treeElmIndex
treeHemlockIndex
treeHickoryIndex
treeJuniperIndex
treeMahoganyIndex
treeMapleIndex
treeMulberryIndex
treeOakIndex
treePineIndex
treeCottonwoodIndex
treeSpruceIndex
treeSycamoreIndex
treeWalnutIndex
treeWillowIndex

The Tomorrow.io index representing the extent of grains of the species pollen or mold spores in a cubic meter of the air	0: None
1: Very low
2: Low
3: Medium
4: High
5: Very High	F: [-7 days, +120 Hours]
I: T R
A: US
S: ∧ ∨ ~
P: -
grassIndex

The Tomorrow.io index representing the extent of grains of overall grass pollen or mold spores in a cubic meter of the air	0: None
1: Very low
2: Low
3: Medium
4: High
5: Very High	F: [-7 days, +120 Hours]
I: T M R
A: WW
S: ∧ ∨ ~
P: -
grassGrassIndex

The Tomorrow.io index representing the extent of grains of the species pollen or mold spores in a cubic meter of the air	0: None
1: Very low
2: Low
3: Medium
4: High
5: Very High	F: [-7 days, +120 Hours]
I: T R
A: US
S: ∧ ∨ ~
P: -
weedIndex

The Tomorrow.io index representing the extent of grains of overall weed pollen or mold spores in a cubic meter of the air	0: None
1: Very low
2: Low
3: Medium
4: High
5: Very High	F: [-7 days, +120 Hours]
I: T M R
A: WW
S: ∧ ∨ ~
P: -
weedRagweedIndex

The Tomorrow.io index representing the extent of grains of the species pollen or mold spores in a cubic meter of the air	0: None
1: Very low
2: Low
3: Medium
4: High
5: Very High	F: [-7 days, +120 Hours]
I: T R
A: US
S: ∧ ∨ ~
P: -

Flood
The Tomorrow.io REST Weather API provides the following fields:

Field	Values (Metric, Imperial)	Availability
floodIndex

Global combined fluvial, pluvial and streamflow flood index based on 10, 50, 100, 500 and 5,000 year return period intervals.

**Hourly flood index is only available for the CONUS region. All hourly values globally outside of CONUS represent the daily value.

The flood index only accounts for terrestrial flooding (fluvial and pluvial) and does not include coastal or storm surge related flooding at the coast or in and around inland bays, estuaries, and large tidal bodies of water.	1 - Minor flash flooding possible: Rivers may go out of their banks briefly

2 - Moderate flash flooding possible: Rivers experiencing flooding conditions with minor impacts to homes and businesses

3 - Significant flash flooding possible: Could lead to disruptions with river flooding also significant enough to threaten homes and businesses

4 - Major river and/or flash flooding possible: Major disruptions to transportation, along with significant impacts to homes/businesses

5 - Catastrophic or extreme river and/or flash flooding probable or likely: Extreme impacts along river networks and low-lying areas	F: [-7 days, +5 days]
I: T, I, M, R
A: WW
S: ∧ ∨ ~ ⧖
P: -
streamFlow

Observed and forecast streamflow.

**Hourly stream flow is only available for the CONUS region. All hourly globally outside of CONUS represent the daily value.	Metric: m^3/s (Cubic meters per second)

Imperial: ft^3/s (Cubic feet per second)	F: [-7 days, +5 days]
I: T, I, M, R
A: WW
S: ∧ ∨ ~ ⧖
P: -
Updated about 1 year ago

Lightning
The Tomorrow.io REST Weather API provides the following information:

Field	Values (Metric, Imperial)	Availability
lightningFlashRateDensity

The “Lightning Flash Rate Density” product is the total cloud-cloud and cloud-ground instantaneous lightning flashes per unit time per unit area.

Important Note:
This product does not explicitly depict discrete lightning strikes, but is based on Numerical Weather Prediction (NWP) parameters and serves as a proxy for where lightning is forecasted to occur by showing flashes per unit time per unit area.	Flashes per square km (km^-2 5-min^-1).

Flashes per square mi (fl mi^2 5-min^-1)	F: [0 hours, +90 hours]
I: T, I, M, R
A: WW
S: ∧ ∨ ~ ⧖
P:+
Lightning Flash Rate Density Heatmap

Lightning Flash Rate Density Legend
Updated about 1 year ago

Maritime
The Tomorrow.io REST Weather API provides the following information:

Field	Values (Metric, Imperial)	Availability
waveSignificantHeight

The height of the combined wind waves and swells.	m
ft	F: [-7 days, +5 days]
I: T I M R
A: MARINE
S: ∧ ∨ ~ ⧖
P:-
waveFromDirection

The direction of the combined wind waves and swells are moving in.	degrees	F: [-7 days, +5 days]
I: T I M R
A: MARINE
S:
P: -
waveMeanPeriod

The frequency of the combined wind waves and swells; or, the space and time between each wave.	seconds	F: [-7 days, +5 days]
I: T M
A: MARINE
S: ∧ ∨ ~ ⧖
P: -
windWaveSignificantHeight

The height of the wind waves.	m
ft	F: [-7 days, +5 days]
I: T I M R
A: MARINE
S: ∧ ∨ ~ ⧖
P: -
windWaveFromDirection

The direction of the combined wind waves and swells are moving in.	degrees	F: [-7 days, +5 days]
I: T I M R
A: MARINE
S:
P: -
windWaveMeanPeriod

The frequency of wind waves; or, the space and time between each wave.	seconds	F: [-7 days, +5 days]
I: T M
A: MARINE
S: ∧ ∨ ~ ⧖
P: -
primarySwellWaveSignificantHeight

The height of the primary swell.	m
ft	F: [-7 days, +5 days]
I: T I M R
A: MARINE
S: ∧ ∨ ~ ⧖
P: -
primarySwellWaveFromDirection

The direction of the primary swells are moving in.	degrees	F: [-7 days, +5 days]
I: T I M R
A: MARINE
S:
P: -
primarySwellWaveMeanPeriod

The frequency of primary swells; or, the space and time between each wave.	seconds	F: [-7 days, +5 days]
I: T M
A: MARINE
S: ∧ ∨ ~ ⧖
P: -
secondarySwellWaveSignificantHeight

The height of the secondary swells.	m
ft	F: [-7 days, +5 days]
I: T I M R
A: MARINE
S: ∧ ∨ ~ ⧖
P: -
secondarySwellWaveFromDirection

The direction of the secondary swells are moving in.	degrees	F: [-7 days, +5 days]
I: T I M R
A: MARINE
S:
P: -
secondarySwellWaveMeanPeriod

The frequency of secondary swells; or, the space and time between each wave.	seconds	F: [-7 days, +5 days]
I: T M
A: MARINE
S: ∧ ∨ ~ ⧖
tertiarySwellWaveSignificantHeight

The height of the tertiary swells.	m
ft	F: [-7 days, +5 days]
I: T M
A: MARINE
S: ∧ ∨ ~ ⧖
P: -
tertiarySwellWaveFromDirection

The direction of the tertiary swells are moving in.	degrees	F: [-7 days, +5 days]
I: T I M R
A: MARINE
S:
P: -
tertiarySwellWaveMeanPeriod

The frequency of tertiary swells; or, the space and time between each wave.	seconds	F: [-7 days, +5 days]
I: T M
A: MARINE
S: ∧ ∨ ~ ⧖
P: -
seaSurfaceTemperature

The temperature of sea water near the surface (including the part under sea-ice, if any).	Celsius [-90,60]
Fahrenheit [-130,140]	F: [-7 days, +5 days]
I: T M
A: MARINE
S: ∧ ∨ ~ ⧖
P: -
seaCurrentSpeed

The velocity of sea water from one location to another driven by the rise and fall of the tides, winds, and the thermohaline circulation.	m/s
mph	F: [-7 days, +5 days]
I: T M
A: MARINE
S: ∧ ∨ ~ ⧖
P: -
seaCurrentDirection

The direction of movement of sea water from one location to another driven by the the rise and fall of the tides, winds, and the thermohaline circulation.	degrees	F: [-7 days, +5 days]
I: T M
A: MARINE
S: ∧ ∨ ~ ⧖
P: -
tides

Amplitude of ocean tide in meters or feet.	m
ft	F: [-7 days, +5 days]
I: T M
A: MARINE
S: ∧ ∨ ~ ⧖
P: -

Solar
The Tomorrow.io REST Weather API provides the following information:

Field	Values (Metric, Imperial)	Availability
solarGHI

The total amount of shortwave radiation received from above by a surface horizontal to the ground	W/m^2
Btu/ft2	F: [-7 days, +15 days]
I: T, I, M, R
A: WW
S: ∧ ∨ ~ ⧖
P: +
solarDNI

The diffuse (i.e., scattered) component of GHI reaching the surface of the earth at each point	W/m^2
Btu/ft2	F: [-7 days, +15 days]
I: T, I, M, R
A: WW
S: ∧ ∨ ~ ⧖
P: +
solarDHI

The direct component of GHI reaching the surface of the earth at each point	W/m^2
Btu/ft2	F: [-7 days, +15 days]
I: T, I, M, R
A: WW
S: ∧ ∨ ~ ⧖
P: +

Access Keys
Permissions
Access to the Tomorrow.io REST Weather API requires a valid access key with the right permissions, allowing it to be used to make requests to specific endpoints.

A default, "private" access token is available on your Dashboard and allows access to all of your resources via the various endpoints. Make sure to keep this key safe on server-side applications.

Multiple API keys can be created by your account manager, to support different development environments or different use cases.

Authentication
Your API keys carry full privileges, so make sure to keep them secure.

Be sure to include a valid API key with every request in order to access the API. Requests not properly authenticated will return a 403 error code.

API key authentication is slightly different from traditional basic authentication, as there is no email or user-name value, There are two ways to authenticate, you can either add the key value in query parameters or in the request header, like so:

Query Parameters
Request Header

curl --request POST \
  --url 'https://api.tomorrow.io/v4/locations?apikey=API_KEY' \
  --header 'content-type: application/json'

Rate Limiting & Tokens
Rate Limiting
According to your plan, you are limited to a certain amount of requests per hour and day to any of the API endpoints. You can check the returned HTTP headers to get your current rate limits status.

When surpassing your rate-limiting you will get a response with a 429 error code.

Getting the remaining rate-limits in the header is currently available only for Enterprise accounts:

Headers	Description
X-RateLimit-Limit-second
X-RateLimit-Limit-day
X-RateLimit-Limit-hour	The maximum number of requests that the API key is permitted to make per second/day/hour.
X-RateLimit-Remaining-second
X-RateLimit-Remaining-day
X-RateLimit-Remaining-hour	The number of requests remaining in the current rate limit window.
*If you need a higher rate limit, please reach out to sales@tomorrow.io.

Tokens
In case you are using the API through the token system, you will see the following headers in the response where {product} is the relevant product that your request deducted tokens from.

Header	Description
X-Tokens-Cost-{product}	The number of tokens the following {product} (i.e historical) request cost.
X-Tokens-Remaining-{product}	The number of tokens remaining for the specific {product}
{product} that are supported:

Historical
On demand events
*In case you have multiple API keys, each one is assigned with its own rate limits and tokens. The balance of each key is deducted with every request made using that specific API key.

Pagination
Requests that return more than a single result will often times be “paged” such that we return a limited number of records for each request. All top-level API resources have bulk fetches via "GET" API methods in order to list Locations, Insights, and Alerts along with their Linked Locations.

As of today, the structure of the request relies on cursor-based pagination such that the list starts at a pre-defined page offset and continues until a pre-defined limit - as resolved for self under links.

The response format is similar such that the collection of the resources is listed under the resource name in the body's data attribute, while the links to traverse to next or prev pages are detailed under links.

Below is an example of a paginated response:

Pagination

{
    "data": {
        "locations": [
            {
                "id": "5ece4524726e55000703833f",
                "name": "North Carolina",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        -79.48081469070964,
                        34.57785716540468
                    ]
                },
                "createdAt": "2020-05-27T10:47:00.229Z",
                "updatedAt": "2020-05-27T10:47:00.229Z"
            }
        ]
    },
    "links": {
    	"self": "http://api.tomorrow.io/v4/locations?offset=3&limit=1",
    	"prev": "http://api.tomorrow.io/v4/locations?offset=2&limit=1",
    	"next": "http://api.tomorrow.io/v4/locations?offset=4&limit=1",
    }
}

Error Handling
Our API uses conventional HTTP response codes to indicate the outcome of an API request. Codes in the 2xx range indicate success, 4xx category indicates errors in the provided information (such as missing or misused parameters or access restrictions) and 5xx codes imply there's an error with our servers (which will rarely happen).

API error messages are returned in JSON format and machine-parsable HTTP status in the header. While the text for an error message and type may change, the code ID and its indication will stay the same.

At Tomorrow.io, we don't fail often - but when we do, we try to fail gracefully. That's why our API makes an incredible effort to always return the best data available and note any warnings that surfaced while doing so. We call these "soft errors" and, much like "hard errors" they will be provided as part of the response.

Hard Errors
Soft Errors

{
    "code": 404001,
    "type": "Not Found",
    "message": "The insight associated with the request could not be found: 38f689d83c264eb0b084ba095f2ea332."
}
4xx Range
400 BAD REQUEST:

To read more on usage limits (rate-limiting) see the Usage Limiting section.

Code	Type	Description
400001	Invalid Body Parameters	The entries provided as body parameters were not valid for the request.
400002	Invalid Query Parameters	The entries provided as query parameters were not valid for the request.
400003	Missing Required Body Parameters	The request is missing some required body parameters.
400004	Missing Required Query Parameters	The request is missing the required query parameters.
400005	Rule Violation	The request violated some logic requirement.
400006	Missing Required Header Parameters	The request is missing some required header parameters.
400007	Invalid Path Parameters	The entries provided as path parameters were not valid for the request.
401 UNAUTHORIZED:

Code	Type	Description
401001	Invalid Key	The method requires authentication, but it was not presented or is invalid.
402 PAYMENT REQUIRED:

Code	Type	Description
402001	Insufficient Tokens	Adding additional tokens is required
403 FORBIDDEN:

Code	Type	Description
403001	Access Denied	The authentication token in use is restricted and cannot access the requested resource.
403002	Account Limit	The plan limit for a resource has been reached.
403003	Forbidden Action	The plan is restricted and cannot perform this action.
404 NOT FOUND:

Code	Type	Description
404001	Not Found	A resource id was not found.
5xx Range
500 INTERNAL SERVER ERROR:

Code	Type	Description
500001	Unknown	Possibly a temporary issue due to downtime. Wait and retry the operation.
503001	Unavailable	Service is currently unavailable, please wait for a while and retry the operation.
Supporting header: Retry-After
Request ID
Each API request has an associated request identifier. You can find this value in the response headers, under X-Correlation-ID.

If you ever need to contact us about a specific request, providing the request identifier will ensure the fastest-possible resolution.

Updated 4 months ago