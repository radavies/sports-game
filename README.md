# sports-game
Silly Sports Sim Game

### What is the game?

* What is your role?
  * Owner - you can buy upgrades, players, managers etc but the sim is stat based
  
### What UI do we need?

* Dashboard
  * Where the game is played from - opens up other UIs as required
  * Player overview
  * Club overview (finances, upgrades etc)
  * Calendar (upcoming events)
  * League table
  * "Inbox" / social media
  * Advance time 

* Save / Load


### ToDo
* Save / load data structures etc

### Ideas

* Sound? (goals scored, crowd noise)
* board expectations?
* Add managers
* Add European Teams
* Add Rest of World Teams
* Injuries / sickness
* Team modifiers - fired up, on a run, on a bad run etc
* Should the game run on a proper calendar? (if so need to refactor the ages to be DoBs)

### Doc Links

* https://doc.qt.io/qt.html
* https://doc.qt.io/qtforpython-6/api.html
* https://www.riverbankcomputing.com/static/Docs/PyQt6/
* If PyQt thread debugging doesn't work - https://youtrack.jetbrains.com/issue/PY-46891
  * "I modified the pydev_monkey_qt.py by adding pyside6 to the import "trys". This works, as long as you do not use numpy. Once you do, you get the error specified here:"
  * Also add PYDEVD_PYQT_MODE=pyqt6 to the env variable of debugger