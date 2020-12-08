# 03-02. LISTS BASICS [Exercise]
# 08. Seize the Fire

fire = list(input().split('#'))
water = int(input())
effort = 0
fire_out = 0

print("Cells:")
for cell in fire:
    delim_index = cell.find("=")
    fire_type = cell[:delim_index-1]
    fire_value = int(cell[delim_index+1:])
    if water >= fire_value:
        if (fire_type == 'Low' and 1 <= fire_value <= 50) or (fire_type == 'Medium' and 51 <= fire_value <= 80) or (fire_type == 'High' and 81 <= fire_value <= 125):
            water -= fire_value
            fire_out += fire_value
            effort += 0.25 * fire_value
            print(f"- {fire_value}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire_out}")
