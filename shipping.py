weight = 32

print ("Ground Shipping:")
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight >= 2 and weight <= 6:
  cost_ground = weight * 2 + 20
elif weight >= 6 and weight <= 10:
  cost_ground = weight * 4 + 20
elif weight >= 10:
  cost_ground = weight * 4.75 + 20
print(cost_ground)

print("")

print ("Premium Ground Shipping:")
print (125)

print("")

print ("Drone Shipping:")
if weight <= 2:
  cost_drone = weight * 4.5 + 20
elif weight >= 2 and weight <= 6:
  cost_drone = weight * 9 + 20
elif weight >= 6 and weight <= 10:
  cost_drone = weight * 12 + 20
elif weight >= 10:
  cost_drone = weight * 14.25 + 20
print(cost_drone)