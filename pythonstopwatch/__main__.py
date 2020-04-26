"""Main file for application"""
import os
from tkinter import ACTIVE, DISABLED, Tk, Frame, BOTTOM, Label, PhotoImage, Button, TOP
from pythonstopwatch.stopwatch import StopWatch
from pythonstopwatch.constants.colors import TEXT_COLOR, BG_COLOR
from pythonstopwatch.constants.strings import COPYRIGHT_TEXT, PROJECT_TITLE


def start_pressed(stop_watch, start_button, reset_button, lap_button, play_img, pause_img):
    """
    Start button pressed, set state of reset button to be ACTIVE
    If stopwatch is running then call stop and, change image
    else call start and change image
    :param stop_watch: Stop Watch
    :param start_button: Start Button
    :param reset_button: Reset Button
    :param lap_button: Lap Button
    :param play_img: Play/Start Image
    :param pause_img: Pause/Stop Image
    """
    reset_button['state'] = ACTIVE
    if stop_watch.is_running():
        stop_watch.stop()
        start_button['image'] = play_img
        lap_button['state'] = DISABLED
    else:
        stop_watch.start()
        start_button['image'] = pause_img
        lap_button['state'] = ACTIVE


def reset_pressed(stop_watch: StopWatch, stop_button, reset_button, lap_button, play_image):
    """
    Reset the stopwatch
    :param stop_watch: Start Button
    :param stop_button: Stop Button
    :param reset_button: Reset Button
    :param lap_button: Lap Button
    :param play_image: Play/Start Image
    """
    stop_watch.reset()
    stop_button['image'] = play_image
    reset_button['state'] = DISABLED
    lap_button['state'] = DISABLED


def lap_pressed(stop_watch):
    stop_watch.lap_time()


def main():
    """
    Main function. starting point of application
    """
    root = Tk()  # blank window
    root.title(PROJECT_TITLE)
    root['bg'] = BG_COLOR
    root.geometry("900x600")  # give size to the window
    root.resizable(False, False)
    top_frame = Frame(root)
    stop_watch = StopWatch(root, bg=BG_COLOR)  # pass root to this
    bottom_frame = Frame(root)
    top_frame.pack()
    bottom_frame.pack(side=BOTTOM)
    copyright_label = Label(bottom_frame, text=COPYRIGHT_TEXT, bg=BG_COLOR, fg=TEXT_COLOR)  # only for aesthetics
    stop_watch.pack(side=TOP)
    copyright_label.pack(side=BOTTOM)

    # load images
    root_dir = os.path.dirname(os.path.abspath(__file__))
    play_image = PhotoImage(file=os.path.join(root_dir + os.sep + 'assets' + os.sep + 'play.png'))
    pause_image = PhotoImage(file=os.path.join(root_dir + os.sep + 'assets' + os.sep + 'pause.png'))
    reset_image = PhotoImage(file=os.path.join(root_dir + os.sep + 'assets' + os.sep + 'reset_enabled.png'))
    lap_image = PhotoImage(file=os.path.join(root_dir + os.sep + 'assets' + os.sep + 'lap_split.png'))

    sub_sample_size = 7
    play_image = play_image.subsample(sub_sample_size)
    pause_image = pause_image.subsample(sub_sample_size)
    reset_image = reset_image.subsample(sub_sample_size)

    start_button = Button(root, command=lambda: start_pressed(stop_watch,
                                                              start_button, reset_button, lap_button, play_image,
                                                              pause_image),
                          bg=BG_COLOR, image=play_image, border=0, highlightthickness=0)
    lap_button = Button(root,
                        command=lambda: lap_pressed(stop_watch),
                        state=DISABLED, bg=BG_COLOR, image=lap_image, border=0, highlightthickness=0)
    reset_button = Button(root,
                          command=lambda: reset_pressed(stop_watch, start_button, reset_button, lap_button, play_image),
                          bg=BG_COLOR, image=reset_image, state=DISABLED, border=0,
                          highlightthickness=0)

    lap_button.place(x=325, y=450)
    start_button.place(x=425, y=450)
    reset_button.place(x=525, y=450)
    root.mainloop()


if __name__ == '__main__':
    main()
