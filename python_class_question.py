from pathlib import Path
from pandas import read_html
import time
from .database_connection import database_connection
import random


BASE_DIR = Path(__file__).resolve().parent # base directory for this application

def extract_html(file):
    html_file = file
    html_tables = read_html(html_file)  # Read the HTML file and extract all tables
    df = html_tables[0]  # Extract the table in the HTML file

    records = df.to_dict(orient="records")  # Convert dataframe rows into a list of dictionaries
    all_colours = []
    
    # Loop through each row and extract the colours
    for row in records:
        # Split comma-separated colours and strip whitespace
        colour = [colour.strip() for colour in row["COLOURS"].split(",")]
        all_colours += colour  # Add extracted colours to list
    
    return all_colours


def colour_counts(all_colours: list):
    """Return a dictionary with colour frequencies."""
    colour_count = {}
    for colour in all_colours:
        if colour in colour_count:
            colour_count[colour] += 1
        else:
            colour_count[colour] = 1
    return colour_count


def colours_mode(colours: dict):
    """Return the highest colour frequency (mode)."""
    if not colours:
        return "Error processing colour table"
    
    # Start with first frequency value
    highest = next(iter(colours.values()))
    
    # Find the maximum count
    for value in colours.values():
        if highest < value:
            highest = value
    
    return highest


def colours_median(colours: list):
    """Return the index position of the median element."""
    len_of_colours = len(colours)
    
    # If odd number of items middle index devide the  number by 2
    if len_of_colours % 2 == 1:
        median = len_of_colours // 2
    else:
        # If even choose the lower middle index
        median = (len_of_colours // 2 - 1)
    return median


def calculate_variance(colour_counts: dict):
    """Calculate variance of colour frequencies."""
    counts = colour_counts.values()
    mean_count = sum(list(counts)) / len(counts)

    # Only the last variance value is returned here
    for count in counts:
        variance = (count - mean_count) ** 2 / len(counts)
    return variance


def save_to_db(query, colours):
    """Insert each colour and its count into the database."""
    values = colours
    
    for key, value in values.items():
        connection = database_connection()  # Connect to DB
        cursor = connection.cursor()

        try:
            insert_values = (key, value)
            cursor.execute(query, insert_values)  # Execute insert query
            connection.commit()  # Save changes

        except Exception as e:
            return "Error occurred while inserting data"
        
        finally:
            connection.close()  # Close DB connection
            cursor.close()
    

def search(list_of_numbers):
    """Search for a number and return index if found."""
    prompt = int(input("Enter a number: "))

    if prompt in list_of_numbers:
        return f"Number found at location: {list_of_numbers.index(prompt)}"
    
    # Recursively repeat if not found
    return search(list_of_numbers)


def random_number():
    """Generate a 4-bit random binary number and convert to base 10."""
    random_num = ""
    for _ in range(4):
        random_num += str(random.randint(0, 1))  # Random bit (0 or 1)
    
    base_10 = int(random_num, 2)  # Convert binary string to decimal
    
    return f"Base 10 of {random_num} = {base_10}"


def sum_fibonacci(number):
    """Return Fibonacci sequence up to 'number' and its sum."""
    if number == 0:
        return [0]
    if number == 1:
        return [0, 1]
    
    initail_fibo = [0, 1]
    
    # Loop until Fibonacci number reaches the number
    for i in range(initail_fibo[-1], number):
        next_number = initail_fibo[-1] + initail_fibo[-2]
        initail_fibo.append(next_number)
    
    return initail_fibo, sum(initail_fibo)



if __name__ == "__main__":
    # Calculate Fibonacci
    fibonacci_sequence = sum_fibonacci(50)
    fibonacci = fibonacci_sequence[0]
    sum_of_fibonacci = fibonacci_sequence[1]
    print(f"The total sum of the first 50 fibonacci = {sum_of_fibonacci}. \n fibonacci = {fibonacci}")

    # Extract table from HTML file
    file_name = BASE_DIR / "python_class_question.html"
    print(f"Extracting tables from {file_name} \n")
    time.sleep(2)
    tables = extract_html(file_name)
   
    # Count colour frequencies
    colour_counts = colour_counts(tables)

    # Mean, median, and mode
    max_colour = colours_mode(colour_counts)
    median_colour = tables[colours_median(tables)]

    # Colour variance
    variance_colours = calculate_variance(colour_counts)

    # Get most frequent colour
    for key, value in colour_counts.items():
        if value == max_colour:
            colour = key

    print(f"The most worn cloth for the week is {colour}: Counts = {max_colour} times")
    print(f"Median colour = {median_colour}")
    print(f"Variance: {variance_colours}")

    # Number search within a sequence
    numbers = [2, 4, 5, 7, 8, 3, 0, 9]
    print(search(list_of_numbers=numbers))

    # Convert random number to base 10
    print(random_number())
    
    # Populate PostgreSQL database
    query = "INSERT INTO colours_table (colour, frequencies) VALUES(%s, %s)"
    print(save_to_db(query=query, colours=colour_counts))
