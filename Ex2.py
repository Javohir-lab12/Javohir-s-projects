def calculate_average(score1, score2, score3):
    return sum(score1, score2, score3) / 3

def drop_lowest(score1, score2, score3):
    return (sum(score1, score2, score3) - min(score1, score2, score3))/2

def calculate_weighted(assignments, midterm, final):
     return (assignments * .3 + midterm * .3 +final * .4)/3

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
        "F"
def needs_improvement(current_avg, target_grade):
    return current_avg >= target_grade 
    
assignments_score = 
midterm_score = 
final_score = 
score1, score2, score3 = 
average = 
print("STUDENT GRADE CALCULATOR")
print("="*40)
print(f"Assignment Scores: {score1, score2, score3}")
print(f"Midterm Score: {midterm_score}")
print("-"*40)
print(f"Regular Assignment Average: {calculate_average(score1, score2, score3)}")
print(f"Average with Lowest Dropped: {drop_lowest(score1, score2, score3)}")
print(f"Using Better Average:  {drop_lowest(score1, score2, score3)}\n")
print(f"Weighted Course Average: {calculate_weighted(assignments, midterm_score, final)}")
print(f"Letter Grade: {determine_grade(average)}\n")
if average < 90 :
    print("Needs improvement for an 'A': Yes")
    print(f"Points needed: 4.05")
    print(f"Already meets or exceeds 'B' grade requirement")