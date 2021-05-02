"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 100  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    graphics.life_count(lives)

    # Add animation loop here!
    while NUM_LIVES > 0:
        if graphics.out_bottom():
            lives -= 1
            graphics.life_count(lives)
            if lives > 0:
                graphics.reset_position()
                graphics.game_end()
            else:
                graphics.game_over()
                break
        if graphics.brick_count == 0:
            graphics.game_clear()
            break
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        graphics.touch_paddle()
        graphics.clear()
        pause(FRAME_RATE)





if __name__ == '__main__':
    main()
