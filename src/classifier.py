def classify_file(extension):

    extension = extension.lower()

    document_types = [
        ".pdf",
        ".doc",
        ".docx",
        ".txt",
        ".md"
    ]

    spreadsheet_types = [
        ".xls",
        ".xlsx",
        ".csv"
    ]

    image_types = [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp"
    ]

    code_types = [
        ".py",
        ".js",
        ".html",
        ".css",
        ".java",
        ".cpp"
    ]

    archive_types = [
        ".zip",
        ".rar",
        ".7z"
    ]

    if extension in document_types:
        return "Document"

    if extension in spreadsheet_types:
        return "Spreadsheet"

    if extension in image_types:
        return "Image"

    if extension in code_types:
        return "Code"

    if extension in archive_types:
        return "Archive"

    return "Other"