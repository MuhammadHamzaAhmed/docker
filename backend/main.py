"""
Usage: main.py

Start flask api at port 5000
"""
from example_module import *
import traceback

if __name__ == '__main__':
    try:
        app.run(host="0.0.0.0", port=5000, debug=True)
    except Exception as e:
        traceback.print_exc()
        print(e)
