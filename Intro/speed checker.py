speed = float(input())
slow = "slow"
average = "average"
fast = "fast"
ultra_fast = "ultra fast"
extremely_fast = "extremely fast"

if speed <= 10:
    print(slow)
elif speed <= 50:
    print(average)
elif speed <= 150:
    print(fast)
elif speed <= 1000:
    print(ultra_fast)
elif speed > 1000:
    print(extremely_fast)
