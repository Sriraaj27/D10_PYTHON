are_friends = input("Are users friends? (Yes/No): ")

if are_friends == "yes":
    print("Both Users can Exchange Messages")
else:
    acc_public = input("Are users accounts public? (Yes/No): ")
    if acc_public == "yes":
        print("Account is Public, Users can Exchange Messages")
    else:
        print("Account is Private, Users cannot Exchange Messages")
