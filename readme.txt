We have read and abided by the rules laid out above, 
we have not used anyone else's work for your project, 
our work is only my own and my group's.

Members: Yalin Liu,    Yujia Liu,                         Zhengyang ling 
from section 7           from section 7                 from section 2

Everyone’s work is equal

We named our project as Automatic MineSweeper (AMS)
Our code has comments. And printed a lot of information you may need.
We finished the Bonuse( Global Information part and Better Decision.)
When AMS has marked all mines, AMS will open all the remaining grids and end the mission early.
When AMS opens all safety grids 
(total number of grids - number of mines = number of safety grids)
AMS will mark all the remaining grids as flags and end the mission early which get higher score.

2.1part is solver. We wrote two 2.2 versions and we used them both and part2 of 2.2 include the Better Decision
 (I comment them in our code)
The superposition of these two versions of 2.2 makes our AMS extremely powerful


Using AMS can help you automatically complete minesweeper （include global and better decision）
steps1. run AMS
steps2. Enter dimension and NumberOfMines 
steps3. You will get cleared, flags, score and the matrix that AMS opened

cleared: Stores the order in which AMS opens the grid(excluding flags)
flags: Stores the order that we flags
score is the score that AMS earned. max score is the NumberOfMines 
e.g 40/40 means you have 40 score with 40 max
     39/40 means you have 39 score with 40 max
etc

we also made a gif maker,
if you want to use it you can turn our comments part into code in the end part in solver.

