"""Classes for melon orders."""

class AbstractMelonOrder():
    """"an abstract melon class"""

    def __init__(self, species, qty, tax):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.shipped = False 
        self.tax = tax 
        
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
        self.species = species
        self.qty = qty
        self.shipped = False 
        self.order_type = "domestic"
        self.tax = 0.08

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
