# shotty

Tool to manage AWS EC2 snapshots

## Installation

```sh
pip3 install https://s3.amazonaws.com/tacoda-dist/shotty/shotty-0.1-py3-none-any.whl
```

## Configuration

TODO: YAML

## Usage

### Commands

- `instances`
- `volumes`
- `snapshots`

### Options

- `project`

## Building From Source

### Running Locally

`pipenv run python src/shotty.py <command> <subcommand> <--project=PROJECT>`

Information below is available in help

### Building with `setuptools`

```sh
pipenv install -d setuptools
```

Setup script is in `setup.py`

We can do many things with the setup script.

To package, we want to generate a wheel.

`pipenv run python setup.py bdist_wheel`

After building the wheel, we can install with `pip`

`pip3 install dist/shotty-0.1-py3-none-any.whl`

`pip3 show shotty`

Use like a CLI:

`shotty instances list`

Distribute via PyPI, S3 or system repos

`pip3` can install from a URL (relevant if hosting on S3)
