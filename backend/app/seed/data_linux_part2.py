"""
Seed data for the Linux course — Part 2 (Lessons 6-10, final batch).
"""

LINUX_LESSONS_PART2 = [
    {
        "slug": "linux-06-package-management",
        "title": "6. Package Management (apt / pkg)",
        "level": "intermediate",
        "explanation": (
            "Package managers install and update software easily. On Debian/Ubuntu Linux, use 'apt'. "
            "On Termux (Android), use 'pkg', which works similarly. Common commands: update the package "
            "list, then install/upgrade/remove specific packages. Always update before installing to "
            "get the latest available versions."
        ),
        "examples": (
            "# On Debian/Ubuntu Linux\n"
            "sudo apt update\n"
            "sudo apt install python3\n"
            "sudo apt remove python3\n"
            "\n"
            "# On Termux (Android) - no 'sudo' needed\n"
            "pkg update\n"
            "pkg install python\n"
            "pkg install git\n"
        ),
        "practice": (
            "1. Update your package list (apt update or pkg update)\n"
            "2. Install a small utility package like 'tree' or 'curl'\n"
            "3. Check the installed version with the tool's --version flag"
        ),
        "mini_project": (
            "Mini Project: Dev Environment Setup Script\n"
            "Write a shell script that updates packages and installs python, git, and curl in one run, "
            "printing a success message after each step."
        ),
        "quiz": {
            "title": "Package Management Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which package manager command is used on Termux (Android)?",
                    "option_a": "apt",
                    "option_b": "pkg",
                    "option_c": "brew",
                    "option_d": "yum",
                    "correct_option": "b",
                    "explanation": "Termux uses 'pkg' as a friendly wrapper around its package management system.",
                },
                {
                    "text": "Why run 'apt update' before installing a package?",
                    "option_a": "It's not necessary",
                    "option_b": "It refreshes the list of available packages and versions",
                    "option_c": "It deletes old packages",
                    "option_d": "It restarts the computer",
                    "correct_option": "b",
                    "explanation": "Updating refreshes package metadata so you install the latest available version.",
                },
                {
                    "text": "On Debian/Ubuntu, which command installs a package?",
                    "option_a": "apt install <package>",
                    "option_b": "apt get <package>",
                    "option_c": "apt add <package>",
                    "option_d": "apt new <package>",
                    "correct_option": "a",
                    "explanation": "'apt install <package>' is the standard command to install software on Debian/Ubuntu.",
                },
            ],
        },
    },
    {
        "slug": "linux-07-process-management",
        "title": "7. Process Management (ps, top, kill)",
        "level": "intermediate",
        "explanation": (
            "Every running program is a 'process' with a unique Process ID (PID). ps shows currently "
            "running processes; ps aux shows all of them in detail. top shows a live, updating view of "
            "processes and resource usage (press q to quit). kill <PID> stops a specific process; "
            "kill -9 <PID> force-kills an unresponsive one."
        ),
        "examples": (
            "ps aux                 # list all running processes\n"
            "top                    # live view of processes (press q to quit)\n"
            "\n"
            "# Find and kill a stuck process\n"
            "ps aux | grep python\n"
            "kill 1234              # gracefully stop process with PID 1234\n"
            "kill -9 1234           # force-kill it if it won't stop\n"
        ),
        "practice": (
            "1. Run ps aux and identify a process you recognize\n"
            "2. Run top and observe CPU/memory usage live, then press q to exit\n"
            "3. Start a long-running command (like 'sleep 100 &'), find its PID, and kill it"
        ),
        "mini_project": (
            "Mini Project: Process Monitor Script\n"
            "Write a shell script that runs 'ps aux', filters (using grep) for a specific keyword like "
            "'python', and prints only matching lines."
        ),
        "quiz": {
            "title": "Process Management Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does PID stand for?",
                    "option_a": "Process Identity Data",
                    "option_b": "Process ID",
                    "option_c": "Program Install Directory",
                    "option_d": "Personal Instance Data",
                    "correct_option": "b",
                    "explanation": "PID (Process ID) is the unique number the OS assigns to each running process.",
                },
                {
                    "text": "Which command shows a live, updating view of running processes?",
                    "option_a": "ps",
                    "option_b": "top",
                    "option_c": "list",
                    "option_d": "watch",
                    "correct_option": "b",
                    "explanation": "top displays a continuously updating list of processes and resource usage.",
                },
                {
                    "text": "Which command forcefully stops an unresponsive process with PID 1234?",
                    "option_a": "kill 1234",
                    "option_b": "kill -9 1234",
                    "option_c": "stop 1234",
                    "option_d": "end 1234",
                    "correct_option": "b",
                    "explanation": "kill -9 sends SIGKILL, forcefully terminating a process that won't respond to a normal kill.",
                },
            ],
        },
    },
    {
        "slug": "linux-08-environment-variables",
        "title": "8. Environment Variables and PATH",
        "level": "intermediate",
        "explanation": (
            "Environment variables store configuration values available to programs, e.g. HOME, USER, "
            "PATH. PATH is a special variable listing directories the shell searches for executable "
            "commands — that's how typing 'python' finds the right program. Use 'export VAR=value' to "
            "set one, and 'echo $VAR' to read it."
        ),
        "examples": (
            "echo $HOME              # your home directory\n"
            "echo $PATH              # directories searched for commands\n"
            "\n"
            "export MY_NAME=\"Kabiru\"\n"
            "echo $MY_NAME\n"
            "\n"
            "export PATH=$PATH:/my/custom/bin   # add a folder to PATH\n"
        ),
        "practice": (
            "1. Print your PATH variable and identify a few of the listed directories\n"
            "2. Create your own environment variable and echo it back\n"
            "3. Add a new folder to PATH temporarily and confirm with echo $PATH"
        ),
        "mini_project": (
            "Mini Project: Custom Command Setup\n"
            "Create a small shell script, make it executable, place it in a folder, then add that "
            "folder to your PATH so you can run the script by name from anywhere."
        ),
        "quiz": {
            "title": "Environment Variables and PATH Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What is PATH used for?",
                    "option_a": "Storing your password",
                    "option_b": "Listing directories the shell searches to find commands",
                    "option_c": "Tracking file permissions",
                    "option_d": "Storing your home folder name only",
                    "correct_option": "b",
                    "explanation": "PATH tells the shell where to look for executable programs when you type a command name.",
                },
                {
                    "text": "How do you set an environment variable in bash?",
                    "option_a": "set VAR=value",
                    "option_b": "export VAR=value",
                    "option_c": "VAR := value",
                    "option_d": "env VAR value",
                    "correct_option": "b",
                    "explanation": "'export VAR=value' sets and exports an environment variable in bash.",
                },
                {
                    "text": "How do you read the value of an environment variable called MY_NAME?",
                    "option_a": "echo MY_NAME",
                    "option_b": "echo $MY_NAME",
                    "option_c": "print(MY_NAME)",
                    "option_d": "read MY_NAME",
                    "correct_option": "b",
                    "explanation": "Prefixing a variable name with $ reads its value in the shell.",
                },
            ],
        },
    },
    {
        "slug": "linux-09-piping-redirection",
        "title": "9. Piping and Redirection",
        "level": "intermediate",
        "explanation": (
            "Piping (|) sends the output of one command as input to another, letting you chain simple "
            "tools into powerful workflows. Redirection sends output to a file: > overwrites a file "
            "with output, >> appends to it. < reads input from a file instead of the keyboard."
        ),
        "examples": (
            "ls -la | grep \".py\"       # list files, then filter for .py files\n"
            "\n"
            "echo \"Hello\" > greeting.txt      # write (overwrite) to a file\n"
            "echo \"World\" >> greeting.txt     # append to the same file\n"
            "cat greeting.txt                 # Hello\\nWorld\n"
            "\n"
            "ps aux | grep python | wc -l     # chain 3 commands together\n"
        ),
        "practice": (
            "1. Use ls | grep to filter files by a keyword\n"
            "2. Use > to save command output to a file, then >> to append more\n"
            "3. Chain 3 commands together with two pipes to solve a small task"
        ),
        "mini_project": (
            "Mini Project: Log Filter Tool\n"
            "Create a text file with 20 lines of fake log entries (some containing the word 'ERROR'). "
            "Use grep with piping to filter only ERROR lines and save them to errors_only.txt using >."
        ),
        "quiz": {
            "title": "Piping and Redirection Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does the | (pipe) symbol do?",
                    "option_a": "Deletes a file",
                    "option_b": "Sends one command's output as input to another command",
                    "option_c": "Comments out a line",
                    "option_d": "Ends a script",
                    "correct_option": "b",
                    "explanation": "Piping chains commands, feeding the output of the left command into the right command.",
                },
                {
                    "text": "What's the difference between > and >> in redirection?",
                    "option_a": "There is no difference",
                    "option_b": "> overwrites the file, >> appends to it",
                    "option_c": "> appends, >> overwrites",
                    "option_d": "> is for reading, >> is for writing",
                    "correct_option": "b",
                    "explanation": "> replaces a file's content entirely; >> adds new content to the end without erasing existing content.",
                },
                {
                    "text": "Which command would you pipe into to search/filter text output?",
                    "option_a": "grep",
                    "option_b": "mkdir",
                    "option_c": "touch",
                    "option_d": "chmod",
                    "correct_option": "a",
                    "explanation": "grep searches text for lines matching a pattern, commonly used after a pipe.",
                },
            ],
        },
    },
    {
        "slug": "linux-10-shell-scripting",
        "title": "10. Shell Scripting Basics",
        "level": "advanced",
        "explanation": (
            "A shell script is a text file of commands run in sequence, saved with a .sh extension. "
            "Start with a shebang line '#!/bin/bash' to specify the interpreter. Scripts can use "
            "variables, if statements, and for loops, similar to Python but with different syntax. "
            "Make a script executable with chmod +x, then run it with ./script.sh."
        ),
        "examples": (
            "#!/bin/bash\n"
            "# backup.sh - a simple shell script\n"
            "\n"
            "NAME=\"Kabiru\"\n"
            "echo \"Starting backup for $NAME...\"\n"
            "\n"
            "for file in *.txt; do\n"
            "    echo \"Backing up: $file\"\n"
            "done\n"
            "\n"
            "if [ -d \"backup\" ]; then\n"
            "    echo \"Backup folder already exists\"\n"
            "else\n"
            "    mkdir backup\n"
            "    echo \"Created backup folder\"\n"
            "fi\n"
        ),
        "practice": (
            "1. Write a script that prints a personalized greeting using a variable\n"
            "2. Write a script with a for loop that lists all .txt files in the current directory\n"
            "3. Write a script with an if statement that checks whether a given folder exists"
        ),
        "mini_project": (
            "Mini Project: Automated Backup Script\n"
            "Write a shell script backup.sh that: creates a 'backup' folder if it doesn't exist, copies "
            "all .txt files in the current directory into it, and prints a summary of how many files "
            "were backed up. Make it executable and run it with ./backup.sh."
        ),
        "quiz": {
            "title": "Shell Scripting Basics Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What line typically starts a bash shell script?",
                    "option_a": "#!/bin/bash",
                    "option_b": "<script>",
                    "option_c": "start-bash",
                    "option_d": "#!bash-start",
                    "correct_option": "a",
                    "explanation": "The shebang '#!/bin/bash' tells the system which interpreter should run the script.",
                },
                {
                    "text": "How do you make a script file executable?",
                    "option_a": "chmod +x script.sh",
                    "option_b": "chown +x script.sh",
                    "option_c": "run script.sh",
                    "option_d": "exec script.sh",
                    "correct_option": "a",
                    "explanation": "chmod +x adds execute permission, allowing the script to be run directly.",
                },
                {
                    "text": "How do you run an executable script named backup.sh in the current directory?",
                    "option_a": "backup.sh",
                    "option_b": "./backup.sh",
                    "option_c": "run backup.sh",
                    "option_d": "sh -run backup.sh",
                    "correct_option": "b",
                    "explanation": "'./' explicitly runs a script from the current directory.",
                },
            ],
        },
    },
]
