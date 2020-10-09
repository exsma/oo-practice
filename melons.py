"""Classes for melon orders."""

class AbstractMelonOrder():
    """"an abstract melon class"""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax 
        self.shipped = False 
        
    def get_total(self):
        """Calculate price, including tax."""
        
        base_price = 5
        
        if self.species == 'Christmas':
            base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price

        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, 'domestic', 0.08)
        self.shipped = False 
        

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.shipped = False 
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_total(self):
        """Calculate price, including tax."""

        total = super().get_total(self)
        
        if self.qty < 10:
            total + 3.00

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
# Create a class GovernmentMelonOrder that inherits from AbstractMelonOrder.
# There will be no tax on government orders.
# The GovernmentMelonOrder class should include:
# a variable passed_inspection which is False until a successful inspection occurs
# a method mark_inspection(passed) that takes a Boolean input, passed, 
# and updates whether or not the melon has passed inspection. 
# This method should update the attribute passed_inspection.
class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__ (self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False 
        self.tax = 0 
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed

