#!/bin/bash

# A simple script that overlays the output and the original image so I can quickly compare them

convert out.png -matte -channel A +level 0,50% +channel op1.png
convert sample.png -matte -channel A +level 0,50% +channel op2.png
convert op1.png op2.png -gravity center -composite overlay.png