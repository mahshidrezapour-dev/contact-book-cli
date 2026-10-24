#پروژه سوم
#دفترچه مخاطبین واقعی +حذف و اضافه و نمایش مخاطبان و سرچ 
#با exit  خارج میشه

def contacts():
    while True:
        name=input("name:").strip()
        if name:
            break
        print("name cannot be empty")
    while True:
        number=input("number:").strip()
        if number.isdigit() and 7<= len(number) <= 11:
            break
        print("please enter a valid phone number")
    phone={
        "name": name ,
        "number": number
    }
    return phone
all_contacts={}
while True:
    try:
        i=int(input("how many contacts do you have ? >>>"))
        if i <0:
            print("number of contacts cannot be negative")
        else:
            break
    except ValueError:
        print("please enter a valid integer")

for count in range(i):
    person=contacts()
    
    while person["name"] in all_contacts:
        print("This contact already exists. Enter a different name.")
        person = contacts()
    all_contacts[person["name"]] = person
print(all_contacts)
    
menu=""
while menu.lower()!="exit":
    menu=input("what do you want to do ? ")
    if menu.lower()=="show contacts":
        print(all_contacts)
    elif menu.lower()=="delete":
        a=input("which contact? >>")
        if a in all_contacts:
            del all_contacts[a]
            print ("successfully deleted")
        else:
            print("not found")

    elif menu.lower()=="add":
        print("adding the contact...")
        person=contacts()
        while person["name"] in all_contacts:
            print("This contact already exists. Enter a different name.")
            person = contacts()

        all_contacts[person["name"]] = person
        print("Successfully added")
        
    elif menu.lower()=="search":
        place=input("who are you searching for >>>")
        if place in all_contacts:
            print(all_contacts[place]["number"])
        else:
            print("not found")
    else:
        print("not found")
