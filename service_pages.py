# -*- coding: utf-8 -*-
"""Service pages with full menus — transcribed from the live site."""

def dishes(items):
    """items: list of (name, desc, tags)"""
    out = '<ul class="dish-list">'
    for name, desc, *rest in items:
        tags = f'<span class="dish-tags">{rest[0]}</span>' if rest else ""
        d = f'<div class="dish-desc">{desc}</div>' if desc else ""
        out += f'<li><span class="dish">{name}{tags}</span>{d}</li>'
    return out + "</ul>"

def courses(items):
    """items: list of (course_label, name, desc)"""
    out = '<ul class="dish-list">'
    for label, name, desc in items:
        d = f'<div class="dish-desc">{desc}</div>' if desc else ""
        out += f'<li><span class="course-label">{label}</span><span class="dish">{name}</span>{d}</li>'
    return out + "</ul>"

TAILORED = '<p class="menu-note">Example menu &mdash; courses, ingredients and portion sizes are tailored to your evening. Minimum 6 guests.</p>'

PRIVATE_CHEF = """
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">&middot; Private Chef Experience &middot;</span>
      <h1>Staying in is the new going out.</h1>
      <p class="lead">Experience the luxury of restaurant-standard dining in the intimacy of your own home. From bespoke menu design to the final polished glass &mdash; we help you stay a part of the conversation, not the preparation or clean up!</p>
      <div class="btn-row">
        <a class="btn btn--solid" href="/contact-us/">Enquire Now</a>
        <a class="btn" href="#how-it-works">How it works</a>
      </div>
    </div>
    <img src="/images/private-chef-table.png" alt="Elegantly set dining table for a private chef experience">
  </div>
</section>

<section class="section">
  <div class="wrap card-grid card-grid--2">
    <div class="card">
      <span class="eyebrow">Refined Precision</span>
      <h3><em>Degustation</em></h3>
      <p>From intimate three-course affairs to an expansive eight-course journey. These dinners are set to WOW &mdash; a great excuse to celebrate a big milestone, impress some guests or treat yo' self! Take the hands-off approach and trust Jake to create something beautiful, or if you've got some ideas of what you'd like to be indulging in, we would love to hear them &mdash; it's up to you.</p>
      <p class="fine">Minimum 6 Guests &middot; 3 &mdash; 8 Courses</p>
      <div class="btn-row" style="margin-top:0.5rem;">
        <a class="btn btn--solid" href="/contact-us/">Enquire Now</a>
        <a class="btn" href="#private-menus">Example Menus</a>
      </div>
    </div>
    <div class="card">
      <span class="eyebrow">Communal Luxury</span>
      <h3>The <em>Banquet</em></h3>
      <p>We are big believers in the ethos that great food is meant to be savoured and shared with your favourite people &mdash; this dining style does exactly that. Imagine vibrant, abundant platters shared around the table &mdash; we find this dining style naturally invokes conversation and connection.</p>
      <p class="fine">6 &mdash; 20 Guests &middot; Shared Banquet</p>
      <div class="btn-row" style="margin-top:0.5rem;">
        <a class="btn btn--solid" href="/contact-us/">Enquire Now</a>
        <a class="btn" href="#private-menus">Example Menus</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--cream" id="private-menus">
  <div class="wrap">
    <div class="section-head section-head--center">
      <span class="eyebrow">Sample Menus</span>
      <h2>A Taste of What's Possible</h2>
      <p>Designed as a starting point and to spark inspiration &mdash; every menu we create is tailored to your occasion, your guests, and the season.</p>
    </div>

    <h3 style="margin-bottom:0.3rem;">The Degustation</h3>
    <p style="margin-bottom:1.4rem;">A curated tasting journey, course by course.</p>
    <div>
      <div class="tabs" role="tablist" aria-label="Degustation menus">
        <button class="tab" role="tab" aria-selected="true" data-panel="menu-east">The East</button>
        <button class="tab" role="tab" aria-selected="false" data-panel="menu-garden">The Garden</button>
        <button class="tab" role="tab" aria-selected="false" data-panel="menu-coastal">Coastal</button>
        <button class="tab" role="tab" aria-selected="false" data-panel="menu-harvest">The Harvest</button>
      </div>
      <div class="panel" id="menu-east">""" + courses([
        ("First", "Mushroom Parfait", "Shiitake, Pickled Shallot, Danish Rye"),
        ("Second", "Citrus Kosho Tiger Prawns", "Bisque, Misozuke Kohlrabi, Wasabi Emulsion, Shiso"),
        ("Third", "Slow Braised Thai Beef Short Rib", "Green Curry Sauce, Sticky Rice Rouleau, Salsa, Bok Choy"),
        ("Fourth", "Coconut Panna Cotta", "Raspberry, Lime, Lavender Salt"),
      ]) + TAILORED + """</div>
      <div class="panel" id="menu-garden" hidden>""" + courses([
        ("First", "Heirloom Tomato Tart", "Whipped Ricotta, Basil Oil, Aged Balsamic, Flaked Sea Salt"),
        ("Second", "Roasted Cauliflower Velout&eacute;", "Curry Leaf Butter, Crispy Capers, Toasted Almond"),
        ("Third", "Burrata &amp; Stone Fruit", "White Peach, Pickled Shallot, Pistachio Crumb, Fresh Tarragon"),
        ("Fourth", "Slow-Roasted Root Vegetables", "Saffron &amp; Honey Glaze, Whipped Goats Curd, Pomegranate, Dukkah"),
        ("Fifth", "Olive Oil Cake", "Candied Citrus, Cr&egrave;me Fra&icirc;che, Rosemary Sugar"),
      ]) + TAILORED + """</div>
      <div class="panel" id="menu-coastal" hidden>""" + courses([
        ("First", "Chilled Oysters", "Cucumber Granita, Finger Lime, Shallot Vinegar"),
        ("Second", "Smoked Salmon Rillette", "Dill Cr&egrave;me Fra&icirc;che, Pickled Fennel, Rye Crisp"),
        ("Third", "Seared Scallops", "Cauliflower Pur&eacute;e, Brown Butter, Crispy Pancetta, Micro Herbs"),
        ("Fourth", "Pan-Roasted Hapuka", "Saffron &amp; Mussel Broth, Fennel Confit, Sourdough Cro&ucirc;te"),
        ("Fifth", "Lemon Posset", "Sea Salt Shortbread, Candied Zest, Fresh Raspberry"),
        ("Sixth", "Vanilla &amp; White Chocolate Tart", "Salted Caramel, Toasted Coconut, Lime Curd"),
      ]) + TAILORED + """</div>
      <div class="panel" id="menu-harvest" hidden>""" + courses([
        ("First", "Wild Mushroom &amp; Chestnut Velout&eacute;", "Truffle Oil, Crispy Sage, Toasted Hazelnut"),
        ("Second", "Whipped Goats Curd &amp; Roasted Fig", "Walnut Praline, Aged Honey, Endive, Sourdough Crisp"),
        ("Third", "Seared Duck Breast", "Cassis Jus, Caramelised Quince, Pickled Blackberry, Watercress"),
        ("Fourth", "Slow-Braised Venison Shoulder", "Celeriac Pur&eacute;e, Roasted Root Vegetables, Red Wine &amp; Juniper Jus"),
        ("Fifth", "Poached Pear &amp; Gorgonzola", "Candied Walnuts, Bitter Leaves, Pomegranate Dressing"),
        ("Sixth", "Salted Caramel Tarte Tatin", "Vanilla Cr&egrave;me Fra&icirc;che, Toasted Pepitas, Autumn Spice"),
      ]) + TAILORED + """</div>
    </div>

    <h3 style="margin:3.4rem 0 0.3rem;">The Banquet</h3>
    <p style="margin-bottom:1.4rem;">Generous platters made for passing and sharing.</p>
    <div>
      <div class="tabs" role="tablist" aria-label="Banquet menus">
        <button class="tab" role="tab" aria-selected="true" data-panel="bq-starters">Starters</button>
        <button class="tab" role="tab" aria-selected="false" data-panel="bq-mains">The Main Event</button>
        <button class="tab" role="tab" aria-selected="false" data-panel="bq-sides">Salads &amp; Sides</button>
        <button class="tab" role="tab" aria-selected="false" data-panel="bq-finish">To Finish</button>
      </div>
      <div class="panel" id="bq-starters"><span class="eyebrow">To Begin</span>""" + dishes([
        ("Pacific Oyster", "Peach, Habanero Chilli Oil, Finger Lime"),
        ("Chicken Liver &amp; Truffle P&acirc;t&eacute; Cigar", "Chives"),
        ("King George Whiting in Hibiscus Batter", "Spring Onion Aioli"),
        ("Sourdough &amp; Cultured Butter", "Lovage"),
      ]) + TAILORED + """</div>
      <div class="panel" id="bq-mains" hidden><span class="eyebrow">Centre of the Table</span>""" + dishes([
        ("12-Hour Lamb Shoulder", "Yuzu Pumpkin Pur&eacute;e, Preserved Lemon, Saltbush, Crumbled Pepitas"),
        ("Whole Roasted Snapper", "Charred Lemon, Salsa Verde, Crispy Capers"),
        ("Slow-Braised Beef Short Rib", "Red Wine Jus, Horseradish Cr&egrave;me Fra&icirc;che, Watercress"),
        ("Potato Galette", "Black Garlic Sauce"),
      ]) + TAILORED + """</div>
      <div class="panel" id="bq-sides" hidden><span class="eyebrow">To Accompany</span>""" + dishes([
        ("Heirloom Tomato &amp; Burrata", "Toasted Pine Nuts, Fresh Basil, Aged Balsamic"),
        ("Charred Broccolini", "Almonds, Preserved Lemon, Chilli, Tahini Dressing"),
        ("Roasted Beetroot &amp; Carrot", "Pomegranate, Feta, Toasted Walnuts, Honey &amp; Thyme Dressing"),
        ("Crushed Herb Potatoes", "Confit Garlic, Lemon Zest, Flat Leaf Parsley"),
        ("Classic Caesar", "Baby Cos, Pancetta, Parmesan, Anchovies, Rosemary Croutons"),
      ]) + TAILORED + """</div>
      <div class="panel" id="bq-finish" hidden><span class="eyebrow">Dessert</span>""" + dishes([
        ("Roasted Stone Fruit", "Whipped Mascarpone, Thyme &amp; Lemon Oil, Crumbed Hazelnut"),
        ("Praline Cr&egrave;me Br&ucirc;l&eacute;e", "Caramelised Sugar Crust, served warm"),
        ("The Purple Fig", "Lady Figs, Honey, Crushed Meringue"),
        ("Dark Chocolate Cremeux", "Cherry Compote, Clotted Cream, Almond Crumble"),
      ]) + TAILORED + """</div>
    </div>
  </div>
</section>

<section class="section" id="how-it-works">
  <div class="wrap split">
    <img src="/images/jake-plating.png" alt="Jake plating a dish">
    <div>
      <span class="eyebrow">How It Works</span>
      <h2>From first enquiry to <em>the final dish.</em></h2>
      <div class="steps" style="grid-template-columns:1fr;gap:1.6rem;margin-top:1.6rem;">
        <div class="step">
          <span class="num">01</span>
          <h3>Enquire</h3>
          <p>Share your date, guest count, and any dietary preferences through our simple enquiry form. We'll come back to you promptly.</p>
        </div>
        <div class="step">
          <span class="num">02</span>
          <h3>Consult</h3>
          <p>We talk about what you want, any favourite dishes or inspiration, and curate a bespoke seasonal menu tailored to your occasion and guests. Once you are happy with the menu, we request a 30% deposit to secure the date.</p>
        </div>
        <div class="step">
          <span class="num">03</span>
          <h3>Enjoy</h3>
          <p>We arrive with fresh ingredients, cook, serve, and leave your kitchen spotless. You simply show up to your own table and enjoy time with your guests.</p>
        </div>
      </div>
      <div class="btn-row">
        <a class="btn btn--solid" href="/contact-us/">Begin Your Experience</a>
      </div>
    </div>
  </div>
</section>
"""

EVENT_CATERING = """
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">&middot; Event Catering &middot;</span>
      <h1>Grand moments, intimate details.</h1>
      <p class="lead">From bespoke weddings to milestone celebrations, we will bring some seasonal soul to your special events. Browse our menus to get a feel for our style, and if you have a vision in mind, however formed or unformed &mdash; get in touch and we can make it happen together.</p>
      <div class="btn-row">
        <a class="btn btn--solid" href="/contact-us/">Enquire Now</a>
      </div>
    </div>
    <img src="/images/event-catering.jpg" alt="Artisan at Home event catering">
  </div>
</section>

<section class="section">
  <div class="wrap card-grid card-grid--4">
    <div class="card">
      <span class="eyebrow">Mixing &amp; Mingling</span>
      <h3><em>Canap&eacute;s</em></h3>
      <p>Roaming bites or a beautifully presented table spread &mdash; delicious little morsels perfect for mingling.</p>
      <a class="text-link" href="#event-menu">Explore Seasonal Menu &darr;</a>
    </div>
    <div class="card">
      <span class="eyebrow">Artisan Abundance</span>
      <h3>Grazing <em>&amp; Boards</em></h3>
      <p>A visual feast of handcrafted dips, NZ cheeses, cured meats and seasonal fruits &mdash; beautiful and abundant.</p>
      <a class="text-link" href="#event-menu">Explore Seasonal Menu &darr;</a>
    </div>
    <div class="card">
      <span class="eyebrow">Communal Luxury</span>
      <h3>The <em>Shared Table</em></h3>
      <p>Vibrant, laden platters passed around a table that encourages connection and makes the evening memorable.</p>
      <a class="text-link" href="#event-menu">Explore Seasonal Menu &darr;</a>
    </div>
    <div class="card">
      <span class="eyebrow">You host, we feed</span>
      <h3>Delivered <em>Catering</em></h3>
      <p>Baby shower, engagement party, or a simple Sunday with friends. We take care of the food so you can focus on the people.</p>
      <a class="text-link" href="/services/corporate-catering/">View Catering Menu &rarr;</a>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="wrap split">
    <img src="/images/wedding-catering.webp" alt="Wedding catering by Artisan at Home">
    <div>
      <span class="eyebrow">Planning a Wedding?</span>
      <h2>Your day, <em>your way.</em></h2>
      <p><strong>No fixed packages. No off-the-shelf menus. Just food and the memories it makes.</strong></p>
      <p>Our event catering gives you a real feel for the quality and style we love to bring &mdash; but when it comes to weddings, everything is completely bespoke. The menu, the format, the flow of the day is all designed around you.</p>
      <p>We work with all budgets and all visions. Some couples come to us with a clear picture of exactly what they want, whereas others aren't sure where to start &mdash; and hearing about your ideas, your day, the moments you want to create, is one of our favourite parts of what we do.</p>
      <p>This is your day, and our job is simply to make it delicious. We'll give you as much or as little guidance as you need along the way.</p>
      <p>The best first step is just a conversation &mdash; no obligation, no pressure. Choosing who caters your wedding is a big decision, and we want you to feel completely confident that we're the right fit before you commit to anything.</p>
      <div class="btn-row"><a class="btn btn--solid" href="/contact-us/">Start the Conversation</a></div>
    </div>
  </div>
</section>

<section class="section" id="event-menu">
  <div class="wrap">
    <div class="section-head section-head--center">
      <span class="eyebrow">Our Offering</span>
      <h2>Event Menus</h2>
      <p>Explore our menus below &mdash; select a category to see what we're cooking. Due to the nature of working with the seasons, there may be times when we will make substitutions to ensure the best quality ingredients are being used.</p>
    </div>
    <div>
      <div class="tabs" role="tablist" aria-label="Event menus">
        <button class="tab" role="tab" aria-selected="true" data-panel="ev-cold">Cold Canap&eacute;s</button>
        <button class="tab" role="tab" aria-selected="false" data-panel="ev-warm">Warm Canap&eacute;s</button>
        <button class="tab" role="tab" aria-selected="false" data-panel="ev-graze">Grazing &amp; Boards</button>
        <button class="tab" role="tab" aria-selected="false" data-panel="ev-shared">Shared Table</button>
      </div>

      <div class="panel" id="ev-cold">
        <div class="menu-cols">
          <div class="menu-col">
            <h3>Signature Selection</h3>
            <p class="menu-price">$7.50 each</p>""" + dishes([
            ("Mushroom Parfait", "Cabernet Sauvignon Pickled Shallot &amp; Toasted Danish Rye"),
            ("Whipped Chicken Liver Parfait", "Pedro Xim&eacute;nez Infused Sultanas, Toasted Brioche"),
            ("Charred Baby Capsicums", "Chorizo, Cream Cheese, Almond &amp; Honey"),
            ("Tuna Ceviche Tostada", "Avocado &amp; Wasabi Emulsion, Micro Coriander"),
            ("Smoked Salmon Rillette", "Pickled Cucumber, Rye Crostini, Fresh Dill &amp; Caviar"),
            ("Olive, Guindilla &amp; Boquerones Gilda", ""),
            ]) + """
          </div>
          <div class="menu-col">
            <h3>Classic Selection</h3>
            <p class="menu-price">$5.50 each</p>""" + dishes([
            ("Roast Beef &amp; Horseradish", "Toasted Baguette"),
            ("Smoked Salmon on Cucumber Rounds", "Dill &amp; Lemon Zest"),
            ("Tomato &amp; Basil Bruschetta", "Garlic Crostini"),
            ("Vietnamese Spring Rolls", "Chicken &amp;/or Vegetarian, Nuoc Cham Dipping Sauce"),
            ("Whipped Feta &amp; Fig Chutney", "Olive Oil Croutons"),
            ("Caprese Skewers", "Bocconcini, Cherry Tomato &amp; Basil"),
            ]) + """
          </div>
        </div>
        <p class="menu-note">Minimum order 20 pieces per variety. Mix and match across selections. We recommend 4&ndash;6 pieces per person for a drinks reception.</p>
      </div>

      <div class="panel" id="ev-warm" hidden>
        <div class="menu-cols">
          <div class="menu-col">
            <h3>Signature Selection</h3>
            <p class="menu-price">$7.50 each</p>""" + dishes([
            ("Moroccan Lamb &amp; Pistachio Sliders", "Lemon &amp; Mint Yoghurt, Crumbled Feta"),
            ("Sage Pork Belly Bites", "Crackling &amp; Sour Apple Pur&eacute;e"),
            ("Mini Fish Sliders", "Lemon &amp; Dill Aioli"),
            ("Pork &amp; Fennel Scotched Egg", "Caramelised Onion Ketchup &amp; Pickled Shallots"),
            ("Garlic &amp; Ginger King Prawn Wonton Cup", "Wasabi Emulsion"),
            ]) + """
          </div>
          <div class="menu-col">
            <h3>Classic Selection</h3>
            <p class="menu-price">$5.50 each</p>""" + dishes([
            ("Chicken Satay Skewers", "Spring Onion &amp; Coriander"),
            ("Pork &amp; Fennel Sausage Rolls", "Red Onion Jam"),
            ("Lamb Koftas", "Mint Yoghurt Dip"),
            ("Potato &amp; Spinach Samosas", "Toasted Coconut Raita"),
            ("Chipotle Beef Croquettes", "Coriander &amp; Lime Sour Cream"),
            ]) + """
          </div>
        </div>
        <p class="menu-note">Minimum order 20 pieces per variety. Mix and match across selections. We recommend 4&ndash;6 pieces per person for a drinks reception.</p>
      </div>

      <div class="panel" id="ev-graze" hidden>
        <div class="menu-cols">
          <div class="menu-col">
            <h3>Cheese &amp; Charcuterie</h3>
            <p class="menu-price">$26pp</p>
            <p>Selection of 3&ndash;4 cheeses, cured meats, house mushroom parfait &amp; chicken liver parfait, homemade crackers and dips &mdash; feta whip, onion jam, hummus.</p>
          </div>
          <div class="menu-col">
            <h3>Cheese Board</h3>
            <p class="menu-price">$23pp</p>
            <p>Selection of 3&ndash;4 cheeses, vegetable crudit&eacute;s, house mushroom parfait, homemade crackers and dips &mdash; feta whip, onion jam, hummus.</p>
          </div>
        </div>
        <p class="menu-note">Minimum 20 guests. All grazing boards are priced based on guest numbers and duration. Get in touch for a quote if you are looking for something more bespoke.</p>
      </div>

      <div class="panel" id="ev-shared" hidden>
        <div class="menu-cols">
          <div class="menu-col">
            <h3>Mains</h3>""" + dishes([
            ("Slow Cooked Lamb Shoulder", "Red Chimichurri &amp; Fresh Mint"),
            ("House Harissa Roasted Free Range Chicken", "Coriander &amp; Cucumber Salsa"),
            ("Whole Beef Eye Fillet", "Bordelaise Sauce &amp; Braised Shallots"),
            ("Roasted Pork Belly", "Grain Mustard Parsley Sauce &amp; Baked Apple"),
            ("Smoked Beef Brisket", "Shallot &amp; Cornichon Salsa"),
            ("Citrus &amp; Dijon Baked Salmon", "Pickled Cucumber"),
            ]) + """
            <h3 style="margin-top:2rem;">Desserts</h3>""" + dishes([
            ("Tiramisu", "Espresso &amp; Marsala, Dark Cocoa", "V"),
            ("Treacle Tart", "Clotted Cream, Candied Lemon Zest", "V"),
            ("Seasonal Eton Mess", "Seasonal Fruits, Whipped Cream", "V &middot; GF"),
            ("Artisan Cheese Board", "Kapiti Brie, Whitestone Aged Cheddar, Blue Cheese, Quince Paste, Honeycomb", "V &middot; GF"),
            ]) + """
          </div>
          <div class="menu-col">
            <h3>Sides &amp; Salads</h3>""" + dishes([
            ("Roasted Kabocha Pumpkin", "Pomegranate, Macadamia Dukkah", "VG &middot; GF"),
            ("Roast Potatoes, Harissa &amp; Yoghurt", "Fresh Mint, Smoked Paprika", "V &middot; GF"),
            ("Seasonal Greens, Burnt Butter &amp; Hazelnuts", "Broccolini, Cavolo Nero, Lemon Zest", "V &middot; GF"),
            ("Rainbow Carrots, Labneh &amp; Pistachio", "Fennel Seed &amp; Maple, Fresh Dill", "V &middot; GF"),
            ("Roasted Beetroot &amp; Feta Salad", "Pomegranate, Orange, Toasted Walnuts &amp; Balsamic Dressing", "V &middot; GF"),
            ("Cos Wedge Salad", "Pickled Red Onion, Radish, Tahini &amp; Sumac", "VG &middot; GF"),
            ("Curry Leaf &amp; Cumin Roasted Cauliflower Chickpea Salad", "Toasted Almonds, Ginger Coconut Dressing", "VG &middot; GF"),
            ]) + """
          </div>
        </div>
        <p class="menu-note">GF gluten free &nbsp;|&nbsp; DF dairy free &nbsp;|&nbsp; V vegetarian &nbsp;|&nbsp; VG vegan &nbsp;|&nbsp; Our menu is seasonal &mdash; substitutions may apply to ensure the best quality produce. We would love to work with you to tailor a menu for your event.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--pine cta-band">
  <div class="wrap">
    <span class="eyebrow">Start Planning</span>
    <h2>Your table is <em>waiting to be set.</em></h2>
    <p class="lead" style="margin:1rem auto 0;">Every event is different, and so is every client. Tell us about your event, ask us anything, and see how it feels. No commitment, no pressure, just a genuine chat about what's possible.</p>
    <div class="btn-row">
      <a class="btn" style="border-color:#f6f2e8;color:#f6f2e8;" href="/contact-us/">Start Planning</a>
    </div>
    <p class="fine" style="margin-top:1.6rem;">A little heads up &mdash; weekends and public holidays are our most popular dates, so early conversations are encouraged.</p>
  </div>
</section>
"""

CORPORATE_CATERING = """
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">&middot; Corporate Catering &middot;</span>
      <h1>Catering that doesn't taste like catering</h1>
      <p class="lead">From boardroom lunches to end of year celebrations, we bring high-end hospitality to the workplace. We take the classics, the crowd pleasers, the things people know and love &mdash; then bring them to life with seasonal produce and a bit of Artisan at Home creative tweaking.</p>
      <div class="btn-row">
        <a class="btn btn--solid" href="#order-form">Order Now</a>
        <a class="btn" href="#catering-menu">Catering Menu</a>
      </div>
    </div>
    <img src="/images/corporate-boardroom.png" alt="Artisan at Home corporate catering">
  </div>
</section>

<section class="section">
  <div class="wrap card-grid card-grid--4">
    <div class="card">
      <span class="eyebrow">Light Bites</span>
      <h3>Morning &amp; <em>Afternoon Tea</em></h3>
      <p>The classics are still around for a reason. Scones, slices, a lemony treat &mdash; we're not here to reinvent the wheel. But we do think the wheel deserves good butter, seasonal fruit, and a little more thought than it usually gets. Familiar food, made with a little extra something...</p>
      <a class="text-link" href="#catering-menu">Explore the Menu &darr;</a>
    </div>
    <div class="card">
      <span class="eyebrow">Plated &amp; Boxed</span>
      <h3>Catered <em>Lunches</em></h3>
      <p>Think big, bright, beautiful salads to generously filled sandwiches packed with flavour. Choose from stand-alone lunch options or day packages &mdash; built for one-off workshops or weekly WIPs.</p>
      <a class="text-link" href="#catering-menu">Explore the Menu &darr;</a>
    </div>
    <div class="card">
      <span class="eyebrow">Networking</span>
      <h3>Event <em>Catering</em></h3>
      <p>New product launch, or finally got the new CRM integrated and want to celebrate? Our event catering spans refined canap&eacute;s and roaming bites or something a little more substantial with platters and shared plates.</p>
      <a class="text-link" href="#catering-menu">Explore the Menu &darr;</a>
    </div>
    <div class="card">
      <span class="eyebrow">The All-In-One</span>
      <h3>Catering <em>Packages</em></h3>
      <p>Analysis paralysis? Tell us your numbers and we'll take care of the rest. Choose from AM/PM Tea combos to multi-day catering. Zero decision fatigue, complete satisfaction.</p>
      <a class="text-link" href="#catering-menu">Explore Packages &darr;</a>
    </div>
  </div>
</section>

<section class="section section--cream" id="catering-menu">
  <div class="wrap">
    <div class="section-head section-head--center">
      <span class="eyebrow">Corporate Catering</span>
      <h2>The Menu</h2>
      <p>Everything is made fresh to order. Select a category below to explore what we offer, or download the full menu PDF to share with your team.</p>
      <div class="btn-row" style="justify-content:center;">
        <a class="btn" href="/menus/2026-delivered-catering-menu.pdf">Download Menu PDF</a>
      </div>
    </div>
    <div>
      <div class="tabs" role="tablist" aria-label="Corporate menus">
        <button class="tab" role="tab" aria-selected="true" data-panel="cc-tea">Morning &amp; Afternoon Tea</button>
        <button class="tab" role="tab" aria-selected="false" data-panel="cc-sweet">Sweet Treats</button>
        <button class="tab" role="tab" aria-selected="false" data-panel="cc-salads">Autumn Salads</button>
        <button class="tab" role="tab" aria-selected="false" data-panel="cc-sandwiches">Gourmet Sandwiches</button>
        <button class="tab" role="tab" aria-selected="false" data-panel="cc-packages">Catering Packages</button>
      </div>

      <div class="panel" id="cc-tea">
        <div class="menu-cols">
          <div class="menu-col">
            <h3>The Minis</h3>
            <p class="menu-price">$4.00 each &middot; min order 8 of each type</p>""" + dishes([
            ("Parmesan Scones &amp; Thyme Butter", "", "v"),
            ("Cherry &amp; Almond Scones", "", "v"),
            ("Date Scones &amp; Zesty Orange Butter", "", "v"),
            ("Orange &amp; Almond Muffins", "", "v &middot; gf"),
            ("Tomato &amp; Feta Frittata", "", "v &middot; gf"),
            ("Bacon &amp; Cheddar Frittata", "", "gf"),
            ]) + """
            <h3 style="margin-top:2rem;">Fresh &amp; Fruity</h3>
            <p class="menu-price">$8.75 snack &middot; $14.00 regular</p>""" + dishes([
            ("Organic Coconut Chia Pots", "Seasonal Fruits, Nuts, Seeds &amp; Cacao Nibs", "vg &middot; gf"),
            ("Yoghurt Pots", "Blueberry Compote &amp; House Made Granola", "v"),
            ]) + """
            <h3 style="margin-top:2rem;">Fruit Platters</h3>
            <p class="menu-price">$65 small (serves 6&ndash;8) &middot; $125 large (serves 16&ndash;20)</p>
          </div>
          <div class="menu-col">
            <h3>Mini Sausage Rolls</h3>
            <p class="menu-price">$5.50 each</p>""" + dishes([
            ("Pork &amp; Fennel", "Apple Jam"),
            ("Greek Lamb &amp; Feta", "Minted Yoghurt"),
            ("Curry Lentil &amp; Cashew", "Mango &amp; Chilli Chutney", "v"),
            ]) + """
            <h3 style="margin-top:2rem;">Mini Pasties</h3>
            <p class="menu-price">$5.50 each</p>""" + dishes([
            ("Reuben Pastie", "Pastrami, Sauerkraut &amp; Swiss Cheese, Thousand Island Dressing"),
            ("Mexi Chicken Pastie", "Fajita Chicken, Cheese, Jalape&ntilde;o &amp; Chipotle Sour Cream"),
            ("Cheesy Leek &amp; Potato Pastie", "Onion Marmalade", "v"),
            ]) + """
            <h3 style="margin-top:2rem;">Whole Frittatas &amp; Quiches</h3>
            <p class="menu-price">$90 &middot; serves 10&ndash;12</p>""" + dishes([
            ("Quiche Lorraine", ""),
            ("Smoked Salmon &amp; Leek Quiche", ""),
            ("Broccoli &amp; Blue Cheese Quiche", "", "v"),
            ("Tomato &amp; Feta Frittata", "", "v &middot; gf"),
            ("Mushroom &amp; Brie Frittata", "", "v &middot; gf"),
            ("Bacon &amp; Cheddar Frittata", "", "gf"),
            ]) + """
          </div>
        </div>
      </div>

      <div class="panel" id="cc-sweet" hidden>
        <div class="menu-cols">
          <div class="menu-col">
            <h3>Bite-Sized</h3>
            <p class="menu-price">$3.00 bite-sized &middot; min order 8 of each type &middot; $6 slice</p>""" + dishes([
            ("Burnt Butter &amp; Banana Blondie", "", "v"),
            ("Dark Chocolate &amp; Sea Salt Brownie", "", "vg"),
            ("Apricot &amp; Chocolate Crumble Slice", "", "v"),
            ("Millionaire's White Chocolate &amp; Raspberry", "", "v"),
            ("Lemon &amp; Coconut Baklava", "", "vg"),
            ]) + """
          </div>
          <div class="menu-col">
            <h3>Whole Cakes</h3>
            <p class="menu-price">Mini (2&ndash;4) $50 &middot; Midi (8&ndash;12) $75 &middot; Maxi (15&ndash;20) $130</p>""" + dishes([
            ("Hummingbird &amp; Salted Caramel", "", "v"),
            ("Orange &amp; Almond", "", "v &middot; gf"),
            ("Raspberry &amp; Vanilla Burnt Butter", "", "v"),
            ("Lemon Meringue", "", "v"),
            ("Tropical Mango &amp; Lime", "", "v"),
            ("Chocolate, Sage &amp; Blackberry", "", "v"),
            ]) + """
          </div>
        </div>
      </div>

      <div class="panel" id="cc-salads" hidden>
        <p class="menu-price">Small (6&ndash;8) $50 &middot; Medium (15&ndash;20) $85 &middot; Large (25&ndash;35) $160</p>
        <p class="fine" style="margin-bottom:1.2rem;">Portions are designed to be enjoyed as a side.</p>""" + dishes([
        ("Mediterranean Potato Salad", "Olive &amp; Caper, Lemon &amp; Herby Olive Oil Dressing", "vg &middot; gf"),
        ("Cauliflower Power", "Curry Leaf &amp; Cumin Roasted Cauliflower &amp; Chickpea, Toasted Almonds, Ginger Coconut Dressing", "vg &middot; gf"),
        ("The Big Green Bowl", "Citrusy Zucchini, Broccoli Rice, Sauerkraut, Rocket &amp; Toasted Pumpkin Seeds", "vg &middot; gf"),
        ("Bring the Beet Back", "Roasted Beetroot &amp; Carrot, Pomegranate, Feta, Toasted Walnuts &amp; Balsamic Dressing", "v &middot; gf"),
        ("Classic Caesar", "Baby Cos, Pancetta, Parmesan, Anchovies, Rosemary Croutons"),
        ("The Kimchi Kick", "Kimchi &amp; Sesame Cucumber Brown Rice, Charred Broccoli, Edamame &amp; Fermented Chilli Dressing", "vg &middot; gf"),
        ]) + """
      </div>

      <div class="panel" id="cc-sandwiches" hidden>
        <p class="menu-price">$12.50 each &middot; min order 8</p>
        <p class="fine" style="margin-bottom:1.2rem;">Arrive sliced in half &middot; platter or individually wrapped.</p>""" + dishes([
        ("Pastrami &amp; Sauerkraut", "Horseradish Mayo &amp; Shredded Iceberg"),
        ("Smoked Salmon &amp; Lemon Caper Cream Cheese", "Pickled Cucumber &amp; Red Onion"),
        ("Chicken &amp; Maple Glazed Pancetta", "Basil Pesto &amp; Rocket"),
        ("Honey Glazed Ham &amp; Dill Pickle", "Mustard, Lettuce &amp; Fresh Apple"),
        ("Whipped Feta, Rocket &amp; Fig Chutney", "Pickled Red Onions, Walnuts &amp; Thyme", "v"),
        ("Kim-cheese &amp; Sesame Egg Mayo", "Chives &amp; Gem Lettuce", "v"),
        ("Garlic &amp; Herb Mushroom &amp; Mozzarella", "Lemon Zucchini Ribbon &amp; Olive Oil", "v"),
        ("Harissa Grilled Eggplant &amp; Cashew Ricotta", "Caramelised Onion Jam &amp; Dukkah", "vg"),
        ]) + """
      </div>

      <div class="panel" id="cc-packages" hidden>
        <p style="max-width:46rem;margin-bottom:2rem;">Just tell us your headcount and we'll handle the rest. All packages require a minimum of 8 guests and include delivery within 15km of Auckland CBD.</p>
        <div class="card-grid">
          <div class="card">
            <span class="eyebrow">Bundle 01</span>
            <h3>AM or PM Tea</h3>
            <p>Selection of Sweet &amp; Savoury House-Made Minis (2&ndash;3 pieces per person) &middot; Seasonal Fruit</p>
            <p class="menu-price">$17 pp &middot; min 8 guests</p>
          </div>
          <div class="card">
            <span class="eyebrow">Bundle 02</span>
            <h3>The Working Lunch</h3>
            <p>Full Gourmet Sandwich <em>or</em> Full Salad (min 8 of each selection) &middot; Seasonal Fruit &middot; Sweet Bite</p>
            <p class="menu-price">$22 pp &middot; min 8 guests</p>
          </div>
          <div class="card">
            <span class="eyebrow">Bundle 03</span>
            <h3>The Full Day</h3>
            <p><strong>Morning Tea:</strong> Sweet &amp; Savoury House-Made Minis (2&ndash;3 pp) &middot; <strong>Lunch:</strong> Gourmet Sandwich or Salad &amp; a Sweet Bite &middot; <strong>Afternoon Tea:</strong> Savoury &amp; Sweet Items (2&ndash;3 pp)</p>
            <p class="menu-price">$50 pp &middot; min 8 guests</p>
          </div>
        </div>
        <p class="menu-note">Pricing is per person and excludes delivery outside 15km of Auckland CBD. Dietary requirements are always accommodated &mdash; just let us know when you order. Got a specific brief? <a href="/contact-us/">Get in touch</a> and we'll put something bespoke together.</p>
      </div>
    </div>
    <p class="fine" style="margin-top:2.4rem;text-align:center;">v Vegetarian &nbsp;&middot;&nbsp; vg Vegan &nbsp;&middot;&nbsp; gf Gluten Free &nbsp;&middot;&nbsp; df Dairy Free &nbsp;&middot;&nbsp; ef Egg Free</p>
  </div>
</section>

<section class="section" id="order-form">
  <div class="wrap">
    <div class="section-head section-head--center">
      <span class="eyebrow">Place Your Order</span>
      <h2>Ready to Book?</h2>
      <p>Fill in the details below and Abi or Jake will be in touch within 24 hours to confirm your order.</p>
    </div>
    <!-- IMPORTANT: replace YOUR_FORM_ID with your Formspree form ID (see README) -->
    <form class="form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
      <div><label for="o-name">Contact Name</label><input id="o-name" name="contact_name" type="text" autocomplete="name" required></div>
      <div><label for="o-company">Company/Event Name</label><input id="o-company" name="company" type="text" autocomplete="organization"></div>
      <div><label for="o-email">Email</label><input id="o-email" name="email" type="email" autocomplete="email" required></div>
      <div><label for="o-phone">Contact Number</label><input id="o-phone" name="phone" type="tel" autocomplete="tel" required></div>
      <div class="full"><label for="o-address">Delivery Address</label><input id="o-address" name="delivery_address" type="text" autocomplete="street-address" required></div>
      <div><label for="o-date">Date Required</label><input id="o-date" name="date_required" type="date" required></div>
      <div><label for="o-time">Preferred Delivery Time</label><input id="o-time" name="delivery_time" type="time"></div>
      <div><label for="o-headcount">Headcount</label><input id="o-headcount" name="headcount" type="number" min="1"></div>
      <div><label for="o-dietary">Dietary Requirements</label><input id="o-dietary" name="dietary" type="text"></div>
      <div class="full"><label for="o-order">Order</label><textarea id="o-order" name="order" required placeholder="Tell us what you'd like to order"></textarea></div>
      <button class="btn btn--solid" type="submit">Send Order</button>
    </form>
  </div>
</section>
"""
