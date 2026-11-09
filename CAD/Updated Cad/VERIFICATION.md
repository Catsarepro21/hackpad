# Verification and ordering status

The case was checked against an exported PCB model and the repository's KiCad board outline and mounting-hole coordinates. The PCB outline is 73.6 x 67.05 mm and the four mounting-hole coordinates agree with the case model. The case includes 0.4 mm nominal clearance per side around the PCB and 14.4 mm switch openings.

The local solid intersection check reported no overlaps with the 110 exported component solids in the assumed placement. This does not verify the actual positions of the instances in Onshape Assembly 2. That assembly displayed import warnings and two invalid instances during inspection. The STEP export contained two invalid encoder solids; their shape and any checks involving them are not fully reliable until the imports are repaired and rechecked. The physical case, insert retention, switch retention, cable plug, and actual keycaps have not been tested.

The STEP and STL case solids passed validity and closed-mesh checks. The top requires support when printed in its provided orientation. Check the heat-set inserts against the included test piece before ordering a final case.

KiCad 10.0.6 DRC on the repository PCB reported 24 warnings and 0 unconnected items: silkscreen clearances and a locally unavailable footprint library. The checked-in Gerber archive's copper and mask layers differ from fresh exports of the current board; the outline and silkscreen layers matched after removing generator and date metadata. The drill files were not compared. Do not assume the existing archive matches the current PCB: regenerate and review the full fabrication package, including drills, before placing an order.

The actual M3 screw-head dimensions, selected insert variant, USB cable plug, and keycap shape were not supplied or physically measured. This revision is a candidate for a test print, not a guarantee of manufactured fit.
