import os
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

DATA_DIRS = [
    ('~/linuxcnc/configs/mill_touch_sim', 'configs/mill_touch_sim'),
    ]

def data_files_from_dirs(data_dirs):
    data_files = []
    for dest_dir, source_dir in data_dirs:
        dest_dir = os.path.expanduser(dest_dir)
        for root, dirs, files in os.walk(source_dir):
            root_files = [os.path.join(root, i) for i in files]
            dest = os.path.join(dest_dir, os.path.relpath(root, source_dir))
            data_files.append((dest, root_files))

    return data_files

data_files = (data_files_from_dirs(DATA_DIRS))

setup(
    name="mill_touch",
    version="0.1.0",
    author="John Doe",
    author_email="<doe.john@example.com>",
    description="mill_touch - A QtPyVCP based Virtual Control Panel for LinuxCNC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/USERNAME/REPO",
    download_url="https://github.com/USERNAME/REPO/tarball/master",
    packages=find_packages(),
    data_files=data_files,
    include_package_data=True,
    entry_points={
        'gui_scripts': [
            'mill_touch=mill_touch:main',
        ],
        'qtpyvcp.vcp': [
            'mill_touch=mill_touch',
        ],
    },
)
