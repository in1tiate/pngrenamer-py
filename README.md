# pngrenamer-py
Short Python 3 script to parse a large amount of files and append the ".png" extension to files with PNG headers.

I wrote this to parse a directory of around 6,000 files with no extension (of which some were PNG images) in around ten minutes.

**Requirements:**
 - Python 3.7+

**Notes:**
 - This is fairly specialized code written for the purpose of parsing a single directory with no child directories. As such this script does not run recursively, i.e. iterate through all subdirectories.
 - This was created specifically for a Windows machine, as Linux has no need for file extensions. It should work on Linux anyway, though.

**Usage:**
 - Place files in a directory called "bins"
 - Place pngrenamer.py next to the "bins" directory
 - Run the script
