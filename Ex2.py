def calculate_average(score1, score2, score3):
    return sum((score1, score2, score3)) / 3

def drop_lowest(score1, score2, score3):
    return (sum((score1, score2, score3)) - min(score1, score2, score3))/2

def calculate_weighted(assignments, midterm, final):
     return assignments * 0.3 + midterm * 0.3 + final * 0.4

def determine_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >=70:
        return "C"
    elif average >=60:
        return "D"
    else:
        return "F"
def needs_improvement(current_avg, target_grade):
    return current_avg >= target_grade 
    
def process(assignments_score1, assignments_score2, assignments_score3, midterm_score, final_score):
    assignment_avg = (assignments_score1 + assignments_score2 + assignments_score3)/3
    weighted_avg = calculate_weighted(assignment_avg, midterm_score, final_score)
    print("STUDENT GRADE CALCULATOR")
    print("="*40)
    print(f"Assignment Scores: {assignments_score1, assignments_score2, assignments_score3}")
    print(f"Midterm Score: {midterm_score}")
    print("-"*40)
    print(f"Regular Assignment Average: {calculate_average(assignments_score1, assignments_score2, assignments_score3):.2f}")
    print(f"Average with Lowest Dropped: {drop_lowest(assignments_score1, assignments_score2, assignments_score3):.2f}")
    print(f"Using Better Average:  {drop_lowest(assignments_score1, assignments_score2, assignments_score3):.2f}\n")
    print(f"Weighted Course Average: {calculate_weighted(assignment_avg, midterm_score, final_score):.2f}")
    print(f"Letter Grade: {determine_grade(assignment_avg)}\n")
    print(f"Needs improvement for an 'A': {"Yes" if needs_improvement(assignment_avg, 90) else "No"}")
    if assignment_avg < 90:
        print(f"Points needed: {90 - weighted_avg:.2f}") 
    else:
        ...
    if assignment_avg >= 90:
        print(f"Already meets or exceeds 'A' grade requirement")
    elif assignment_avg >= 80:
        print(f"Already meets or exceeds 'B' grade requirement")
    elif assignment_avg >= 70:
        print(f"Already meets or exceeds 'C' grade requirement")
    elif assignment_avg >= 60:
        print(f"Already meets or exceeds 'D' grade requirement")
    else:
        print(f"Already meets or exceeds 'F' grade requirement")
process(85, 78, 92, 88, 82)
