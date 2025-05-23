import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageTk, EpsImagePlugin
import json
import io

ICON_SIZE = (50, 50)

class DiagramBuilderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Architecture Diagram Builder")
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.toolbar = tk.Frame(self.root)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
        tk.Button(self.toolbar, text="Add Server", command=lambda: self.add_component("server")).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self.toolbar, text="Add DB", command=lambda: self.add_component("db")).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self.toolbar, text="Export PNG", command=self.export_png).pack(side=tk.RIGHT, padx=5, pady=5)
        tk.Button(self.toolbar, text="Save", command=self.save_diagram).pack(side=tk.RIGHT, padx=5, pady=5)
        tk.Button(self.toolbar, text="Load", command=self.load_diagram).pack(side=tk.RIGHT, padx=5, pady=5)

        self.images = {
            "server": self.generate_placeholder_image("Srv"),
            "db": self.generate_placeholder_image("DB")
        }

        self.components = []
        self.connections = []
        self.drag_data = {"item": None, "x": 0, "y": 0}
        self.selected = None

        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def generate_placeholder_image(self, label):
        img = Image.new("RGB", ICON_SIZE, "lightgray")
        draw = ImageDraw.Draw(img)
        draw.rectangle([5, 5, 45, 45], outline="black", width=2)
        draw.text((15, 15), label, fill="black")
        return ImageTk.PhotoImage(img)

    def add_component(self, ctype):
        x, y = 100 + len(self.components) * 60, 100
        img_id = self.canvas.create_image(x, y, image=self.images[ctype], anchor=tk.CENTER)
        self.components.append({"id": img_id, "type": ctype, "x": x, "y": y})

    def on_click(self, event):
        item = self.canvas.find_closest(event.x, event.y)[0]
        for comp in self.components:
            if comp["id"] == item:
                if self.selected and self.selected != comp:
                    # draw line
                    x1, y1 = self.selected["x"], self.selected["y"]
                    x2, y2 = comp["x"], comp["y"]
                    line = self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)
                    self.connections.append({"from": self.selected["id"], "to": comp["id"], "line": line})
                    self.selected = None
                else:
                    self.selected = comp
                self.drag_data["item"] = comp
                self.drag_data["x"] = event.x
                self.drag_data["y"] = event.y
                return
        self.selected = None

    def on_drag(self, event):
        if not self.drag_data["item"]:
            return
        dx = event.x - self.drag_data["x"]
        dy = event.y - self.drag_data["y"]
        comp = self.drag_data["item"]
        comp["x"] += dx
        comp["y"] += dy
        self.canvas.move(comp["id"], dx, dy)
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

        # Update lines
        for conn in self.connections:
            if conn["from"] == comp["id"] or conn["to"] == comp["id"]:
                self.canvas.delete(conn["line"])
        self.redraw_lines()

    def on_release(self, event):
        self.drag_data["item"] = None

    def redraw_lines(self):
        new_connections = []
        for conn in self.connections:
            from_id, to_id = conn["from"], conn["to"]
            f = next(c for c in self.components if c["id"] == from_id)
            t = next(c for c in self.components if c["id"] == to_id)
            line = self.canvas.create_line(f["x"], f["y"], t["x"], t["y"], arrow=tk.LAST)
            new_connections.append({"from": from_id, "to": to_id, "line": line})
        self.connections = new_connections

    def save_diagram(self):
        file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file:
            data = {
                "components": [{"type": c["type"], "x": c["x"], "y": c["y"]} for c in self.components],
                "connections": [{"from": conn["from"], "to": conn["to"]} for conn in self.connections]
            }
            with open(file, "w") as f:
                json.dump(data, f)

    def load_diagram(self):
        file = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file:
            with open(file, "r") as f:
                data = json.load(f)
            self.canvas.delete("all")
            self.components = []
            self.connections = []
            id_map = {}
            for comp in data["components"]:
                img_id = self.canvas.create_image(comp["x"], comp["y"], image=self.images[comp["type"]], anchor=tk.CENTER)
                id_map[len(id_map)] = img_id
                self.components.append({"id": img_id, "type": comp["type"], "x": comp["x"], "y": comp["y"]})
            for conn in data["connections"]:
                from_id = id_map[conn["from"]]
                to_id = id_map[conn["to"]]
                f = next(c for c in self.components if c["id"] == from_id)
                t = next(c for c in self.components if c["id"] == to_id)
                line = self.canvas.create_line(f["x"], f["y"], t["x"], t["y"], arrow=tk.LAST)
                self.connections.append({"from": from_id, "to": to_id, "line": line})

    def export_png(self):
        file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file:
            self.canvas.update()
            ps = self.canvas.postscript(colormode='color')
            img = Image.open(io.BytesIO(ps.encode('utf-8')))
            img.save(file, "png")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiagramBuilderApp(root)
    root.mainloop()
