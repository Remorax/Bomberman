# README

A bash-shell game built using Python. Have fun!

1. The game runs frame-by-frame.

2. The board is a square with walls along the borders and in certain positions of the board. There are also 10 bricks, which randomly spawn on the board.

3. The score and the number of lives left are displayed above the board.

4. Empty tiles are shown by black squares.

5. Bricks (yellow with red tildes) can be destroyed by explosions, but walls (white) cannot.

6. The bomberman spawns at the top left corner of the board. Symbol is '[^^]'(top) and ' ][ ' (bottom) (dark blue with cyan background).
 
7. There are a total of 4 enemies (red with green background) in the game:
	• Normal enemy: Moves one cell per frame in a pseudo random fashion, and has one life only. There are 2 normal enemies in the game. Symbol is '[xx]'(top) and ' ][ '(bottom)
	• Strong enemy: Same as normal enemy, but has two lives. Symbol is '|xx|'(top) and '|][|' (bottom)
	• Fast enemy: Same as normal enemy, but moves twice as fast. Symbol is '[>>]'(top) and ' // ' (bottom)

8. The bomberman can move in four directions, W(up) S(down) A(left) D(right), stay at the same position using 'Q', drop a bomb ('B') or ask for a powerup('P').

9. Until you enter a valid move, the game won't progress.

10. Destroying a brick gives you 10 points, while killing an enemy gives you 50 points.

11. The bomberman has only one life, so be really careful!

12. A bomb detonates after 3 frames of being deployed. Without the explosion powerup, the explosion spreads to a maximum of 4 squares (could be lesser if 	  walls are there) and the explosion is shown by red '^'.

13. Each powerup costs a specific number of points which will be deducted from your score.

14. On pressing 'P', a pseudo random powerup appers based on your score at any random position in a 5 block square from your current position.

15. Each powerup has a specific timer, which is shown in the powerup symbol. Collect the powerup before the time runs out, or it will be destroyed. If the
   enemy reaches the powerup before you do, it'll be destroyed on contact with him.

16. Once you successfully collect the powerup, it'll last for a predefined number of moves before the effects wear out.

17. There are 4 types of powerups:

	• Speed powerup: Its' symbol is '<<' and the counter. Makes you twice as fast as earlier, but you can't skip through walls. You can only move two cells in one direction if both the cells 	are empty. If the second one is empty, you move by only one cell. It costs 20 points, and lasts for 8 frames before the effects wear out.
	
	• Wallpass powerup: Its' symbol is 'WALL' and the counter. Allows you to pass through walls. If the speed powerup is currently equipped, you can pass through the wall and skip to the other side without going inside it. Otherwise you can go inside the wall. Deploying a bomb while inside the wall will destroy the wall permanently, but no points will be awarded. It costs 30 points, and lasts for 5 frames before the effects wear out.
	
	• Explosion powerup: Its' symbol is 'BOOM' and the counter. Your bomb has twice the blast radius in each direction. Again you can't destroy a wall and so the explosion won't spread beyond it. It costs 40 points, and this bomb can be used twice before the effects wear out. 
	
	• Wallpass powerup: Its' symbol is 'IMMO' and the counter. Bomberman becomes immortal, so can take 3 kills without any damage before the effects wear out. It costs 60 points.

18. Trying to deploy a powerup with less than 20 points is not a valid move.	

19. Standing at the spot where the bomb was deployed will result in a death, but the explosion arrows('^') won't be shown.

20. Running the game:

	• Go to the '20161188' directory.
	
	• Run 'pip3 install -r requirements.txt'
	
	• Then 'python3 game.py'
