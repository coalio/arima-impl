import os
import dateobject as d
from wwo_hist import retrieve_hist_data

# Set working directory to the directory of this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Set API key (read from "./wwo.key")
with open("wwo.key", "r") as f:
    key = f.read().strip()

# Set parameters
frequency = 1 
# The start date should be current date minus 1 month
start_date = str(d.current_date() - d.month(1))
end_date = str(d.current_date())
location_list = ["managua"]
api_key = key 
print("Start date: " + start_date)
print("End date: " + end_date)
hist_weather_data = retrieve_hist_data(api_key,
                                       location_list,
                                       start_date,
                                       end_date,
                                       frequency,
                                       location_label = False,
                                       export_csv = True,
                                       store_df = True)
