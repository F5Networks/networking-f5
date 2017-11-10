# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = python -msphinx
SPHINXPROJ    = F5ML2DriverforOpenStack
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)


# build live preview of docs locally
.PHONY: preview
preview:
	@echo "Running autobuild. View live edits at:"
	@echo "  http://0.0.0.0:8000"
	@echo ""
	sphinx-autobuild --host 0.0.0.0 -b html $(ALLSPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/html

