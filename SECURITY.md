# Security Policy

## Supported Versions

We actively support the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |
| < 0.1   | :x:                |

## Reporting a Vulnerability

We take the security of our software seriously. If you believe you have found a security vulnerability in this project, please report it to us as described below.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please send an email to gh.pascon@gmail.com with the following information:

- Type of issue (e.g. buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit the issue

This information will help us triage your report more quickly.

### What to Expect

- We will acknowledge receipt of your vulnerability report within 48 hours
- We will provide a detailed response within 7 days indicating the next steps in handling your report
- We will keep you informed of the progress towards a fix and full announcement
- We may ask for additional information or guidance

### Responsible Disclosure

We kindly ask that you:

- Allow us reasonable time to resolve the issue before making any information public
- Make a good faith effort to avoid privacy violations, destruction of data, and interruption or degradation of our service
- Only interact with accounts you own or with explicit permission of the account holder

## Security Measures

This project implements several security measures:

### Code Quality
- Static analysis with flake8 and mypy
- Dependency scanning
- Automated security scans with bandit

### CI/CD Security
- No hardcoded secrets in repository
- Use of GitHub's trusted publishing for PyPI
- Minimal required permissions for workflows
- Secure artifact handling

### Dependencies
- Regular dependency updates
- Vulnerability scanning of dependencies
- Minimal dependency footprint

## Security Best Practices for Users

When using this package:

1. Always use the latest version
2. Verify package integrity when installing
3. Review the changelog for security-related updates
4. Report any suspicious behavior

## Contact

For security concerns, contact: gh.pascon@gmail.com

For general questions, use [GitHub Issues](https://github.com/ghpascon/publish_lib_ghp/issues).