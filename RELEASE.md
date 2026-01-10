# Release Process

This document describes how to release a new version of `publish-lib-ghp` to PyPI.

## Overview

Our release process is fully automated using GitHub Actions. When you push a Git tag in the format `vX.Y.Z`, the CI/CD pipeline will:

1. Run the complete test suite on multiple Python versions and operating systems
2. Perform code quality checks (formatting, linting, type checking)
3. Build the package
4. Validate the distribution files
5. Publish to PyPI using trusted publishing (no API tokens required)

## Prerequisites

Before creating a release:

1. Ensure all changes are merged to the `main` branch
2. All tests are passing in CI
3. Code quality checks are passing
4. Version is updated in `pyproject.toml`

## Release Steps

### 1. Update the Version

Update the version in `pyproject.toml` using Poetry:

```bash
# For patch releases (bug fixes)
poetry version patch

# For minor releases (new features, backward compatible)
poetry version minor

# For major releases (breaking changes)
poetry version major

# For specific version
poetry version 1.2.3
```

### 2. Update CHANGELOG.md (Recommended)

Update `CHANGELOG.md` with the new version and changes:

```markdown
## [1.2.3] - 2026-01-10

### Added
- New feature X
- New feature Y

### Fixed
- Bug fix Z

### Changed
- Breaking change A (if any)
```

### 3. Commit Version Changes

```bash
git add pyproject.toml CHANGELOG.md
git commit -m "Bump version to v1.2.3"
git push origin main
```

### 4. Create and Push Git Tag

```bash
# Get the current version from pyproject.toml
VERSION=$(poetry version --short)

# Create the tag
git tag "v$VERSION"

# Push the tag (this triggers the release pipeline)
git push origin "v$VERSION"
```

### 5. Monitor the Release

1. Go to the [Actions tab](https://github.com/ghpascon/publish_lib_ghp/actions)
2. Watch the "Publish to PyPI" workflow
3. If successful, check [PyPI](https://pypi.org/project/publish-lib-ghp/)

## Semantic Versioning

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR** version when you make incompatible API changes
- **MINOR** version when you add functionality in a backward compatible manner
- **PATCH** version when you make backward compatible bug fixes

Examples:
- `1.0.0` → `1.0.1` (patch: bug fix)
- `1.0.1` → `1.1.0` (minor: new feature)
- `1.1.0` → `2.0.0` (major: breaking change)

## Pre-release Versions

For pre-release versions, use:

```bash
# Alpha versions
poetry version prerelease  # 1.0.0 → 1.0.0a1
poetry version prerelease  # 1.0.0a1 → 1.0.0a2

# Beta versions
poetry version 1.0.0b1

# Release candidates
poetry version 1.0.0rc1
```

## Testing Releases Locally

Before creating a tag, you can test the release process locally:

### 1. Build the Package

```bash
poetry build
```

### 2. Check the Distribution

```bash
poetry run twine check dist/*
```

### 3. Test Installation

```bash
# Create a temporary virtual environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install the built package
pip install dist/publish_lib_ghp-*.whl

# Test the package
python -c "from publish_lib_ghp import Greeting; print(Greeting().say_hello('Test'))"

# Clean up
deactivate
rm -rf test_env
```

## Rollback Process

If a release has issues:

### 1. Remove from PyPI (if possible)

PyPI allows deletion only within the first 72 hours and only if no one has downloaded the package.

### 2. Create a Hotfix Release

```bash
# Fix the issue
git checkout main
# Make your fixes
git add .
git commit -m "Hotfix: Description of fix"

# Create a patch release
poetry version patch
git add pyproject.toml
git commit -m "Bump version to v1.2.4 (hotfix)"
git push origin main

# Tag and release
VERSION=$(poetry version --short)
git tag "v$VERSION"
git push origin "v$VERSION"
```

## Troubleshooting

### Version Mismatch Error

If the pipeline fails with "Project version does not match tag version":

1. Ensure the version in `pyproject.toml` matches your tag
2. The tag should be in format `vX.Y.Z` (with 'v' prefix)
3. The version in pyproject.toml should be `X.Y.Z` (without 'v' prefix)

### Test Failures

If tests fail during release:

1. Check the [Actions tab](https://github.com/ghpascon/publish_lib_ghp/actions) for details
2. Fix the failing tests
3. Delete the problematic tag: `git tag -d vX.Y.Z && git push origin --delete vX.Y.Z`
4. Repeat the release process

### PyPI Publishing Issues

If publishing to PyPI fails:

1. Check that the package name is available and unique
2. Ensure GitHub Actions has proper permissions
3. Verify the trusted publishing configuration

## Security Notes

- ✅ No API tokens are stored in the repository
- ✅ Publishing uses GitHub's trusted publishing feature
- ✅ All workflows require approval for the `release` environment
- ✅ Package signatures are handled automatically

## Getting Help

- Check existing [Issues](https://github.com/ghpascon/publish_lib_ghp/issues)
- Review [GitHub Actions documentation](https://docs.github.com/en/actions)
- Consult [PyPI publishing guide](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)