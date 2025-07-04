# Git Workflow Documentation

## Branch Strategy: Trunk-Based Development

We use a trunk-based development workflow with the following conventions:

### Branch Types

| Type | Pattern | Example | Purpose |
|------|---------|---------|---------|
| Feature | `feat/<description>` | `feat/binance-websocket` | New functionality |
| Bugfix | `fix/<description>` | `fix/ccxt-rate-limit` | Bug fixes |
| Experiment | `exp/<description>` | `exp/shap-analysis` | Research/experiments |
| Hotfix | `hotfix/<description>` | `hotfix/telegram-auth` | Production fixes |

### Commit Message Format

Following [Conventional Commits](https://conventionalcommits.org/):

```
<type>(scope): <subject>

<body – wrap at 72 chars>

<footer – Closes #issue or BREAKING CHANGE: ...>
```

### Daily Workflow

1. **Create feature branch**:
   ```bash
   git checkout -b feat/my-feature
   ```

2. **Make changes and commit**:
   ```bash
   git add .
   git commit -m "feat(scope): add new functionality"
   ```

3. **Push and create PR**:
   ```bash
   git push --set-upstream origin feat/my-feature
   gh pr create --fill --web
   ```

4. **After merge, cleanup**:
   ```bash
   git checkout main
   git pull --ff-only
   git branch -d feat/my-feature
   ```

### Rules

- ❌ **Never commit directly to main**
- ✅ All changes go through Pull Requests
- ✅ CI must pass before merge
- ✅ Pre-commit hooks format code automatically
- ✅ Use semantic versioning for releases
