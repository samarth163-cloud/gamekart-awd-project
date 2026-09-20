import React, { useEffect, useState } from "react";
import Navbar from "../Component/Navbar";
import { useNavigate, useParams } from "react-router-dom";

const UpdateProduct = () => {
  const [formData, setFormdata] = useState({});
  const { id } = useParams();
  const navigate = useNavigate();
  const fetchData = async () => {
    const response = await fetch(`http://localhost:5000/getProducts/${id}`);
    if (response.ok) {
      const data = await response.json();
      setFormdata(data);
    } else {
      console.error("Failed to fetch product");
    }
  };
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormdata({ ...formData, [name]: value });
    console.log(formData);
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch(`http://localhost:5000/updateProducts/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    });
    if (response.ok) {
      console.log("Product updated successfully");
      navigate("/");
    } else {
      console.error("Failed to update product");
    }
  };

  useEffect(() => {
    fetchData();
  }, []);
  return (
    <Navbar>
      <section className="admin-panel">
        <div className="admin-panel-header">
          <div>
            <p className="admin-kicker">Catalog</p>
            <h3 className="admin-panel-title">Update Product</h3>
            <p className="admin-panel-subtitle">
              Edit the product details and save the latest information.
            </p>
          </div>
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
                  className="form-control"
                  id="productName"
                  name="pname"
                  value={formData.pname}
                  onChange={(e) => handleChange(e)}
                  required
                />
              </div>
              <div className="col-12 col-md-6">
                <label htmlFor="productPrice" className="form-label">
                  Product Price
                </label>
                <input
                  type="number"
                  className="form-control"
                  id="productPrice"
                  name="price"
                  value={formData.price}
                  onChange={(e) => handleChange(e)}
                  required
                />
              </div>
              <div className="col-12">
                <label htmlFor="productDescription" className="form-label">
                  Product Description
                </label>
                <textarea
                  className="form-control"
                  id="productDescription"
                  name="description"
                  rows="4"
                  value={formData.description}
                  onChange={(e) => handleChange(e)}
                  required
                ></textarea>
              </div>
              <div className="col-12">
                <button type="submit" className="btn btn-primary rounded-3 px-4">
                  Update Product
                </button>
              </div>
            </div>
          </form>
        </div>
      </section>
    </Navbar>
  );
};

export default UpdateProduct;
