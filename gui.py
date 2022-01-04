import tkinter as tk
from tkinter import END

from youtube import get_youtube_video

# CONST
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 200


def load_gui():
    # Top level window
    frame = tk.Tk()
    frame.title("Video Downloader")
    cfg_tuple = center_window(frame)
    frame.geometry('%dx%d+%d+%d' % (cfg_tuple[0], cfg_tuple[1], cfg_tuple[2], cfg_tuple[3]))

    # Label Creation - URL
    label = tk.Label(frame, text="URL:")
    label.pack()

    # TextBox Creation - video_url
    tb_video_url = tk.Text(frame, height=1, width=100)
    tb_video_url.pack()

    # TODO: Checkboxes (Youtube, twitter, instagram)

    # Button Creation - Download
    download_button = tk.Button(frame,
                                text="Download",
                                command=lambda: retrieve_input(tb_video_url))
    download_button.pack()

    # TODO: Create a filedialog to change output folder
    # TODO: Create a label that shows the current output folder

    # Run
    frame.mainloop()


def center_window(win):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    width = SCREEN_WIDTH
    height = SCREEN_HEIGHT
    x = screen_width / 2 - width / 2 + 200
    y = screen_height / 2 - height / 2
    resp_tuple = (width, height, x, y)
    return resp_tuple


def retrieve_input(textbox_input):
    video_url = textbox_input.get("1.0", "end-1c")
    if len(video_url) >= 24:  # TODO: Change validator (with Regex)
        get_youtube_video(video_url)
        textbox_input.delete('1.0', END)
    else:
        textbox_input.delete('1.0', END)
        pass
        # TODO: Create info label: Invalid URL
