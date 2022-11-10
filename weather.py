import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    # """Takes a temperature and returns it in string format with the degrees
    #     and celcius symbols.

    # Args:
    #     temp: A string representing a temperature.
    # Returns:
    #     A string contain the temperature and "degrees celcius."
    # """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    iso_string_format = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    string_date = iso_string_format.strftime("%A %d %B %Y")
    return str(string_date)
    
    # """Converts and ISO formatted date into a human readable format.

    # Args:
    #     iso_string: An ISO date string..
    # Returns:
    #     A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    # """
    pass


def convert_f_to_c(temp_in_farenheit):
    temp_in_farenheit = (float(temp_in_farenheit))
    temp_in_celcius = (float(((temp_in_farenheit - 32)*5)/9))
    rounded_temp = round(temp_in_celcius,1)
    return rounded_temp

    # """Converts an temperature from farenheit to celcius.

    # Args:
    #     temp_in_farenheit: float representing a temperature.
    # Returns:
    #     A float representing a temperature in degrees celcius, rounded to 1dp.
    # """
    # pass


def calculate_mean(weather_data):
    total = 0
    how_many = 0
    for num in weather_data:
        total += float(num)
        how_many += 1
    mean = total/how_many
    return mean

    # """Calculates the mean value from a list of numbers.

    # Args:
    #     weather_data: a list of numbers.
    # Returns:
    #     A float representing the mean value.
    # """
    # pass


def load_data_from_csv(csv_file):
    with open(csv_file, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file) 
        headings = next(reader)
        csv_list = []
        for line in reader:
            csv_list.append(line)
        return csv_list

    # with open(csv_file, encoding="utf-8") as csv_file:
    #     reader = csv.reader(csv_file)
    #     headings = next(reader)
    #     csv_list = []
    #     for line in reader:
    #         line[1] = int(line[1])
    #         csv_list.append(line)
    #     return csv_list

    # """Reads a csv file and stores the data in a list.

    # Args:
    #     csv_file: a string representing the file path to a csv file.
    # Returns:
    #     A list of lists, where each sublist is a (non-empty) line in the csv file.
    # """
    # pass


def find_min(weather_data):
    if weather_data == []:
        return ()
    else: 
        weather_data = [float(num) for num in weather_data]
        min_num = min(weather_data)
        index_num = [index for index, num in enumerate(weather_data) if num == min_num]
        return min_num, index_num[-1]

    # """Calculates the minimum value in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The minium value and it's position in the list.
    # """
    # pass


def find_max(weather_data):
    if weather_data == []:
        return ()
    else: 
        weather_data = [float(num) for num in weather_data]
        max_num = max(weather_data)
        index_num = [index for index, num in enumerate(weather_data) if num == max_num]
        return float(max_num), index_num[-1]

    # """Calculates the maximum value in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The maximum value and it's position in the list.
    # """
    # pass


def generate_summary(weather_data):
    total = len(weather_data)
    min_temps = []
    max_temps = []
    iso_date = ''

    for item in weather_data:
        min_temp = item[1]
        min_temps.append(min_temp) 
        max_temp = item[2]
        max_temps.append(max_temp)
        
    min_temp_and_index = find_min(min_temps)
    max_temp_and_index = find_max(max_temps)
    
    average_low_temp_f = calculate_mean(min_temps)
    average_high_temp_f = calculate_mean(max_temps)
    average_low_c = convert_f_to_c(average_low_temp_f)
    average_high_c = convert_f_to_c(average_high_temp_f)
        
    summary_of_weather = f"{total} Day Overview\n   The lowest temperature will be {min_temp_and_index}, and will occur on Sunday.\n    The highest temperature will be {max_temp_and_index}, and will occur on Monday.\n    The average low this week is {average_low_c}.\n   The average high this week is {average_high_c}."
    
    return summary_of_weather

    # ["2021-07-02T07:00:00+08:00", 49, 67],
    # ["2021-07-03T07:00:00+08:00", 57, 68],
    # ["2021-07-04T07:00:00+08:00", 56, 62],
    # ["2021-07-05T07:00:00+08:00", 55, 61],
    # ["2021-07-06T07:00:00+08:00", 53, 62]

    # """Outputs a summary for the given weather data.

    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """
    pass


def generate_daily_summary(weather_data):

    # for item in weather_data:
         

    # daily_summary = f"---- {date} ----\n    Minimum Temperature: {min_temp}\n   Maximum Temperature: {max_temp}"
    # return daily_summary

#     """Outputs a daily summary for the given weather data.

#     Args:
#         weather_data: A list of lists, where each sublist represents a day of weather data.
#     Returns:
#         A string containing the summary information.
#     """
    pass
