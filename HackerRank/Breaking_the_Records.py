#breaking the records

n=int(input())
game_scores=[int(var) for var in input().split()]

high_score=game_scores[0]
low_score=game_scores[0]
count_high_scr=0
count_low_scr=0

for score in game_scores:
    if score>high_score:
        count_high_scr+=1
        high_score=score
    elif score<low_score:
        count_low_scr+=1
        low_score=score
print(count_high_scr,count_low_scr)
