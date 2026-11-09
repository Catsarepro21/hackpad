# Macropad case — PCB fit revision

Use the new Macropad model and files, not the original Top Half / Bottom Half exports.

## Print files
- Macropad_Base_PRINT.stl: already sitting on its flat outside base; supports off.
- Macropad_Top_PRINT.stl: inverted and placed at Z=0; use removable supports under the recessed switch panel and other overhangs. Keep supports out of the small holes where possible. The rear panel is raised to clear the encoder bodies.
- Insert_Test_4.3_4.4_4.5mm.stl: holes run left-to-right from 4.3 to 4.5 mm. The case uses the middle, 4.4 mm size. Test your inserts in this coupon first.

Suggested starting settings: 0.2 mm layers, 4 walls, 5 top/bottom layers, 20% infill, PLA or PETG. Verify supports and hole quality in your slicer before printing.

## Hardware and assembly
4 M3 x 16 mm screws, 4 M3 inserts measuring 5 mm outside diameter x 4 mm long.
The linked listing's selected variant could not be read; these dimensions follow the supplied M3x5x4 specification. Confirm the actual inserts match before heating them in.
Heat-set the inserts into the four 4.4 mm pockets on the INSIDE of the top. Set them flush with the inside boss ends; do not push them up to the outer surface.
Place the PCB on the four base standoffs. Carefully engage the switches with the six plate openings and guide the encoder shafts through the two round openings. Make sure switch clips engage before tightening. Install the screws from underneath through the base and PCB holes into the inserts. Tighten lightly.
Screws project 3.4 mm into the 4 mm inserts. Heads sit in shallow 6.2 mm diameter recesses and protrude below the base; use stick-on feet if wanted. Screw head style was not supplied, so verify head diameter fits the recess.
USB connector is at the rear access opening. The reset button is serviceable by removing the base.

## Modeled checks
Outer footprint: 79.2 x 72.65 mm. Assembled body height: 20.2 mm excluding screw heads, switches, shafts and keycaps.
PCB: 73.6 x 67.05 x 1.51 mm from the current Onshape export, with 0.4 mm clearance per side.
Main plate: 1.5 mm, six 14.4 mm square openings on the actual 19.05 mm switch pitch. Top surface lies 0.1 mm below the modeled switch flange.
Rear panel: two 8.2 mm encoder shaft openings with body relief underneath.
Walls and base floor: 2.4 mm. Four PCB mounting holes follow the actual irregular hole positions, not a symmetric corner pattern.
No solid intersections were found against any of the 110 exported PCB/component solids. Both case solids are valid and the STL meshes have no open or nonmanifold edges. The two halves meet without overlapping.
Keycap check uses an 18.6 x 18.6 mm envelope with its bottom at Z=7 mm or above. Actual keycaps were not supplied; unusually large or low-skirt keycaps are not verified. Knobs and USB cable plug dimensions were not supplied.

This is a checked CAD revision for a first print, not a physically tested enclosure. Print the insert coupon first; actual printer tolerances, switch clip retention, keycaps, solder joints and the selected insert variant still require a physical fit check.
