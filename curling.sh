echo "starting filtering process"
grep -o 'srcset=.*.jpeg' proxy.txt > intern.txt
grep -o 'https://images.pexels.com/photos.*.jpeg' intern.txt > result.txt
python curler_extension.py