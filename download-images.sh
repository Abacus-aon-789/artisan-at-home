#!/bin/bash
# ============================================================
# Download all images + the menu PDF from the live WordPress
# site into this project. RUN THIS ON YOUR OWN COMPUTER while
# the WordPress site is still online (before you switch DNS!).
#
# Usage:  cd into this folder, then run:  bash download-images.sh
# ============================================================
set -e
mkdir -p images menus

dl () {
  echo "Downloading $2 ..."
  curl -fsSL "$1" -o "$2"
}

# Header logo (transparent) + footer/favicon logomark
dl "https://artisanathome.nz/wp-content/uploads/2026/02/Gemini_Generated_Image_qw1g16qw1g16qw1g-removebg-preview.png" "images/logo-mark.png"
dl "https://artisanathome.nz/wp-content/uploads/2026/02/06-Artisan-at-home_logomark-green-scaled-e1771228979740.png" "images/logo-green.png"
dl "https://artisanathome.nz/wp-content/uploads/2026/02/06-Artisan-at-home_logomark-green-2048x2048.png" "images/favicon.png"

# Social share image
dl "https://artisanathome.nz/wp-content/uploads/2026/01/website-landing-page-image.png" "images/og-image.png"

# Home
dl "https://artisanathome.nz/wp-content/uploads/2026/03/cd4cf5a5-c88e-455e-9d76-6b829be92255.jpg" "images/hero-home.jpg"

# Private chef
dl "https://artisanathome.nz/wp-content/uploads/2026/03/Gemini_Generated_Image_qr1fk4qr1fk4qr1f-e1773809404777.png" "images/private-chef-table.png"
dl "https://artisanathome.nz/wp-content/uploads/2026/03/c7e53270-ea6e-4165-9a1a-e87805805d7d.png" "images/jake-plating.png"

# Event catering
dl "https://artisanathome.nz/wp-content/uploads/2026/04/IMG_0244.jpg" "images/event-catering.jpg"
dl "https://artisanathome.nz/wp-content/uploads/2026/02/IMG_0925.webp" "images/wedding-catering.webp"

# Corporate catering
dl "https://artisanathome.nz/wp-content/uploads/2026/03/corporate-catering-boardroom-Edited.png" "images/corporate-boardroom.png"

# Our story
dl "https://artisanathome.nz/wp-content/uploads/2026/02/IMG_0775.jpg" "images/abi-jake.jpg"
dl "https://artisanathome.nz/wp-content/uploads/2026/03/Untitled-design1-scaled.jpg" "images/jake-portrait.jpg"
dl "https://artisanathome.nz/wp-content/uploads/2026/02/IMG_0910.webp" "images/abi-portrait.webp"
dl "https://artisanathome.nz/wp-content/uploads/2026/03/6c0e95ec-1bbc-472f-9905-d8b77cf0bb1b-scaled.jpg" "images/kitchen-together.jpg"

# Corporate catering menu PDF
dl "https://artisanathome.nz/wp-content/uploads/2026/04/2026-Delivered-Catering-Menu-Artisan-at-Home.pdf" "menus/2026-delivered-catering-menu.pdf"

echo ""
echo "All done! 14 images + 1 PDF downloaded."
echo "Tip: images like favicon.png are 2048px — consider compressing with https://squoosh.app before deploying."
