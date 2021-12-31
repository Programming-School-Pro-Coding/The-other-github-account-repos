def Weather():
          is_hot = True
          is_cold = False
          if is_hot == True:
                    print("Go to drinking water", "because the weather is hot")
          elif is_cold == True:
                    print("Wear a heavy clothes")
          elif is_hot == False:
                    print("The Weather is beautiful")
          elif is_cold == False:
                    print("The Weather is pretty")
          elif is_cold == False and is_hot == False:
                    is_cold = True
                    is_hot = False
          else:
                    print("😀😀")