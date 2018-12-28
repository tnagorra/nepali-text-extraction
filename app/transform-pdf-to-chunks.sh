if [ -z "$1" ]; then
    echo "Specify pdf to be extracted!"
    exit 1
fi

current=$(dirname $0)
tmp="$current/tmp"
chunks="$tmp/chunks"

mkdir "$tmp"
# Convert pdf to html
echo "Starting pdf extraction"
pdf2txt.py -o "$tmp/sabdakosh.html" -t html "$1"
echo "Completed pdf extraction"

# Tidy html
echo "Starting html tidying"
tidy -o "$tmp/sabdakosh-tidy.html" -config "$current/tidyconf.txt" "$tmp/sabdakosh.html"
echo "Completed html tidying"

# Split large html into manageable chunks
echo "Starting html chunk creation"
mkdir "$chunks"
csplit -n 5 -f "$chunks/" "$tmp/sabdakosh-tidy.html" '/Page [0-9]/-1' '{*}'
echo "Completed html chunk creation"

# Add .html extension to chunks
echo "Starting html chunks renaming"
cd "$chunks"
for f in *; do mv $f `basename $f `.html; done;
echo "Completed html chunks renaming"
