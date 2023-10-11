import sys
import pip
package_name = "flask_cors"
try:
    pip.main(["install", package_name])
    print("akal")
except Exception as e:
    print("error", e)
python_executable = sys.executable
print(f"The Python interpreter is located at: {python_executable}")