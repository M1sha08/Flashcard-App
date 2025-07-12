""" session_logic.py """

import json
import datetime

cards_data_file = "cards_data.json"


def flip_card(card, card_state):
  if card_state == None:
    card_state = "front"
    print(f"Front: {card['front_text']} ")
  elif card_state == "front":
    card_state = "back"
    print(f"Back: {card['back_text']} ")
  elif card_state == "back":
    card_state = "front"
    print(f"Front: {card['front_text']} ")
    
  return card_state

def update_card_date_data(current_card, difficulty_level):

  with open(cards_data_file, "r", encoding="utf-8") as file:
    cards = json.load(file)
  
  for card in cards:
    if card["front_text"] == current_card["front_text"] and card["back_text"] == current_card["back_text"]:

      card["difficulty_level"] = difficulty_level
      card["last_reviewed_date"] = datetime.datetime.now().isoformat()

      if difficulty_level == "easy":
        card["next_review_date"] = (datetime.datetime.now() + datetime.timedelta(minutes=30)).isoformat()
      elif difficulty_level == "medium":
        card["next_review_date"] = (datetime.datetime.now() + datetime.timedelta(minutes=15)).isoformat()
      elif difficulty_level == "hard":
        card["next_review_date"] = (datetime.datetime.now() + datetime.timedelta(minutes=5)).isoformat()

      card["number_of_reviews"] += 1

  with open(cards_data_file, "w", encoding="utf-8") as file:
    json.dump(cards, file, indent=2, ensure_ascii=False)


def get_all_due_cards():
  try:
    with open(cards_data_file, "r", encoding="utf-8") as file:
      cards = json.load(file)
  except json.JSONDecodeError:
      return

  due_cards = []

  for card in cards:
    if card["next_review_date"] is None or card["next_review_date"] <= datetime.datetime.now().isoformat():
      due_cards.append(card)

  return due_cards


def get_next_card(due_cards):
  if not due_cards:
    return
  next_card = due_cards.pop(0)

  return next_card