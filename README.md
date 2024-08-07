# Kill-The-Code

## Overview

- The `Kill-The-Code` Python Program provides a robust mechanism for remotely controlling code execution by monitoring a specified URL for a kill signal. This script periodically checks the content of a file hosted at the provided URL and executes or halts execution based on the response. It also includes functionality for self-destruction upon receiving a specific kill signal, making it suitable for various cybersecurity applications.

## Features

- **Remote Control:** Monitors a URL for kill signals to remotely control code execution.
- **Pause and Resume:** Allows pausing and resuming based on signals from the URL.
- **State Tracking:** Compares previous and current states to manage execution or halt.
- **Self-Destruction:** Deletes the script file upon receiving a specific kill signal.
- **Configurable Interval:** Set a time interval (default 600 seconds) for checking the kill switch.
- **Dynamic Execution:** Embeds user code into the script for versatile functionality.
- **Output Naming:** Specify the output file name or use the default `output.py`.

## How to Use
![Kill-The-Code](https://github.com/user-attachments/assets/071aeca4-3fc9-4cb0-8804-c67434ae6c45)

1. **Clone the Repository:**

    ```
    git clone https://github.com/malwarekid/kill-the-code.git && cd kill-the-code
    ```

2. **Run the Script:**

    ```
    python3 kill-the-code.py
    ```

```
python3 Kill-The-Code.py

    __ __ _ ____    ________               ______          __   
   / //_/(_) / /   /_  __/ /_  ___        / ____/___  ____/ /__ 
  / ,<  / / / /_____/ / / __ \/ _ \______/ /   / __ \/ __  / _ \
 / /| |/ / / /_____/ / / / / /  __/_____/ /___/ /_/ / /_/ /  __/
/_/ |_/_/_/_/     /_/ /_/ /_/\___/      \____/\____/\__,_/\___/ 

                                            By @malwarekid

Enter the raw URL of your kill.txt file: http://0.0.0.0:8888/kill.txt
Enter the path of your Python file to add Kill Switch: code.py
Enter the time interval in seconds (default 600): 30
Enter the name of the output file (default 'output.py'): 
Combined code written to output.py
```

3. **Enter Input Parameters:**

   - **Kill Switch URL:** Enter the URL where the kill switch file is hosted (e.g., `http://example.com/kill.txt`).
   - **Python File to Protect:** Enter the path to the Python file you want to protect with the kill switch.
   - **Time Interval:** Enter the time interval (in seconds) for checking the kill switch URL (default is 600 seconds).
   - **Output File Name:** Enter the name of the output file (default is `output.py`).

4. **Output File:** The script will generate a combined Python file with the kill switch functionality, saved with the specified name or default to `output.py`.

## Requirements

- Python 3.x
- Requests library

## Installation

Ensure you have the required dependencies:

```
pip install requests
```

## Example

```
python3 kill-the-code.py
```

When prompted, provide the necessary details:

```
Enter the raw URL of your kill.txt file: http://example.com/kill.txt
Enter the path of your Python file to add Kill Switch: path/to/your_script.py
Enter the time interval in seconds (default 600): 600
Enter the name of the output file (default 'output.py'): output.py
```

The script will generate a Python file with integrated kill switch functionality based on the provided inputs.

## Contributors

- [MalwareKid](https://github.com/malwarekid)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Notes

- **Feedback:** Your feedback is welcome. Connect with me on [Instagram](https://www.instagram.com/malwarekid/) and [GitHub](https://github.com/malwarekid/). Happy Hacking!
