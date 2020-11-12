# Tyme

![language: python][shield-language] ![license: GPL][shield-license] ![python: 3.7][shield-python-version] ![Tyme CI/CD](https://github.com/Cynnexis/tyme/workflows/Tyme%20CI/CD/badge.svg)

Tyme is a basic command-line interface that compute the time between two hours.

## Getting Started

### Prerequisites

You need [Python 3.7][python 3.7] to execute this script.

Here is the command to install all necessary packages:

With pip:

```bash
pip install --no-cache-dir -r requirements.txt
```

With conda (and its environment):

```bash
conda install --name myenv -c conda-forge --file requirements.txt
```

### Installing

To install this script, you first need to clone this project, and
then execute [`tyme.py`](https://github.com/Cynnexis/tyme/blob/master/tyme.py).

### Usage

To execute `tyme`, you just need to pass the time expression you want to compute:

**Example:**

```bash
$ python tyme.py (12h24 - 8h22) + (16:45- 13h)
7h47
```

#### Run with Docker 🐳

It is possible to run `tyme` from the given `Dockerfile`.

To execute `tyme` using docker, please refer to the example below:

```bash
cd path/to/tyme
make build-docker
docker run -it --rm cynnexis/tyme run "(12h24 - 8h22) + (16:45- 13h)"
```

> Please note the quotes around the time expression.

If you want to build the Dockerfile without using a Makefile:

```bash
docker build -t cynnexis/tyme .
```

### Alias

If your using bash, you can setup an alias to call `tyme`:

First, let's create a conda environment if you have not done iet yet:

```bash
cd path/to/tyme
conda create --name tyme python=3.7.6
conda install --name tyme -c conda-forge --file requirements.txt
```

Then, activate the environment:

```bash
conda activate tyme
```

Download the last dependencies:

```bash
pip install -r requirements.txt
```

Get the path to your Python environment:

```bash
which python
```

For this tutorial, let's assume the path is `/home/user/anaconda3/envs/tyme/bin/python`. Create an alias with the
following command:

```bash
echo alias tyme="/home/user/anaconda3/envs/tyme/bin/python /absolute/path/to/tyme/tyme.py" >> ~/.bash_aliases
```

And it's ready! To get all the commits messages of a local repository, go to your project folder, and execute the
`tyme` command such as:

```bash
tyme 12h - 8h
```

## Built With

* [Python 3.7][python 3.7]
* [typeguard][typeguard]
* [GitHub Actions][githubactions]
* [YAPF][yapf]

## Contributing

Contribution are not permitted yet, because this project is
really simple and should not be a real problem. You noticed a bug
in the script or in the source code? Feel free to post an issue
about it.

## Author

* **Valentin Berger ([Cynnexis](https://github.com/Cynnexis)):** developer

## License

This project is under the GNU Affero General Public License v3.0.
Please see the [LICENSE.txt](https://github.com/Cynnexis/tyme/blob/master/LICENSE.txt)
file for more detail (it's a really fascinating story written in
there!)

[python 3.7]: https://www.python.org/downloads/release/python-374/
[typeguard]: https://pypi.org/project/typeguard/
[githubactions]: https://github.com/features/actions
[yapf]: https://github.com/google/yapf
[shield-language]: https://img.shields.io/badge/language-python-yellow.svg
[shield-license]: https://img.shields.io/badge/license-GPL-blue.svg
[shield-python-version]: https://img.shields.io/badge/python-3.7-yellow.svg
