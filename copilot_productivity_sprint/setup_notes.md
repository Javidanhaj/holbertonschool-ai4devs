# AI Coding Assistant Setup Notes

## Objective
Prepare a development environment for the Copilot Productivity Sprint using Visual Studio Code and an AI coding assistant.

## Tools and extensions

| Component | Tool | Version |
| --- | --- | --- |
| Operating system | Windows / macOS / Linux | Check on the computer used |
| IDE | Visual Studio Code | Run `code --version` |
| Version control | Git | Run `git --version` |
| AI coding assistant | GitHub Copilot (VS Code extension) | Check the Extensions panel |
| AI chat assistant | GitHub Copilot Chat, if available with the installed Copilot extension | Check the Extensions panel |

> Record the exact locally installed version numbers after setup. The values above are verification instructions, not claims that installation has already been completed.

## Setup procedure

1. Install Visual Studio Code from the official Visual Studio Code website, or open an existing installation.
2. Open **Extensions** (`Ctrl+Shift+X` on Windows/Linux; `Cmd+Shift+X` on macOS).
3. Search for **GitHub Copilot**, verify that the publisher is GitHub, and install or enable the extension. If prompted, install the related Copilot Chat extension or enable its chat features.
4. Sign in to GitHub through the authorization flow in VS Code. Use an eligible account or the free offering if available.
5. Open a project folder in VS Code and create a small test file, such as `test.py`.
6. Type a simple function signature or comment and check whether inline AI suggestions appear. Accept a suggestion with `Tab` if offered.
7. Open Copilot Chat and ask it to explain the test function. Review the response rather than accepting it blindly.
8. Open the integrated terminal and check `code --version` and `git --version`. Check the Copilot extension version in the Extensions view.

## Verification checklist

- [ ] VS Code opens and can edit project files.
- [ ] Git is available in the integrated terminal.
- [ ] GitHub Copilot (or a comparable AI coding assistant) is enabled.
- [ ] GitHub sign-in / provider authorization succeeds.
- [ ] Inline suggestions appear in a test file.
- [ ] AI chat can explain a small snippet of code.
- [ ] Actual IDE, extension, and tool versions are recorded in the table.

## Notes and limitations

AI-generated suggestions are not automatically correct or secure. All generated code should be reviewed and tested before use. Keep access tokens and API keys out of repository files. The steps above document the planned setup and test process; check off each item only after verifying it locally.
