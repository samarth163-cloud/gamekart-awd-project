const mongoose = require("mongoose");

const adminSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  email: {
    type: String,
    required: true,
    unique: true,
  },
  password: {
    type: String,
    required: true,
  },
});
const productSchema = new mongoose.Schema({
  pname: String,
  pimg: String,
  description: String,
  price: Number,
});

const register = new mongoose.Schema({
  name: String,
  email: String,
  password: String,
  gender: String,
  city: String,
  profile: String
});
const cart = new mongoose.Schema({
  order_date: { type: Date, default: Date.now },
  pid: String,
  uid: String,
  status: { type: String, default: "cart" },
});
const Product = mongoose.model("product", productSchema, "products");
const User = mongoose.model("admin", adminSchema, "admins");
const Register = mongoose.model("register", register, "registers");
const Cart = mongoose.model("cart", cart, "carts");

module.exports = { User, Product, Register, Cart };
