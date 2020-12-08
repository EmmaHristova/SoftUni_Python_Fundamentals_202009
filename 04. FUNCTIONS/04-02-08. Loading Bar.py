# 04-02. LISTS BASICS [Exercise]
# 08. Loading Bar

def loading_bar(number):
    loaded = 0
    loading = number
    if number < 100:
        while loading > 0:
            loaded += 1
            loading -= 10
        full = '%' * loaded
        empty = '.' * (10 - loaded)
        print(f"{number}% [{full}{empty}]")
        print('Still loading...')
    else:
        print('100% Complete!')
        print('[%%%%%%%%%%]')


loading_bar(int(input()))
