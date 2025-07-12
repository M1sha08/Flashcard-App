""" flashcard_app.py """

from flashcard import Flashcard
from session import Session
import data_manager

class FlashcardApp:
  def __init__(self):
    pass
    
  
  def run(self):
    while True:
      user_answer = input("Do you want to (Create/Edit/Delete) a Card, (Start) study session, or (Quit)? ").strip().lower()

      if user_answer == "create":
        self.create_flashcard()
      elif user_answer == "edit":
        self.edit_flashcard()
      elif user_answer == "delete":
        self.delete_flashcard()
      elif user_answer in ["start", "start session"]:
        session = Session()
        session.start_session()
      elif user_answer in ["quit", "exit", "q"]:
        break
      else:
        print("Invalid option. Please try again.")

  def create_flashcard(self):
    print("Provide front and back text of the card to create the card.")

    front = input("Front: ").strip().lower()
    back = input("Back: ").strip().lower()

    if not data_manager.check_existence_of_card(front, back):
      card = Flashcard(front, back)
      data_manager.create_card_data(card)
      print("Card created!")

  def edit_flashcard(self):
    print("Provide front and back text of the card to edit the card.")

    old_front = input("Old Front: ").strip().lower()
    old_back = input("Old back: ").strip().lower()

    if data_manager.check_existence_of_card(old_front, old_back):
      new_front = input("New front: ").strip().lower()
      new_back = input("New back: ").strip().lower()

      data_manager.edit_card_data(old_front, old_back, new_front, new_back)

    print("Card doesn't exist. Try creating it instead.")

  def delete_flashcard(self):
    print("Provide front and back text of the card to delete the card.")

    front = input("Front: ").strip().lower()
    back = input("Back: ").strip().lower()
    if data_manager.check_existence_of_card(front, back):
      data_manager.delete_card_data(front, back)
      return
    print("Card doesn't exist.")
        



