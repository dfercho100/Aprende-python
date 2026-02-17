distance_mi = 8
is_raining = False
has_bike = False
has_car = True
has_ride_share_app = False

if not distance_mi:
    print("False")

if distance_mi <= 1 and not is_raining:
    print("True")
elif (distance_mi > 1 or distance_mi <= 6) and not is_raining and has_bike:
    print("True")
elif distance_mi > 6 and (not has_car or not has_ride_share_app):
    print("True")
else:
    print("False")