# In terminal run:
# make release

# Reads version from pyproject.toml
version := $(shell python -c 'import tomlib; print(tomlib.load(open("pyproject.toml", "rb"))["project"]["version"])')

.SILENT: release

release: changelog build upload git_release clean

changelog:
	scriv collect

build:
	python -m build

upload:
	python -m twine upload --repository-url https://pip.funbit.io --username funbit dist/* --skip-existing

git_release:
	-git commit -a -m $(version)
	git push
	git tag -a $(version) -m $(version)
	git push origin $(version)
	scriv github-release

clean:
	-rm -r build