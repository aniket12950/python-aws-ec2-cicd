import subprocess

print("=================================")
print(" Starting Deployment")
print("=================================")

try:
    result = subprocess.run(
        ["python3", "app.py"],
        check=True,
        capture_output=True,
        text=True
    )

    print(result.stdout)

    print("=================================")
    print(" Deployment Successful")
    print("=================================")

except subprocess.CalledProcessError as e:
    print("Deployment Failed!")
    print(e.stderr)