# Guess The Number II

- Guess The Number II is a Python terminal game
- Users can try beat the computer guessing a number betweenn 1 and 10.
###
- The live link can be found here - [Guess The Number II](https://guess-the-number-2.herokuapp.com/) 

![Responsive Mockup](/assets/images/AmIResponsiveScren.JPG)

## How to play 

Guess The Number is a classic guessing game. 
######
The user can play against the computer by inputting the values on the terminal. 
######
The game will tell the player immediately to guess a higher or lower number.

## Features
####
#### Existing Features

- Randon computer selection 
  - Once the player choose computer will make a ramdom selection 
   - The player will not be able to see that
####
- Example when the player win 

<img alt="Win" src="/assets/images/winWin.JPG" width="50%">

###

- Example when the player lose  

<img alt="Lower number" src="/assets/images/firstGuess.JPG" width="50%">

###

- Example when the player Draw 
  

<img alt="Higher number" src="/assets/images/secondGuess.JPG" width="50%">

###
- Play again 
  - When the game is finished the user will be prompeted to press '1' to play again or 'q' to exit the game.
###
  <img alt="Play Again" src="/assets/images/playAgain.JPG" width="50%">

  ####
  - Exit game 
    - once the player press 'q' to exit it will be showed a banner and the game will finish.
    ####
      <img alt="Exit" src="/assets/images/ExitGame.JPG" width="50%">

      ####
- Input validation and error checking 
  - if the player type invalid a input it will be validated
  ###
<img alt="validation" src="/assets/images/InputValidation.JPG" width="50%">

####
<img alt="validation2" src="/assets/images/" width="50%">
### Testing

I have tested the project doing the following

- passed on [PEP8](http://pep8online.com/). ()
- Tried invalid inputs 
- Tested on Heroku and the Terminal.

  #### Bugs

 

  #### Remain Bugs



 #### Validator Testing 
 - [PEP8](http://pep8online.com/)
   
 #### Deployment 
- When you create the app, you will need to add two buildpacks from the Settings tab. The ordering is as follows:

   - heroku/python
    - heroku/nodejs
    - You must then create a Config Var called - PORT. Set this to 8000

    
  -  Connect your GitHub repository and deploy as normal.

  #### Credits

   - [W3Schools](https://www.w3schools.com/python/python_datetime.asp)
   - [Code Institute](https://www.CodeInstitute.net)
   - [Youtube](https://www.youtube.com/)
   - [pyfiglet](https://pypi.org/project/pyfiglet/0.7/)

