def calculate_final_score_needed():
    # Prompt user for inputs
    desired_grade = input("Enter desired grade> ")
    min_average_required = float(input("Enter minimum average required> "))
    current_average = float(input("Enter current average in course> "))
    final_weight = float(input("Enter how much the final counts as a percentage of the course grade> "))

    # Calculate the score needed on the final exam
    final_weight_decimal = final_weight / 100
    score_needed = (min_average_required - (1 - final_weight_decimal) * current_average) / final_weight_decimal

    # Output the result
    print(f"You need a score of {score_needed:.2f} on the final to get a {desired_grade}.")

# Run the program
calculate_final_score_needed()
AW
