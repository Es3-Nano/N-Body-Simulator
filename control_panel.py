import tkinter as tk
import bodies

response_trys = 3

def control_panel(toggle_pause_callback, dt_change_callback, softening_change_callback,fast_foward_callback, add_body_callback, delete_body_callback):
    control_panel_width = 500
    control_panel_height = 500

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
    
    pause_button = tk.Button(frame, text="\u25b6", command=toggle_pause_callback,font=font_selected, bg="black", fg="white")
    fps_label = tk.Label(frame, text="FPS: 0", font=font_selected, bg=label_color, fg=text_color, anchor="w", width=25)
    num_bodies_label = tk.Label(frame, text="Number of Bodies: 0", font=font_selected, bg=label_color, fg=text_color, anchor="w", width=25)
    physics_time_label = tk.Label(frame, text="Physics Time: 0", font=font_selected, bg=label_color, fg=text_color, anchor="w", width=25)
    message_label = tk.Label(frame, text="Message: None", font=font_selected, bg=label_color, fg=text_color, anchor="w", width=25)
        
    add_body = tk.Button(frame, text="Add Body \u25cf",font=font_selected, bg="green", fg="white", command=add_body_callback)
    delete_body = tk.Button(frame, text="Delete Body \u25cf",font=font_selected, bg="red", fg="white", command=delete_body_callback)

    dt_slider = tk.Scale(frame, from_=0.001, to=0.05, resolution=0.001, orient="horizontal", label="Time Step", bg="black", fg="white", command=dt_change_callback)
    dt_slider.set(0.01)
    fast_foward_steps_slider = tk.Scale(frame, from_=1, to=50, resolution=1, orient="horizontal", label="Fast Forward Steps", bg="black", fg="white", command=fast_foward_callback)
    fast_foward_steps_slider.set(1)
    softening_slider = tk.Scale(frame, from_=0.5, to=10.0, resolution=0.1,orient="horizontal", label="Softening", bg="black", fg="white", command=softening_change_callback)
    softening_slider.set(bodies.b_radii/2)

    fps_label.pack(pady=4)
    num_bodies_label.pack(pady=4)
    physics_time_label.pack(pady=4)
    message_label.pack(pady=4)
    pause_button.pack(side=tk.LEFT, pady=4)
    add_body.pack(side=tk.LEFT, pady=4)
    delete_body.pack(side=tk.LEFT, pady=4)
    softening_slider.pack(pady=4)
    dt_slider.pack(pady=4)
    fast_foward_steps_slider.pack(pady=4)

    return root, fps_label, num_bodies_label, physics_time_label, pause_button, message_label

def update_control_panel(fps, num_bodies, physics_time, fps_label, num_bodies_label, physics_time_label, message_label, message):
    fps_label.config(text=f"FPS: {fps:.0f}")
    num_bodies_label.config(text=f"Number of Bodies: {num_bodies:.2f}")
    physics_time_label.config(text=f"Physics Time: {physics_time:.2f}")
    message_label.config(text=f"Message: {message}")

def open_add_body_popup(root, position, create_body_callback):
    popup = tk.Toplevel(root)
    popup.title("Add Body")
    popup.geometry("250x200")

    tk.Label(popup, text="Mass:").pack()
    mass_entry = tk.Entry(popup)
    mass_entry.pack()

    tk.Label(popup, text="X Velocity:").pack()
    xvel_entry = tk.Entry(popup)
    xvel_entry.pack()

    tk.Label(popup, text="Y Velocity:").pack()
    yvel_entry = tk.Entry(popup)
    yvel_entry.pack()

    def submit():
        try:
            m = float(mass_entry.get())
            xv = float(xvel_entry.get())
            yv = float(yvel_entry.get())
        except ValueError:
            tk.Label(popup, text="Invalid input, using defaults", fg="red").pack()
            m, xv, yv = 100.0, 0.0, 0.0
        # position is screen coords already; create_body expects sim coords
        create_body_callback(m, position[0] - bodies.screen_width / 2,
                              bodies.screen_height / 2 - position[1], xv, yv)
        popup.destroy()

    submit_btn = tk.Button(popup, text="Add", command=submit)
    submit_btn.pack(pady=10)
    popup.bind('<Return>', lambda event: submit())