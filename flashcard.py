""" flashcard.py """
class Flashcard:
  def __init__(self, front, back, difficulty="medium"):
    self.front = front
    self.back = back
    self.difficulty = difficulty

  def update(self, front=None, back=None, difficulty=None):
    if front: self.front = front
    if back: self.back = back
    if difficulty: self.difficulty = difficulty

  def __str__(self):
    return f"Front: {self.front}, Back: {self.back}"