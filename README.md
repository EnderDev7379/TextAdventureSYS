# Python Module TextAdventureSYS

## What is it?

___
TextAdventureSYS is a module created by Ender to make creating Text Adventures easy, so even complete beginners in Python can make ther own Text Adventures.

## How to use it?

___

### Importing

First of all, like with any module, you need to import TextAdventureSYS:

```python
import TextAdventureSYS
```

### Start Menu

There is an optional start menu in the module in which you can set the name, author and if there is an options menu (which is currently in development and dosen't work):

```python
import TextAdventureSYS

TextAdventureSYS.startMenu(GameTitle = str, GameAuthor = str, hasOptions = bool)
```

Again this start menu is completly optional and you can choose to jump directly into the adventure without any Start Menu if you don't call the `TextAdventureSYS.startMenu()` function.  

### Typewriter

There is a Typewriter function which was the first function created, actually, it was the inspiration to make TextAdventureSYS, and this is how you use it:

```python
import TextAdventureSYS

TextAdventureSYS.typewriter(text = str, delay = int, endLine = bool)
```

### Choice

The choice function gives the player a choice and then saves the choice number in a variable called choiceOutcome, the choice function is called and choiceOutcome is accesed like this:

```python
import TextAdventure 
```

## Examples

___

### Example 1

Here is a little example with everything that you learned:

```python
import TextAdventureSYS

TextAdventureSYS.startMenu("Spooky Spooktober Game", "Ender", False)
TextAdventureSYS.typewriter("Your are walking through a looooong hallway, and suddendly...", 0.3, True)
TextAdventureSYS.typewriter("...all the light went out.", 0.5, True)
```

This will print:

```
Spooky Spooktober Game by Ender
Type start to enter the adventure
Type help for commands
Made with TextAdventureSYS by Ender
>>
```

As long as you enter the command `help` it will print `Help currently unaveable`, clean the screen and then print the start menu again.  
If you enter the command `start` it will print `starting the adventure` slowly with a delay of 0.5 seconds and clean the screen, then the script will continue to the typewriter functions, which will print:

```
You are walking through a looooong hallway, and suddendly...
```

with a 0.3 second delay between characters and then in a new line:

```
...all the lights went out.
```

with a 0.5 delay between characters.