import sys
import os
from pathlib import Path

REDIRECT = """\
<!DOCTYPE html>
<html>
  <head>
    <title>Redirecting to %(path)s</title>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url=%(path)s">
    <link rel="canonical" href="%(path)s">
  </head>
</html>
"""

# First copy the gh-pages branch of the relevant repos here (without .git)
# Then run:
#   python3 add_redirect.py p4p
repo_name = sys.argv[1]

os.chdir(Path(__file__).parent / repo_name)
for root, dirs, files in os.walk("."):
  for fname in files:
    if fname.endswith(".html"):
      path = f"https://epics-base.github.io/{Path(repo_name) / root / fname}"
      with open(Path(root) / fname, "w") as f:
        f.write(REDIRECT % locals())
