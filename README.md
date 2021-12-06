# fair-blackjack
finding a way to make a blackjack fair (by changing the cards we use)

## what
this was an open ended probability project for my stats class. the goal was to create a configuration of playing cards that would make blackjack more fair for typical players who do not count cards and perhaps follow a loose strategy. the script goes through 8192 combinations of changes to the deck of cards.

for my test, each type of card within a deck can either be seen 4 times in the deck, or 40 times. this increase is i believe a fair amount to see a change in probability and not too overwhelmingly impactful. since there are 13 different cards in a deck and 2 "states" a kind of card can have, there are 2 to the power 13 different possible configurations, or 8192. since suits have no role blackjack, they are not considered. you can think of the 4 to 40 as each suti having 10 of that card instead of only 1.

to keep things consistent and simple, doubling and splitting will not be considered. players can only hit or stand. dealers, like in real blackjack, have a soft 17 limit. players have a fixed strategy based on conditions i found from [here](https://www.blackjackapprenticeship.com/blackjack-strategy-charts/). (doubling is considered hitting).

the results of the are recorded into a google sheet using the `gspread` module, which interacts with the google sheets API. change the respective values and reconfigure `gspread` with your credentials if you wish to test yourself.

## requirements
`pip3 install gspread` or `pip3 install requirements.txt`

create a google API service account specifically for sheets. see [this](https://docs.gspread.org/en/latest/oauth2.html#for-bots-using-service-account) to see how to set it up. make sure to create a blank google sheet and share it with the service account.

## usage
run `main.py`

## results
results from my tests can be found [here](https://docs.google.com/spreadsheets/d/1B-N6luLgy6glRgmO7cnVN7cbUKhdAnqsSTQD_568_n4/edit?usp=sharing). you can draw your own conclusions about the results. though here are some of my findings:
- adding more face cards and 10s results in more ties
- 5, 6, and 7 seem to be the worst cards to add as they increase losses
- adding aces, 2s, 3s, 10s and face cards results in fairer odds, meaning wins and losses are quite close.
- 8 seems to be a great card as well
