from TextAdventureSYS import typewriter
typewriter("This is a typewriter test. The delay between characters should be 0.3 because no delay was specified.")
typewriter("This is a typewriter test. The delay between characters should be 0.1.", 100)
typewriter("Line1")
typewriter("Line2: delay=100, endLine=False ", delay=100, endLine=False)
typewriter("Line2")
typewriter("This is all ", endLine=False)
typewriter("in one line ", endLine=False)
typewriter("because endLine was set to False")