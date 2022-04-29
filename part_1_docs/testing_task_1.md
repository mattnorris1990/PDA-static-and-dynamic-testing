### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # if card.value = 1:  << this should be '==' rather than '='
      return True

    # else       << this should end with a colon
      return False
   
  # dif highest_card(self, card1 card2):    << 'dif' should be 'def'; 'card1' should be followed by a comma
  # if card1.value > card2.value:   << starting here to the end of the function, this should be indented so it's within the function
    # return card     << 'card' won't return anything, logically should say 'card1' 
  else:
    return card2
  


# def cards_total(self, cards):  << this entire function needs to be indented to be within the class
  # total   << this needs an assigned value - logically would read 'total = 0'
  for card in cards:
    total += card.value
    # return "You have a total of" + total   
    # ^^^ this return is indented incorrectly for the intended result - should be outside of the for loop. 'Total' needs to be converted to string (str(total)). The string should also arguably include a space at the end, however i've not made this change because it wouldn't stop the programme working.
  
```
