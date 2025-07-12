""" data_manager.py """

import os
import json

cards_data_file = "cards_data.json"

def create_card_data(card):

  card = {
    "front_text": card.front,
    "back_text": card.back,
    "difficulty_level": None,
    "last_reviewed_date": None,
    "next_review_date": None,
    "number_of_reviews": 0
  }

  cards = []

  if os.path.exists(cards_data_file):
    with open(cards_data_file, "r", encoding="utf-8") as file:
      try:
        cards = json.load(file)
      except json.JSONDecodeError:
        pass

  cards.append(card)

  with open(cards_data_file, "w", encoding="utf-8") as file:
    json.dump(cards, file, indent=2, ensure_ascii=False)

def check_existence_of_card(front_text, back_text):

  if not os.path.exists(cards_data_file):
    return False

  with open(cards_data_file, "r", encoding="utf-8") as file:
    try:
      cards = json.load(file)
    except json.JSONDecodeError:
      return False
    
    for card in cards:
      if front_text == card["front_text"] and back_text == card["back_text"]:
        return True

  return False

def edit_card_data(old_front, old_back, new_front, new_back):
  if not os.path.exists(cards_data_file):
    return 
    
  with open(cards_data_file, "r", encoding="utf-8") as file:
    try:
      cards = json.load(file)
    except json.JSONDecodeError:
      return
    
    for card in cards:
      if card["front_text"] == old_front and card["back_text"] == old_back:
        card["front_text"] = new_front
        card["back_text"] = new_back
        

        with open(cards_data_file, "w", encoding="utf-8") as file:
          json.dump(cards, file, indent=2, ensure_ascii=False)
        return True
    
    return False
  
def delete_card_data(front, back):
  if not os.path.exists(cards_data_file):
    return
  
  with open(cards_data_file, "r", encoding="utf-8") as file:
    try:
      cards = json.load(file)
    except json.JSONDecodeError:
      return
    
    updated_cards = [
      card for card in cards
      if not (card["front_text"] == front and card["back_text"] == back)
    ]

    if len(updated_cards) == len(cards):
      return False # Nothing was deleted

    with open(cards_data_file, "w", encoding="utf-8") as file:
      json.dump(updated_cards, file, indent=2, ensure_ascii=False)
      
    return True
    