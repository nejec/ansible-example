SHELL := /bin/bash

ANSIBLE_INVENTORY ?= linux-servers.yml

.DEFAULT_GOAL := help
.PHONY: help vagrant/*

help: ## Prints this text
	@printf "\nTargets:\n\n"
	@grep -E '^[a-zA-Z_/%\-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'
	@printf "\nDocs:\n\n"
	@printf "See docs folder for detailed documentation and guides.\n\n"

setup: environment vendor ## Install ansible and vendor dependencies

environment: ## Install all required python modules
	@echo "#### Preparing environment for Ansible"
	pip install --no-cache -r requirements.txt

vendor: vendor/roles vendor/collection ## Install dependencies (external ansible roles)

vendor/roles: ## Install dependencies (external ansible roles)
	@echo "#### Downloading required external roles"
	ansible-galaxy role install \
		--role-file vendor/vendor.yml \
		--roles-path vendor/ \
		--force

vendor/collection: ## Install dependencies (external ansible collections)
	@echo "#### Downloading required external collections"
	ansible-galaxy collection install \
		--requirements-file vendor/vendor.yml \
		--force

test: test/syntax test/lint ## Test the syntax, lint files

test/syntax:
	@echo "#### Testing ansible play syntax"
	find ./playbooks -maxdepth 1 -type f -name '*.yml' | xargs -t -n1 ansible-playbook --syntax-check -i $(ANSIBLE_INVENTORY)

test/lint:
	@echo "#### Testing ansible play syntax and lint"
	find . -mindepth 2 -type f \
		-name '*.yml' \
		-not -path "./vendor/*" \
		-not -path "./playbooks/*" \
		-not -path "./.direnv/*" | xargs -L1 -n1 ansible-lint
