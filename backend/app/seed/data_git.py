"""
Seed data for the Git & GitHub course — complete (Lessons 1-5).
"""

GIT_LESSONS = [
    {
        "slug": "git-01-introduction",
        "title": "1. Introduction to Git and Version Control",
        "level": "beginner",
        "explanation": (
            "Git is a version control system that tracks changes to your code over time, letting you "
            "see history, undo mistakes, and collaborate with others without overwriting each other's "
            "work. Start tracking a project with 'git init', which creates a hidden .git folder "
            "storing all the history."
        ),
        "examples": (
            "git init                # start tracking a new project\n"
            "git status              # see what's changed\n"
            "git --version           # confirm git is installed\n"
        ),
        "practice": (
            "1. Install Git if it's not already installed (apt install git or pkg install git)\n"
            "2. Create a new folder and run git init inside it\n"
            "3. Run git status and observe the output"
        ),
        "mini_project": (
            "Mini Project: First Tracked Project\n"
            "Create a new folder called my_first_repo, initialize it with git init, create a README.md "
            "file inside it, then run git status to see it listed as an untracked file."
        ),
        "quiz": {
            "title": "Introduction to Git Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What is Git primarily used for?",
                    "option_a": "Editing photos",
                    "option_b": "Tracking changes to code over time",
                    "option_c": "Compiling programs",
                    "option_d": "Browsing the internet",
                    "correct_option": "b",
                    "explanation": "Git is a version control system that records and manages changes to files over time.",
                },
                {
                    "text": "Which command starts tracking a new project with Git?",
                    "option_a": "git start",
                    "option_b": "git init",
                    "option_c": "git new",
                    "option_d": "git create",
                    "correct_option": "b",
                    "explanation": "git init initializes a new, empty Git repository in the current folder.",
                },
                {
                    "text": "Which command shows the current status of tracked/untracked changes?",
                    "option_a": "git status",
                    "option_b": "git show",
                    "option_c": "git check",
                    "option_d": "git info",
                    "correct_option": "a",
                    "explanation": "git status shows which files are staged, modified, or untracked.",
                },
            ],
        },
    },
    {
        "slug": "git-02-staging-committing",
        "title": "2. Staging and Committing",
        "level": "beginner",
        "explanation": (
            "Git works in stages: you modify files, then 'stage' the ones you want to save with "
            "'git add', then 'commit' them permanently to history with a descriptive message using "
            "'git commit -m'. Staging lets you choose exactly which changes go into each commit, even "
            "if you've edited many files."
        ),
        "examples": (
            "git add README.md          # stage a specific file\n"
            "git add .                  # stage all changed files\n"
            "git commit -m \"Add README with project description\"\n"
            "git log                    # view commit history\n"
        ),
        "practice": (
            "1. Modify a file, then stage it with git add\n"
            "2. Commit it with a clear, descriptive message\n"
            "3. Run git log to see your commit in the history"
        ),
        "mini_project": (
            "Mini Project: Commit History Practice\n"
            "Make 3 separate small changes to a project (e.g. add 3 different files one at a time), "
            "staging and committing each one separately with a meaningful message, then review the "
            "full history with git log."
        ),
        "quiz": {
            "title": "Staging and Committing Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does 'git add' do?",
                    "option_a": "Permanently saves changes to history",
                    "option_b": "Stages changes to be included in the next commit",
                    "option_c": "Deletes a file",
                    "option_d": "Uploads code to GitHub",
                    "correct_option": "b",
                    "explanation": "git add moves changes into the 'staging area', preparing them for a commit.",
                },
                {
                    "text": "Which command permanently records staged changes with a message?",
                    "option_a": "git save",
                    "option_b": "git commit -m 'message'",
                    "option_c": "git record",
                    "option_d": "git push -m",
                    "correct_option": "b",
                    "explanation": "git commit -m 'message' creates a permanent snapshot with a descriptive message.",
                },
                {
                    "text": "Which command shows the history of commits?",
                    "option_a": "git history",
                    "option_b": "git log",
                    "option_c": "git list",
                    "option_d": "git commits",
                    "correct_option": "b",
                    "explanation": "git log displays the commit history, including messages, authors, and dates.",
                },
            ],
        },
    },
    {
        "slug": "git-03-branching-merging",
        "title": "3. Branching and Merging",
        "level": "intermediate",
        "explanation": (
            "A branch is an independent line of development, letting you work on a feature without "
            "affecting the main codebase. Create one with 'git branch name' or 'git checkout -b name', "
            "switch with 'git checkout name', and combine changes back into another branch with "
            "'git merge name'."
        ),
        "examples": (
            "git branch feature-login          # create a new branch\n"
            "git checkout feature-login        # switch to it\n"
            "# ... make changes and commit them ...\n"
            "git checkout main                 # switch back to main\n"
            "git merge feature-login           # merge changes into main\n"
        ),
        "practice": (
            "1. Create a new branch called practice-branch\n"
            "2. Switch to it, make a change, and commit it\n"
            "3. Switch back to main and merge practice-branch into it"
        ),
        "mini_project": (
            "Mini Project: Feature Branch Workflow\n"
            "Simulate a real workflow: create a branch called add-about-page, add an about.md file and "
            "commit it, switch to main, and merge add-about-page in. Confirm the file now exists on main."
        ),
        "quiz": {
            "title": "Branching and Merging Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What is a branch in Git?",
                    "option_a": "A backup of the whole repository",
                    "option_b": "An independent line of development within the same repository",
                    "option_c": "A type of commit",
                    "option_d": "A remote server",
                    "correct_option": "b",
                    "explanation": "Branches let you develop features or fixes in isolation before merging them back.",
                },
                {
                    "text": "Which command switches to an existing branch?",
                    "option_a": "git switch-to",
                    "option_b": "git checkout branch-name",
                    "option_c": "git move branch-name",
                    "option_d": "git go branch-name",
                    "correct_option": "b",
                    "explanation": "git checkout branch-name (or git switch branch-name) changes your active branch.",
                },
                {
                    "text": "Which command combines changes from one branch into your current branch?",
                    "option_a": "git combine",
                    "option_b": "git merge branch-name",
                    "option_c": "git join branch-name",
                    "option_d": "git add branch-name",
                    "correct_option": "b",
                    "explanation": "git merge integrates the commits from the named branch into your current branch.",
                },
            ],
        },
    },
    {
        "slug": "git-04-github-remote",
        "title": "4. Working with GitHub (remote, push, pull, clone)",
        "level": "intermediate",
        "explanation": (
            "GitHub hosts Git repositories online, enabling backup and collaboration. 'git remote add "
            "origin <url>' links your local repo to a GitHub repository. 'git push' uploads your local "
            "commits to GitHub; 'git pull' downloads and merges changes from GitHub. 'git clone <url>' "
            "downloads an entire existing repository to your machine."
        ),
        "examples": (
            "# Link a local repo to GitHub and push it\n"
            "git remote add origin https://github.com/username/my-repo.git\n"
            "git push -u origin main\n"
            "\n"
            "# Get the latest changes from GitHub\n"
            "git pull origin main\n"
            "\n"
            "# Download a repository that already exists on GitHub\n"
            "git clone https://github.com/username/some-repo.git\n"
        ),
        "practice": (
            "1. Create a new empty repository on GitHub\n"
            "2. Link a local project to it with git remote add origin, then push your commits\n"
            "3. Clone a public repository to practice git clone"
        ),
        "mini_project": (
            "Mini Project: Publish Your Project\n"
            "Take one of your earlier practice projects, initialize Git if needed, create a GitHub "
            "repository for it, push all your commits, and confirm the code appears correctly on "
            "GitHub.com."
        ),
        "quiz": {
            "title": "GitHub Remote Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which command uploads your local commits to GitHub?",
                    "option_a": "git upload",
                    "option_b": "git push",
                    "option_c": "git send",
                    "option_d": "git commit --remote",
                    "correct_option": "b",
                    "explanation": "git push uploads local commits to the linked remote repository.",
                },
                {
                    "text": "Which command downloads and merges changes from GitHub into your local branch?",
                    "option_a": "git pull",
                    "option_b": "git fetch-merge",
                    "option_c": "git download",
                    "option_d": "git sync",
                    "correct_option": "a",
                    "explanation": "git pull fetches remote changes and merges them into your current branch.",
                },
                {
                    "text": "Which command downloads an entire existing GitHub repository to your machine?",
                    "option_a": "git copy",
                    "option_b": "git clone <url>",
                    "option_c": "git download <url>",
                    "option_d": "git get <url>",
                    "correct_option": "b",
                    "explanation": "git clone creates a full local copy of a remote repository, including its history.",
                },
            ],
        },
    },
    {
        "slug": "git-05-collaboration-conflicts",
        "title": "5. Collaboration: Pull Requests and Merge Conflicts",
        "level": "advanced",
        "explanation": (
            "A Pull Request (PR) on GitHub proposes merging changes from one branch into another, "
            "letting teammates review code before it's merged. A merge conflict happens when Git can't "
            "automatically combine changes (e.g. two people edited the same line). Git marks the "
            "conflicting section in the file with <<<<<<<, =======, >>>>>>> markers — you edit the file "
            "to resolve it, then add and commit the result."
        ),
        "examples": (
            "# After a conflicting merge, a file might contain:\n"
            "<<<<<<< HEAD\n"
            "print(\"Version from main branch\")\n"
            "=======\n"
            "print(\"Version from feature branch\")\n"
            ">>>>>>> feature-branch\n"
            "\n"
            "# You manually edit to keep the correct version, then:\n"
            "git add conflicted_file.py\n"
            "git commit -m \"Resolve merge conflict\"\n"
        ),
        "practice": (
            "1. Read about how to open a Pull Request on GitHub.com after pushing a branch\n"
            "2. Intentionally create a merge conflict by editing the same line on two branches\n"
            "3. Resolve the conflict manually and complete the merge with git add + git commit"
        ),
        "mini_project": (
            "Mini Project: Simulated Team Collaboration\n"
            "Create two branches that both modify the same line of a file differently. Merge one into "
            "main, then try merging the second — resolve the resulting conflict by hand, choosing the "
            "correct final content, and complete the merge."
        ),
        "quiz": {
            "title": "Collaboration and Merge Conflicts Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What is a Pull Request used for?",
                    "option_a": "Deleting a repository",
                    "option_b": "Proposing and reviewing changes before merging them",
                    "option_c": "Downloading a repository",
                    "option_d": "Renaming a branch",
                    "correct_option": "b",
                    "explanation": "A Pull Request lets teammates review proposed changes on GitHub before they're merged.",
                },
                {
                    "text": "When does a merge conflict occur?",
                    "option_a": "Every time you run git merge",
                    "option_b": "When Git can't automatically combine changes to the same part of a file",
                    "option_c": "Only when using GitHub",
                    "option_d": "When you delete a branch",
                    "correct_option": "b",
                    "explanation": "Conflicts happen when overlapping changes can't be automatically reconciled by Git.",
                },
                {
                    "text": "After manually resolving a conflict in a file, what's the next step?",
                    "option_a": "Delete the file",
                    "option_b": "git add the file, then git commit to complete the merge",
                    "option_c": "Nothing more is needed",
                    "option_d": "Run git init again",
                    "correct_option": "b",
                    "explanation": "After editing out the conflict markers, stage and commit the resolved file to finish the merge.",
                },
            ],
        },
    },
]
