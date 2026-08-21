const SALAD_SIZES = [
  { label: "Small (serves 6–8)", price: 50 },
  { label: "Medium (serves 15–20)", price: 92 },
  { label: "Large (serves 25–35)", price: 175 }
];
const CAKE_SIZES = [
  { label: "Mini (serves 2–4)", price: 50 },
  { label: "Midi (serves 8–12)", price: 105 },
  { label: "Slab (serves 15–20)", price: 130 }
];
const INDIVIDUAL_SALADS = [
  { label: "Mediterranean Potato Salad", price: 14.5 },
  { label: "Cauliflower Power", price: 14.5 },
  { label: "The Big Green Bowl", price: 14.5 },
  { label: "Bring the Beet Back", price: 14.5 },
  { label: "Classic Caesar", price: 14.5 },
  { label: "The Kimchi Kick", price: 14.5 }
];

const MENU = [
  {
    cat: "Morning & Afternoon Tea",
    note: "Min order 8 of each type.",
    groups: [
      { options: [
        { name: "Parmesan Scones & Thyme Butter", img: "/images/cat-morning-tea.jpg", price: 7, min: 8, tags: "v" },
        { name: "Date Scones & Zesty Orange Butter", img: "/images/cat-morning-tea.jpg", price: 7, min: 8, tags: "v" },
        { name: "Orange & Almond Muffins", price: 5.5, min: 8, tags: "v · gf" },
        { name: "Tomato & Feta Frittata", price: 5.5, min: 8, tags: "v · gf" },
        { name: "Bacon & Cheddar Frittata", price: 5.5, min: 8, tags: "gf" },
        { name: "Pork & Fennel Sausage Roll", desc: "Apple jam", price: 5.5, min: 8 },
        { name: "Greek Lamb & Feta Sausage Roll", desc: "Minted yoghurt", price: 5.5, min: 8 },
        { name: "Curry Lentil & Cashew Sausage Roll", desc: "Mango & chilli chutney", price: 5.5, min: 8, tags: "v" },
        { name: "Reuben Pastie", desc: "Pastrami, sauerkraut & Swiss cheese, Thousand Island dressing", price: 5.5, min: 8 },
        { name: "Mexi Chicken Pastie", desc: "Fajita chicken, cheese, jalapeño & chipotle sour cream", price: 5.5, min: 8 },
        { name: "Cheesy Leek & Potato Pastie", desc: "Onion marmalade", price: 5.5, min: 8, tags: "v" }
      ]}
    ]
  },
  {
    cat: "Fresh & Fruity",
    groups: [
      { options: [
        { name: "Coconut Chia Pots", img: "/images/cat-fresh-fruity.jpg", desc: "Seasonal fruits, nuts, seeds & cacao nibs", tags: "vg · gf", min: 8,
          variants: [ { label: "Snack (8oz)", price: 8.75 }, { label: "Regular (12oz)", price: 14 } ] },
        { name: "Yoghurt Pots", img: "/images/cat-fresh-fruity.jpg", desc: "Blueberry compote & house-made granola", tags: "v", min: 8,
          variants: [ { label: "Snack (8oz)", price: 8.75 }, { label: "Regular (12oz)", price: 14 } ] },
        { name: "Fruit Platter", img: "/images/gallery-3.jpg", variants: [ { label: "Small (serves 6–8)", price: 65 }, { label: "Large (serves 16–20)", price: 125 } ] },
        { name: "Fruit Skewers", img: "/images/gallery-5.jpg", desc: "Min order 20", price: 5.5, min: 20 }
      ]}
    ]
  },
  {
    cat: "Whole Quiche & Frittatas",
    note: "Serves 12 · arrive pre-sliced unless otherwise requested.",
    groups: [
      { options: [
        { name: "Quiche Lorraine", price: 127 },
        { name: "Smoked Salmon & Leek Quiche", desc: "House-smoked salmon", price: 127 },
        { name: "Broccoli & Blue Cheese Quiche", price: 127, tags: "v" },
        { name: "Tomato & Feta Frittata", desc: "With our house-made tomato jam", price: 127, tags: "v · gf" },
        { name: "Mushroom & Brie Frittata", price: 127, tags: "v · gf" },
        { name: "Bacon & Cheddar Frittata", price: 127, tags: "gf" }
      ]}
    ]
  },
  {
    cat: "Winter Salads",
    note: "Our portion sizes are designed to be enjoyed as a side.",
    groups: [
      { options: [
        { name: "Mediterranean Potato Salad", desc: "Olive & caper, lemon & herby olive oil dressing", tags: "vg · gf", variants: SALAD_SIZES },
        { name: "Cauliflower Power", desc: "Curry leaf & cumin roasted cauliflower & chickpea, toasted almonds, ginger coconut dressing", tags: "vg · gf", variants: SALAD_SIZES },
        { name: "The Big Green Bowl", desc: "Citrusy zucchini, broccoli rice (stems and all), our house sauerkraut, rocket & toasted pumpkin seeds", tags: "vg · gf", variants: SALAD_SIZES },
        { name: "Bring the Beet Back", desc: "Roasted beetroot & carrot, pomegranate, feta, toasted walnuts & balsamic dressing", tags: "v · gf", variants: SALAD_SIZES },
        { name: "Classic Caesar", desc: "Baby cos, pancetta, parmesan, anchovies, rosemary croutons", variants: SALAD_SIZES },
        { name: "The Kimchi Kick", desc: "Kimchi & sesame cucumber brown rice, charred broccoli, edamame & fermented chilli dressing", tags: "vg · gf", variants: SALAD_SIZES },
        { name: "Individual Salad", desc: "Minimum order of 8 of each type", min: 8, variants: INDIVIDUAL_SALADS }
      ]}
    ]
  },
  {
    cat: "Gourmet Sandwiches",
    note: "Flavour packed Turkish Pide bread sandwiches, arrive sliced in half unless otherwise requested. Min order of 6 of each variety.",
    groups: [
      { options: [
        { name: "Pastrami & Sauerkraut", img: "/images/cat-sandwiches.jpg", desc: "Our house-made sauerkraut, horseradish mayo & shredded iceberg", price: 16.5, min: 6, special: true, badge: "Seasonal Special" },
        { name: "Smoked Salmon & Lemon Caper Cream Cheese", desc: "Salmon we smoke ourselves, our pickled cucumber & red onion", price: 16.5, min: 6 },
        { name: "Chicken & Maple Glazed Pancetta", desc: "Basil pesto & rocket", price: 16.5, min: 6 },
        { name: "Honey Glazed Ham & Dill Pickle", desc: "Mustard, lettuce & fresh apple", price: 16.5, min: 6 },
        { name: "Whipped Feta, Rocket & Fig Chutney", desc: "Pickled red onions, walnuts & thyme", price: 16.5, min: 6, tags: "v" },
        { name: "Kim-cheese & Sesame Egg Mayo", desc: "Chives & gem lettuce", price: 16.5, min: 6, tags: "v" },
        { name: "Garlic & Herb Mushroom & Mozzarella", desc: "Lemon zucchini ribbon & olive oil", price: 16.5, min: 6, tags: "v" },
        { name: "Harissa Grilled Eggplant & Cashew Ricotta", desc: "Caramelised onion jam & dukkah", price: 16.5, min: 6, tags: "vg" }
      ]}
    ]
  },
  {
    cat: "Sweet Bites",
    note: "Minimum 8 of each type, or grab a mixed selection.",
    groups: [
      { options: [
        { name: "Burnt Butter & Banana Blondie", img: "/images/cat-sweet-bites.jpg", price: 5, min: 8, tags: "v" },
        { name: "Dark Chocolate & Sea Salt Brownie", price: 5, min: 8, tags: "vg" },
        { name: "Apricot & Chocolate Crumble Slice", price: 5, min: 8, tags: "v" },
        { name: "Millionaire's White Chocolate & Raspberry", price: 5, min: 8, tags: "v" },
        { name: "Lemon & Coconut Baklava", price: 5, min: 8, tags: "vg" },
        { name: "Sweet Bites Selection — 50 bites", desc: "A mixed selection of our sweet bites (50 pieces)", price: 190 }
      ]}
    ]
  },
  {
    cat: "Whole Cakes",
    note: "Choose your flavour and size.",
    groups: [
      { options: [
        { name: "Hummingbird & Salted Caramel", img: "/images/cat-cakes.jpg", tags: "v", variants: CAKE_SIZES },
        { name: "Orange & Almond", tags: "v · gf", variants: CAKE_SIZES },
        { name: "Raspberry & Vanilla Burnt Butter", tags: "v", variants: CAKE_SIZES },
        { name: "Lemon Meringue", tags: "v", variants: CAKE_SIZES },
        { name: "Tropical Mango & Lime", tags: "v", variants: CAKE_SIZES },
        { name: "Chocolate & Hazelnut", tags: "v", variants: CAKE_SIZES }
      ]}
    ]
  },
  {
    cat: "Extras",
    note: "Add the finishing touches to your order.",
    groups: [
      { options: [
        { name: "Knife, Fork, Plate & Napkin Set", desc: "The full set", price: 2 },
        { name: "Forks", price: 0.3 },
        { name: "Knives", price: 0.3 },
        { name: "Spoons", price: 0.3 },
        { name: "Side Plates", price: 0.3 },
        { name: "Plates", price: 0.5 },
        { name: "Napkins", price: 0.3 }
      ]}
    ]
  }
];

if (typeof module !== "undefined" && module.exports) {
  module.exports = { MENU: MENU, SALAD_SIZES: SALAD_SIZES, CAKE_SIZES: CAKE_SIZES, INDIVIDUAL_SALADS: INDIVIDUAL_SALADS };
}
