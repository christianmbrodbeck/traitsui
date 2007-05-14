# dynamic_notification --- Example of dynamic 
#                          notification
from enthought.traits.api import Float, HasTraits, Trait

class Part (HasTraits):
  cost = Trait(0.0)

class Widget (HasTraits):
  part1 = Trait(Part)
  part2 = Trait(Part)
  cost  = Float(0.0)

  def __init__(self):
    self.part1 = Part()
    self.part2 = Part()
    self.part1.on_trait_change(self.update_cost, 'cost')
    self.part2.on_trait_change(self.update_cost, 'cost')

  def update_cost(self):
    self.cost = self.part1.cost + self.part2.cost
    
"""
>>> w = Widget()
>>> w.part1.cost = 2.25
>>> w.part2.cost = 5.31
>>> print w.cost
7.56
"""
