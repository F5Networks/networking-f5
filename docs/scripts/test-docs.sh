#!/usr/bin/env bash
# Test docs build, grammar, and links
# can be run standalone or with docker-docs.sh

set -x
set -e

echo "Building docs with Sphinx"
make html

echo "Checking grammar and style"
make grammar-check

echo "Checking links"
make -C docs/ linkcheck
