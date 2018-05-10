# What
A dummy project (2 of 2) to demonstrate what seems like incorrect behavior in pipenv.

# How
1. `$ pipenv install && pipenv install -d` to install dependencies. For convenience sake, I checked in the gzipped library to this repo.
2. `$ pipenv run pytest` and watch it fail due to missing protobuf dependencies.
3. `$ pipenv install ./dependency/samplelibrary-0.0.1.tar.gz` to force it to install the library.
4. `$ pipenv run pytest` and it passes!
