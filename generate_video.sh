#!/bin/bash

path=$1
mkdir -p /tmp/timelapse
tmp_path=/tmp/timelapse
echo "Copying noon files to $tmp_path as consecutive numbered files"

i=1
for photo in $(find $path -name 'tree-20*_12:*.jpg' | sort); do
    cp $photo $tmp_path/$i.jpg
    i=$((i+1))
done

echo "Generating $tmp_path/treelapse.mp4"
# convert jpgs into mp4
(cd $tmp_path && ffmpeg -i %d.jpg -c:v libx264 -vf fps=60 -pix_fmt yuv420p treelapse.mp4)

echo "Transforming $tmp_path/treelapse.mp4 to iOS format"
ffmpeg -i $tmp_path/treelapse.mp4 -vcodec libx264 -profile:v main -level 3.1 -preset medium -crf 23 -x264-params ref=4 -acodec copy -movflags +faststart treelapse-ios.mp4
