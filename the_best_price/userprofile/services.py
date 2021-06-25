def calculate_avg_score(scores):
    sum = 0
    for score in scores:
        point = score.score
        sum += point
    sum /= len(scores)
    return sum
