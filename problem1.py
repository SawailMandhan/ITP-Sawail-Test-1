def clinic():
  #print receipt of the patient using python programming
    print("Melanie Dental Clinic")
    name=input("Enter patient's name: ")
    cleaning=input("Was cleaning performed (y/n): ")
    cavity=input("Was cavity-filling performed (y/n): ")
    xray=input("Was X-Ray performed (y/n): ")
    total=0
    #final payement will according to services taken by patient
    if cleaning.lower()=="y":
        total+=60
    if cavity.lower()=="y":
        total+=200
    if xray.lower()=="y":
        total+=100
    if total>300:
        total=total*90/100
    elif total>200:
        total=total*95/100  
      #print 15% tax will also added in the final payment
    tax=15/100*total
    fulltotal=total+tax
    print("\n")
    print("Melanie Dental Clinic")