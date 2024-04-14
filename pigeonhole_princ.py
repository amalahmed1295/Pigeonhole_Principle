## pigeonhole principle: Finding how Many have chosen the same
## subject(proving that at least one subject has the propability of M/N)

# Calculate the appearance of subjects
def calculate_repeated_subjects(subjects):
    # Create a dictionary to store the count of each subject
    subject_count = dict()
    # count to ensure if there is at least one subject has been repeated or not
    count = 0
    # Variable to hold the total sum of the repeated subjects 
    total_freq=0
    
    # Iterate through the subjects chosen by students
    for subject in subjects:
        # If the subject is already in the dictionary, it's a duplicate
        if subject in subject_count:
            subject_count[subject] += 1
        # Initialize count for the second occurrence
            count += 1
        # Otherwise, add it to the dictionary
        else: subject_count[subject] = 1

    # Check if there are at least one repeated subject
    if count > 0:
        print("Repeated subjects and their counts:")
        # Loop over the subjects and their repeatition
        for subject, freq in subject_count.items():
            # if the subject appears more than once
            if freq != 1:
                # Print the subject and its frequency
                print(f"{subject}: {freq}")
                # Total frequency is the total number of students who chosen the same subjects
                total_freq += freq
        return total_freq
    else:
        # No repeated subjects found
        return None


def main():
    # Number of students
    num_students = 10
    # Iteration variable
    i = 0
    
    # The subjects of which students can choose from
    class_subjects = ["qura'an", "islamic", "math", "history", "geography", "reading",
                      "literature and rhetoric", "sciences", "english"]
    print(f"Among the given subjects: {class_subjects}, choose one favorite subject only:")
    # Creat a list to hold students' choices
    subjects = list()
    # Iterate over the number of students
    while i < num_students:
        # Scan student choice from a user
        scan= input(f"Student '{i+1}': ")
        # Change the inputed charecters to lower case to avoid mistakes 
        lowercase_subject = scan.lower()
        # Check if the entered subject is in the subjects list or not
        # If not ask the user to choose again
        if lowercase_subject not in class_subjects:
            print(f"Please choose one of the given subjects only!")
        else:
            # If it is, add it to the subjects list and encrement i by 1
            subjects.append(lowercase_subject)
            i= i+1
    # function call
    repeated_subject = calculate_repeated_subjects(subjects)
    # if there are repeated subjects, use their total frequency
    if repeated_subject is not None:
        print(f"Among {num_students} students, {repeated_subject} students have chosen the same subjects as their favourite subject, which means at least one subject has been chosen twice.")
    # if there are no repeated subjects
    else:
        print(f"Among {num_students} students, no students have chosen the same favorite subject.")

