# RangleRig
A WIP Maya Script for easily creating usable and functional character rigs effortlessly

Please Note that this is a work in progress and you may expericence unfinished features and bugs.

Thanks
Benjamin Wilkinson

Setting Up Rangle Rig

  1. Download RangleRig as zip
  2. Copy the RangleRig folder to C:\Users\%user%\Documents\maya\2016\scripts
  3. From the shelves folder copy the shelfRangleRig.mel file to C:\Users\%user%\Documents\maya\2016\prefs\shelves
  4. Start Maya and click the first icon on the RangleRig shelf 'IRR' (This may open a bunch  of Windows just close them)


Quick Start Guide
  
  1. On the RangleRig Shelf click the last icon 'RRUI' this will open the Rangle Rig Rig Creation UI
  2. Start by naming the Rig (You will get and error if you do not name your rig)
  3. In the UI under 'Premade Rigs' click 'Setup Human Biped', this should create some joint arranged to make a human in t-pose
  4. Translate and Roatate this joints to fit your character.
  5. When you are ready click the 'Create Rig' button and Rangle Rig will create a rig with all the controls.
  
  At the minute there are still issues with various aspects of the rig that are currently being fixed.

Using a Rangle Rig rig
  
  -The visibilty and setting for any created rig are current stored under the top node of the rig yourCharacterName_rig in their     respective groups eventually this will be controlled by an animation UI tool
  
  -Ik Foot roll controls are located on ik foot control
  
  Planned Features
  
  - Hand and Face rigs
  - Animation UI
  - Control Editor UI
  - Quadruped Preset
  - Support for building custom rigs or adding additional body parts to a preset rig
  - Saving custom rigs as a preset
  - Addtional body parts (e.g tails, wings, tentacles etc..)
