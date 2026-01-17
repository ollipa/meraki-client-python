color := $(shell tput setaf 2)
off := $(shell tput sgr0)
TARGETS = meraki_client codegen tests

.PHONY: all
all: lint test

.PHONY: lint
lint: format linter typecheck

.PHONY: test
test:
	@printf '\n\n*****************\n'
	@printf '$(color)Running tests$(off)\n'
	@printf '*****************\n'
	uv run pytest

.PHONY: typecheck
typecheck:
	@printf '\n\n*****************\n'
	@printf '$(color)Running type checker$(off)\n'
	@printf '*****************\n'
	uv run ty check ${TARGETS}

.PHONY: format
format:
	@printf '\n\n*****************\n'
	@printf '$(color)Running format$(off)\n'
	@printf '*****************\n'
	uv run ruff format --check ${TARGETS}

.PHONY: linter
linter:
	@printf '\n\n*****************\n'
	@printf '$(color)Running linter$(off)\n'
	@printf '*****************\n'
	uv run ruff check ${TARGETS}

.PHONY: generate
generate:
ifndef VERSION
	$(error VERSION is required. Usage: make generate VERSION=1.66.0)
endif
	@printf '\n\n*****************\n'
	@printf '$(color)Generating SDK$(off)\n'
	@printf '*****************\n'
	@uv run python codegen/main.py -v $(VERSION)
	@printf "Formatting the generated code..."
	@uv run ruff check --quiet --select I,F401,RUF022 --fix meraki_client
	@uv run ruff format meraki_client > /dev/null
	@printf "Done!\n"
