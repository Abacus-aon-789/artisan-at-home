#!/bin/bash
# Double-click this file to publish your website.
# It saves your latest changes and sends them to GitHub,
# and Vercel then puts them live automatically (~1 minute).

cd "$(dirname "$0")" || exit 1

echo "============================================="
echo "  Publishing Artisan at Home website..."
echo "============================================="
echo ""

git add -A
git commit -m "Update website $(date '+%Y-%m-%d %H:%M')" || echo "(No new changes to save.)"
echo ""
echo "Sending to GitHub..."
git push

echo ""
echo "============================================="
echo "  All done! Your live site updates in ~1 min."
echo "  Check: https://artisan-at-home.vercel.app"
echo "  You can close this window."
echo "============================================="
