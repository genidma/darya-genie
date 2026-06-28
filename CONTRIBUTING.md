# Contributing to Darya Genie

## Development Workflow

This repository uses a structured branching strategy to ensure code quality, security, and proper testing before merging into production:

### Branch Structure

1. **`main`** - Production branch
   - Contains code that has been tested, audited, and is ready for deployment
   - Must be stable and production-ready

2. **`main-dev`** - Integration and testing branch  
   - Receives merged PRs from feature branches after testing
   - Used for ongoing development and feature consolidation
   - All changes pass rigorous testing and security audits here

3. **`feature/*`** - Feature branches
   - Created from `main` for new features or significant changes
   - Each feature should have isolated development with clear scope

### Recommended Workflow

1. **Create a feature branch:**
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes:**
   - Work on the feature branch
   - Keep changes focused and well-tested
   - Follow the project's code conventions

3. **Test your changes:**
   ```bash
   pytest tests/
   ```

4. **Create a pull request:**
   - Open a PR to merge into `main-dev` branch
   - PR must pass CI/CD pipeline including:
     - Automated testing
     - Security audits (dependency checks)
     - Static analysis (SAST)

5. **Review and merge:**
   - Code review by maintainers
   - If approved, merge into `main-dev`

6. **Monitor integration:**
   - Changes in `main-dev` are tested before promotion
   - Only stable, audited changes reach `main`

### Code Standards

- Follow existing code style and patterns
- Write clean, readable code with minimal comments
- All new code must pass existing test suite
- Security best practices are mandatory

### Security Review Process

Before merging to `main-dev`:

1. **Dependency audit:**
   ```bash
   pip-audit -r src/api/requirements.txt
   ```

2. **Static analysis:**
   ```bash
   bandit -r src/api/
   ```

### Getting Started Locally

1. Fork the repository
2. Clone your fork
3. Set up your development environment
4. Follow the workflow above

### Need Help?

- Ask for help in discussions
- Check existing documentation
- Look at the project's history for patterns

## Developer Guidelines

This repository operates under specific guidelines to ensure code quality, security, and maintainability. Please review and follow these standards when contributing.

### Code Review Process

Before code can be merged into `main-dev`, it must undergo a comprehensive review process:

1. **Initial Review:**
   - All pull requests must be reviewed by at least one maintainer
   - Code must pass automated tests and security audits
   - Changes should be focused and well-documented

2. **Security Requirements:**
   - All new dependencies must be vetted for security vulnerabilities
   - Code must follow security best practices
   - Sensitive information must never be committed

3. **Testing Requirements:**
   - All existing tests must continue to pass
   - New functionality must have comprehensive test coverage
   - Integration tests must verify end-to-end functionality

### Branch Management

The branching strategy ensures that only production-ready code reaches the main branch:

1. **Feature Development:**
   - All new features or significant changes should be developed in isolated feature branches
   - Feature branches should not be created from `main-dev` to prevent merge conflicts
   - Feature branches should be created from the latest `main`

2. **Testing and Integration:**
   - Feature branches are merged into `main-dev` after passing all tests
   - `main-dev` contains consolidated features that have been tested together
   - Regular integration testing ensures compatibility between components

3. **Release Management:**
   - Only vetted, tested changes are promoted from `main-dev` to `main`
   - Release candidates should be created as needed from `main-dev`
   - Hotfixes may require special approval and expedited process

### Code Quality Standards

1. **Code Style:**
   - Follow the existing code patterns and conventions
   - Consistent formatting and naming conventions
   - No code comments unless absolutely necessary (except for complex logic)

2. **Testing:**
   - All existing tests must pass before merging
   - New functionality requires test coverage
   - Integration tests verify end-to-end scenarios

3. **Documentation:**
   - Maintain existing documentation
   - Update README or relevant docs for new features
   - Keep documentation in sync with code changes

### Development Best Practices

1. **Before Coding:**
   - Check existing implementations for similar patterns
   - Verify requirements are clear and complete
   - Understand the security and performance implications

2. **During Development:**
   - Write clean, efficient code
   - Ensure all tests pass
   - Follow the repository's coding standards

3. **Before Merging:**
   - Ensure thorough testing
   - Perform security review
   - Get appropriate approvals

### Security Considerations

This project requires strict security practices:

1. **Code Security:**
   - Never commit secrets, API keys, or passwords
   - Use environment variables for sensitive configuration
   - Follow secure coding practices

2. **Dependency Security:**
   - Keep dependencies up to date
   - Regularly audit for vulnerabilities
   - Use dependency locks where appropriate

3. **Access Control:**
   - Only trusted collaborators should have merge access
   - Review all changes for security implications
