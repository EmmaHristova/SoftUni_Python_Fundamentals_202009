# 08-02. TEXT PROCESSING [Exercise]
# 07. String Explosion

string = input()
is_processed = False
idx = 0

while idx < len(string):
    if string[idx] == '>' and string[idx+1].isdigit() and int(string[idx+1]) > 0:
        explosions = 1
        strength = int(string[idx+1])
        exploded = 0
        while exploded < strength:
            idx_to_explode = idx+explosions
            if idx_to_explode > len(string)-1:
                is_processed = True
                break
            if string[idx_to_explode] != '>':
                string = string[0:idx_to_explode] + string[idx_to_explode+1::]
                exploded += 1
            else:
                strength += int(string[idx_to_explode+1])
                explosions += 1
    if is_processed:
        break
    idx += 1

print(string)
