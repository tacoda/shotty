# shotty

Tool to manage AWS EC2 snapshots

## Configuring

TODO: YAML

## Running

`pipenv run python src/shotty.py <command> <subcommand> <--project=PROJECT>`

Information below is available in help

### Commands

- `instances`
- `volumes`
- `snapshots`

### Options

- `project`

### Building with `setuptools`

`pipenv install -d setuptools`

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
