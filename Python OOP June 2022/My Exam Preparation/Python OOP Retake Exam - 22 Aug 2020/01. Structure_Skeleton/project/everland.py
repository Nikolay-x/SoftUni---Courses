from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        monthly_consumption = sum([r.monthly_cost for r in self.rooms])
        return f"Monthly consumption: {monthly_consumption}$."

    def pay(self):
        result = []
        for r in self.rooms:
            if r.budget >= r.monthly_cost:
                r.budget -= r.monthly_cost
                result.append(f"{r.family_name} paid {r.monthly_cost}$ and have {r.budget}$ left.")
            else:
                result.append(f"{r.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(r)
        return "\n".join(result)

    def status(self):

        result = f"Total population: {sum(r.members_count for r in self.rooms)}\n"
        for r in self.rooms:
            result += f"{r.family_name} with {r.members_count} members. Budget: {r.budget}$, Expenses: {r.expenses}$\n"
            if r.children:
                for i, c in enumerate(r.children):
                    result += f"--- Child {i+1} monthly cost: {c.get_monthly_expense()}$\n"
            if r.appliances:
                total_cost = r.calculate_items_expenses(r.appliances)
                result += f"--- Appliances monthly cost: {total_cost}$\n"
        return result.strip()
