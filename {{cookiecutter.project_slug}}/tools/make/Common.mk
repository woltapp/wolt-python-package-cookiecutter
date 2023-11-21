# use sane shell by default, as well as other settings
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables --no-builtin-rules
.DEFAULT_GOAL = help

# location for source files
SRC ?= src/

# Hack to make help rule work, given that rule has suffix ' ## <help text'.
# Minor adjustments to make it work properly with included files
.PHONY: help
help: ## This help dialog
	@grep -hE '^[a-zA-Z-][a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort -u -t: -k1,1 | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-22s\033[0m %s\n", $$1, $$2}'

.PHONY: grep-tech-debt
grep-tech-debt:  ## Grep for lines with various types of tech debt
	@echo "### ❗Checking for FIXMEs"
	@git grep --line-number --ignore-case --extended-regexp '# (fixme|xxx)' $(SRC) || echo "No FIXMEs ✅"
	@echo "### 🚧 Silenced issues"
	@git grep --line-number --ignore-case --extended-regexp '# (noqa|type: ignore|xxx)' $(SRC) || echo "No silenced issues ✅"
	@echo "### 🚧 TODOs"
	@git grep --line-number --ignore-case --extended-regexp '# (todo|tbd)' $(SRC) || echo "No TODOs ✅"

######################################################################################################
# Common rules which probably should be present regardless of technologies, but implemented
# in specific files or root Makefile. Avoid modifying this file, because it would be updated by the template
#
# Note that specifying .PHONY here means actual implementation
# needs only rule body (repeating .PHONY is not needed)
######################################################################################################

.PHONY: deps
deps: ## Set installed dependencies (including dev) to match those in the lock file

.PHONY: build
build: ## Build project and/or container image(s)

.PHONY: build-dev
build-dev: ## Build project and/or container image(s) for local development/testing

# this rule should do asdf install, setup .envrc etc, anything that helps new devs in getting started
.PHONY: dev-setup
dev-setup: ## Prepare project ready for local development

.PHONY: fmt
fmt: ## Apply all automated formatters

.PHONY: release
release: ## Create new release

.PHONY: local-run
local-run: ## Run system locally without docker

.PHONY: docker-run
docker-run: ## Run system locally with docker

.PHONY: test
test: ## Run automated tests

.PHONY: lint
lint: ## Analyze code for issues/smells