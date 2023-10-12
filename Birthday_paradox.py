def count_shared_birthdays(birthday_list):

    birthday_counts = {}

    for birthday in birthday_list:
        if birthday in birthday_counts:
            birthday_counts[birthday] += 1
        else:
            birthday_counts[birthday] = 1
            
    shared_birthdays = {}
    for birthday, count in birthday_counts.items():
        if count > 1:
            shared_birthdays[birthday] = count
    return shared_birthdays

def main():
    while True:
        num_people = int(input("Enter the number of people (0 to exit): "))
        
        if num_people == 0:
            print("Exiting the program.")
            break 
        
        birthday_list = []
        for i in range(num_people):
            birthday = int(input(f"Enter the birthday for person {i + 1} (1-365): "))
            birthday_list.append(birthday)
        
        shared_birthdays = count_shared_birthdays(birthday_list)
        
        if shared_birthdays:
            print("Shared birthdays:")
            for birthday, count in shared_birthdays.items():
                print(f"Birthday {birthday}: {count} people")
        else:
            print("No shared birthdays in the group.")

if __name__ == "__main__":
    main()
