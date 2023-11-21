include tools/make/*.mk
# please keep any rules idempotent if possible.
# NOTE: whenever useful, we'll use sentinel pattern with .make- prefix to avoid unnecessary work

# please keep dev-setup idempotent
dev-setup: deps

# use 'make -B deps' to force execution of rule
# `make deps` allows us to absract details of package manager without changing developer flow or github actions
deps: .make-dev-deps

# this should install all dependencies, and only those mentioned in the lock file
# Note that rule should be idempotent and return immediately if there's nothing to do, so that
# eg. test can depend on this. Strictly speaking this depends on 'pyproject.toml' too, but often those changes
# are not relevant to dependencies and user can always do `make -B <rule> to force rebuild`
.make-dev-deps: poetry.lock
	poetry install --with docs --sync
	touch $@
