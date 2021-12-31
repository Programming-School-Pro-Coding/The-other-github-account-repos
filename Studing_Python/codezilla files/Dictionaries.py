convert_Month = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "Ma" : "May",
    "Ju" : "June",
    "J" : "July",
    "Aug" : "August",
    "Sep" : "Septamper",
    "Oct" : "Octoper",
    "Nov" : "November",
    "Dec" : "December",
    0 : 1,
    bool : True,
    list : ["Mohamed", "Mohamed born since 2009", 1, True]
}
#print(convert_Month["Jan"])
#print(convert_Month.get("Feb", "The value does not exist"))
#print(convert_Month.get(0, "The value does not exist"))
print(convert_Month.get(list, "The value does not exist"))