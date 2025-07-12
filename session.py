""" session.py """

import session_logic

class Session():
  def __init__(self):

    self.due_cards = session_logic.get_all_due_cards()
    self.current_card = session_logic.get_next_card(self.due_cards)
    self.card_state = None

    self.start_session()

  def start_session(self):
    print("Session Started!")
    self.session_loop()

  def session_loop(self):
    while True:
        if self.current_card is None:
            print("No more cards are left!")
            break

        print(f"Front: {self.current_card['front_text']}")  # Show front
        self.card_state = "front"

        while True:
            answer = input("flip or rate? ")
            if answer == "flip":
                self.card_state = session_logic.flip_card(self.current_card, self.card_state)
            elif answer == "rate":
                break
            else:
                print("Invalid option")

        while True:
            difficulty_lvl = input("Rate the card: (easy/medium/hard): ")
            if difficulty_lvl in ["easy", "medium", "hard"]:
                session_logic.update_card_date_data(self.current_card, difficulty_lvl)
                print("To the next card!")
                break
            else:
                print("Invalid option!")

        self.card_state = None
        self.current_card = session_logic.get_next_card(self.due_cards)

