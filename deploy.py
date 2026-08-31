import subprocess
import sys

print("=" * 35)
print("     Starting Deployment")
print("=" * 35)

try:
    process = subprocess.Popen(
        [sys.executable, "app.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print(stdout)
        print("=" * 35)
        print("     Deployment Successful")
        print("=" * 35)
    else:
        print("Deployment Failed!")
        print(stderr)

except Exception as error:
    print("An unexpected error occurred:")
    print(error)