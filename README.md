# ProcGenTD
Procedurally generated tower defense game


This game generates a tower defense map and launches a game object on a remote server.
The game object acquires one or more offense and defense players, then fills remaining slots with AI players.
Then, the game object begins to send game updates to each player view, which are web-apps or mobile apps running on human player devices.
When a human player initiates a game, a controller object is generated alongside the view.
Controller objects are also generated on the AI server.
The controller objects receive game updates, to determine which actions are allowed and as input to the AI routine. 


To do:
* Write make map module to generate the random maps (image and data structure)
* Write game server to start game, collect players, and connect to controllers and views.
* Creat digital image assets for towers, units and map.
* Write AI controller logic for offense and defense.
* Write web-app view (receives game updates, displays current game)
* Write web-app controller (receives game updates, display available options, send actions to game)
* Write game logic on server - change game state according to actions and time stepping

