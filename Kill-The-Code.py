import os
import time
import requests
from requests.exceptions import RequestException
import re

def main():
    print("\033[38;2;255;69;172m" + r'''
    __ __ _ ____    ________               ______          __   
   / //_/(_) / /   /_  __/ /_  ___        / ____/___  ____/ /__ 
  / ,<  / / / /_____/ / / __ \/ _ \______/ /   / __ \/ __  / _ \
 / /| |/ / / /_____/ / / / / /  __/_____/ /___/ /_/ / /_/ /  __/
/_/ |_/_/_/_/     /_/ /_/ /_/\___/      \____/\____/\__,_/\___/ 

                                            By @malwarekid
''' + "\033[0m")

    try:
        url = input("\033[32mEnter the raw URL of your\033[0m \033[31mkill.txt\033[0m \033[32mfile:\033[0m ")
        file_to_execute = input("\033[32mEnter the path of your \033[34mPython\033[0m \033[32mfile to add Kill Switch:\033[0m ")
        check_interval = input("\033[32mEnter the time interval in seconds (\033[33mdefault 600\033[32m):\033[0m ") or '600'
        check_interval = int(check_interval) if check_interval.isdigit() else 600
        check_interval = check_interval if check_interval > 0 else 600
        output_file = input("\033[32mEnter the name of the output file (\033[33mdefault 'output.py'\033[32m): \033[0m") or 'output.py'
        
        if not os.path.isfile(file_to_execute):
            raise FileNotFoundError(f"The file \033[31m{file_to_execute}\033[32m does not exist.")
        
        with open(file_to_execute, "r") as file:
            user_code = file.read()

        user_import_statements = re.findall(r"(import .*\n|from .* import .*\n)", user_code)
        user_code = re.sub(r"(import .*\n|from .* import .*\n)", "", user_code)

        script_import_statements = [
            "import os\n",
            "import time\n",
            "import requests\n",
            "from requests.exceptions import RequestException\n"
        ]

        all_import_statements = list(set(user_import_statements + script_import_statements))
        imports = "".join(all_import_statements)

        user_code = '\n'.join(['        ' + line if line.strip() != '' else line for line in user_code.split('\n')])

        kill_switch_code = f'''
{imports}
class KillSwitch:
    def __init__(self, url, check_interval={check_interval}):
        self.url = url
        self.check_interval = check_interval
        self.prev_state = None

    def check_kill_switch(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text.strip()
        except RequestException as e:
            print(f"Error: {{e}}")
            return None

    def run(self):
        try:
            while True:
                current_state = self.check_kill_switch()
                if current_state is None:
                    pass
                elif current_state == '1' and self.prev_state == '0':
                    self.execute_code()
                elif current_state == '0' and self.prev_state == '1':
                    pass
                elif current_state == '100':
                    self.self_destruct()
                    break
                self.prev_state = current_state
                time.sleep(self.check_interval)
        except KeyboardInterrupt:
            print("\\nOperation interrupted by user. Exiting...")

    def execute_code(self):
{user_code}

    def self_destruct(self):
        print("\\nKill switch file indicates self-destruction. Deleting this script.")
        os.remove(__file__)  

if __name__ == "__main__":
    kill_switch = KillSwitch("{url}", {check_interval})
    kill_switch.run()
'''

        with open(output_file, "w") as file:
            file.write(kill_switch_code)

        print(f"\033[32mCombined code written to \033[34m{output_file}\033[0m")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except RequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    except KeyboardInterrupt:
        print("\nOperation interrupted by user. Exiting...")

if __name__ == "__main__":
    main()
