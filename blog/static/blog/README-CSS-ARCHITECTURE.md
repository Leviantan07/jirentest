# CSS Architecture — Quick Start

## 📍 Where CSS is Located

```
blog/static/blog/
└── index.css              ← Load THIS from templates (✅ Updated)
    ├── base.css           (Variables, reset, typography)
    ├── bootstrap-overrides.css (Bootstrap customizations)
    ├── components/
    │   ├── layout.css     (Navigation and sidebar)
    │   ├── shells-auth.css
    │   ├── buttons-badges.css
    │   ├── forms-inputs.css
    │   ├── tables.css
    │   ├── lists-alerts.css
    │   ├── cards-panels.css
    │   ├── kanban.css
    │   ├── stitch-sprint.css
    │   ├── utilities-theme.css
    │   └── main-consolidated-pending.css (← Temporary fallback)
    ├── css/
    │   ├── git_accordion_consolidated.css
    │   └── _archive.css
    └── main-original-backup.css (← For reference only)
```

## ✅ What's Working

- [x] CSS loads from modular `index.css` entry point
- [x] Templates updated to reference `index.css`
- [x] Base styles (variables, typography, reset) functional
- [x] Bootstrap overrides applied
- [x] Layout components (navbar, sidebar) extracted
- [x] Full fallback (`main-consolidated-pending.css`) ensures no visual regression

## 🔧 Next Steps (Phase 2-5)

### Option 1: Automated Tooling (Recommended if available)
```python
# hypothetical script to automate fragmentation
python scripts/fragment_css.py \
  --source components/main-consolidated-pending.css \
  --targets shells-auth.css buttons-badges.css forms-inputs.css ...
```

### Option 2: Manual Fragmentation
See `CSS-REFACTORING-ROADMAP.md` for detailed section breakdowns

## 🧪 Testing

After making changes:
```bash
# 1. Collect static files
python manage.py collectstatic --noinput

# 2. Clear browser cache
# 3. Test on these pages:
# - Home, Projects, Tickets, Sprint board, Admin, Login
```

## 📊 Target Metrics

- **Current**: 150 KB (main.css, 5448 lines)
- **Target**: 130 KB (modularized + deduplicated, ~15% reduction)
- **Components**: 9 modules + 2 consolidation files
- **Deduplication**: 111+ Type B duplicates to eliminate
- **Orphan Prevention**: 34 unused classes documented in _archive.css

## 💾 Backups

- `main-original-backup.css` — Keep this! Original unmodified file.
- `components/main-consolidated-pending.css` — Temporary safety net. Delete once fragmentation complete.

## 🎓 Architecture Philosophy

- **Modular**: Each component in its own file for clarity
- **Ordered**: Foundation → Layout → Components → Fallback
- **Progressive**: Can be completed phase-by-phase without breaking
- **Documented**: Every step has comments explaining the reasoning
- **Safe**: Backups and fallback mechanisms ensure rollback capability

---

**Status**: Ready for Phase 2 (Fragmentation)
**Time Estimate**: 4 weeks phased
**Risk Level**: LOW (fallback in place, templates updated, backups secured)
