import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext

from scanner import scan_repository
from classifier import classify_file
from exporter import (
    save_census_json,
    save_markdown_report
)

selected_folder = None


def select_folder():

    global selected_folder

    selected_folder = filedialog.askdirectory()

    if selected_folder:

        folder_label.config(
            text=selected_folder
        )


def run_census():

    if not selected_folder:

        output_box.delete(
            "1.0",
            tk.END
        )

        output_box.insert(
            tk.END,
            "Please select a folder first."
        )

        return

    output_box.delete(
        "1.0",
        tk.END
    )

    output_box.insert(
        tk.END,
        "Running census...\n\n"
    )

    root.update()

    files = scan_repository(
        selected_folder
    )

    for file in files:

        file["category"] = classify_file(
            file["extension"]
        )

    save_census_json(
        files,
        "repository_census.json"
    )

    save_markdown_report(
        files,
        "repository_report.md"
    )

    category_counts = {}

    for file in files:

        category = file["category"]

        category_counts[category] = (
            category_counts.get(category, 0) + 1
        )

    output_box.delete(
        "1.0",
        tk.END
    )

    output_box.insert(
        tk.END,
        f"Files Scanned: {len(files)}\n\n"
    )

    output_box.insert(
        tk.END,
        "Categories\n"
    )

    output_box.insert(
        tk.END,
        "----------\n"
    )

    for category, count in sorted(
        category_counts.items()
    ):

        output_box.insert(
            tk.END,
            f"{category}: {count}\n"
        )

    status_label.config(
        text="Census Complete"
    )


root = tk.Tk()

root.title(
    "Repository Census Engine"
)

root.geometry(
    "1000x700"
)

title = tk.Label(
    root,
    text="Repository Census Engine",
    font=("Segoe UI", 22, "bold")
)

title.pack(
    pady=10
)

select_button = tk.Button(
    root,
    text="Select Folder",
    command=select_folder
)

select_button.pack(
    pady=5
)

folder_label = tk.Label(
    root,
    text="No folder selected"
)

folder_label.pack(
    pady=5
)

run_button = tk.Button(
    root,
    text="Run Census",
    command=run_census
)

run_button.pack(
    pady=5
)

output_box = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=100,
    height=25
)

output_box.pack(
    padx=10,
    pady=10
)

status_label = tk.Label(
    root,
    text="Ready"
)

status_label.pack(
    pady=5
)

root.mainloop()