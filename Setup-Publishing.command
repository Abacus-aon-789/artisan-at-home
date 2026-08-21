#!/bin/bash
# ====================================================================
# ONE-TIME SETUP — double-click this ONCE to connect your website
# folder to GitHub. After this, use "Publish.command" for everyday
# publishing (one double-click).
# ====================================================================

cd "$(dirname "$0")" || exit 1

# Make the publish buttons double-clickable for next time
chmod +x Publish.command Setup-Publishing.command 2>/dev/null

echo "==============================================="
echo "  One-time publishing setup — Artisan at Home"
echo "==============================================="
echo ""

# Clear any half-finished attempt and start clean
rm -rf .git

git init -q
git config user.email "hello@artisanathome.nz"
git config user.name "Artisan at Home"
git config credential.helper osxkeychain

echo "Saving a snapshot of your website..."
git add -A
git commit -q -m "Website update $(date '+%Y-%m-%d %H:%M')"
git branch -M main
git remote add origin https://github.com/Abacus-aon-789/artisan-at-home.git

echo ""
echo "Now sending it to GitHub for the first time."
echo "------------------------------------------------------------"
echo "If it asks, type your GitHub USERNAME and press Enter,"
echo "then PASTE your Personal Access Token as the password and"
echo "press Enter. (The token stays invisible as you paste — that's"
echo "normal, it is working.)"
echo "------------------------------------------------------------"
echo ""
git push -u origin main --force

echo ""
echo "==============================================="
echo "  Setup complete!"
echo "  From now on, just double-click Publish.command"
echo "  whenever you want your changes to go live."
echo "==============================================="
echo "  You can close this window."
