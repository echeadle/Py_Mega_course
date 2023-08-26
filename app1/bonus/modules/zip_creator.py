import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path,"w") as zip:
        for file in filepaths:
            file = pathlib.Path(file)
            zip.write(file)


if __name__ == "__main__":
    make_archive(["parsers14.py", "converters14.py"], dest_dir="dest")