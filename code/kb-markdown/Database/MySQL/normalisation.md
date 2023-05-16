Normalisation = 2NF

Table: booking_location
mobile_number(PK)
vehicle_owner
location_name
complete_address
city_name
pincode

e.g.
[9090909090, "ajay", "adarsh colony", "HN 153", "mzn", "251001"]

Table: specification
vehicle_number (PK)
vehicle_model
vehicle_type
vehicle_category
vehicle_colour
vehicle_image
price_per_hour
fuel_type
mobile_number(foreign key)

e.g.
["up012", "zxi", "car", "Sedan", "black", "img", "100", "petrol", 9090909090] 


