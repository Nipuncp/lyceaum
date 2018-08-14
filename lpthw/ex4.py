#Initialize no. of cars = 100
cars = 100
#Initialize space in car as 4
space_in_a_car = 4.0
#Initialize drivers
drivers = 30
#Initialize passengers
passengers = 90
#compute undriven cars
cars_not_driven = cars - drivers
#Initialize cars driven as no.of drivers
cars_driven = drivers
#Initialise car pool capacity
car_pool_capacity = cars_driven * space_in_a_car
#Initialise average passengers per car
average_passengers_per_car = passengers / cars_driven

#Print all the data into terminal
print ("There are", cars, "available")
print ("THere are only", drivers, "available")
print ("There will be", cars_not_driven,"empty cars today")
print ("We can transport", car_pool_capacity, "people today")
print ("We have", passengers, "to car pool today")
print ("We need to put ",average_passengers_per_car,"average passengers per car")
