from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        # self.guests = 0

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        # room = [r for r in self.rooms if r.number == room_number][0]
        # room.take_room(people)

        for room in self.rooms:
            if room.number == room_number:  # and not room.is_taken:
                room.take_room(people)
                # self.guests += room.guests

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:  # and room.is_taken:
                room.free_room()
                # self.guests -= room.guests

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]

        result = f"Hotel {self.name} has {self.guests} total guests\n"
        result += f"Free rooms: {', '.join(free_rooms)}\n"
        result += f"Taken rooms: {', '.join(taken_rooms)}"
        return result
