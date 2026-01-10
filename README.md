# publish-lib-ghp

[![PyPI version](https://badge.fury.io/py/publish-lib-ghp.svg)](https://badge.fury.io/py/publish-lib-ghp)
[![Python versions](https://img.shields.io/pypi/pyversions/publish-lib-ghp.svg)](https://pypi.org/project/publish-lib-ghp/)
[![Tests](https://github.com/ghpascon/publish_lib_ghp/workflows/Test/badge.svg)](https://github.com/ghpascon/publish_lib_ghp/actions?query=workflow%3ATest)
[![Code Quality](https://github.com/ghpascon/publish_lib_ghp/workflows/Code%20Quality/badge.svg)](https://github.com/ghpascon/publish_lib_ghp/actions?query=workflow%3A%22Code+Quality%22)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A professional Python library demonstrating best practices for packaging and publishing to PyPI using modern tools and automated CI/CD.

## 🚀 Features

- **Professional packaging** with Poetry and pyproject.toml
- **Automated CI/CD** with GitHub Actions
- **Comprehensive testing** with pytest and coverage reporting
- **Code quality enforcement** with Black, isort, flake8, and mypy
- **Trusted publishing** to PyPI (no API tokens required)
- **Semantic versioning** with automated releases
- **Dynamic versioning** using importlib.metadata
- **Security scanning** with bandit
- **Pre-commit hooks** for code quality

## 📦 Installation

```bash
pip install publish-lib-ghp
```

## 🔧 Usage

```python
from publish_lib_ghp import Greeting, Operations

# Create instances
greeting = Greeting()
operations = Operations()

# Basic greeting functionality
message = greeting.say_hello("World")
print(message)  # Output: Hello, World!

# Time-specific greetings
morning_msg = greeting.get_greeting_with_time("Alice", "morning")
print(morning_msg)  # Output: Good morning, Alice!

# Say goodbye
goodbye_msg = greeting.say_goodbye("Bob")
print(goodbye_msg)  # Output: Goodbye, Bob!

# Mathematical operations
result = operations.add(5, 3)
print(result)  # Output: 8
```

## 🛠️ Development

### Prerequisites

- Python 3.11+
- [Poetry](https://python-poetry.org/docs/#installation)

### Setup

```bash
# Clone the repository
git clone https://github.com/ghpascon/publish_lib_ghp.git
cd publish_lib_ghp

# Install dependencies
poetry install

# Install pre-commit hooks
poetry run pre-commit install
```

### Testing

```bash
# Run all tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=src/publish_lib_ghp --cov-report=html

# Run specific test file
poetry run pytest tests/test_greeting.py
```

### Code Quality

```bash
# Format code
poetry run black src tests
poetry run isort src tests

# Lint code
poetry run flake8 src tests

# Type checking
poetry run mypy src

# Run all quality checks
poetry run pre-commit run --all-files
```

### Building

```bash
# Build the package
poetry build

# Check the build
poetry run twine check dist/*
```

## 📋 API Reference

### Greeting Class

#### `say_hello(name: str) -> str`

Say hello to someone.

**Parameters:**
- `name` (str): The name of the person to greet

**Returns:**
- str: A greeting message

**Raises:**
- ValueError: If name is empty or not a string

#### `say_goodbye(name: str) -> str`

Say goodbye to someone.

**Parameters:**
- `name` (str): The name of the person to say goodbye to

**Returns:**
- str: A goodbye message

**Raises:**
- ValueError: If name is empty or not a string

#### `get_greeting_with_time(name: str, time_of_day: str) -> str`

Get a time-specific greeting.

**Parameters:**
- `name` (str): The name of the person to greet
- `time_of_day` (str): Time of day ('morning', 'afternoon', 'evening')

**Returns:**
- str: A time-specific greeting message

**Raises:**
- ValueError: If name is invalid or time_of_day is not recognized

### Operations Class

#### `add(a: int, b: int) -> int`

Perform addition of two integers.

**Parameters:**
- `a` (int): The first number
- `b` (int): The second number

**Returns:**
- int: The sum of a and b

**Example:**
```python
ops = Operations()
result = ops.add(5, 3)  # Returns 8
```

## 🚀 Release Process

This project uses automated releases via GitHub Actions. See [RELEASE.md](RELEASE.md) for detailed instructions.

### Quick Release

```bash
# Update version
poetry version patch  # or minor/major

# Commit and tag
git add pyproject.toml
git commit -m "Bump version to v$(poetry version --short)"
git push origin main
git tag "v$(poetry version --short)"
git push origin "v$(poetry version --short)"
```

The CI/CD pipeline will automatically:
1. Run tests across multiple Python versions
2. Perform code quality checks
3. Build the package
4. Publish to PyPI

## 📝 Documentation

- [Release Process](RELEASE.md) - How to create and publish releases
- [Publishing Guide](PUBLISHING.md) - Comprehensive guide for package publishing
- [Contributing](CONTRIBUTING.md) - How to contribute to this project
- [Security Policy](SECURITY.md) - Security guidelines and reporting
- [Changelog](CHANGELOG.md) - Project history and changes

## 🏗️ Project Structure

```
publish_lib_ghp/
├── .github/
│   └── workflows/          # GitHub Actions CI/CD pipelines
├── src/
│   └── publish_lib_ghp/    # Main package code
├── tests/                  # Test suite
├── pyproject.toml         # Project configuration (single source of truth)
├── README.md              # This file
├── CHANGELOG.md           # Version history
├── RELEASE.md             # Release process guide
├── PUBLISHING.md          # Publishing guide
├── CONTRIBUTING.md        # Contribution guidelines
├── SECURITY.md            # Security policy
└── LICENSE                # MIT License
```

## 🔐 Security

This project follows security best practices:

- ✅ No hardcoded secrets or API tokens
- ✅ Trusted publishing to PyPI via GitHub Actions
- ✅ Automated security scanning with bandit
- ✅ Dependency vulnerability checking
- ✅ Code signing and verification

See our [Security Policy](SECURITY.md) for details.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Quick Start

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Run quality checks: `poetry run pre-commit run --all-files`
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to the branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Poetry](https://python-poetry.org/) for modern Python packaging
- [GitHub Actions](https://github.com/features/actions) for CI/CD
- [PyPI](https://pypi.org/) for package distribution
- [pytest](https://pytest.org/) for testing framework

## 📊 Project Status

- ✅ **Active Development**: This project is actively maintained
- ✅ **Production Ready**: Suitable for production use
- ✅ **Well Tested**: Comprehensive test coverage
- ✅ **Documented**: Complete documentation available
- ✅ **Secure**: Follows security best practices

---

**Author:** Gabriel Henrique Pascon  
**Email:** gh.pascon@gmail.com  
**GitHub:** [@ghpascon](https://github.com/ghpascon)