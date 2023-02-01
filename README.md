# Clash of Clans Clanmate Evaluator
A simple Python program using the Clash of Clans (mobile game) developer API. The program is designed to assist with identifying active and frequently contributing players in your clan, and choosing who deserves which clan roles.
<br><br>
Developed by Jayden Houghton, 2023
<br><br>

The program:
<ol>
  <li>Retrieves the clan member list</li>
  <li>Retrieves player data for each member in the clan</li>
  <li>Calculates a ranking score for each player depending on their stats and clan contribution</li>
  <li>Outputs the players and their score in order of highest to lowest</li>
</ol>
<br>

Note:
<ul>
  <li>The clan tag is hardcoded in the program. This is to avoid repetitively inputting the same tag every time the program is run for the clan you manage.</li>
  <li>This program uses the Python requests module and will require it to be installed.</li>
  <li>In order to connect to the CoC API, a token must be generated from the developer page: https://developer.clashofclans.com/#/register.
  <li>If your computer uses a dynamic ip address, you will need to create a new CoC API token and update the config file every time it changes. Alternately, switch to a static ip address.</li>
</ul>