# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.
Please note we have a [code of conduct](CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.

## Development environment setup

To set up a development environment, please follow these steps:

1. Fork the [GitHub Group Project Repository](https://github.com/oliveoil222/CS386-Project)
2. Clone your Fork using 
   ```sh
   git clone https://github.com/YOUR_GITHUB_USERNAME_HERE/CS386-Project.git
   ```
2. Switch to the dev branch using `git checkout -b dev`
3. 
   ```sh
   cd CS386-Project
   ```
4. 
    - Linux/MacOS: ```python -m venv .venv```
    - On Linux, you will need the python#.##-full package and/or python-is-python3 in order to setup dev environment.
    - On MacOS, use `python3` instead. You may need to homebrew Python or install via installer on [Python's Website](https://python.org)
    - Windows: `py -3 -m venv .venv` You will need to install Python, and make sure to add to PATH environment variables. If having trouble because the Microsoft Store keeps opening, use the following article: [Microsoft Store keeps opening when I type Python](https://stackoverflow.com/a/58773979)
5. 
    - Linux/MacOS: ```. .venv/bin/activate```
    - Windows: ```.venv\Scripts\activate```
6. 
   ```py
   pip install -r requirements.txt
   ```
7. Run the application in dev/debug mode with the command 
   ```py
   flask --app ssts run --debug
   ```
Note: Debug mode will reload on py file changes, great for developing in real time.

## Issues and feature requests

You've found a bug in the source code, a mistake in the documentation or maybe you'd like a new feature? You can help us by [submitting an issue on GitHub](https://github.com/oliveoil222/CS386-Project/issues). Before you create an issue, make sure to search the issue archive -- your issue may have already been addressed!

Please try to create bug reports that are:

- _Reproducible._ Include steps to reproduce the problem.
- _Specific._ Include as much detail as possible: which version, what environment, etc.
- _Unique._ Do not duplicate existing opened issues.
- _Scoped to a Single Bug._ One bug per report.

**Even better: Submit a pull request with a fix or new feature!**

### How to submit a Pull Request

1. Search our repository for open or closed
   [Pull Requests](https://github.com/oliveoil222/CS386-Project/pulls)
   that relate to your submission. You don't want to duplicate effort.
2. Fork the project
3. Checkout the dev branch (`git checkout -b dev`) **This is where all new features go!**
4. Commit your changes (`git commit -m 'feat: add amazing_feature'`) Super Simple Ticketing System [SSTS] uses a simple .
5. Push to the branch (`git push origin dev`)
6. [Open a Pull Request](https://github.com/oliveoil222/CS386-Project/compare?expand=1)
7. If the feature/fix is accepted, the change will then move to the canary branch to be tested before moving to stable/main to be included as a rolling release.
