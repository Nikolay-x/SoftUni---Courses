experience_needed = float(input())
total_battles = int(input())

total_exp = 0
battle_count = 0
is_exp_collected = False

for battle in range(1, total_battles + 1):
    cur_battle_exp = float(input())
    battle_count += 1
    total_exp += cur_battle_exp
    if battle % 3 == 0:
        total_exp += cur_battle_exp * 0.15
    if battle % 5 == 0:
        total_exp -= cur_battle_exp * 0.1
    if battle % 3 == 0 and battle % 5 == 0:
        total_exp += cur_battle_exp * 0.05
    if total_exp >= experience_needed:
        is_exp_collected = True
        break

if is_exp_collected:
    print(f"Player successfully collected his needed experience for {battle_count} battles.")
else:
    more_exp_needed = experience_needed - total_exp
    print(f"Player was not able to collect the needed experience, {more_exp_needed:.2f} more needed.")
