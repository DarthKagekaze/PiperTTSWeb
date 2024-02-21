import os
import subprocess
import sys





PORT = 8880






subprocess.run(["python", "-m", "http.server", str(PORT)])