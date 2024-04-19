def find_favorite_bond_actor(year_of_birth):
    # Define the tenure of each Bond actor
    roger_moore = (1973, 1986)
    timothy_dalton = (1987, 1994)
    pierce_brosnan = (1995, 2005)
    sean_connery = (1962, 1973)  # Assuming you meant Sean Connery as the first Bond
    daniel_craig = (2006, 2021)

    # Calculate the year the individual turned 18
    year_turned_18 = year_of_birth + 18

    # Determine the Bond actor based on the year they turned 18
    if roger_moore[0] <= year_turned_18 <= roger_moore[1]:
        return "Roger Moore"
    elif sean_connery[0] <= year_turned_18 <= sean_connery[1]:
        return "Sean Connery"
    elif timothy_dalton[0] <= year_turned_18 <= timothy_dalton[1]:
        return "Timothy Dalton"
    elif pierce_brosnan[0] <= year_turned_18 <= pierce_brosnan[1]:
        return "Pierce Brosnan"
    elif daniel_craig[0] <= year_turned_18 <= daniel_craig[1]:
        return "Daniel Craig"
    else:
        return "No match found - the individual's 18th year does not align with the tenure of any known Bond actor."

# Example usage:
# If a person was born in 1975, their favorite Bond actor would be determined as follows:
year_of_birth=int(input("please enter your birth year: " ))
favorite_bond_actor = find_favorite_bond_actor(year_of_birth)
print(f"The favorite Bond actor for someone born in {year_of_birth} is {favorite_bond_actor}.")