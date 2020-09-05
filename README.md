# Timelapse Camera 

## How to use

- Activate the python virtual environment by running `env/bin/activate`
- Run `./extract_photos.py /mnt/sdcard0` to copy the photos to a directory, named with their EXIF metadata created_at timestamp
- Run `./generate_video.sh PATH-TO-PHOTOS` to generate the timelapse using ffmpeg

## Dependencies for `generate_video.sh`

- ffmpeg
- libquicktime2

## What this is for:
Code for the Wingscapes WCT-00125 timelapse camera: https://www.amazon.com/gp/product/B01FJZQONW/

![WCT-00125](https://images-na.ssl-images-amazon.com/images/I/91t22jAdPnL._AC_SX679_.jpg)

