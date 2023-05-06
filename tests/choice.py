from tests import choice
playerChoice = choice("As you enter the next room, the lights flicker. What will you do?", ["Enter the next room", "Hide in the closet.", "Do nothing."])
match playerChoice:
    case 1:
        print("You were killed by Rush. Game over!")
    case 2:
        print("You hid from Rush. You live another room.")
    case 3:
        print("Bruh, you went afk, that's cringe. You were killed by Rush. L+Bozo+Noob+SkillIssue")