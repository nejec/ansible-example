# Ansible automation repository

For mod_security info read `MODSEC_README.md`.

## Development environment

### Dependencies

- python3.9
- vagrant
- direnv

> **_NOTE:_** For running vagrant vms virtualbox or libvirtd is required.

> **_NOTE:_**  development dependencies can be also installed using `nix-shell`, which provides
> more reliable and deterministic development environment.

### Using development environment

```shell
direnv allow
make setup
```

If you change `requirements.txt` or ansible `vendor.yml` you
can re-run setup to update your environment:

```shell
make setup
```

### Using nix-shell

[nix](https://nixos.org/) provides alternative way to install required system
dependencies (like python and vagrant), without touching your system install.
This provides a clean and deterministic way to install all required tools, without
polluting your system.

First you will have to install [nix](https://nixos.org/), which provides
`nix-shell` command that you can use to enter development environment. If you
have `direnv` and `nix-shell` installed, `nix-shell` environment will be loaded
automatically.

You can manually enter nix shell using `nix-shell` command.

### Using visual studio code devcontainers

This project provides vscode devevelopment container environment.
It uses dockerized dev environment that starts shell container and
dockerized `libvirtd`. The only dependency is docker (on linux)
or docker desktop with enabled nested virtualization.

## Running vagrant testing scenarios

Vagrant provides a local testing playground, that automatically downloads vm images,
runs vms and provisions ansible playbooks.

Starting a vagrant scenario is simple as:

```shell
make vagrant/<name_of_scenario>
```

### Running vagrant

```shell
VAGRANT_SCENARIO=<name_of_scenario> vagrant up [--no-provision]
VAGRANT_SCENARIO=<name_of_scenario> vagrant provision
VAGRANT_SCENARIO=<name_of_scenario> vagrant ssh <machine_name>
VAGRANT_SCENARIO=<name_of_scenario> vagrant destroy
```

## Basic ansible short cheatsheat

Everything is run from root directory.

Run a playbook: e.g.

```sh
ansible-playbook playbooks/default.yml -i inventories/ls21_parsed.yml (--limit ubuntu2004 --tags splunk-forwarder)
```

Run a single command

```sh
ansible -i inventories/ls21_parsed.yml all -m ansible.builtin.shell -a 'env'
```
