        from scanner import scan_repository


    folder = input(
        "Enter folder path: "
    )

    files = scan_repository(
        folder
    )

    print(
        f"\nFiles found: {len(files)}"
    )

    for file in files[:10]:

        print(file)