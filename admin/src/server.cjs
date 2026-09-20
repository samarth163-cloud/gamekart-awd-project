const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const { User, Product, Register, Cart } = require("./userModel.cjs");
const multer = require("multer");
const path = require("path");
const app = express();
app.use(cors());

app.use(express.json());
app.use("/uploads", express.static(path.join(__dirname, "uploads")));
const port = 5000;

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

// User login
app.post("/login", async (req, res) => {
  const { email, password } = req.body;
  try {
    const user = await User.findOne({ email, password });
    if (user) {
      const id = user._id;
      res.json({ message: "Login successful", id });
    } else {
      res.status(401).json({ message: "Invalid email or password" });
    }
  } catch (err) {
    res.status(500).json({ message: "Internal server error" });
  }
});
// Get all users
app.get("/users", async (req, res) => {
  try {
    const users = await Register.find();
    res.json(users);
  } catch (err) {
    console.error("Error fetching users:", err);
    res.status(500).json({ message: "Internal server error" });
  }
});
// Get all orders
app.get("/orders", async (req, res) => {
  try {
    const cartdata = await Cart.aggregate([
      {
        $match: { status: "ordered" },
      },
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
    ]);
    res.status(200).send(cartdata);
    console.log(cartdata);
  } catch (err) {
    console.error(err);
    res.status(500).send("Error fetching comments");
  }
});

// Add a new product
app.post("/products", upload.single("pimg"), async (req, res) => {
  //   console.log("Body:", req.body);
  //   console.log("File:", req.file);
  const { pname, description, price } = req.body;
  const pimg = req.file ? req.file.filename : null;

  try {
    const newProduct = new Product({
      pname,
      pimg,
      description,
      price,
    });
    await newProduct.save();
    res.status(201).json({ message: "Product added successfully" });
  } catch (err) {
    console.log(err);
    res.status(500).json({ message: "Internal server error" });
  }
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
// Get a single product
app.get("/getProducts/:id", async (req, res) => {
  try {
    const product = await Product.findById(req.params.id);
    if (product) {
      res.json(product);
    } else {
      res.status(404).json({ message: "Product not found" });
    }
  } catch (err) {
    console.error("Error fetching products:", err);
  }
});
// Update a product
app.put("/updateProducts/:id", async (req, res) => {
  const { id } = req.params;
  const { pname, description, price } = req.body;

  try {
    const updatedProduct = await Product.findByIdAndUpdate(
      id,
      { pname, description, price },
      { new: true }
    );
    if (updatedProduct) {
      res.json({
        message: "Product updated successfully",
        Product: updatedProduct,
      });
    } else {
      res.status(404).json({ message: "Product not found" });
    }
  } catch (err) {
    console.error("Error updating product:", err);
    res.status(500).json({ message: "Internal server error" });
  }
});
// Delete a product
app.delete("/Delproducts/:id", async (req, res) => {
  const { id } = req.params;
  try {
    await Product.findByIdAndDelete(id);
    res.json({ message: "Product deleted successfully" });
  } catch (err) {
    console.error("Error deleting product:", err);
    res.status(500).json({ message: "Internal server error" });
  }
});

app.listen(port, () => {
  console.log(`Server is running on ${port}`);
});
