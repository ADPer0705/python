I am currently thinking about how I'll organise the data required for the game;

I am considering the following 
 - assign a value to each kind chess piece
     - also a value, say 0 if there is no chess piece
 - assign a value for each colour, say
     - w for white
     - b for black
 - make a list of all the possible combination of pieces and colour
 - make a dictionary with all the squares on the board corrosponding to an element on the list 
     - note that an item for 'no piece' is also there in the list for assigning to the empty squares
 - squares will be numbered as usual, stored as a list of pair of phile and rank
 - at the moment I am not adding any gui so color is not a requirement at the moment,
   but I will soon add color as to avoid making changes after writing much code

This is just a rough plan, I'll think about it furthur,
