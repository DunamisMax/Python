# Input: Age of the person
age = 25

# Check if the age is less than 13
if age < 13:
    # If true, the person is a child
    print("You are a child.")
# Check if the age is between 13 and 19 (inclusive)
elif 13 <= age <= 19:
    # If true, the person is a teenager
    print("You are a teenager.")
# Check if the age is between 20 and 64 (inclusive)
elif 20 <= age <= 64:
    # If true, the person is an adult
    print("You are an adult.")
# If none of the above conditions are true
else:
    # The person is a senior
    print("You are a senior.")

# Output for age = 25: "You are an adult."
