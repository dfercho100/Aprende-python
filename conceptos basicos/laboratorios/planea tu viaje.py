distance_mi= 5
is_raining= True  
has_bike= True
has_car= False 
has_ride_share_app = True 
if not distance_mi:
    print(False)
elif distance_mi <= 1:
        if not is_raining:
            print(True) 
        else:
            print(False)
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
else:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False) 
# salio False, lo que es correcto, ya que la distancia es de 5 millas, y aunque tiene una app de ride share, esta lloviendo, por lo que no es una buena opcion para viajar. un carro seria una mejor opcion, pero no tiene uno.