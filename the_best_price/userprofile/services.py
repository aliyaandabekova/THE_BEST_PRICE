def calculate_avg_score(scores):
    sum = 0
    for score in scores:
        point = score.score
        sum += point
    avg_score = sum / len(scores)
    avg_score = round(avg_score,2)
    return avg_score
