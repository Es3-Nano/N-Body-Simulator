import tkinter as tk


def control_panel():
    control_panel_width = 500
    control_panel_height = 300

    root = tk.Tk()

    root.title("Simulation Control Panel")
    root.configure(background="black")
    root.minsize(control_panel_width, control_panel_height - 100)
    root.maxsize(control_panel_width, control_panel_height + 200)
    root.geometry(f"{control_panel_width}x{control_panel_height}+1400+600")

    frame = tk.Frame(root, width=control_panel_width * 0.9, height=control_panel_height * 0.9, bg="black")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    font_selected = ("Sn Pro", 15)
    label_color = "black"
    text_color = "white"

    fps_label = tk.Label(frame, text="FPS: 0", font=font_selected, bg=label_color, fg=text_color, anchor="w", width=25)
    num_bodies_label = tk.Label(frame, text="Number of Bodies: 0", font=font_selected, bg=label_color, fg=text_color, anchor="w", width=25)
    physics_time_label = tk.Label(frame, text="Physics Time: 0", font=font_selected, bg=label_color, fg=text_color, anchor="w", width=25)

    fps_label.pack(pady=4)
    num_bodies_label.pack(pady=4)
    physics_time_label.pack(pady=4)

    return root, fps_label, num_bodies_label, physics_time_label


def update_control_panel(fps, num_bodies, physics_time, fps_label, num_bodies_label, physics_time_label):
    fps_label.config(text=f"FPS: {fps:.0f}")
    num_bodies_label.config(text=f"Number of Bodies: {num_bodies:.2f}")
    physics_time_label.config(text=f"Physics Time: {physics_time:.2f}")
