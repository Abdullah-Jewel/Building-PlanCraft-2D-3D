# Guide articles. Each: slug, title, description, body (HTML). Written for Bangladeshi home builders; figures are planning-level ranges.
A = []
def art(slug, title, desc, body):
    A.append(dict(slug=slug, title=title, desc=desc, body=body))

art('cost-to-build-a-house-in-bangladesh',
 'How much does it cost to build a house in Bangladesh?',
 'A practical way to estimate construction cost per square foot in Bangladesh, what drives it, and how to build your own estimate.',
 """
<p>Almost every plot owner asks the same first question: how much will the building cost? There is no single answer, but there is a sound method. Cost is built from quantities (how much concrete, steel, brick and finish the plan needs) multiplied by local prices. The result is then divided by the built-up area to give a cost per square foot (sft).</p>
<h2>Why a flat "per sft" rate misleads</h2>
<p>You will hear rates such as "Tk 2,500 to Tk 3,500 per sft" for ordinary residential work. Treat them as a starting guess only. Two houses of the same floor area can differ by 40% or more because of:</p>
<ul>
<li><b>Foundation:</b> soft soil, a high water table or a tall building needs piles or a raft, which costs far more than simple footings.</li>
<li><b>Number of floors:</b> columns, beams and steel grow quickly above four storeys.</li>
<li><b>Finish level:</b> tiles, doors, windows, sanitary fittings, paint and electrical points make up a large share of the budget.</li>
<li><b>Market prices:</b> rod and cement prices move through the year and differ between Dhaka, Chattogram, Sylhet and smaller towns.</li>
</ul>
<h2>The main cost groups</h2>
<ol>
<li><b>Earthwork and foundation:</b> excavation, footings or raft, plinth beams.</li>
<li><b>RCC frame:</b> columns, beams, slabs and stairs, which carry most of the steel and cement.</li>
<li><b>Brick masonry and plaster.</b></li>
<li><b>Floors, wall tiles, paint and waterproofing.</b></li>
<li><b>Doors, windows, grills and railings.</b></li>
<li><b>Electrical, plumbing and sanitary work.</b></li>
<li><b>Utilities:</b> septic tank, water tank, connections, and a lift in taller buildings.</li>
<li><b>Labour, overhead and a contingency</b> for price changes and surprises.</li>
</ol>
<h2>Building a better estimate</h2>
<p>Draw the plan to scale, take off the quantities, and price each group with quotes from your own dealers. The <a href="../app/">PlanCraft 3D planner</a> does this for you: it measures walls, floors, openings, columns and pipes from your drawing, and its cost screen lets you edit every unit price and see the total in taka, dollars, rupees or euros.</p>
<h2>Keep a contingency</h2>
<p>Add at least 5% for price changes, and more if you plan to build over many months. Cement and steel prices can move several percent in a season.</p>
<p class="note">This is a planning guide, not a quotation. Confirm structural design and final cost with a licensed engineer and local contractors before you commit money.</p>
""")

art('standard-room-sizes-for-bangladeshi-homes',
 'Standard room sizes for Bangladeshi homes (in feet)',
 'Comfortable size ranges for bedrooms, kitchens, bathrooms and living rooms, with notes on furniture clearances.',
 """
<p>Good room sizes come from the furniture and the movement space around it, not from a rule of the same number for every plot. The ranges below are common starting points for apartments and houses in Bangladesh. Adjust them to your plot and family.</p>
<h2>Typical sizes</h2>
<table>
<tr><th>Room</th><th>Comfortable size (ft)</th><th>Notes</th></tr>
<tr><td>Master bedroom</td><td>12 x 14 to 14 x 16</td><td>Double bed plus wardrobe and 2 ft of walking space</td></tr>
<tr><td>Child or guest bedroom</td><td>10 x 12 to 12 x 13</td><td>Single or double bed, small wardrobe</td></tr>
<tr><td>Living room</td><td>12 x 16 to 14 x 20</td><td>Sofa set, TV unit and a clear route to other rooms</td></tr>
<tr><td>Dining area</td><td>10 x 10 to 10 x 12</td><td>Four to six seat table with chair pull-out space</td></tr>
<tr><td>Kitchen</td><td>8 x 10 to 10 x 12</td><td>Counter, sink, gas point, fridge and ventilation</td></tr>
<tr><td>Attached bathroom</td><td>5 x 7 to 6 x 8</td><td>Commode, basin and shower with a dry and wet zone if possible</td></tr>
<tr><td>Common bathroom</td><td>5 x 6 to 6 x 7</td><td>Place near the living area</td></tr>
<tr><td>Corridor</td><td>3 to 3.5 wide</td><td>Two people should be able to pass</td></tr>
<tr><td>Balcony</td><td>4 to 5 deep</td><td>Wide enough for a chair</td></tr>
</table>
<h2>Clearances that make a room feel right</h2>
<ul>
<li>Leave about 2 to 2.5 ft beside and at the foot of a bed.</li>
<li>Keep 3 ft between a sofa and a TV unit at the very least, and more for a bigger screen.</li>
<li>Door swings should not hit a bed, wardrobe or another door.</li>
<li>Every habitable room needs a window to the outside for light and cross ventilation.</li>
</ul>
<h2>Test your plan before building</h2>
<p>Drop real furniture into a plan and walk through it. In the <a href="../app/">PlanCraft 3D planner</a> you can place beds, sofas, counters and sanitary fittings at their real sizes, then switch to first-person view to feel the space.</p>
<p class="note">Sizes are guidance only. Local building rules set minimum room areas and window sizes, so check with your city authority.</p>
""")

art('estimating-cement-sand-and-bricks',
 'How to estimate cement, sand, stone chips and bricks',
 'The simple volume method engineers use to estimate concrete materials and brick quantities, with worked numbers.',
 """
<p>Material estimates follow one method: find the volume of work, apply the mix proportions, then add wastage. The same method works for a footing, a slab or a wall.</p>
<h2>Concrete: from volume to bags</h2>
<p>Concrete is mixed by volume of cement : sand : stone chips. A common structural mix is 1 : 1.5 : 3. Because dry materials fill gaps when wet, you multiply the wet volume by about 1.54 to get the dry volume.</p>
<ol>
<li>Find the wet volume. For a slab 20 ft x 15 ft x 5 in thick: 6.1 m x 4.6 m x 0.127 m, about 3.5 m³.</li>
<li>Dry volume = 3.5 x 1.54, about 5.4 m³.</li>
<li>The mix total is 1 + 1.5 + 3 = 5.5 parts. Cement is 1/5.5 of the dry volume, about 0.98 m³.</li>
<li>A 50 kg bag is roughly 0.035 m³, so cement is about 28 bags.</li>
<li>Sand is 1.5/5.5 of the dry volume, about 1.5 m³ (about 52 cft). Stone chips are 3/5.5, about 2.9 m³ (about 103 cft).</li>
</ol>
<p>Add 5 to 10% for wastage and spillage. In round numbers, a cubic metre of 1 : 1.5 : 3 concrete uses about 8 bags of cement.</p>
<h2>Brick walls</h2>
<p>A standard first-class brick wall of 5 in thickness needs roughly 450 to 500 bricks per cubic metre of wall including mortar joints. Subtract the area of doors and windows before you multiply by the wall thickness. Mortar for the wall is usually 1 : 4 cement to sand.</p>
<h2>Plaster</h2>
<p>Plaster 12 to 15 mm thick on both faces of a wall uses a 1 : 4 cement-sand mortar. Estimate the volume as wall area x thickness, then use the same dry-volume method.</p>
<h2>Let the planner do the arithmetic</h2>
<p>The cost screen in the <a href="../app/">PlanCraft 3D planner</a> carries these steps through your whole drawing and lists the totals in bags, cft and pieces, so you can compare it with a contractor's number.</p>
<p class="note">These are estimation rules. Mix design, site conditions and the engineer's drawings decide the quantities you actually order.</p>
""")

art('reinforcement-steel-by-bar-diameter',
 'Reinforcement steel by bar diameter: 10, 12, 16 and 20 mm',
 'How much each rebar diameter weighs, how many 12 m bars you need, and where each size is used in a building.',
 """
<p>Steel is the largest single cost in the frame of a building, and it is bought by weight. Knowing the weight per metre of each diameter lets you check a bar schedule or a supplier's delivery.</p>
<h2>Weight per metre</h2>
<p>The unit weight of a round bar in kg per metre is the diameter in mm squared divided by 162 (about). This gives:</p>
<table>
<tr><th>Diameter</th><th>kg per metre</th><th>kg per 12 m bar</th><th>Bars per tonne</th></tr>
<tr><td>10 mm</td><td>0.617</td><td>7.4</td><td>about 135</td></tr>
<tr><td>12 mm</td><td>0.888</td><td>10.7</td><td>about 94</td></tr>
<tr><td>16 mm</td><td>1.58</td><td>18.9</td><td>about 53</td></tr>
<tr><td>20 mm</td><td>2.47</td><td>29.6</td><td>about 34</td></tr>
</table>
<h2>Where each size is used</h2>
<ul>
<li><b>10 mm:</b> stirrups and ties in columns and beams, and slab reinforcement in light work.</li>
<li><b>12 mm:</b> slab bars, secondary beam bars and stair reinforcement.</li>
<li><b>16 mm:</b> main bars in beams and columns for ordinary buildings.</li>
<li><b>20 mm:</b> heavily loaded columns, footings and the lower floors of taller buildings.</li>
</ul>
<p>The final sizes and spacing always come from the structural engineer's drawings. They depend on loads, spans and the number of storeys.</p>
<h2>Counting bars and wastage</h2>
<p>Divide the weight needed by the weight of a 12 m bar to get the number of bars. Add wastage for cutting, laps and bending, usually 3 to 7%. Binding wire is about 1% of the steel weight.</p>
<h2>See it for your own plan</h2>
<p>The cost screen of the <a href="../app/">PlanCraft 3D planner</a> splits the estimated steel for footings, columns, beams, slabs and stairs into 10, 12, 16 and 20 mm bars, with a 12 m bar count and the cost at your own price per kg.</p>
<p class="note">The split in the planner is a planning estimate based on typical ratios. It is not a bar bending schedule. Use your engineer's schedule when you buy and cut steel.</p>
""")

art('setback-and-plot-boundary-basics',
 'Setbacks and plot boundaries: what to know before you draw',
 'What a setback is, why it matters before you start a plan, and how to check your plot against local rules.',
 """
<p>A setback is the open space you must leave between your building and the plot boundary. It gives light, air, fire access and room for neighbours. Drawing the plan without it is one of the commonest reasons for a rejected approval.</p>
<h2>Why setbacks exist</h2>
<ul>
<li>Light and ventilation reach every side of a building.</li>
<li>Fire services and rescue can reach the building.</li>
<li>Services such as drains and cables have a route.</li>
<li>Neighbours keep privacy and are not built against.</li>
</ul>
<h2>What decides your setbacks</h2>
<p>Setbacks vary with the authority, the plot size, the building height, and the width of the road in front. In Dhaka the rules are administered by RAJUK; other cities and municipalities have their own bodies. Larger and taller buildings usually need larger setbacks than a small low-rise house. Always get the current rule from the authority that approves your drawing, not from a friend's plan.</p>
<h2>A simple workflow</h2>
<ol>
<li>Get your survey measurements and the boundary lengths from the land record or a surveyor.</li>
<li>Note which side faces the road.</li>
<li>Ask the approving authority for the setback on the front, rear and sides for your plot and height.</li>
<li>Draw the plot, offset the lines inward by the setback, and keep all walls inside the inner line.</li>
</ol>
<h2>Check it in the planner</h2>
<p>The <a href="../app/">PlanCraft 3D planner</a> has a plot and setback tool. You enter the plot size, choose the road side, set the front, rear and side distances, and the plan shows the boundary and the setback line as dashed lines. Any wall that crosses the setback is circled in red.</p>
<p class="note">The planner does not know the rules in your city. Use the numbers your authority gives you, and have the final drawing checked by a licensed architect.</p>
""")

art('column-grid-and-structural-basics',
 'Column grid basics: where columns go and how far they span',
 'Why columns go at corners and junctions, how span affects beam size, and when you need an engineer.',
 """
<p>In an RCC frame, columns carry the weight of floors down to the foundation. Where you place them affects the cost, the room layout and the look of the house.</p>
<h2>Where columns normally go</h2>
<ul>
<li>At the outside corners of the building.</li>
<li>Where walls meet (junctions and T-junctions).</li>
<li>Along long walls, so that no beam spans too far.</li>
<li>Beside the staircase and lift shaft.</li>
</ul>
<h2>Span and cost</h2>
<p>A longer span between columns needs a deeper beam and more steel. Many residential buildings keep spans to around 12 to 15 ft in one direction, but the right value depends on the loads and the engineer's design. Moving a few columns on paper at the planning stage is cheap. Moving them after the foundation is cast is not.</p>
<h2>Column size</h2>
<p>Small low-rise houses often use columns such as 10 x 12 in or 12 x 15 in. Taller buildings need larger columns at the lower floors. The size follows the number of storeys, the span, and the concrete and steel grade, so it is the engineer who finalises it.</p>
<h2>Hide columns in walls</h2>
<p>Place columns so they sit inside walls or at corners. A column in the middle of a bedroom wastes space and spoils furniture layout. Aligned columns on every floor also give a cleaner load path.</p>
<h2>Try a layout</h2>
<p>The <a href="../app/">PlanCraft 3D planner</a> can generate a column grid automatically at wall corners, wall junctions and where a span is longer than your limit. You can then move, delete or add columns and see the effect in 2D, 3D and in the cost estimate.</p>
<p class="note">A generated grid is a planning aid only. It is not structural design. A licensed structural engineer must design and sign off the frame.</p>
""")

art('sun-orientation-and-ventilation',
 'Sun, orientation and ventilation for a house in Bangladesh',
 'How to place rooms, windows and verandas for sun and breeze in Bangladesh, and how to test it with a sun path.',
 """
<p>Bangladesh lies at around 21 to 26 degrees north. The sun is high in summer, lower in winter, and in the hot months it rises and sets slightly north of east and west. These facts shape a comfortable layout.</p>
<h2>Which side gets what</h2>
<ul>
<li><b>South side:</b> gets winter sun, and a short overhang shades it in summer when the sun is nearly overhead. Good for living rooms and bedrooms.</li>
<li><b>West side:</b> receives strong afternoon heat. Put bathrooms, stairs, storage or a veranda here, and keep windows small and shaded.</li>
<li><b>East side:</b> gives gentle morning sun. Good for kitchens and bedrooms.</li>
<li><b>North side:</b> has soft, steady light. Good for study rooms and kitchens, but it gets little winter sun.</li>
</ul>
<h2>Breeze</h2>
<p>In summer, the prevailing wind often comes from the south or south-east. Open windows on that side, and put an opening on the opposite wall so air passes through the room. A window with no matching opening on another wall brings little breeze.</p>
<h2>Shade and rain</h2>
<p>Deep verandas, chajja (sunshades) and trees reduce heat. Heavy monsoon rain means window and door heads need drip details and proper waterproofing on the roof.</p>
<h2>Test a design with a sun path</h2>
<p>The <a href="../app/">PlanCraft 3D planner</a> has an interactive north arrow and sun controls. Rotate north to match your plot, choose a month and the time of day, and the 3D view shows the sun angle and shadows. Try the summer solstice at 3 pm to see how much heat a west wall will take.</p>
<p class="note">Orientation is only one factor. Plot shape, neighbours and road access often decide the layout, so treat these points as guidance.</p>
""")

art('plumbing-septic-tank-and-drainage-layout',
 'Plumbing, septic tank and drainage layout basics',
 'How to group wet rooms, route waste pipes to a septic tank and soak pit, and place an overhead water tank.',
 """
<p>Plumbing is cheapest and most reliable when wet areas are planned together at the start. Bathrooms and the kitchen stacked in the same place on every floor keep pipes short.</p>
<h2>Group wet areas</h2>
<p>Put bathrooms back to back or one above another. They can then share a vertical drainage stack. Fewer stacks mean fewer penetrations through slabs and less cost.</p>
<h2>Waste and water lines</h2>
<ul>
<li><b>Waste (soil and drain) pipes:</b> usually 3 to 4 in PVC, sloped continuously towards the stack. Avoid sharp bends.</li>
<li><b>Water supply pipes:</b> smaller, pressure-rated pipes (CPVC or PPR) from the overhead tank to taps, showers and the kitchen.</li>
<li><b>Vent pipes:</b> keep the drainage system breathing so water traps do not empty.</li>
</ul>
<h2>Septic tank and soak pit</h2>
<p>Where there is no sewer line, waste flows to a septic tank and then to a soak pit. The tank is sized by the number of users and the desilting interval, and it needs a safe distance from any drinking water source such as a tube well. Tank location also needs space for a vehicle or workers to reach the manhole for cleaning.</p>
<h2>Overhead water tank</h2>
<p>Place the tank on the roof, over a column or wall line that can carry its weight when full, and close to the water risers. Plan a pump and overflow pipe.</p>
<h2>Draw it first</h2>
<p>The <a href="../app/">PlanCraft 3D planner</a> has a plumbing layer. Place inlet points, waste outlets, drainage stacks, septic tank, soak pit and the overhead tank, then use the pipe tool to join them. Water pipes appear in blue and drains in brown, and the cost estimate counts the pipe length you drew.</p>
<p class="note">Tank sizes, pipe diameters and distances are set by local regulation and a plumbing designer. Use this guide for planning only.</p>
""")

art('staircase-design-and-glass-railings',
 'Staircase design: riser, tread, landing and glass railings',
 'The comfortable stair proportions, how landings work, and what to check when you choose a glass railing.',
 """
<p>Stairs are used many times a day, so small errors in their proportions are felt every time. A comfortable stair has steps of equal height and depth, enough headroom, and a safe handrail.</p>
<h2>Riser and tread</h2>
<ul>
<li><b>Riser</b> (the height of one step): about 5.5 to 7 in (140 to 175 mm) is comfortable for homes.</li>
<li><b>Tread</b> (the depth of one step): about 10 to 11 in (250 to 280 mm).</li>
<li>A handy check: twice the riser plus the tread should fall near 24 to 25 in (about 610 to 640 mm).</li>
<li>All steps in one flight must be the same height.</li>
</ul>
<h2>Width and headroom</h2>
<p>A home stair is often 3 to 3.5 ft wide. Allow clear headroom of about 7 ft (2.1 m) measured above the line of the step edges.</p>
<h2>Choosing the shape</h2>
<ul>
<li><b>Straight:</b> simplest and cheapest but needs a long space.</li>
<li><b>L-shaped or U-shaped with a landing:</b> turns the flight, saves length and gives a resting point.</li>
<li><b>Winder, curved or spiral:</b> save floor area, but are harder to use and often need special design.</li>
</ul>
<h2>Glass railings</h2>
<p>Tempered or laminated glass with a stainless steel handrail looks light and lets light through. Check the glass type and thickness with the supplier, the fixing method, and the height of the rail. Keep gaps small enough that a child cannot pass through.</p>
<h2>See it in 3D</h2>
<p>The <a href="../app/">PlanCraft 3D planner</a> offers straight, L, U, winder, curved and spiral stairs with glass railings. Switch to first-person view and walk up the flight to feel the proportions before the concrete is poured.</p>
<p class="note">Check the stair rules in your local building code. Stair dimensions and railing height are safety items.</p>
""")

art('planning-a-multi-storey-building',
 'Planning a multi-storey building: what changes above four floors',
 'Why foundation, columns, lifts, fire safety and approvals change as a building gets taller, and how to prepare a plan.',
 """
<p>Adding floors is not a simple repeat of the ground floor. The loads at the base multiply, and new rules apply as the building grows taller.</p>
<h2>What changes with height</h2>
<ul>
<li><b>Foundation:</b> more load needs a larger footing, a raft or piles. Soil testing becomes essential.</li>
<li><b>Columns and beams:</b> lower-floor columns grow larger and carry more steel.</li>
<li><b>Lateral forces:</b> wind and earthquake matter more, and shear walls or a core may be needed. Bangladesh lies in a seismically active region.</li>
<li><b>Lift:</b> usually expected beyond about five or six storeys, and it needs a shaft, machine room and pit.</li>
<li><b>Fire safety:</b> more exits, a protected staircase, and water supply for firefighting.</li>
<li><b>Approvals:</b> taller buildings face stricter setbacks and review.</li>
</ul>
<h2>Keep the plan repeatable</h2>
<p>Repeat the stair, lift and wet areas in the same position on every floor. Stack columns directly. This keeps cost down and the load path simple.</p>
<h2>Prepare before you hire</h2>
<ol>
<li>Draw each floor and check the stair and lift positions.</li>
<li>Decide the roof use: terrace, water tank, stair cover room.</li>
<li>Run a rough cost to see whether the budget supports the height.</li>
<li>Hire a structural engineer and get a soil test before you finalise.</li>
</ol>
<h2>Use floors in the planner</h2>
<p>The <a href="../app/">PlanCraft 3D planner</a> supports ten or more floors, with a floor selector, copy-floor-up, a roof with a parapet and stair cover room, and a cost estimate that switches to a raft foundation and heavier steel as the building rises.</p>
<p class="note">Do not build multi-storey from a planning tool. A licensed structural engineer must design the frame and foundation for the actual soil.</p>
""")

art('how-to-use-plancraft-3d',
 'How to use PlanCraft 3D: a quick start',
 'A step-by-step guide to drawing walls, placing doors and furniture, switching floors, and estimating cost in PlanCraft 3D.',
 """
<p>PlanCraft 3D runs in your browser, on a phone or a computer, and needs no sign-up. Your drawings stay on your own device.</p>
<h2>1. Start a plan</h2>
<p>Open the <a href="../app/">planner</a>. Choose <b>Create my plan</b> and enter the width and length of your plot in feet or metres, or open the sample house to look around.</p>
<h2>2. Draw walls</h2>
<p>Pick the wall tool, then click and drag. Walls can be any angle, down to 0.01 degree, and snap to neighbouring walls. Use Snap to keep them neat.</p>
<h2>3. Add doors, windows and floors</h2>
<p>Choose the door or window tool and click on a wall. Use the floor zone tool to name rooms and choose floor finishes such as tile, wood or concrete.</p>
<h2>4. Place furniture and fittings</h2>
<p>Open the catalogue to add beds, sofas, counters, bathroom fittings, lights and sockets. Rotate with the R key or the handle.</p>
<h2>5. Add floors and a roof</h2>
<p>Use the floor selector to add storeys, copy a floor up, and choose a flat, hip or gable roof.</p>
<h2>6. Look in 3D</h2>
<p>Switch to 3D and orbit, or use first-person to walk through. Show one floor, all floors, or only up to a chosen floor. The quality setting lowers the resolution on slower phones.</p>
<h2>7. Engineering tools</h2>
<ul>
<li><b>Column grid:</b> generate columns at corners, junctions and long spans.</li>
<li><b>Plot and setbacks:</b> draw the boundary and setback lines.</li>
<li><b>North and sun:</b> test shadows by month and hour.</li>
<li><b>Plumbing layer:</b> place fixtures and draw pipes.</li>
<li><b>Dimension tool:</b> drag to measure.</li>
</ul>
<h2>8. Estimate the cost</h2>
<p>Open the cost screen to see totals for foundation, frame, masonry, finishes and services. Edit any unit price, switch currency, and read the rebar schedule by diameter. Download the result as a CSV file.</p>
<h2>9. Export</h2>
<p>Export PDF, PNG images, and a DXF file for AutoCAD or similar programs.</p>
<p class="note">PlanCraft 3D is a planning tool. Estimates are approximate and structural design must come from a licensed engineer.</p>
""")
