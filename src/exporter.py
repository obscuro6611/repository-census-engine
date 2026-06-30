import json
from collections import Counter


def save_census_json(data, filename):

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


def save_markdown_report(data, filename):

    category_counts = Counter()

    for file in data:

        category_counts[
            file["category"]
        ] += 1

    report = []

    report.append(
        "# Repository Census\n"
    )

    report.append(
        f"Total Files: {len(data)}\n"
    )

    report.append(
        "## Categories\n"
    )

    for category, count in sorted(
        category_counts.items()
    ):

        report.append(
            f"- {category}: {count}"
        )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "\n".join(report)
        )