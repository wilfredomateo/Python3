from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Define calculate_shipping_cost() here:
def calculate_shipping_cost(from_coords, to_coords, shipping_type='Overnight'):
  
  #Unpack the tuples
  from_lat, from_long = from_coords
  to_lat, to_long = to_coords
  distance = get_distance(from_lat, from_long, to_lat, to_long)

  #Another way to call get_distance without having to unpack the tuple
  #distance = get_distance(*from_coords, *to_coords)

  #Get shipping rate
  shipping_rate = SHIPPING_PRICES[shipping_type]

  #Calculate price
  price = distance * shipping_rate

  #Return the formatted price
  return format_price(price)

# Test the function by calling 
test_function(calculate_shipping_cost)

# Define calculate_driver_cost() here


# Test the function by calling 
# test_function(calculate_driver_cost)

# Define calculate_money_made() here


# Test the function by calling 
# test_function(calculate_money_made)
