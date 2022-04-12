# 3.Време + 15 минути
# Да се напише програма, която чете час и минути от 24-часово денонощие, въведени от потребителя и изчислява колко ще е часът след 15 минути. Резултатът да се отпечата във формат часове:минути. Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59. Часовете се изписват с една или две цифри. Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.
#
# вход
# 1
# 46
#
# изход
# 2:01

hours = int(input())
minutes = int(input())

if minutes + 15 < 60:
    hours = hours
    minutes = minutes + 15
else:
    hours = hours + (minutes + 15) // 60
    minutes = (minutes + 15) % 60

if hours <= 23:
    if minutes < 10:
        print(f"{hours}:0{minutes}")
    else:
        print(f"{hours}:{minutes}")
else:
    if minutes < 10:
        print(f"{hours % 23 - 1}:0{minutes}")
    else:
        print(f"{hours % 23 - 1}:{minutes}")
