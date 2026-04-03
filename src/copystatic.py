import shutil
import os


def copy_static_to_public(from_dir, to_dir):
    if os.path.exists(to_dir):
        shutil.rmtree(to_dir)

    os.mkdir(to_dir)

    for item in os.listdir(from_dir):
        from_path = os.path.join(from_dir, item)
        to_path = os.path.join(to_dir, item)

        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_static_to_public(from_path, to_path)
