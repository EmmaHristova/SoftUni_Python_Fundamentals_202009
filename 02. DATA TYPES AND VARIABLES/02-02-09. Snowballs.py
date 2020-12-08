# 02-02. DATA TYPES AND VARIABLES [Exercise]
# 09. Snowballs

snowballs = int(input())

snowball_value = 0
snowball_value_win = 0

for snowball in range(snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = int(snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > snowball_value_win:
        snowball_value_win = snowball_value
        snowball_snow_win = snowball_snow
        snowball_time_win = snowball_time
        snowball_quality_win = snowball_quality

print(f"{snowball_snow_win} : {snowball_time_win} = {snowball_value_win} ({snowball_quality_win})")
