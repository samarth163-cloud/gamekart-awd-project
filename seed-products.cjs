const mongoose = require("mongoose");

const productSchema = new mongoose.Schema({
  pname: String,
  pimg: String,
  description: String,
  price: Number,
});

const Product = mongoose.model("product", productSchema, "products");

const gamingProducts = [
  {
    pname: "HyperX Cloud Pro Headset",
    pimg: "headphone-pro.jpg",
    description:
      "Premium wireless gaming headset with 7.1 surround sound, noise-cancelling mic, memory foam cushions, and 30-hour battery life. Built for marathon sessions.",
    price: 4999,
  },
  {
    pname: '34" Curved Gaming Monitor',
    pimg: "curved-monitor.jpg",
    description:
      "Ultra-wide 34-inch curved QHD display with 165Hz refresh rate, 1ms response time, HDR400 support, and AMD FreeSync Premium for tear-free visuals.",
    price: 28999,
  },
  {
    pname: "PlayStation 5 Console",
    pimg: "console-ps5.jpg",
    description:
      "Next-gen gaming console with ultra-fast SSD, ray tracing, 4K/120fps output, haptic feedback DualSense controller, and access to exclusive AAA titles.",
    price: 49999,
  },
  {
    pname: "Xbox Series X",
    pimg: "xbox-series-x.jpg",
    description:
      "The most powerful Xbox ever built. 12 teraflops of GPU power, 4K gaming at 120fps, Quick Resume, and backwards compatibility with thousands of games.",
    price: 49990,
  },
  {
    pname: "RGB Mechanical Keyboard",
    pimg: "keyboard-mechanical.jpg",
    description:
      "Full-size mechanical gaming keyboard with Cherry MX switches, per-key RGB backlighting, aluminum frame, macro keys, and USB passthrough.",
    price: 7499,
  },
  {
    pname: "Stealth Wireless Gaming Mouse",
    pimg: "mouse-wireless.jpg",
    description:
      "Lightweight 63g wireless gaming mouse with 25K DPI optical sensor, 70-hour battery life, PTFE glide feet, and 5 programmable buttons.",
    price: 3999,
  },
  {
    pname: "Titan Pro Gaming Chair",
    pimg: "gaming-chair.jpg",
    description:
      "Ergonomic racing-style gaming chair with 4D armrests, lumbar support pillow, cold-cure foam padding, 165° recline, and steel frame base.",
    price: 18999,
  },
  {
    pname: "Elite Pro Controller",
    pimg: "controller-rgb.jpg",
    description:
      "Pro-grade wireless controller with back paddles, adjustable triggers, interchangeable thumbsticks, RGB lighting, and Hall-effect joysticks.",
    price: 5999,
  },
  {
    pname: "Meta Quest VR Headset",
    pimg: "vr-headset.jpg",
    description:
      "All-in-one VR headset with pancake lenses, mixed reality passthrough, Snapdragon XR2 Gen 2 processor, and access to 500+ immersive VR titles.",
    price: 44999,
  },
  {
    pname: "Stream Deck Controller",
    pimg: "stream-deck.jpg",
    description:
      "15-key LCD macro pad for streamers and creators. One-touch scene switches, media controls, app launches, and customizable animated icons.",
    price: 12999,
  },
];

async function seed() {
  try {
    await mongoose.connect("mongodb://localhost:27017/dbProject");
    console.log("Connected to MongoDB");

    // Clear existing products
    await Product.deleteMany({});
    console.log("Cleared existing products");

    // Insert new products
    const result = await Product.insertMany(gamingProducts);
    console.log(`Successfully inserted ${result.length} gaming products:`);
    result.forEach((p) => console.log(`  - ${p.pname} (₹${p.price})`));

    await mongoose.disconnect();
    console.log("\nDone! Disconnected from MongoDB.");
  } catch (err) {
    console.error("Error seeding products:", err);
    process.exit(1);
  }
}

seed();
