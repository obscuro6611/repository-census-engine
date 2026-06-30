from scanner import scan_repository
from classifier import classify_file
from exporter import (
    save_census_json,
    save_markdown_report
)


folder = input(
    "Enter folder path: "
)

files = scan_repository(
    folder
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

print(
    f"\nFiles scanned: {len(files)}"
)

print(
    "\nrepository_census.json created."
)

print(
    "repository_report.md created."
)