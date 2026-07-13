---
name: project-building-and-deployment
user-invocable: true
description: "Use when you need a structured workflow for preparing, building, packaging, and deploying a Python project in this repository."
---

# Project Building and Deployment Skill

This skill helps with the end-to-end process for building, packaging, and deploying Python projects in this workspace.

## When to use

- Preparing a Python project for release
- Checking build and dependency configuration
- Packaging a project for distribution
- Writing deployment instructions or deployment automation
- Verifying environment setup and deployment readiness

## Workflow

1. Review project structure and runtime requirements.
2. Confirm the required Python version and dependencies.
3. Validate virtual environment setup and dependency installation.
4. Verify packaging configuration and build scripts.
5. Check deployment targets and deployment commands.
6. Summarize the steps for building and deploying the project.

## Outputs

- A concise build checklist for the selected project
- Required commands for environment setup, dependency install, and build
- Packaging and distribution guidance (wheel, sdist, Docker, etc.)
- Deployment instructions for the target environment
- Recommended project-specific files to add or improve (e.g. README, requirements, Dockerfile)

## Quality checks

- Ensure the instructions match the repository layout and project dependencies
- Confirm all external service requirements are documented (Ollama, OpenAI, API keys)
- Prefer reproducible commands for Windows PowerShell and Python venv
- Keep build and deployment guidance specific to the selected project

## Example prompts

- "/project-building-and-deployment prepare the expense-agent for release"
- "/project-building-and-deployment create deployment instructions for RAG_Implementaion"
- "/project-building-and-deployment review packaging and Docker options for this project"
