# Makefile for building and testing project documentation

.PHONY: help
help:
	@echo "  clean             to remove the build directory for a fresh build"
	@echo "  html              to remove the build directory and run a fresh HTML build"
	@echo "  docs-test         to run the docs tests"
	@echo "  preview           to run a live preview of docs using sphinx-autobuild"
	@echo "  docker-html       to build docs in a docker container"
	@echo "  docker-preview    to build live preview of docs using sphinx-autobuild in a docker container"
	@echo "  docker-test       to build and test docs in a docker container"
	@echo "  grammar-check     run the grammar check in a docker container"
	@echo "  deploy-release    deploys a tagged release to clouddocs.f5.com"
	@echo "  docker-test       deploys branch to clouddocs.f5.com"

# Remove the _build directory for a fresh build
.PHONY: clean
clean:
	rm -rf docs/_build

# Remove _build directory and run a fresh HTML build
.PHONY: html
html:
	make clean
	make -C docs/ html

# Build live preview of docs
.PHONY: preview
preview:
	make clean
	make -C docs preview

# Remove _build directory and run the docs tests
.PHONY: docs-test
docs-test:
	make clean
	./docs/scripts/test-docs.sh

# run HTML build in a Docker container
.PHONY: docker-html
docker-html:
	./docs/scripts/docker-docs.sh make html

# Build live preview of docs in a Docker container
.PHONY: docker-preview
docker-preview:
	DOCKER_RUN_ARGS="-p 127.0.0.1:8000:8000" ./docs/scripts/docker-docs.sh make preview

# run docs quality tests in a Docker container
.PHONY: docker-test
docker-test:
	./docs/scripts/docker-docs.sh make docs-test

# run the grammar check in a Docker container
.PHONY: grammar-check
grammar-check:
	write-good `find docs -iname '*.rst'` --passive --so --no-illusion --thereIs --cliches

# deploy docs to production site
# if this is a tagged release, the docs go to /products/openstack/agent/<branch>/vX.Y
.PHONY: deploy-release
deploy-release:
	./docs/scripts/deploy-docs.sh publish-product-docs-to-prod openstack/agent/mitaka $RELEASE_TAG

# deploy docs to production site
# if this is not a tagged release, the docs go to /products/openstack/agent/<branch>
.PHONY: deploy-branch
deploy-branch:
	./docs/scripts/deploy-docs.sh publish-product-docs-to-prod openstack/agent mitaka
