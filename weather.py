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
    return string_date
    
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
        return max_num, index_num[-1]

    # """Calculates the maximum value in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The maximum value and it's position in the list.
    # """
    # pass


def generate_summary(weather_data):

    #     return f"{total} Day Overview"
    # f"The lowest temperature will be {min_temp}, and will occur on {date}."
    # f"The highest temperature will be {max_temp}, and will occur on {date}."
    # f"The average low this week is {average_low_temp}."
    # f"The average high this week is {average_high_temp}."


    # """Outputs a summary for the given weather data.

    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """
    pass


def generate_daily_summary(weather_data):

    # for item in weather_data:
    #     for 

    # return f"---- {date} ----"
    # f"Minimum Temperature: {min_temp}"
    # f"Maximum Temperature: {max_temp}"


#     """Outputs a daily summary for the given weather data.

#     Args:
#         weather_data: A list of lists, where each sublist represents a day of weather data.
#     Returns:
#         A string containing the summary information.
#     """
    pass
