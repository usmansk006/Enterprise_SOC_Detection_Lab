# 09 — Scripts

This section contains scripts used for controlled security testing, automation, validation, and SOC lab operations.

## Organization

- `windows/` — Windows endpoint testing and validation scripts
- `linux/` — Linux/Wazuh server utility scripts

## Security

Scripts must not contain:

- Passwords
- API keys
- Authentication tokens
- Private keys
- Hard-coded credentials
- Other sensitive information

All testing scripts are intended for use within the authorized laboratory environment.
