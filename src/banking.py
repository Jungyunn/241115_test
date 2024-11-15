from abc import ABC, abstractmethod

class InterestRateStrategy(ABC):
    @abstractmethod
    def apply_interest_rate(self, amount):
        pass
    
class OrdinaryMember(InterestRateStrategy):
    def apply_interest_rate(self, amount):
        interests = amount * 0.02
        return amount + interests

class PremiumMember(InterestRateStrategy):
    def apply_interest_rate(self, amount):
        interests = amount * 0.024
        return amount + interests