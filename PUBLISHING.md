# Publishing Guide

This guide explains how to publish Python packages to PyPI using this project as a template.

## Table of Contents

- [Project Setup](#project-setup)
- [Poetry Configuration](#poetry-configuration)
- [GitHub Actions Setup](#github-actions-setup)
- [PyPI Trusted Publishing](#pypi-trusted-publishing)
- [Release Workflow](#release-workflow)
- [Best Practices](#best-practices)

## Project Setup

### 1. Project Structure

Ensure your project follows this structure:

```
your-project/
├── .github/
│   └── workflows/
│       ├── test.yml
│       ├── publish.yml
│       └── code-quality.yml
├── src/
│   └── your_package/
│       ├── __init__.py
│       └── your_modules.py
├── tests/
│   ├── __init__.py
│   └── test_*.py
├── pyproject.toml
├── README.md
├── LICENSE
├── CHANGELOG.md
└── RELEASE.md
```

### 2. pyproject.toml Configuration

Your `pyproject.toml` should be the single source of truth for your project metadata:

```toml
[tool.poetry]
name = "your-package-name"
version = "0.1.0"
description = "Your package description"
authors = ["Your Name <your.email@example.com>"]
license = "MIT"
readme = "README.md"
homepage = "https://github.com/username/your-package"
repository = "https://github.com/username/your-package"
documentation = "https://github.com/username/your-package#readme"
keywords = ["python", "your", "keywords"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Typing :: Typed",
]
packages = [{include = "your_package", from = "src"}]

[tool.poetry.dependencies]
python = "^3.11"
# Your runtime dependencies here

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"
pytest-cov = "^4.1.0"
black = "^23.0.0"
isort = "^5.12.0"
flake8 = "^6.0.0"
mypy = "^1.5.0"
pre-commit = "^3.4.0"
twine = "^4.0.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

### 3. Dynamic Version Loading

In your `src/your_package/__init__.py`:

```python
"""Your package description."""

import sys

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version

try:
    __version__ = version("your-package-name")
except Exception:
    # Fallback for development environments
    __version__ = "0.0.0-dev"

# Your exports
from .your_module import YourClass

__all__ = ["YourClass", "__version__"]
```

## Poetry Configuration

### Installation

```bash
# Install Poetry (if not already installed)
curl -sSL https://install.python-poetry.org | python3 -

# Or using pip
pip install poetry
```

### Basic Commands

```bash
# Initialize a new project
poetry new your-project

# Install dependencies
poetry install

# Add dependencies
poetry add requests
poetry add --group dev pytest

# Update dependencies
poetry update

# Build package
poetry build

# Publish (manual)
poetry publish
```

## GitHub Actions Setup

### 1. Workflow Files

Create three workflow files in `.github/workflows/`:

#### test.yml
- Runs on pushes and pull requests
- Tests across multiple Python versions and operating systems
- Includes code quality checks

#### code-quality.yml
- Focuses on code formatting, linting, and type checking
- Runs security scans

#### publish.yml
- Triggered only by version tags (`v*.*.*`)
- Publishes to PyPI using trusted publishing

### 2. Secrets and Environment Variables

No secrets are required! The publishing workflow uses GitHub's trusted publishing feature.

## PyPI Trusted Publishing

### Setup

1. Go to [PyPI](https://pypi.org/manage/account/publishing/)
2. Add a new trusted publisher:
   - **PyPI Project Name**: `your-package-name`
   - **Owner**: `your-github-username`
   - **Repository name**: `your-repository-name`
   - **Workflow filename**: `publish.yml`
   - **Environment name**: `release` (optional but recommended)

### Benefits

- ✅ No API tokens to manage
- ✅ Automatic token rotation
- ✅ Enhanced security
- ✅ Audit trail
- ✅ No secrets in repository

## Release Workflow

### 1. Development Cycle

```bash
# Work on your changes
git checkout -b feature/new-feature
# Make changes, add tests
git add .
git commit -m "Add new feature"
git push origin feature/new-feature

# Create PR and merge to main
```

### 2. Prepare Release

```bash
# Update version
poetry version patch  # or minor/major

# Update CHANGELOG.md
# Commit changes
git add pyproject.toml CHANGELOG.md
git commit -m "Bump version to v1.2.3"
git push origin main
```

### 3. Create Release

```bash
# Create and push tag
VERSION=$(poetry version --short)
git tag "v$VERSION"
git push origin "v$VERSION"
```

### 4. Monitor

- Watch GitHub Actions for build/publish status
- Check PyPI for successful publication
- Verify installation: `pip install your-package-name`

## Best Practices

### Code Quality

1. **Use pre-commit hooks**:
   ```bash
   poetry run pre-commit install
   ```

2. **Follow PEP 8** with Black formatting
3. **Add type hints** and use mypy
4. **Write comprehensive tests** with good coverage
5. **Document your code** with docstrings

### Versioning

1. **Follow Semantic Versioning**: `MAJOR.MINOR.PATCH`
2. **Use poetry version** command to update versions
3. **Tag releases** with `v` prefix: `v1.2.3`
4. **Maintain a CHANGELOG.md**

### Testing

1. **Test on multiple Python versions**
2. **Include edge cases** and error conditions
3. **Aim for high test coverage** (>85%)
4. **Test package installation** before releasing

### Security

1. **Use trusted publishing** instead of API tokens
2. **Enable branch protection** on main branch
3. **Require reviews** for pull requests
4. **Run security scans** (bandit, safety)

### Documentation

1. **Write clear README.md** with examples
2. **Include installation instructions**
3. **Document API** with docstrings
4. **Maintain release notes**

## Common Issues and Solutions

### Package Name Conflicts

```bash
# Check if name is available
pip search your-package-name

# Reserve name on PyPI before first upload
```

### Build Failures

```bash
# Test build locally
poetry build
poetry run twine check dist/*

# Check for missing files
poetry show --tree
```

### Import Errors

```bash
# Test installation in clean environment
python -m venv test_env
source test_env/bin/activate
pip install your-package-name
python -c "import your_package; print(your_package.__version__)"
```

### Version Mismatches

- Ensure tag format: `vX.Y.Z`
- Ensure pyproject.toml version: `X.Y.Z`
- Check workflow logs for specific errors

## Example Commands Summary

```bash
# Complete release workflow
poetry version patch
git add pyproject.toml
git commit -m "Bump version to v$(poetry version --short)"
git push origin main
git tag "v$(poetry version --short)"
git push origin "v$(poetry version --short)"

# Local testing
poetry build
poetry run twine check dist/*
poetry run pytest
```

## Further Reading

- [Poetry Documentation](https://python-poetry.org/docs/)
- [PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Python Packaging Guide](https://packaging.python.org/)
- [Semantic Versioning](https://semver.org/)