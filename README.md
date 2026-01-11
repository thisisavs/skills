# Claude Code Skills (Public)

Custom skills (slash commands) for [Claude Code](https://claude.ai/claude-code).

## Skills

| Skill | Description |
|-------|-------------|
| `/nanobanana` | Generate and edit images using Google Gemini |
| `/veo` | Generate videos using Google Veo |
| `/wind-down` | Session end checklist - review & update docs |

## Usage

To use these skills, copy them to your Claude Code skills folder:

```bash
# Windows
copy skills\<skill-name> %USERPROFILE%\.claude\skills\

# Mac/Linux
cp -r skills/<skill-name> ~/.claude/skills/
```

Then invoke with `/<skill-name>` in Claude Code.

## Structure

```
skills/
├── nanobanana/
│   ├── SKILL.md
│   └── scripts/generate.py
├── veo/
│   └── SKILL.md
└── wind-down/
    └── SKILL.md
```

## License

Feel free to use and modify these skills.
