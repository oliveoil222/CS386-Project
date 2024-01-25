# CS386-Project
Help Desk Ticketing Project for Spring CS 386
---
## Installation
- TODO: Figure out how to deploy production style.
- Likely use NGINX, Gunicorn, and Google Cloud?
---
## Development Environment Setup
1. Fork the GitHub Group Project Repository
2. Clone your Fork using ```git clone https://github.com/YOUR_GITHUB_USERNAME_HERE/CS386-Project.git```
3. ```cd CS386-Project```
4. Linux/MacOS: ```python -m venv .venv```
On Linux, you will need the python#.##-full package and/or python-is-python3 in order to setup dev environment.
On MacOS, use `python3` instead. You may need to homebrew Python or install via installer on [Python's Website](https://python.org)
Windows: `py -3 -m venv .venv` You will need to install Python, and make sure to add to PATH environment variables. If having trouble because the Microsoft Store keeps opening, use the following article: [Microsoft Store keeps opening when I type Python](https://stackoverflow.com/a/58773979)
5. Linux/MacOS: ```. .venv/bin/activate```
Windows: ```.venv\Scripts\activate```
6. ```pip install -r requirements.txt```
7. Run the application in dev/debug mode with the command `flask --app ssts run --debug`
Note: Debug mode will reload on py file changes, great for developing in real time.
---
## Handy Documentation Links
- [Flask Documentation](https://flask.palletsprojects.com/en/3.0.x/)
- [Jinja Templating](https://jinja.palletsprojects.com/en/3.1.x/templates/)
- [Click Documentation](https://click.palletsprojects.com/en/8.1.x/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
---
## Contributors
- Olivia V. [oliveoil222](https://github.com/oliveoil222)
- Hannah P. [hannahpenado](https://github.com/hannahpenado)
- Charles D. [cmd644](https://github.com/cmd644)
- Dallon J. [dallonjarman](https://github.com/dallonjarman)
- Sam C. [GH Username](https://github.com)
- Jared K. [GH Username](https://github.com/)
