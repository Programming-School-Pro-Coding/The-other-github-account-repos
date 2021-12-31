is_sleep = True
want_to_sleep = False

if is_sleep and want_to_sleep:
    print("Go to bed to sleep")
    print(is_sleep)
    print(want_to_sleep)
elif is_sleep and not want_to_sleep:
    print("go to bed to sleep because you sleep")
    print(is_sleep)
    print(want_to_sleep)
elif not is_sleep and want_to_sleep:
    print("go to sleep bacause you want to sleep")
    print(is_sleep)
    print(want_to_sleep)
elif not is_sleep and not want_to_sleep:
    print("Go to play because you not want to sleep")
else:
    print("All condition are false")
