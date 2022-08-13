

def total_points(homework,test,bonus):
    total = (homework + test + bonus)
    total = "{:.2f}" .format(total)
    return total


def average_points(homework,test,bonus):
    average = (homework + test + bonus) / 3
    average ="{:.2f}" .format(average)  
    return average

def letter_grade(homework,test,bonus):
    score = homework + test + bonus
    if score > 100:
        return ('Invalid Score, cannot exceed 100')
    
    elif score >= 90:
        return ('Letter Grade = A')
    elif score >= 80:
        return ('Letter Grade = B')
    elif score >= 70:
        return ('Letter Grade = C')
    elif score >= 60:
        return ('Letter Grade = D')
    
    elif  0 < score < 60:
        return ('Letter Grade = F')
     
    else: 
        return ('Invalid Score, cannot be lower than 0')



