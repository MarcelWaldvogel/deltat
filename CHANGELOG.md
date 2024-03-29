# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/)
and this project adheres to [Semantic Versioning](https://semver.org/).


# 1.1.2 - 2021-11-18
## Added

## Fixed
- `project_url`, not `package_url`

## Changed
- Clean `build` directory first


# 1.1.1 - 2021-11-18
## Added

## Fixed

## Changed
- Only project metadata to meet the desires of repositories and analyzers


# 1.1.0 - 2021-07-05
## Added
- Test cases, finally!

## Fixed
- Week support did not work at all; weeks could not be used

## Changed
- No longer throws an `AssertionError` on unparseable strings, but our own
  `TimeFormatError`, a subclass of `ValueError`. (Floating-point parsing
  errors continue to return `ValueError`, so you can catch both with that
  exception.)


# 1.0.1 - 2021-06-22
## Added
- The trailing `s` for seconds is now optional

## Fixed

## Changed


# 1.0.0 - 2020-11-18
## Added
- Is now a Python package
- Support for weeks

## Fixed

## Changed


# 0.9.0 - 2020-11-18
## Added
- Created from https://stackoverflow.com/a/51916936/2445204
- Documented origin, license
- Improved code readability
- Allowed spaces for more readable string

## Fixed

## Changed

