# Git Commit Message Standards

## 📝 **Conventional Commits Specification**

The most widely adopted standard is **Conventional Commits**, which provides a lightweight convention for commit messages.

### **Format:**
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### **Types:**

| Type | Description |
|------|-------------|
| **feat** | A new feature |
| **fix** | A bug fix |
| **docs** | Documentation only changes |
| **style** | Changes that don't affect code meaning (white-space, formatting, etc.) |
| **refactor** | Code change that neither fixes a bug nor adds a feature |
| **perf** | Code change that improves performance |
| **test** | Adding missing tests or correcting existing tests |
| **build** | Changes that affect build system or external dependencies |
| **ci** | Changes to CI configuration files and scripts |
| **chore** | Other changes that don't modify src or test files |
| **revert** | Reverts a previous commit |

### **Examples:**

```
feat: add email notification on login
```
```
fix(auth): prevent race condition in token refresh
```
```
docs: update API documentation for user endpoints
```
```
style: remove trailing whitespace
```
```
refactor: simplify error handling in payment processor
```
```
test: add unit tests for user service
```
```
revert: revert "feat: add new login flow"
```

## 📋 **Commit Message Best Practices**

### **Subject Line (First Line):**
- **Limit to 50 characters** (or 72 max)
- Use **imperative mood** ("add" not "added")
- **Capitalize** the first letter
- **No period** at the end
- Summarize the change, not what you did

### **Body (Optional):**
- Wrap at **72 characters**
- Explain **what** and **why**, not how
- Use bullet points for multiple points
- Can include motivation, implementation details, or reasoning

### **Footer (Optional):**
- Reference issues/PRs: `Fixes #123`, `Closes #456`
- Breaking changes: `BREAKING CHANGE: description`

## 🎯 **Why Follow Standards?**

1. **Automated changelog generation**
2. **Semantic versioning** (feat = minor, fix = patch, BREAKING = major)
3. **Better collaboration** and code review
4. **Easier debugging** and issue tracking
5. **Machine-readable** history

## 🔧 **Tools to Enforce Standards**

- **Commitlint** - Lint commit messages
- **Husky** + **lint-staged** - Git hooks
- **Commitizen** - Interactive commit CLI
- **Standard Version** - Auto-generate changelog
- **Semantic Release** - Automated versioning

## 📚 **Git Commit Best Practices**

- ✅ Commit **often**, with **atomic changes**
- ✅ Write messages in **present tense** ("fix" not "fixed")
- ✅ Use **consistent prefixes** for project areas
- ❌ Don't use vague messages ("update", "fix", "changes")
- ❌ Don't include unrelated changes
- ❌ Don't have WIP commits in main branches

## 💡 **Good vs Bad Examples**

### ❌ Bad:
```
fixed stuff
update
changes
bug fix
asdf
```

### ✅ Good:
```
fix: resolve memory leak in websocket connections

- Clean up event listeners on disconnect
- Prevent zombie connections in server pool

Fixes #234
```

## 🔍 **Semantic Versioning Integration**

| Commit Type | Version Bump |
|------------|--------------|
| fix | Patch (1.0.0 → 1.0.1) |
| feat | Minor (1.0.0 → 1.1.0) |
| BREAKING CHANGE | Major (1.0.0 → 2.0.0) |

## 🌐 **Multi-language Projects**

Consider adding emoji prefixes for visual scanning:
- ✨ `feat:` for new features
- 🐛 `fix:` for bug fixes
- 📝 `docs:` for documentation
- 💄 `style:` for styling
- ♻️ `refactor:` for code refactoring
- ✅ `test:` for tests

This standard is used by many open-source projects and companies including Angular, Jest, and many others.


# When to Commit: Best Practices

## 🎯 **Golden Rule: Commit Often, Push When Ready**

### **Core Principle: Atomic Commits**
Each commit should represent **one logical change** - a single fix, feature, or improvement.

## ✅ **Good Times to Commit**

### **1. After Completing a Logical Unit**
```
❌ DON'T: "fix multiple bugs" (too many things)
✅ DO: "fix login validation error" (single issue)
```

### **2. When You Reach a Checkpoint**
- After passing tests
- When code compiles successfully
- Before taking a break or lunch
- At the end of the day

### **3. Before Complex Operations**
- Before refactoring (commit current working state)
- Before merging branches
- Before trying experimental changes

### **4. For Specific Scenarios**

| Scenario | When to Commit |
|----------|----------------|
| **Bug fix** | Immediately after fixing and testing |
| **New feature** | After each working sub-component |
| **Refactoring** | After each logical restructuring |
| **Documentation** | After each meaningful addition |
| **Test addition** | When tests pass for new scenarios |
| **Configuration** | After each working config change |

## ❌ **When NOT to Commit**

### **1. Broken Code**
```bash
# BAD - Code doesn't compile or tests fail
git commit -m "trying to fix bug"

# GOOD - Working code
git commit -m "fix: handle null input in parser"
```

### **2. Half-Done Features** (unless on feature branch)
```bash
# BAD - Incomplete feature on main branch
git commit -m "partial work on user profile"

# GOOD - On feature branch
git commit -m "wip: add profile picture upload"
```

### **3. Multiple Unrelated Changes**
```bash
# BAD - Mixed changes
git add .
git commit -m "update readme and fix bug and add feature"

# GOOD - Separate commits
git add README.md
git commit -m "docs: update installation instructions"

git add src/parser.js
git commit -m "fix: handle empty string in parser"

git add src/features/
git commit -m "feat: add export to PDF option"
```

### **4. Large Files or Secrets**
Never commit:
- API keys or passwords
- Large binary files (>100MB)
- Node_modules or build artifacts
- Personal configuration files

## 📊 **Commit Frequency Guidelines**

### **By Project Phase**

| Phase | Commit Frequency | Example |
|-------|-----------------|---------|
| **Initial setup** | After each dependency/config | "feat: add express with cors" |
| **Active development** | Every 15-30 minutes | "feat: add user validation" |
| **Bug fixing** | Per bug | "fix: memory leak in cache" |
| **Code review** | After addressing feedback | "refactor: simplify loop logic" |
| **Documentation** | Per section/page | "docs: add API examples" |

### **By Team Size**

| Team Size | Strategy |
|-----------|----------|
| **Solo project** | Commit whenever you want, but follow atomic rule |
| **Small team (2-5)** | Commit after each completed task, push daily |
| **Large team** | Strict atomic commits, rebase before pushing |

## 🚦 **Workflow Examples**

### **Feature Development Flow**
```bash
# Start feature branch
git checkout -b feature/user-auth

# Work on sub-task 1: login form
# ... code ...
git commit -m "feat: add login form UI"

# Work on sub-task 2: validation
# ... code ...
git commit -m "feat: add form validation"

# Work on sub-task 3: API integration
# ... code ...
git commit -m "feat: connect login to API"

# Final polish
git commit -m "style: improve login button styling"
```

### **Bug Fix Flow**
```bash
# Reproduce bug
# Find cause
git commit -m "test: add test case for null input bug"

# Fix the bug
git commit -m "fix: handle null input in parser"

# Verify fix
# (No commit needed for verification)
```

## 📋 **Commit Checklist**

Before each commit, ask:

- [ ] Does this represent **one logical change**?
- [ ] Does the code **compile/run**?
- [ ] Do **tests pass** (if applicable)?
- [ ] Is the commit message **descriptive**?
- [ ] Am I committing **secrets** or **large files**?
- [ ] Did I **review the diff** before committing?

## 🎨 **Commit Size Guidelines**

### **Too Small**
```bash
# Overkill - too granular
git commit -m "add space after if statement"
git commit -m "fix typo in comment"
git commit -m "rename variable x to counter"

# Better - combine related style fixes
git commit -m "style: improve code readability"
```

### **Too Large**
```bash
# Bad - too much
git commit -m "complete rewrite of payment system"

# Better - break into pieces
git commit -m "feat: add payment gateway interface"
git commit -m "feat: implement Stripe integration"
git commit -m "test: add payment processing tests"
git commit -m "docs: update payment documentation"
```

## 🎯 **The Perfect Commit**

### **Characteristics:**
- ✅ **Focused**: One specific change
- ✅ **Tested**: All tests pass
- ✅ **Descriptive**: Clear message explains why
- ✅ **Reversible**: Can be reverted without breaking other features
- ✅ **Independent**: Doesn't depend on uncommitted changes

### **Example Perfect Commits:**
```bash
# Feature addition
git commit -m "feat: add password reset functionality

- Add reset token generation
- Create email service integration
- Implement token validation endpoint
- Add rate limiting for security

Closes #123"

# Bug fix
git commit -m "fix: prevent XSS in user profile input

Sanitize HTML tags in bio field before saving to database.
Use DOMPurify library for sanitization.

Fixes #456"

# Refactoring
git commit -m "refactor: extract payment validation logic

Move validation rules from controller to separate service
for better testability and reusability.

No functional changes."
```

## 📈 **Signs You're Committing at the Right Frequency**

### **Too Infrequent:**
- You dread writing commit messages
- Commits contain 20+ files
- Can't remember what changed
- Hard to revert specific changes
- Merge conflicts are common

### **Too Frequent:**
- Commits break functionality
- Team members complain about noise
- CI pipeline runs constantly
- History is hard to read
- WIP commits everywhere

### **Just Right:**
- Easy to generate changelog
- Simple to revert specific features
- Clear project history
- Smooth code reviews
- Minimal merge conflicts

Remember: **There's no perfect frequency** - adjust based on your project, team, and workflow!