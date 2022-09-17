#!/bin/bash

path_to_convert=$1
path_to_save=$2
path_to_log=$3

ffmpeg -y -i $path_to_convert $path_to_save &> $path_to_log