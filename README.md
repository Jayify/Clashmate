# Clash of Clans Clanmate Evaluator
A simple Python program using the Clash of Clans (mobile game) developer api. The program is designed to assist with identifying active and frequently contributing players in your clan, and choosing who deserves which clan roles.
<br><br>

The program:
<ol>
  <li>Retrieves the clan member list</li>
  <li>Retrieves player data for each member in the clan</li>
  <li>Calculates a ranking score for each player depending on their stats and clan contribution</li>
  <li>Outputs the players and their score in order of best to worst</li>
</ol>
<br>

Note:
<ul>
  <li>The clan tag is hardcoded in the program. This is to avoid repetitively inputing the same tag everytime the program is run for the clan you manage.</li>
  <li>This program uses the Python requests module and will require it to be installed.</li>
</ul>
