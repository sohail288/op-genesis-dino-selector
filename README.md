# Operation Genesis: Dino Selector
This tool has been created to be used alongside mods that increase the number of different dinos in the game.
It solves the problem of manually editing the `DinoList.ini` and `FslHunt.ini` files. Currently, the only mod that I use it with is the [Forgotten Mod ](http://www.moddb.com/mods/jpog-the-forgotten) . 

Instructions:

There is a release available in the releases section on github ([found here](https://github.com/sohail288/op-genesis-dino-selector/releases)). It is windows only.  Other releases can be built using the source since the implementation is platform agnostic.

1) Download the release (sorry about the large file size, electron isn't meant for small apps...).

2) unzip the archive

3) run the executable called `op-gen-dinolist`

4) there is a directory selector. Use it to select the output directory. __If you choose the jpog directory, you may need to re-run the executable with administrative privileges.__

5) At this point, you can choose your dinos using the selection input. Each time you select a dino, the selected dinos indicator (on the right of the selection input) goes up.  Each time you deselect a dino, the selection indicator decrements. Make sure you choose less than 40 dinos. __The app does not stop you__ from choosing more than 40 dinos.

6) once you done, click on save.  This will output the correctly formatted `FslHunt.ini` and `DinoList.ini` files to the selected destination. If you chose the actual jpog directory, you are done at this point. Play the game and hope for the best, __otherwise, move the generated files to the jpog directory__

7) a green banner that says success should appear on the top of the app if all goes well.


There are a number of ways to make this project better. 

possible features to implement:

* fill rest: select your dinos and randomly select remaining dinos
* preselect dinos already in `DinoList.ini` files in the chosen directory
* implement in a lighter weight gui toolkit (possibly tkinter or wxwidgets)
* limit the dinosaurs chosen automatically
* .... let me know

Let me know if any of these are useful


screenshot (yes, yes, super basic):
![screen shot main](https://github.com/sohail288/op-genesis-dino-selector/blob/master/docs/opgen_screen.jpg?raw=true)
