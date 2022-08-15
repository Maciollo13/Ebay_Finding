# Ebay searching bot
From when I remember my hobby is collecting Pokemon TCG cards. 
To raise the value of my collection I wanted to have PSA 10 graded card (this means a card in ideal condition). 
But the cards are very expensive on site as Cardmarket.com, so I've manually searched
Ebay to find one, and trust me it is boring. So I've made this program to automate this task.

## How does it work?
First of all program asks user to type in the keyword he is searching for.
Then it is saved to dictionary, which is nested to the Ebay Finding Api.
And the replay is then converted to "result.csv" file. This file can be sent
to the email choosen by user in config.json.
