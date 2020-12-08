# 07-02. OBJECTS AND CLASSES [Exercise]
# 03. Legendary Farming

key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_materials = {}

enough_quantity = False

while True:
    farming = input().split(' ')

    for i in range(0, len(farming), 2):
        material = farming[i+1].lower()
        quantity = int(farming[i])

        if material in ('shards', 'fragments', 'motes'):
            key_materials[material] += quantity
            if max(key_materials.values()) >= 250:
                enough_quantity = True
                break
        else:
            if material not in junk_materials:
                junk_materials[material] = 0
            junk_materials[material] += quantity

    if enough_quantity:
        break

max_material = max(key_materials, key=key_materials.get)
legendary_item = ''

if max_material == 'shards':
    legendary_item = 'Shadowmourne'
elif max_material == 'fragments':
    legendary_item = 'Valanyr'
elif max_material == 'motes':
    legendary_item = 'Dragonwrath'

key_materials[max_material] -= 250

key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
junk_materials = dict(sorted(junk_materials.items(), key=lambda x: (x[0])))

print(f'{legendary_item} obtained!')
[print(f'{material}: {quantity}') for (material, quantity) in key_materials.items()]
[print(f'{material}: {quantity}') for (material, quantity) in junk_materials.items()]
