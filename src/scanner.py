import os


def scan_repository(root_folder):

    files = []

    for current_path, directories, filenames in os.walk(root_folder):

        for filename in filenames:

            full_path = os.path.join(
                current_path,
                filename
            )

            try:

                stats = os.stat(full_path)

                files.append(
                    {
                        "path": full_path,
                        "name": filename,
                        "extension": os.path.splitext(filename)[1].lower(),
                        "size": stats.st_size
                    }
                )

            except Exception:

                pass

    return files