#!/usr/bin/env python
import exif
import os
from pathlib import Path
import shutil
import sys

EXAMPLE_USAGE="""
No path given to extract_photos.py

  Example Usage:
    $ ./extract_photos.py /mnt/sdcard0/
    /media/tlehman/5501-C42C/DCIM/101_WSCT/WSCT2965.JPG
    /media/tlehman/5501-C42C/DCIM/101_WSCT/WSCT2966.JPG
    ...
    /media/tlehman/5501-C42C/DCIM/101_WSCT/WSCT2969.JPG
    /media/tlehman/5501-C42C/DCIM/101_WSCT/WSCT2970.JPG
"""

if __name__ == "__main__":
    if len(sys.argv) >= 2 and os.path.exists(sys.argv[1]):
        photo_path = sys.argv[1]
        photos = list(Path(photo_path).rglob("*.[jJ][pP][gG]"))
        for photo in photos:
            created_at = exif.Image(photo).datetime_original
            new_filename = "tree-%s.jpg" % created_at.replace(" ", "_")
            new_path = os.path.join(os.getenv("HOME"), "Dropbox/treelapse", new_filename)
            if not os.path.exists(new_path):
                print("Copying %s to %s" % (photo, new_path))
                shutil.copyfile(photo, new_path)
        exit(0)
    else:
        print(EXAMPLE_USAGE)
        exit(1)



