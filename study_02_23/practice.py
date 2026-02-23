import math
white_x, white_y = gameData= [0]

target_x, target_y = -1, -1

for i in range(1, 6):
    if  gameData[i][0] != -1:
        target_x, target_y = gameData[i]
        break 
holes =[]

#최적의 각도, 파워, 최소거리 변수 지정

# 6개 홀 중에서 최적
for h_x, h_y in holes:
    d_target_hole = math.hypot(h_x - target_x, h_y-target_y)

    
    ghost_x = target_x - h_x - target_x *(5.73/d_target_hole)
    ghost_y = target_y - h_y - target_y *(5.73/d_target_hole)

    dx = ghost_x - white_x
    dy = ghost_y - white_y
    
    dist = math.hypot(dx, dy)
    if dist < min_distance:
        min_distance = dist

    angle = math.degrees(math.atan2(dx, dy))
    best_angle = (angle + 360) % 360

    best_power = dist *0.6 +25

angle = best_angle
power = best_power

        
