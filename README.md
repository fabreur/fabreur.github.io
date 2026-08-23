# Fabio Reis - GitHub Pages blog

This repository is a clear, light-mode technical blog based on Jekyll and the Chirpy theme.

## What is included

- `theme_mode: light` to keep the site readable and professional.
- Chirpy navigation, categories, tags, search, syntax highlighting, table of contents, RSS, and responsive layout.
- A custom home-page introduction for Fabio Reis.
- Medium integration: the scheduled GitHub Action reads `https://medium.com/feed/@fabreur` every day and refreshes `_data/medium.json`.
- A dedicated Pages deployment workflow.

## Publish it

1. Create a GitHub repository named `fabreur.github.io`.
2. Upload this project's contents to that repository and push the `main` branch.
3. In **Settings → Pages**, select **GitHub Actions** as the source.
4. Open **Actions → Sync Medium articles** and run it once. The home page will then show your recent Medium posts.

## Before publishing

- Confirm `github.username` in `_config.yml` is your real GitHub username.
- Add an optional `avatar` entry to `_config.yml` when you have a profile picture ready.
- Add local articles under `_posts/` whenever you want the site to become your primary publishing location.
