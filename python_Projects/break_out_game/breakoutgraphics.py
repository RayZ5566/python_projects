"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gcolor import GColor
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.



class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.paddle_offset = paddle_offset

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2 , y=self.window.height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.x = (self.window.width/2)-ball_radius
        self.y = (self.window.height/2)-ball_radius
        self.window.add(self.ball, x=self.x, y=self.y)
        # Default initial velocity for the ball
        self.__dy = 0
        self.__dx = 0
        # Initialize our mouse listeners
        onmouseclicked(self.set_ball_velocity)
        onmousemoved(self.paddle_move)
        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = GColor(int(i * 255 / brick_rows),
                                               int(i * 255 / brick_rows),
                                               int(i * 255 / brick_rows))
                self.brick.x = j * (brick_width + brick_spacing)
                self.brick.y = i * (brick_height + brick_spacing)
                self.window.add(self.brick, x=self.brick.x, y=brick_offset + self.brick.y)

        # Swtich
        self.start = 0  # game switch off 0 start 1
        # lives
        self.lives = GLabel('life: ')
        self.window.add(self.lives, 0, self.lives.height)
        # Brick counters
        self.rows = brick_rows
        self.cols = brick_cols
        self.brick_count = self.rows*self.cols
        self.brick_count_window = GLabel('bricks left: ')
        self.window.add(self.brick_count_window, window_width-self.brick_count_window.width-30,
                        self.brick_count_window.height)
        # Game over
        self.game_over_label = GLabel('GAME OVER!!')
        # Clear
        self.clear_label = GLabel('CLEARED!!')

    def reset_position(self):
        """
        the ball will be added on the window with initial velocity dx=0 dy=0
        """
        self.game_start()
        self.window.add(self.ball, x=self.x, y=self.y)

    def set_ball_velocity(self, c):
        """
        Setting the initial velocity of the ball
        :param c: irrelevant
        :return: initial dx and dy
        """
        if self.start == 0:
            self.game_start()
            self.__dy = INITIAL_Y_SPEED  # initial y speed
            __dx = random.randint(1, MAX_X_SPEED)  # initial x speed
            if random.random() > 0.5:
                __dx = -__dx
            self.__dx = __dx

    def paddle_move(self, m):
        """
        the paddle will get the information of mouse and move horizontally to the mouse position
        :param m: the mouse information
        """
        if 0 <= m.x <= self.window.width-self.paddle.width:
            self.paddle.x = m.x

    def game_start(self):
        self.start = 1
        self.__dx = 0
        self.__dy = 0
        return self.start

    def game_end(self):
        """
        the switch will turn off (1 -> 0) and wait the mouse clicked to restart again
        :return:
        """
        self.start = 0
        # return self.start

    # Getter
    def get_dx(self):
        """Get the horizontal velocity of the ball
            if the ball touched the ball the velocity(dx) would bounce back with minus velocity(-dx)
            :return: horizontal velocity
        """
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
            return self.__dx
        return self.__dx

    def get_dy(self):
        """Get the vertical velocity of the ball
            if the ball touched the roof the velocity(dy) would bounce back with minus velocity(-dy)
            The ball would not bounce back if the ball touched the floor
            :return: vertical velocity
        """
        if self.ball.y <= 0:
            self.__dy = -self.__dy
            return self.__dy
        return self.__dy

    def out_bottom(self):
        """Check if the ball is out of the bottom window"""
        window_bottom = self.window.height
        is_out_bottom = self.ball.y >= window_bottom
        return is_out_bottom

    def touch_paddle(self):
        paddle_top_left = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height)
        paddle_top_right = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)

        if paddle_top_left and paddle_top_left is self.paddle or paddle_top_right and paddle_top_right is self.paddle:
            self.ball.move(0, -self.paddle.height)
            self.__dy = -self.__dy

    def clear(self):
        ball_left = self.ball.x
        ball_right = self.ball.x+self.ball.width
        ball_top = self.ball.y
        ball_bot = self.ball.y+self.ball.height
        maybe_brick_lt = self.window.get_object_at(ball_left,ball_top)
        maybe_brick_rt = self.window.get_object_at(ball_right,ball_top)
        maybe_brick_lb = self.window.get_object_at(ball_left,ball_bot)
        maybe_brick_rb = self.window.get_object_at(ball_right,ball_bot)
        if maybe_brick_lt and maybe_brick_lt is not self.paddle:
            if maybe_brick_lt is not self.brick_count_window:
                if maybe_brick_lt is not self.lives:
                    self.window.remove(maybe_brick_lt)
                    self.__dy = -self.__dy
                    self.brick_count -= 1
        elif maybe_brick_rt and maybe_brick_rt is not self.paddle:
            if maybe_brick_rt is not self.brick_count_window:
                if maybe_brick_rt is not self.lives:
                    self.window.remove(maybe_brick_rt)
                    self.__dy = -self.__dy
                    self.brick_count -= 1
        elif maybe_brick_lb and maybe_brick_lb is not self.paddle:
            if maybe_brick_lb is not self.brick_count_window:
                if maybe_brick_lb is not self.lives:
                    self.window.remove(maybe_brick_lb)
                    self.__dy = -self.__dy
                    self.brick_count -= 1
        elif maybe_brick_rb and maybe_brick_rb is not self.paddle:
            if maybe_brick_rb is not self.brick_count_window:
                if maybe_brick_rb is not self.lives:
                    self.window.remove(maybe_brick_rb)
                    self.__dy = -self.__dy
                    self.brick_count -= 1
        self.brick_counter()

    def life_count(self,life):
        self.lives.text = 'Life: '+ str(life)

    def brick_counter(self):
        self.brick_count_window.text = 'bricks left: '+str(self.brick_count)

    def game_over(self):
        self.window.add(self.game_over_label, (self.window.width-self.game_over_label.width)/2,
                        (self.window.height+self.game_over_label.height)/2)

    def game_clear(self):
        self.window.add(self.clear_label, (self.window.width-self.game_over_label.width)/2,
                        (self.window.height+self.game_over_label.height)/2)
