"""
Seed data for the Linux course — Part 1 (Lessons 1-5).
"""

LINUX_LESSONS_PART1 = [
    {
        "slug": "linux-01-introduction",
        "title": "1. Introduction to Linux and the Terminal",
        "level": "beginner",
        "explanation": (
            "Linux is a free, open-source operating system that powers most servers, and tools like "
            "Termux bring a real Linux environment to Android phones. The terminal (command line) lets "
            "you control your computer by typing commands instead of clicking icons — it's faster and "
            "more powerful once you're comfortable with it."
        ),
        "examples": (
            "# Print a welcome message\n"
            "echo \"Hello from the Linux terminal!\"\n"
            "\n"
            "# Show today's date\n"
            "date\n"
            "\n"
            "# Show which user you are logged in as\n"
            "whoami\n"
        ),
        "practice": (
            "1. Open your terminal (or Termux on Android)\n"
            "2. Run echo with your own custom message\n"
            "3. Run whoami and date and note the output"
        ),
        "mini_project": (
            "Mini Project: Terminal Info Report\n"
            "Run whoami, date, and pwd one after another and write down (in a text file) what each "
            "command told you about your system."
        ),
        "quiz": {
            "title": "Introduction to Linux Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What is the terminal used for?",
                    "option_a": "Only playing games",
                    "option_b": "Controlling the computer by typing text commands",
                    "option_c": "Browsing the internet only",
                    "option_d": "Editing photos",
                    "correct_option": "b",
                    "explanation": "The terminal lets you interact with the operating system using typed commands.",
                },
                {
                    "text": "Which command prints the currently logged-in username?",
                    "option_a": "whoami",
                    "option_b": "username",
                    "option_c": "me",
                    "option_d": "user",
                    "correct_option": "a",
                    "explanation": "whoami prints the username of the current user.",
                },
                {
                    "text": "Which app brings a Linux terminal environment to Android?",
                    "option_a": "Notepad",
                    "option_b": "Termux",
                    "option_c": "Camera",
                    "option_d": "Chrome",
                    "correct_option": "b",
                    "explanation": "Termux provides a full Linux terminal environment on Android devices.",
                },
            ],
        },
    },
    {
        "slug": "linux-02-navigation",
        "title": "2. File System Navigation (pwd, ls, cd)",
        "level": "beginner",
        "explanation": (
            "Linux organizes files in a tree of directories (folders) starting from root '/'. pwd "
            "('print working directory') shows where you currently are. ls lists files in the current "
            "directory (ls -l for details, ls -a to show hidden files). cd changes directory; 'cd ..' "
            "moves up one level, 'cd ~' goes to your home directory."
        ),
        "examples": (
            "pwd                 # show current directory\n"
            "ls                  # list files\n"
            "ls -la              # list all files with details\n"
            "cd Documents        # move into Documents folder\n"
            "cd ..               # move up one level\n"
            "cd ~                # go to home directory\n"
        ),
        "practice": (
            "1. Run pwd to see your current location\n"
            "2. Run ls -la to see all files, including hidden ones (starting with .)\n"
            "3. Create a folder, cd into it, then cd back out with cd .."
        ),
        "mini_project": (
            "Mini Project: Folder Explorer\n"
            "Starting from your home directory, navigate three folders deep (creating them if needed), "
            "print pwd at each level, then navigate all the way back to home using cd ~."
        ),
        "quiz": {
            "title": "File System Navigation Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which command shows your current directory?",
                    "option_a": "cd",
                    "option_b": "ls",
                    "option_c": "pwd",
                    "option_d": "dir",
                    "correct_option": "c",
                    "explanation": "pwd prints the full path of the current working directory.",
                },
                {
                    "text": "Which command lists files in the current directory?",
                    "option_a": "ls",
                    "option_b": "list",
                    "option_c": "show",
                    "option_d": "files",
                    "correct_option": "a",
                    "explanation": "ls lists the contents of the current (or a specified) directory.",
                },
                {
                    "text": "What does 'cd ..' do?",
                    "option_a": "Goes to the home directory",
                    "option_b": "Moves up one directory level",
                    "option_c": "Deletes the current directory",
                    "option_d": "Lists hidden files",
                    "correct_option": "b",
                    "explanation": "'..' refers to the parent directory, so 'cd ..' moves up one level.",
                },
            ],
        },
    },
    {
        "slug": "linux-03-file-operations",
        "title": "3. File Operations (touch, mkdir, cp, mv, rm)",
        "level": "beginner",
        "explanation": (
            "touch creates an empty file. mkdir creates a directory. cp copies a file (cp -r for "
            "directories). mv moves or renames a file. rm deletes a file (rm -r for directories, rm -rf "
            "to force-delete without confirmation — use with extreme caution, deletions are permanent)."
        ),
        "examples": (
            "touch notes.txt         # create an empty file\n"
            "mkdir projects          # create a folder\n"
            "cp notes.txt backup.txt # copy a file\n"
            "mv backup.txt projects/ # move file into a folder\n"
            "rm notes.txt            # delete a file\n"
            "rm -r old_folder        # delete a folder and its contents\n"
        ),
        "practice": (
            "1. Create a file called test.txt with touch\n"
            "2. Copy it to test_backup.txt with cp\n"
            "3. Rename test_backup.txt to archive.txt using mv, then delete both files with rm"
        ),
        "mini_project": (
            "Mini Project: Project Folder Setup Script\n"
            "Using commands, create a folder called my_app, then inside it create src/, tests/, and "
            "docs/ subfolders, plus an empty README.md file inside my_app."
        ),
        "quiz": {
            "title": "File Operations Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which command creates a new empty file?",
                    "option_a": "mkdir",
                    "option_b": "touch",
                    "option_c": "new",
                    "option_d": "create",
                    "correct_option": "b",
                    "explanation": "touch creates a new empty file if it doesn't already exist.",
                },
                {
                    "text": "Which command creates a new directory?",
                    "option_a": "touch",
                    "option_b": "mkdir",
                    "option_c": "newdir",
                    "option_d": "folder",
                    "correct_option": "b",
                    "explanation": "mkdir (make directory) creates a new folder.",
                },
                {
                    "text": "Why should rm -rf be used with extreme caution?",
                    "option_a": "It only works on Windows",
                    "option_b": "It permanently force-deletes files/folders without confirmation",
                    "option_c": "It's slower than other commands",
                    "option_d": "It requires internet access",
                    "correct_option": "b",
                    "explanation": "rm -rf deletes recursively and forcefully with no confirmation and no recycle bin — deletions cannot be undone.",
                },
            ],
        },
    },
    {
        "slug": "linux-04-viewing-editing-files",
        "title": "4. Viewing and Editing Files (cat, less, nano)",
        "level": "beginner",
        "explanation": (
            "cat prints a whole file's contents to the screen at once. less lets you scroll through a "
            "large file page by page (press q to quit). nano is a simple, beginner-friendly terminal "
            "text editor: Ctrl+O saves, Ctrl+X exits. These tools let you inspect and edit files "
            "entirely from the terminal, without a graphical app."
        ),
        "examples": (
            "cat notes.txt        # print entire file content\n"
            "less biglog.txt      # scroll through a large file (press q to quit)\n"
            "nano notes.txt       # open notes.txt in the nano editor\n"
            "# Inside nano: type to edit, Ctrl+O to save, Ctrl+X to exit\n"
        ),
        "practice": (
            "1. Create a file with a few lines of text using nano\n"
            "2. View its contents using cat\n"
            "3. Open a longer file (or create one with many lines) and browse it using less"
        ),
        "mini_project": (
            "Mini Project: Terminal Journal\n"
            "Use nano to write a short journal entry into journal.txt about what you learned today, "
            "save and exit, then use cat to display the entry back on screen."
        ),
        "quiz": {
            "title": "Viewing and Editing Files Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which command prints an entire file's content at once?",
                    "option_a": "less",
                    "option_b": "cat",
                    "option_c": "nano",
                    "option_d": "view",
                    "correct_option": "b",
                    "explanation": "cat outputs the full content of a file directly to the terminal.",
                },
                {
                    "text": "Which key combination saves a file in nano?",
                    "option_a": "Ctrl+S",
                    "option_b": "Ctrl+O",
                    "option_c": "Ctrl+W",
                    "option_d": "Ctrl+Z",
                    "correct_option": "b",
                    "explanation": "In nano, Ctrl+O ('Write Out') saves the current file.",
                },
                {
                    "text": "Which tool is better for scrolling through a very large file page by page?",
                    "option_a": "cat",
                    "option_b": "less",
                    "option_c": "touch",
                    "option_d": "mkdir",
                    "correct_option": "b",
                    "explanation": "less loads content incrementally, making it ideal for browsing large files without flooding the screen.",
                },
            ],
        },
    },
    {
        "slug": "linux-05-permissions",
        "title": "5. Permissions and Ownership (chmod, chown)",
        "level": "intermediate",
        "explanation": (
            "Every file has permissions for the owner, group, and others, covering read (r), write (w), "
            "and execute (x). ls -l shows permissions like '-rwxr-xr--'. chmod changes permissions "
            "(e.g. chmod +x script.sh makes a file executable). chown changes who owns a file — useful "
            "on multi-user Linux servers."
        ),
        "examples": (
            "ls -l script.sh\n"
            "# -rw-r--r-- 1 user user 120 Aug 1 10:00 script.sh\n"
            "\n"
            "chmod +x script.sh     # make the file executable\n"
            "./script.sh            # now you can run it directly\n"
            "\n"
            "chmod 644 notes.txt    # owner read/write, others read-only\n"
        ),
        "practice": (
            "1. Create a shell script file and try running it directly (it should fail without execute permission)\n"
            "2. Use chmod +x to make it executable, then run it again\n"
            "3. Run ls -l and identify what the permission string means for a file of your choice"
        ),
        "mini_project": (
            "Mini Project: Executable Script Toolkit\n"
            "Write 3 small shell scripts (each just echoing a message), make all 3 executable using "
            "chmod, and run each one directly using ./ syntax."
        ),
        "quiz": {
            "title": "Permissions and Ownership Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which command changes a file's permissions?",
                    "option_a": "chown",
                    "option_b": "chmod",
                    "option_c": "perm",
                    "option_d": "access",
                    "correct_option": "b",
                    "explanation": "chmod (change mode) modifies a file's read/write/execute permissions.",
                },
                {
                    "text": "What does chmod +x do to a file?",
                    "option_a": "Deletes the file",
                    "option_b": "Makes the file executable",
                    "option_c": "Makes the file read-only",
                    "option_d": "Renames the file",
                    "correct_option": "b",
                    "explanation": "+x adds execute permission, allowing the file to be run as a program/script.",
                },
                {
                    "text": "Which command changes who owns a file?",
                    "option_a": "chown",
                    "option_b": "chmod",
                    "option_c": "owner",
                    "option_d": "chgrp only",
                    "correct_option": "a",
                    "explanation": "chown (change owner) changes a file's owning user and/or group.",
                },
            ],
        },
    },
]
