import json

def find_cheapest_room(data):
    """
    Finds the cheapest room (lowest shown price) in the provided JSON data.

    Args:
        data: The JSON data containing hotel information.

    Returns:
        A dictionary containing information about the cheapest room:
            - room_type: The name of the cheapest room type.
            - price: The cheapest shown price (float).
            - number_of_guests: The number of guests the room accommodates (int).
    """

    cheapest_price = float('inf')  # Initialize with a high value
    cheapest_room = None

    for room_type, price in data['assignment_results'][0]['shown_price'].items():
        price = float(price)  # Convert price string to float
        if price < cheapest_price:
            cheapest_price = price
            cheapest_room = {
                'room_type': room_type,
                'price': price,
                'number_of_guests': data['assignment_results'][0]['number_of_guests']
            }

    return cheapest_room

def calculate_total_price(data):
    """
    Calculates the total price (net price + taxes) for all rooms in the data.

    Args:
        data: The JSON data containing hotel information.

    Returns:
        A list of dictionaries, where each dictionary represents a room and contains:
            - room_type: The name of the room type.
            - net_price: The net price of the room (float).
            - tax: The total amount of taxes for the room (float).
            - total_price: The total price (net price + taxes) for the room (float).
    """

    room_prices = []
    taxes_data = json.loads(data['assignment_results'][0]['ext_data']['taxes'])
    total_tax = float(taxes_data['TAX']) + float(taxes_data['City tax'])

    for room_type, net_price in data['assignment_results'][0]['net_price'].items():
        net_price = float(net_price)
        room_prices.append({
            'room_type': room_type,
            'net_price': net_price,
            'tax': total_tax,
            'total_price': net_price + total_tax
        })

    return room_prices

def write_output_to_json(data, filename):
    """
    Writes the analysis results to a JSON file.

    Args:
        data: A dictionary containing the analysis results (cheapest room and total prices).
        filename: The name of the output JSON file.
    """

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    # Assuming the JSON data is loaded from a file (replace with your actual loading logic)
    with open('hotel_data.json', 'r') as f:
        data = json.load(f)

    cheapest_room = find_cheapest_room(data)
    total_prices = calculate_total_price(data)

    analysis_results = {
        'cheapest_room': cheapest_room,
        'total_prices': total_prices
    }

    write_output_to_json(analysis_results, 'analysis_results.json')