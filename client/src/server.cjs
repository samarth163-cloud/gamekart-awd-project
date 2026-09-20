const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const { Register,Product,Cart } = require("./userModel.cjs");
const multer = require("multer");
const path = require("path");
const app = express();

app.use(cors());

app.use(express.json());
app.use("/uploads", express.static(path.join(__dirname, "uploads")));
const port = 4000;

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, path.join(__dirname, "uploads"));
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname.toLocaleLowerCase());
  },
});

const upload = multer({ storage });

mongoose
  .connect("mongodb://localhost:27017/dbProject")
  .then(() => {
    console.log("Connected to MongoDB");
  })
  .catch((err) => {
    console.error("Error connecting to MongoDB:", err);
  });

// Get all products
app.get("/getProducts", async (req, res) => {
  try {
    const products = await Product.find();
    res.json(products);
  } catch (err) {
    console.error("Error fetching products:", err);
  }
});

// User signup
app.post("/signup", upload.single("profile"), async (req, res) => {
  const { name, email, password, gender, city } = req.body;
  const profile = req.file ? req.file.filename : null;

  try {
    const newClientUser = new Register({
      name,
      email,
      password,
      gender,
      city,
      profile,
    });
    await newClientUser.save();
    res.status(201).json({ message: "User registered successfully" });
  } catch (err) {
    console.log(err);
    res.status(500).json({ message: "Internal server error" });
  }
});
// User login
app.post("/login", async (req, res) => {
  const { email, password } = req.body;
  try {
    const user = await Register.findOne({ email, password });
    if (user) {
        const id=user._id;
        res.json({ message: "Login successful", id });
    } else {
      res.status(401).json({ message: "Invalid email or password" });
    }
  } catch (err) {
    res.status(500).json({ message: "Internal server error" });
  }
});

// Search products
app.get("/searchProducts", async (req, res) => {
  const { query } = req.query;
  try {
    const products = await Product.find({
      pname: { $regex: query, $options: "i" }, // case-insensitive
    });
    res.json(products);
  } catch (err) {
    console.error("Error searching products:", err);
    res.status(500).json({ message: "Internal server error" });
  }
});

// Get product details
app.get("/prodDetails/:id", async (req, res) => {
  const { id } = req.params;
  try {
    const product = await Product.findById(id);
    if (product) {
      res.json(product);
    } else {
      res.status(404).json({ message: "Product not found" });
    }
  } catch (err) {
    console.error("Error fetching product details:", err);
    res.status(500).json({ message: "Internal server error" });
  }
});

// Add to cart
app.post("/addToCart", async (req, res) => {
  const { pid, uid } = req.body;
  try {
    const addtocart = new Cart({ order_date: Date.now(), pid, uid, status: "cart" });
    await addtocart.save();
    res.status(200).json(addtocart);
  } catch (err) {
    console.error(err);
  }
});

// Check if item is in cart
app.get("/checkCart/:uid/:pid", async (req, res) => {
  const { uid, pid } = req.params;
  try {
    const item = await Cart.findOne({
      uid,
      pid,
      $or: [{ status: "cart" }, { status: { $exists: false } }],
    });
    if (item) {
      return res.json({ inCart: true });
    }
    res.json({ inCart: false });
  } catch (err) {
    console.error(err);
    res.status(500).json({ inCart: false });
  }
});

const cartLookupPipeline = [
  {
    // Convert string fields to ObjectId for lookup
    $addFields: {
      uidObjectId: { $toObjectId: "$uid" },
      pidObjectId: { $toObjectId: "$pid" },
    },
  },
  {
    $lookup: {
      from: "registers",
      localField: "uidObjectId",
      foreignField: "_id",
      as: "user_details",
    },
  },
  {
    $lookup: {
      from: "products",
      localField: "pidObjectId",
      foreignField: "_id",
      as: "product_details",
    },
  },
];

// Get cart items
app.get("/cart/:id", async (req, res) => {
  const { id } = req.params;
  try {
    const cartdata = await Cart.aggregate([
      {
        $match: {
          uid: id,
          $or: [{ status: "cart" }, { status: { $exists: false } }],
        },
      },
      ...cartLookupPipeline,
    ]);
    res.status(200).send(cartdata);
  } catch (err) {
    console.error(err);
    res.status(500).send("Error fetching cart");
  }
});

// Place order
app.post("/placeOrder", async (req, res) => {
  const { id } = req.body;
  try {
    const result = await Cart.updateMany(
      {
        uid: id,
        $or: [{ status: "cart" }, { status: { $exists: false } }],
      },
      { $set: { status: "ordered", order_date: Date.now() } }
    );
    res.status(200).json({ message: "Order placed successfully", result });
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: "Error placing order" });
  }
});

// Get placed orders
app.post("/orders", async (req, res) => {
    const { id } = req.body;
    console.log(id);
  try {
    const cartdata = await Cart.aggregate([
      {
        $match: { uid: id, status: "ordered" },
      },
      ...cartLookupPipeline,
    ]);
    res.status(200).send(cartdata);
    console.log(cartdata);
  } catch (err) {
    console.error(err);
    res.status(500).send("Error fetching comments");
  }
});

// Delete an order
app.delete("/Delorders/:id", async (req, res) => {
  const { id } = req.params;
  try {
    await Cart.findByIdAndDelete(id);
    res.status(200).json({ message: "Order deleted successfully" });
  } catch (err) {
    console.error("Error deleting order:", err);
    res.status(500).json({ message: "Internal server error" });
  }
});
app.listen(port, () => {
  console.log(`Server is running on ${port}`);
});
