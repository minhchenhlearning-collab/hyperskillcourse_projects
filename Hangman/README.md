This project is about creating Hangman game, which is a game of guessing word
This game mainly involves:
1/ Opening the menu command for user to choose between play, exit, results
1.1/ If results -> show how many winning/losing times
1.2/ If exit -> quit
1.3/ If play -> start the game
2/ The game starts by setting a word for guessing from a fixed list of words
3/ Then prompt for user input, checking for error
4/ Users are allowed to input only 1 lowercase word at a time
5/ If it's true -> reveal the word, otherwise, +1 mistake. But if the user guess 1 word for more than 1 times, tell them that they repeat themselves and do not increase mistakes
6/ The game ends when users successfully guess the word within making less than 8 mistakes
