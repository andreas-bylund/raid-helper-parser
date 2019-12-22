
class Raid:

    def __init__(self, event_name, date, time, description):
        self.event_name = event_name
        self.date = date
        self.time = time
        self.description = description
        self.tank = []
        self.hunter = []
        self.priest = []
        self.warrior = []
        self.mage = []
        self.paladin = []
        self.rogue = []
        self.warlock = []
        self.druid = []
        self.late = []
        self.bench = []
        self.absence = []

    def add_attendee(self, role, name):
        role = role.lower()
        if role == "tank":
            self.tank.append(name)
        elif role == "hunter":
            self.hunter.append(name)
        elif role == "priest":
            self.priest.append(name)
        elif role == "warrior":
            self.warrior.append(name)
        elif role == "mage":
            self.mage.append(name)
        elif role == "paladin":
            self.paladin.append(name)
        elif role == "rogue":
            self.rogue.append(name)
        elif role == "warlock":
            self.warlock.append(name)
        elif role == "druid":
            self.druid.append(name)
        elif role == "late":
            self.late.append(name)
        elif role == "bench":
            self.bench.append(name)
        elif role == "absence":
            self.absence.append(name)

    def get_event_name():
        return self.event_name

    def get_tanks():
        return self.tank

    def get_hunters():
        return self.hunter

    def get_priests():
        return self.priest

    def get_warriors():
        return self.warrior

    def get_mages():
        return self.mage

    def get_paladins():
        return self.paladin

    def get_rogues():
        return self.rogue

    def get_warlocks():
        return self.warlock

    def get_druids():
        return self.druid

    def get_late():
        return self.late

    def get_bench():
        return self.bench

    def get_absence():
        return self.absence
