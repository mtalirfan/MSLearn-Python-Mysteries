# if it's raining cats and dogs
#     find a cat
#     if the cat is hungry
#         find some milk
#         give the milk to the cat
#     else
#         pet the cat until it purrs or scratches you
# else
#     be happy that it's not raining animals
#     frolic outside

# ask the candidate a question
activity = input(
    "\nHow would you like to spend your evening?\n(A) Reading a book\n(B) Attending a party\n"
)

while True:
    # print out which activity they chose
    if activity in ["A", "a"]:
        activity.capitalize()
        print(f"You chose A. Sounds fun!")  # {activity.capitalize()}
    elif activity in ["B", "b"]:
        activity.capitalize()
        print(f"You chose B. Cool!")  # {activity.capitalize()}
    else:
        print(f"You must type A or B, let's just say you like to read.")
        # activity = "A"

    if activity in ["A", "a", "B", "b"]:
        break
    else:
        activity = input(
            "\nHow would you like to spend your evening?\n(A) Reading a book\n(B) Attending a party\n"
        )


# ask the candidate a second question
job = input(
    "\nWhat's your dream job?\n(A) Curator at the Smithsonian\n(B) Running a business\n"
)
while True:

    if job in ["A", "a"]:
        print("Curator, nice choice!")
    elif job in ["B", "b"]:
        print("Running a business? Sounds fun!")
    else:
        print(
            "You must type A or B, let's just say you want to be a curator at the Smithsonian."
        )
        # job = "A"

    if job in ["A", "a", "B", "b"]:
        break
    else:
        job = input(
            "\nWhat's your dream job?\n(A) Curator at the Smithsonian\n(B) Running a business\n"
        )


# ask the candidate a third question
value = input("\nWhat's more important?\n(A) Money\n(B) Love\n")

while True:
    if value in ["A", "a"]:
        print("Money, nice choice!")
    elif value in ["B", "b"]:
        print("Love? Sounds fun!")
    else:
        print("You must type A or B, let's just say money is more important to you.")
        # value = "A"

    if value in ["A", "a", "B", "b"]:
        break
    else:
        value = input("\nWhat's more important?\n(A) Money\n(B) Love\n")

# ask the candidate a fourth question
decade = input("\nWhat's your favorite decade?\n(A) 1910s\n(B) 2010s\n")

while True:
    if decade in ["A", "a"]:
        print("1910s, nice choice!")
    elif decade in ["B", "b"]:
        print("2010s? Sounds fun!")
    else:
        print("You must type A or B, let's just say the 1910s is your favorite decade.")
        # decade = "A"

    if decade in ["A", "a", "B", "b"]:
        break
    else:
        decade = input("\nWhat's your favorite decade?\n(A) 1910s\n(B) 2010s\n")

# ask the candidate a fifth question
travel = input("\nWhat's your favorite way to travel?\n(A) Driving\n(B) Flying\n")

while True:
    if travel in ["A", "a"]:
        print("Driving, nice choice!")
    elif travel in ["B", "b"]:
        print("Flying? Sounds fun!")
    else:
        print(
            "You must type A or B, let's just say your favorite way to travel is by driving."
        )
        # travel = "A"

    if travel in ["A", "a", "B", "b"]:
        break
    else:
        travel = input(
            "\nWhat's your favorite way to travel?\n(A) Driving\n(B) Flying\n"
        )

# print out their choices
print(
    f"\nYou chose {activity.capitalize()}, then {job.capitalize()}, then {value.capitalize()}, then {decade.capitalize()}, then {travel.capitalize()}."
)


# create some variables for scoring
sam_like = 0
cam_like = 0
kai_like = 0
indy_like = 0

# update scoring variables based on the activity choice
if activity in ["A", "a"]:
    sam_like = sam_like + 2
    indy_like = indy_like + 2
    kai_like = kai_like + 2
else:
    cam_like = cam_like + 1
    indy_like = indy_like + 1

# update scoring variables based on the job choice
if job in ["A", "a"]:
    sam_like = sam_like + 2
    indy_like = indy_like + 2
    cam_like = cam_like - 1
else:
    sam_like = sam_like - 1
    kai_like = kai_like + 2
    indy_like = indy_like + 1

# update scoring variables based on the value choice
if value in ["A", "a"]:
    sam_like = sam_like - 1
    kai_like = kai_like + 1
else:
    sam_like = sam_like + 2
    cam_like = cam_like + 2
    indy_like = indy_like + 1

# update scoring variables based on the decade choice
if decade in ["A", "a"]:
    cam_like = cam_like + 2
    sam_like = sam_like + 2
else:
    kai_like = kai_like + 1
    indy_like = indy_like + 2

# update scoring variables based on the travel choice
if travel in ["A", "a"]:
    sam_like = sam_like - 2
    kai_like = kai_like + 1
    indy_like = indy_like - 1
else:
    sam_like = sam_like + 1
    cam_like = cam_like + 1
    kai_like = kai_like - 1

# print the results depending on the score
if sam_like >= 3:
    print("You're most like Sharp-Eyed Sam!")
elif cam_like >= 3:
    print("You're most like Curious Cam!")
elif kai_like >= 3:
    print("You're most like Keen Kai!")
else:
    print("You're most like Inquisitive Indy!")
