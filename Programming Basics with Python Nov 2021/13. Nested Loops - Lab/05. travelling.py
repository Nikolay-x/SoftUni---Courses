# 5.Пътуване
# Ани обича да пътува и иска тази година да посети няколко различни дестинации. Като си избере дестинация, ще прецени колко пари ще й трябват, за да отиде до там, и ще започне да спестява. Когато е спестила достатъчно, ще може да пътува.
# От конзолата всеки път ще се четат първо дестинацията и минималния бюджет (десетично число), който ще е нужен за пътуването.
# След това ще се четат няколко суми (десетични числа), които Ани спестява като работи и когато успее да събере достатъчно за пътуването, ще заминава, като на конзолата трябва да се изпише: "Going to {дестинацията}!"
# Когато е посетила всички дестинации, които иска, вместо дестинация ще въведе "End" и програмата ще приключи.
#
# Вход
# Greece
# 1000.00
# 200.00
# 200.00
# 300.00
# 100.00
# 150.00
# 240.00
# Spain
# 1200.00
# 300.00
# 500.00
# 193.00
# 423.00
# End
#
# Изход
# Going to Greece!
# Going to Spain!

command = input()
while command != 'End':
    destination = command
    destination_price = float(input())
    total_savings = 0
    while total_savings < destination_price:
        current_savings = float(input())
        total_savings += current_savings
    print(f"Going to {destination}!")
    command = input()
