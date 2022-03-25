class FeetInches:

    def __init__(self, f, i):
        self.feet = f
        self.inches = i

    def simplify(self):
        """
        if the number of inches is > 12, 
        this regroups the excess into feet
        """
        self.feet += self.inches // 12
        self.inches = self.inches % 12

    def __repr__(self):
        return str(self.feet)+"ft. "+str(self.inches)+"in."

    def __add__(self, other_measurement):
        total_feet = self.feet + other_measurement.feet
        total_inches = self.inches + other_measurement.inches

        # create an new FeetInches object with the new measurements
        total_FI = FeetInches(total_feet, total_inches)
        total_FI.simplify()
        return total_FI

    def __sub__(self, other_measurement):
        total_feet = self.feet - other_measurement.feet
        total_inches = self.inches - other_measurement.inches

        # create an new FeetInches object with the new measurements
        total_FI = FeetInches(total_feet, total_inches)
        total_FI.simplify()
        return total_FI

    def __lt__(self, other):
        self_total = self.feet * 12 + self.inches
        other_total = other.feet * 12 + other.inches

        return self_total < other_total

    def __le__(self, other):
        self_total = self.feet * 12 + self.inches
        other_total = other.feet * 12 + other.inches

        return self_total <= other_total

    def __eq__(self, other):
        self_total = self.feet * 12 + self.inches
        other_total = other.feet * 12 + other.inches

        return self_total == other_total
"""tests

measurement1 = FeetInches(12, 14)
measurement2 = FeetInches(0, 158)
is_lt = measurement1 < measurement2
is_gt = measurement1 > measurement2
is_le = measurement1 <= measurement2
is_ge = measurement1 >= measurement2
is_eq = measurement1 == measurement2
is_ne = measurement1 != measurement2

print("\nmeasurement1  < measurement2", is_lt, "\nmeasurement1  > measurement2",
      is_gt,"\nmeasurement1 <= measurement2", is_le,"\nmeasurement1 >= measurement2", is_ge,"\nmeasurement1 == measurement2", is_eq,"\nmeasurement1 != measurement2", is_ne,)
"""