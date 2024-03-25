<h1 align="center">
  <a href="https://github.com/oliveoil222/CS386-Project">
    <img src="docs/images/ssts.png" alt="Logo" width="100" height="100">
  </a>
</h1>

<div align="center">
  Super Simple Ticketing System [SSTS]
  <br />
  <a href="https://github.com/oliveoil222/CS386-Project/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/oliveoil222/CS386-Project/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
  .
  <a href="https://github.com/oliveoil222/CS386-Project/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+">Ask a Question</a>
</div>

<div align="center">
<br />

[![Project license](https://img.shields.io/github/license/oliveoil222/CS386-Project.svg?style=flat-square)](LICENSE)
[![Pull Requests welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/oliveoil222/CS386-Project/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)

</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Support](#support)
- [Project assistance](#project-assistance)
- [Contributing](#contributing)
- [Authors & contributors](#authors--contributors)
- [Security](#security)
- [Acknowledgements](#acknowledgements)

</details>

---

## About

Super Simple Ticketing System aims to fix a bit of the issues that plague other ticketing softwares. Issues such as slowness, dated interfaces, and miles of training needed to get the fullest out of the software.

### Built With

> Python
> Flask
> MongoDB
> HTML/CSS

## Getting Started

### Prerequisites

> [Python 3.12](https://python.org)
> [Flask](https://flask.palletsprojects.com/en/3.0.x/)
> [NGINX](https://nginx.org)
> [MongoDB Database](https://mongodb.com)
> [requirements.txt](requirements.txt)

### Installation

> Install [NGINX](https://nginx.org) on your favorite Linux OS
> Install [Python < 3.12-full](https://python.org) and Python-is-Python3 as packages
> Clone our stable/main branch with (`git clone https://github.com/oliveoil222/CS386-Project`)
> Then, (`cd CS386-Project`)
> Spin up a virtual environment with (`python -m venv .venv`)
> Activate the virtual environment with (`. .venv/bin/activate`)
> Use (`pip install -r requirements.txt`) to install the prerequisites
> Locate and edit the backendDB file with the (`server-url`) placeholder, and put your MongoDB address there.
> Install GUnicorn as a pip package with (`pip install gunicorn`)
> Run (`gunicorn -w 4 'ssts:app'`) to start the application
> Proxy with NGINX to the listening port.
> Open your web-app via your domain, given you've set DNS records and such.

## Usage

> Visit https://your-domain-here.tld to use the web application.
> Our intuitive web interface should be able to adequately guide a user through using our application. Honestly, play around with it, there isn't too much to mess up!
> Check out our demo application on https://ssts.app!

## Roadmap

See the [open issues](https://github.com/oliveoil222/CS386-Project/issues) for a list of proposed features (and known issues).

- [Top Feature Requests](https://github.com/oliveoil222/CS386-Project/issues?q=label%3Aenhancement+is%3Aopen+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Top Bugs](https://github.com/oliveoil222/CS386-Project/issues?q=is%3Aissue+is%3Aopen+label%3Abug+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Newest Bugs](https://github.com/oliveoil222/CS386-Project/issues?q=is%3Aopen+is%3Aissue+label%3Abug)

## Support

Reach out to the maintainer at one of the following places:

- [GitHub issues](https://github.com/oliveoil222/CS386-Project/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+)
- Contact mainline contributors through their GitHub Profiles. (See Authors and Contributors)

## Project assistance

If you want to say **thank you** or/and support active development of Super Simple Ticketing System [SSTS]:

- Add a [GitHub Star](https://github.com/oliveoil222/CS386-Project) to the project.
- Tweet about the Super Simple Ticketing System [SSTS].
- Write interesting articles about the project on [Dev.to](https://dev.to/), [Medium](https://medium.com/) or your personal blog.

Together, we can make Super Simple Ticketing System [SSTS] **better**!

## Contributing

Please read [our contribution guidelines](docs/CONTRIBUTING.md), and thank you for being involved!

## Authors & contributors

The original setup of this repository is by [Olivia Vester](https://github.com/oliveoil222).
Main repository contributors are 
- Olivia V. [oliveoil222](https://github.com/oliveoil222)
- Hannah P. [hannahpenado](https://github.com/hannahpenado)
- Charles D. [cmd644](https://github.com/cmd644)
- Dallon J. [dallonjarman](https://github.com/dallonjarman)
- Sam C. [SamCain04](https://github.com/SamCain04)
- Jared K. [jjkagie](https://github.com/jjkagie)

For a full list of all authors and contributors, see [the contributors page](https://github.com/oliveoil222/CS386-Project/contributors).

## Security

Super Simple Ticketing System [SSTS] follows good practices of security, but 100% security cannot be assured.
Super Simple Ticketing System [SSTS] is provided **"as is"** without any **warranty**. Use at your own risk.

## License

This project is licensed under the **Unlicense**.

See [LICENSE](LICENSE) for more information.

## Acknowledgements
- Dr. Ana Chaves [chavesana](https://github.com/chavesana) for the opportunity to develop this Python Application.