import zipfile


def extract_archive(archive_path, dest_directory):
    with zipfile.ZipFile(archive_path, "r") as archive:
        archive.extractall(dest_directory)


if __name__ == "__main__":
    extract_archive("/home/echeadle/Udemy-Learn-Py/Py_Mega_Course/app1/archive_extractor/compressed.zip",
                    "/home/echeadle/Udemy-Learn-Py/Py_Mega_Course/app1/archive_extractor/files")
