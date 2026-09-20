import React, { useState, useEffect } from "react";
import Navbar from "../Component/Navbar";

const Product = () => {
  const [products, setProducts] = useState([]);
  const [formData, setFormData] = useState({
    pname: "",
    description: "",
    price: "",
  });
  const [pimg, setPimg] = useState(null);

  // Fetch all products from admin backend
  const fetchProducts = async () => {
    try {
      const response = await fetch("http://localhost:5000/getProducts");
      if (response.ok) {
        const data = await response.json();
        setProducts(data);
      }
    } catch (error) {
      console.error("Error fetching products:", error);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleFileChange = (e) => {
    setPimg(e.target.files[0]);
  };

  // Add a new product
  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = new FormData();
    data.append("pname", formData.pname);
    data.append("description", formData.description);
    data.append("price", formData.price);
    if (pimg) {
      data.append("pimg", pimg);
    }

    try {
      const response = await fetch("http://localhost:5000/products", {
        method: "POST",
        body: data,
      });

      if (response.ok) {
        alert("Product added successfully!");
        setFormData({ pname: "", description: "", price: "" });
        setPimg(null);
        document.getElementById("productImage").value = "";
        fetchProducts();
      } else {
        alert("Failed to add product.");
      }
    } catch (error) {
      console.error("Error adding product:", error);
      alert("Error connecting to server.");
    }
  };

  // Delete a product
  const handleDelete = async (id) => {
    if (!window.confirm("Are you sure you want to delete this product?")) return;
    try {
      const response = await fetch(`http://localhost:5000/Delproducts/${id}`, {
        method: "DELETE",
      });
      if (response.ok) {
        alert("Product deleted successfully!");
        fetchProducts();
      } else {
        alert("Failed to delete product.");
      }
    } catch (error) {
      console.error("Error deleting product:", error);
    }
  };

  return (
    <Navbar>
      <div className="admin-page">
        <section className="admin-panel">
          <div className="admin-panel-header">
            <div>
              <p className="admin-kicker">Catalog</p>
              <h3 className="admin-panel-title">Manage Products</h3>
              <p className="admin-panel-subtitle">
                Add new gaming products with an image, description, and price.
              </p>
            </div>
            <span className="stat-pill">
              <i className="fa-solid fa-book"></i>
              {products.length} Products
            </span>
          </div>
          <div className="admin-panel-body">
            <form onSubmit={handleSubmit}>
              <div className="row g-3">
                <div className="col-12 col-md-6">
                  <label htmlFor="productName" className="form-label">
                    Product Name
                  </label>
                  <input
                    type="text"
                    name="pname"
                    value={formData.pname}
                    onChange={handleChange}
                    className="form-control"
                    id="productName"
                    placeholder="Enter product title"
                    required
                  />
                </div>
                <div className="col-12 col-md-6">
                  <label htmlFor="productImage" className="form-label">
                    Product Image
                  </label>
                  <input
                    type="file"
                    name="pimg"
                    onChange={handleFileChange}
                    className="form-control"
                    id="productImage"
                    required
                  />
                </div>
                <div className="col-12 col-md-8">
                  <label htmlFor="productDescription" className="form-label">
                    Product Description
                  </label>
                  <textarea
                    name="description"
                    value={formData.description}
                    onChange={handleChange}
                    className="form-control"
                    id="productDescription"
                    rows="3"
                    placeholder="Enter product description"
                    required
                  ></textarea>
                </div>
                <div className="col-12 col-md-4">
                  <label htmlFor="productPrice" className="form-label">
                    Product Price (&#8377;)
                  </label>
                  <input
                    type="number"
                    name="price"
                    value={formData.price}
                    onChange={handleChange}
                    className="form-control"
                    id="productPrice"
                    placeholder="Enter price"
                    required
                  />
                </div>
                <div className="col-12">
                  <button type="submit" className="btn btn-primary rounded-3 px-4">
                    Add Product
                  </button>
                </div>
              </div>
            </form>
          </div>
        </section>

        <section className="admin-panel">
          <div className="admin-panel-header">
            <div>
              <p className="admin-kicker">Inventory</p>
              <h3 className="admin-panel-title">Product List</h3>
              <p className="admin-panel-subtitle">
                Review your catalog and remove books when needed.
              </p>
            </div>
          </div>
          <div className="admin-panel-body">
            <div className="table-responsive">
              <table className="table table-hover align-middle admin-table">
                <thead>
                  <tr>
                    <th>Image</th>
                    <th>Name</th>
                    <th>Description</th>
                    <th>Price</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {products.length === 0 ? (
                    <tr>
                      <td colSpan="5" className="empty-state">
                        No products found. Add a product using the form above!
                      </td>
                    </tr>
                  ) : (
                    products.map((prod) => (
                      <tr key={prod._id}>
                        <td>
                          {prod.pimg ? (
                            <img
                              src={`http://localhost:5000/uploads/${prod.pimg}`}
                              alt={prod.pname}
                              className="product-thumb"
                            />
                          ) : (
                            <span className="text-muted">No Image</span>
                          )}
                        </td>
                        <td className="fw-semibold">{prod.pname}</td>
                        <td className="table-description">{prod.description}</td>
                        <td className="price-text">&#8377;{prod.price}</td>
                        <td>
                          <button
                            onClick={() => handleDelete(prod._id)}
                            className="btn btn-outline-danger btn-sm rounded-3 px-3"
                          >
                            Delete
                          </button>
                        </td>
                      </tr>
                    ))
                  )}
                </tbody>
              </table>
            </div>
          </div>
        </section>
      </div>
    </Navbar>
  );
};

export default Product;
