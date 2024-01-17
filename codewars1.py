def order_food(dev_list):
    # Initialize an empty dictionary to store the count of each food option
    food_counts = {}

    # Iterate through the list of developers
    for dev in dev_list:
        # Get the meal option selected by the developer
        meal_option = dev['meal']

        # Update the count in the dictionary
        food_counts[meal_option] = food_counts.get(meal_option, 0) + 1

    return food_counts

# Example usage:
list1 = [
    { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C', 'meal': 'vegetarian' },
    { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript', 'meal': 'standard' },
    { 'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby', 'meal': 'vegan' },
    { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C', 'meal': 'vegetarian' },
]

result = order_food(list1)
print(result)