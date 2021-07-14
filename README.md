# Plaza API

## Getting Started

Clone the repo

```bash
$ git clone git@github.com:plazainc/api.git
```

Create a new environment folder in your project directory

```bash
$ python3 -m venv ~/path-to-repo/.venv
```

Enter the python virtual environment

```bash
$ source ~/projects/plaza/api/.venv/bin/activate
```

Install the required python packages

```bash
$ sudo pip install -r requirements.txt
```

Make sure the following VSCode extensions are installed:

```
Azure Functions
Azure Storage
Python
```

Log into Azure and make sure the Azure subscriptions are showing up

Sync cloud settings to your local environment
1. Press `F1` to open the VSCode command pallette and select `Azure Functions: Download Remote Settings...`
2. Select `plazadev`
3. Accept any confirmations to overwrite files