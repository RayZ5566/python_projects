"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
The project was completed by Ray Lee
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    width_x = width-2*GRAPH_MARGIN_SIZE  # total width can be separated
    total_year = len(YEARS)  # the amount of years in the year list(YEARS)
    year_x = int(year_index*width_x/total_year)
    return year_x


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE,CANVAS_WIDTH-GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,CANVAS_WIDTH-GRAPH_MARGIN_SIZE,CANVAS_HEIGHT-
                       GRAPH_MARGIN_SIZE)
    x_coord = []
    for i in range(len(YEARS)):
        x_coord.append(get_x_coordinate(CANVAS_WIDTH, i))
    for x in x_coord:
        canvas.create_line(GRAPH_MARGIN_SIZE+x,GRAPH_MARGIN_SIZE,GRAPH_MARGIN_SIZE+x,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
        canvas.create_text(GRAPH_MARGIN_SIZE+x+TEXT_DX,CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[x_coord.index(x)],
                           anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    for i in range(len(lookup_names)):
        coordinate = []  # list record the coordinate (x,y) for each year
        c = i % len(COLORS)
        for j in range(len(YEARS)):
            x = get_x_coordinate(CANVAS_WIDTH, j)+GRAPH_MARGIN_SIZE
            if str(YEARS[j]) in name_data[lookup_names[i]]:  # check if the name is in the ranking dictionary or not
                y1 = int(int(name_data[lookup_names[i]][str(YEARS[j])])*(CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/MAX_RANK+GRAPH_MARGIN_SIZE)
                coordinate.append((x, y1))
                canvas.create_text(x+TEXT_DX, y1, text=f'{lookup_names[i]} {name_data[lookup_names[i]][str(YEARS[j])]}',
                                   anchor=tkinter.SW, fill=COLORS[c])  # the text(name, rank) doesn't need to point, the text is added directly
            else:  # if the name is not in the ranking dictionary, the coordinate of y is fixed (at the bottom)
                y2 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                coordinate.append((x, y2))
                canvas.create_text(x+TEXT_DX, y2,
                                   text=f'{lookup_names[i]} *', anchor=tkinter.SW, fill=COLORS[c])

        canvas.create_line(coordinate, fill=COLORS[c], width=LINE_WIDTH)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
