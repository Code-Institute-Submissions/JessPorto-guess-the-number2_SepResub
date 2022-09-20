# Guess The Number II

- Guess The Number II is a Python terminal game
- Users can try beat the computer guessing a number betweenn 1 and 10.
###
- The live link can be found here - [Guess The Number II](https://guess-the-number-2.herokuapp.com/) 

![Responsive Mockup](/assets/images/AmIresponsiveScreen.JPG)

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
  - Once the player choose computer will make a random selection 
   - The player will not be able to see that

####
- Example when the player win 

![Win](/assets/images/winWin.JPG)

###

- Example when the player guessed a lower number 

![Lower number](/assets/images/firstGuess.JPG)

###

- Example when the player guessed a higher number
  

![Higher number](/assets/images/secondGuess.JPG)

###
- Play again 
  - When the game is finished the user will be prompeted to press '1' to play again or 'q' to exit the game.
###
![Play Again](/assets/images/playAgain.JPG)

  ####
  - Exit game 
    - once the player press 'q' to exit it will be showed a message "Thank You" and the game will finish.
    ####
  ![Exit](/assets/images/ExitGame.JPG)

  ####
- Input validation and error checking 
  - if the player type invalid input it will be validated
  ###
![Validation](/assets/images/InputValidation.JPG)

####
![Validation2](/assets/images/InputValidation2.JPG)
### Testing

I have tested the project doing the following

   - passed on [PEP8](http://pep8online.com/). 
   - Tried invalid inputs 
   - Tested on Heroku and the Terminal.

   ![test](/assets/images/pep8Test.JPG)

  #### Bugs
   - Fixed error adding images to readme file, files added to a wrong folder.
 

  #### Remain Bugs
  - No bugs remain



 #### Validator Testing 
 - [PEP8](http://pep8online.com/)
   - Initially found a whitespace that where fixed, no Warnings left.
   ![Test](/assets/images/pep8Error.JPG)
 
   
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
   

