from django.db import models

# Create your models here.


















































# class Airport(models.Model):
#     airport_code = models.CharField(max_length=3, min_length=3)
#     iso_country_code = models.CharField(max_length=2, min_length=2)
#     #localization
#     latitude = models.IntegerField()
#     longitude = models.IntegerField()

# class City(models.Model):
#     #id = models.TextField()
#     iso_country_code = models.CharField(max_length=2, min_length=2)
#     primary_name = models.TextField()
#     admin_district = models.TextField()
#     # localization
#     latitude = models.IntegerField()
#     longitude = models.IntegerField()

# class HotelSearchResponse(models.Model):
#     hotel_id = models.TextField() # A SimpleNights Hotel ID
#     checkin_date = models.TextField(blank=False) # Checkin date
#     checkout_date = models.TextField(blank=False) # Checkout date

#     # room_types = 
#     # rate_plans = 
#     # room_rates = 
#     # hotel_details = 
#     # error

# class HotelSearchRequest(models.Model):
#     hotel_id = models.TextField(blank=False) # Simplenight Hotel ID
#     checkin_date = models.TextField(blank=False) # The checkin date
#     checkout_date = models.TextField() # The checkout date
#     # occupancy = models.ForeignKeyField(Occupancy, on_delete=models.CASCADE)
#     language = models.charField(max_length=2, min_length=2) # Optional. ISO-formatted 2-character language code for hotel details
#     currency = models.TextField() # Optional. ISO-format 3-character currency code

# class Occupancy(models.Model):
#     # description: The number of adults and children
#     adults = models.IntegerField(blank=False) # The number of adults per room
#     children = models.IntegerField(blank=False) # The number of childeren per room

# class Capacity(models.Model):

#     # description: The number of adults and children
#     adults = models.IntegerField(blank=False) # The number of adults per room
#     children = models.IntegerField(blank=False) # The number of childeren per room

# class RoomType(models.Model):
#     # description: The types of physical rooms available
#     code = models.TextField(blank=False) # The unique ID for the room type
#     name = models.TextField(blank=False) # The descriptive name for the room type
#     description = models.TextField() # The long description of the room type


#     # basic_amenities = 
#     # photos =
#     # capacity = 
#     # bed_types = 
#     # unstructured_policies	string
#         # Textual description of hotel rate policies

# # class Amenity

# class Photo(models.Model):
#     url = models.TextField(blank=False) # Hotel image URL. Always in HTTPS.
#     type = models.TextField(blank=False) # The type of hotel image being returned

# class BedTypes(models.Model):
#     # description: The number and type of beds available in the room
#     total_beds = models.IntegerField() # The total number of beds in the room
#     king_beds = models.IntegerField()  # The total number of king-sized beds in the room
#     queen_beds = models.IntegerField() # The total number of queen-sized beds in the room
#     double_beds = models.IntegerField() # The total number of double beds in the room
#     single_or_twin_beds = models.IntegerField() # The total number of single-sized beds in the room
#     murphy_beds = models.IntegerField() # The total number of Murphy-style beds in the room
#     sofa_beds = models.IntegerField() # The total number of convertible sofa beds in the room
#     bunk_beds = models.IntegerField() # The total number of bunk beds in the room
#     other_beds = models.IntegerField() # Any other type of beds in the room

# class RatePlan(models.Mode):
#     # description: Rate plans corresponding to specific hotel bundles and services
#     code = models.TextField(blank=False) # The unique ID for the room rate plan
#     name = models.TextField(blank=False) # Textual description of the rate plan
#     description = models.TextField() # Long description of the rate plan
#     # basic_amenities
#     # cancellation_policy
#     # unstructured_policies                 # Textual description of hotel policies
# class CancellationPolicy(models.Model):
#     # summary = CancellationSummary
#     cancellation_deadline = models.TextField()
#     unstructed_policy = models.TextField() # Textual description of the cancellation policy

# # class CancellationSummary

# class RoomRate(models.Model):
#     code = models.TextField(blank=False) # The unique identifier for a room rate plan


#     room_type_code = models.TextField(blank=False) # The associated unique identifer for a room type
#     rate_plan_code = models.TextField(blank=False) # The associated unique identifier for a rate plan
#     # maximum_allowable_occupancy
#     # maximum_allowable_occupancy	Capacity{...}
#     # total_price_at_booking	Price{...}
#     # total_price_at_checkout	Price{...}
#     # cancellation_rules	[...]
#     # unstructured_policies	[...]
#     room_count = models.IntegerField() # The number of rooms that can be booked for this room rate

# class Price(models.Model):
#     currency = models.CharField(max_length=3, min_length=3, blank=False) # ISO-format 3-character currency code
#     amount = models.FloatField(blank=False) # The Price

# class HotelDetails(models.Model):
#     name = models.TextField(blank=False) # Name of hotel
#     # address = models.
#     # geolocation = 
#     phone_number = models.TextField() # Hotel phone number
#     email = models.TextField() # The hotel email address
#     homepage_url = models.TextField() # URL to the website's homepage
#     # policies
#     # photos

# class GeoLocation(models.Model):

#     latitude = models.IntegerField(blank=False)
#     longitude = models.IntegerField(blank=False)

# class Address(models.Model):

#     address1 = models.TextField(blank=False) # The first line of the address. Required.
#     address2 = models.TextField() # The second line of the address. Optional.
#     address3 = models.TextField() # The third line of the address. Optional.
#     city = models.TextField(blank=False) # The city of the hotel
#     province = models.TextField(blank=False) # The administrative region of the city
#     postal_code = models.TextField(blank=False) # The postal code of the hotel
#     country = models.TextFields(blank=False) # ISO-format two-character country code


# class HotelPolicies(models.Model):
#     checkin_time = models.TextField() # The earliest checkin time
#     checkout_time = models.TextField() # The latest checkout time
#     max_child_age = models.IntegerField() # The maximum age a guest is considered a child

# class AvailabilityError(models.Model):
#     # type= Avai
#     message = models.TextField(blank=False)

# class AvailabilityErrorType(models.Model):
#     pass

# class CardType(models.Model):
#     # description: Card network of the payment card AX = American Express DC = Diner's Club DS = Discovery JC = JCB MC = Mastercard VI = Visa

# class BookingRequest(models.Model):
#     api_version = models.IntegerField(blank=False) # The API version of this booking request message
#     transaction_id = models.TextField(blank=False) # Unique ID for this booking transaction
#     # tracking
#     hotel_id = models.TextField() # The SimpleNight Hotel ID of the property being booked
#     checkin = models.TextField() # The start date of the hotel booking
#     checkout = models.TextField() # The end date of the hotel booking
#     ip_address = models.TextField() # The end user IP address, for tracking purposes. Optional.
#     language = models.TextField(blank=False) # The language of the request, for hotel details and property descriptions
#     # customer
#     # traveler
#     # room_rate
#     # payment

# class Tracking(models.Model):
#     # description: Campaign tracking information
#     campaign_id = models.TextField() # Marketing campaign ID


#     pos_url = models.TextField() # Point of Sale deeplink URL

# class Customer(models.Model):
#     # description: The lead traveler, and booking owner
#     first_name = models.TextField(blank=False) # Booking owner given name
#     last_name = models.TextField(blank=False) # Booking owner family name
#     phone_number = models.TextField(blank=False) # Booking owner primary phone contact
#     email = models.TextField(blank=False) # Booking owner primary email address
#     country = models.CharField(max_length=2, min_length=2,blank=False) # Two character ISO country code of the lead traveler



# class Traveler(models.Model):
#     # description: The lead traveler of the booking	
#     first_name = models.TextField(blank=False) # Lead traveler given name
#     last_name = models.TextField(blank=False) # Lead traveler last name
#     # Occupancy

# class Payment(models.Model):
#     # description: Payment information for the booking
#     # payment_card_parameters
#     # billing_address

# class payment_card_parameters(models.Model):
#     # description: The payment card used for this booking
#     # card_type = 
#     card_number = models.TextField(blank=False) # Payment card number
#     cardholder_name = models.TextField(blank=False) # The name of the payment card holder
#     expiration_month = models.TextField(blank=False) # Two letter month of the card expiration date
#     expiration_date = models.TextField() # Four letter year of the card expiration date
#     cvv = models.TextField(blank=False) # The payment card verification code

# class BookingResponse(models.Model):
#     # description: The booking response for a successful booking
#     api_version = models.IntegerField(blank=False) # The API version of the booking response
#     transaction_id = models.TextField(blank=False) # Echoed transaction_id response
#     # status = 
#     # reservation = 

# class Status(model.Model):
#     # description: Success/Failure indicator for a booking

# class Reservation(models.Model):
#     # description: Confirmation record of the booked itinerary
#     # locator
#     # hotel
#     hotel_id = models.TextField(blank=False) # Echoed Hotel ID of the booked property
#     checkin = models.TextField(blank=False) # Echoed checkin date
#     checkout = models.TextField(blank=False) # Echoed checkout date

#     # customer*	Customer{...}
#     # traveler*	Traveler{...}
#     # room_rate*	RoomRate{...}

# class Locator(model.Model):
#     # description: The record locator
#     id = models.TextField(blank=False) # booking reference
#     pin = models.TextField() # PIN code used to access the reservation






 



 








