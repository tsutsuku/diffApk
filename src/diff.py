

import sys

from bsdiff4 import file_diff, file_patch

print(sys.argv[1] + "," + sys.argv[2] + "," + sys.argv[3])
if sys.argv[1] == "diff":
    file_diff(sys.argv[2], sys.argv[3], sys.argv[4])
else:
    file_patch(sys.argv[2], sys.argv[3], sys.argv[4])
