# ATM Project

**Written by Jinho Lee (jl5027@columbia.edu)

[ATM.py](https://github.com/JinhoLee93/Personal_Projects/blob/main/ATM/atm.py) simulates for the user part of the modern banking system using ATM (Automatic Teller Machine).
It contains basic bank transaction functions such as checking balance, depositing and withdrawing.

User executes program entering command below in terminal
- python3 atm.py

1. ATM simulation starts with the user setting up his/her card with a PIN number and balance.
2. ATM receives the card and checks for the correct PIN number and then moves onto the main menu. 
3. At the main menu, are three options for the user to choose, which are built in ATM class. 
4. If the user enters C, checking balance begins.
5. If the user enters D, depositing begins.
6. If the user enters W, withdrawing begins.
7. After each action, ATM automatically shows the updated balance.
8. If the user would like to quit the program at any point, enter Q.
9. Error handling, such as invalid input or wrong entrance, is in place. 
