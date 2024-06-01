## Project State
Functionnal : you can generate a password of desired length from a .exe file and choose with check boxes what characters the password has.
I want to learn making desktop application as well as web dev but I will prioritize the latest so this project may stay paused like that for some time. 
# Project Motivation
- I know there exist reliable and secure software that generates and store securately passwords, I would recommend to check : https://github.com/Lissy93/awesome-privacy and Dashlane or Bitwarden for your personnal use.
- However, I like creating applications with UI and I want to improve at it. So I need no more reasons not to try to make (some) things myself 🤠 ! 
## Project Goals
1. Create a basic .exe app to generate random passwords of desired length ✅
2. Add settings property such as choosing if the password has numbers, uppercase, lowercase, special characters.


## Project Result
Currently (v2) we can generate a 'customized' password. We can choose its length and some of the characters that it posess (lower, uppercase, numbers, special characters).
It was exactly what I wanted.
This is the current result of this project :
![Version 2](v2.png)


### Improvement
- I looked upon refactorizing the code (the part with the character customization options for the password) but it appeared that it created more complexity than keeping it like that. So in the end, as the application will not scale more than what it currently is I decided to keep it like that.
- However this project is a good opportunity to test automatic testing with pytest and github so I will try to setup such a system. 