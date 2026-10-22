#پروژه سوم
#دفترچه مخاطبین واقعی +حذف و اضافه و نمایش مخاطبان و سرچ 
#با exit  خارج میشه

def contacts():
    name=input("name:")
    number=input("number:")
    while not number.isdigit():
        print("invalid number")
        number=input("number:")
    print("valid number")
    phone={
        "name": name ,
        "number": number
    }
    return phone
all_contacts={}
i=int(input("how many contacts do you have ? >>>"))

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

    elif menu.lower()=="exit":
        break
    else:
        print("not found")