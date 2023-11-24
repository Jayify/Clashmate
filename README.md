# Clashmate

Clashmate: a tool for Clash of Clans leaders to manage, tracking, and evaluate clan members.

Clashmate is a CLI Python program using the Clash of Clans (mobile game) developer API. The program is designed to identify actively participating and frequently contributing players in your clan, in order to assist the clan leader in choosing who deserves which clan roles.

Developed by Jayden Houghton, 2023
<br><br>

## The program:
<ol>
  <li>Retrieves the clan member list</li>
  <li>Retrieves player data for each member in the clan</li>
  <li>Accepts manual data inputs for more accurate data.</li>
  <li>Calculates a ranking score for each player depending on their stats and clan contribution</li>
  <li>Outputs the players and their score in order of highest to lowest</li>
</ol>
<br>

## Setup
<ol>
  <li>Download the most recent release from this repository.</li>
  <li>This program uses the Python requests module and will require it to be installed.</li>
  <li>Open the files in a code editor such as VS Code (with a Python extension) or PyCharm.</li>
  <li>Remove "example_" from the name of the config and player_data files.</li>
  <li>Generate a CoC API token from the developer page: https://developer.clashofclans.com/#/register and copy to the config file.
  <li>(optional) Run the program and choose option 2, then add any manual data to player_data.txt. The default values are 0. The program can be run without this data, however these stat fields will not be taken into account during calculation so the overall ratings will not be as accurate to the player's actual contribution.</li>
  <li>Run the program and choose option 1 for clan evaluation.</li>
  <li>Update the manual data over time.</li>
</ol>
<br>

## Notes:
<ul>
  <li>The clan tag is hardcoded in the program. This is to avoid repetitively inputting the same tag every time the program is run for the clan you manage.</li>
  <li>If your computer uses a dynamic ip address, you will need to create a new CoC API token and update the config file every time it changes. Alternately, switch to a static ip address.</li>
</ul>
<br>

## Evaluation Equation Justification

The purpose of the rating is to give a rough idea of how much a player contributes to the clan. The equation is designed to mainly emphasise participation, however greater scores are given for higher level and higher skilled players as this benefits the clan.

A high level and well contributing player should have a score of around 100. There is no max value, as stats such as donations have no limit.
<br><br>

Example Player Stats:
<li>Hall: 11, trophies: 3,000, donations: 1,000, league: 15 (Masters 1), capital gold: 200,000, cwl: 2 star for each of 7 days, war: 5 starts over 2 attacks over 4 wars, raid: 10,000 for 4 raids, clan games: 4,000</li>
<li>Rating = hall: 11, trophies: 10, donations: 10, leaguePenalty: 0, capital gold: 10, cwl: 10.5 , war: 12.5, raid: 13, clan games: 10 = 76</li>


