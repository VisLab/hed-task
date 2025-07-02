# Code Climate Setup Instructions

## Why Code Climate?

Code Climate provides:
- **Code Quality Analysis**: Detects maintainability issues, code smells, and complexity
- **Test Coverage Reporting**: Alternative to Codecov with excellent GitHub integration
- **Pull Request Reviews**: Automatic code quality feedback on every PR
- **Technical Debt Tracking**: Prioritized list of code improvements
- **Maintainability Ratings**: A-F grades for your codebase

## Setup Steps

### 1. Add Repository to Code Climate

1. Go to [codeclimate.com](https://codeclimate.com)
2. Sign in with your GitHub account
3. Click "Add a repository"
4. Select `VisLab/hed-task` from your repositories
5. Enable both "Maintainability" and "Test Coverage"

### 2. Get Test Reporter ID

1. In your Code Climate dashboard, go to your repository
2. Click on "Settings" → "Test Coverage"
3. Copy the "Test Reporter ID"

### 3. Add Secret to GitHub

1. Go to your GitHub repository settings
2. Navigate to "Secrets and variables" → "Actions"
3. Click "New repository secret"
4. **Name**: `CC_TEST_REPORTER_ID`
5. **Value**: Paste the Test Reporter ID from Code Climate

### 4. Optional: Configure Quality Thresholds

The `.codeclimate.yml` file has been created with sensible defaults for Python projects. You can customize:
- Complexity thresholds
- File/method length limits
- Code duplication sensitivity
- Which plugins to enable/disable

## Benefits for Your Project

✅ **Automated Quality Checks**: Every PR gets automatic code quality feedback
✅ **Coverage Tracking**: Test coverage trends and PR-level coverage changes
✅ **Maintainability Metrics**: Clear A-F grades help prioritize improvements
✅ **Security Analysis**: Bandit integration for security issue detection
✅ **Style Consistency**: PEP8, pycodestyle, and pydocstyle integration

## Comparison: Code Climate vs Codecov

| Feature | Code Climate | Codecov |
|---------|-------------|---------|
| Test Coverage | ✅ Excellent | ✅ Excellent |
| Code Quality | ✅ Advanced | ❌ None |
| Security Analysis | ✅ Built-in | ❌ None |
| Maintainability | ✅ A-F Grades | ❌ None |
| PR Integration | ✅ Excellent | ✅ Excellent |
| Badge Support | ✅ Yes | ✅ Yes |

**Recommendation**: Use both! They complement each other well:
- **Codecov**: Detailed coverage reports and trends
- **Code Climate**: Overall code quality + coverage

Both are free for open source projects.
