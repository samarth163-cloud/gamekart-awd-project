import React, { useEffect, useState } from "react";

import Navbar from "../Component/Navbar";
import { Link } from "react-router-dom";
import Footer from "../Component/Footer";

const ProductPage = () => {
  const [products, setProducts] = useState([]);
  const fetchData = async () => {
    try {
      const response = await fetch("http://localhost:5000/getProducts");
      if (response.ok) {
        const data = await response.json();
        setProducts(data);
      } else {
        console.error("Failed to fetch products");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };
  const handleSearch = async (e) => {
    const query = e.target.value; // current input value
    try {
      const response = await fetch(
        `http://localhost:4000/searchProducts?query=${query}`
      );
      if (response.ok) {
        const data = await response.json();
        setProducts(data);
      } else {
        console.error("Failed to fetch products");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };
  useEffect(() => {
    fetchData();
  }, []);
  return (
    <>
      <Navbar />
      <main className="catalog-page page-shell">
        <div className="container">
          <div className="section-header text-center mb-4">
            <p className="section-kicker">Gaming Gear &amp; Titles</p>
            <h1 className="section-title">Explore Store Catalog</h1>
            <p className="section-subtitle">
              Search the armory or select any item to inspect technical specifications.
            </p>
          </div>

          <div className="row mb-5">
            <div className="col-12 col-md-8 col-lg-6 mx-auto">
              <div className="search-panel">
                <form
                  onSubmit={(e) => {
                    e.preventDefault();
                    handleSearch(e);
                  }}
                >
                  <input
                    type="search"
                    placeholder="Search for gaming gear, consoles, or titles..."
                    onChange={(e) => handleSearch(e)}
                    className="form-control form-control-lg search-input px-4"
                  />
                </form>
              </div>
            </div>
          </div>

          <div className="row g-4">
            {products.length === 0 ? (
              <div className="col-12 text-center py-5">
                <p className="text-muted fs-5">No gaming products found.</p>
              </div>
            ) : (
              products.map((product) => (
                <div key={product._id || product.id} className="col-12 col-md-6 col-lg-4">
                  <div className="book-card h-100 d-flex flex-column">
                    <div className="book-card-image-wrap">
                      <Link to={`/prodDetail/${product._id}`}>
                        <img
                          className="book-card-img"
                          src={`http://localhost:5000/uploads/${product.pimg}`}
                          alt={product.pname}
                        />
                      </Link>
                    </div>
                    <div className="book-card-content d-flex flex-column flex-grow-1 p-4">
                      <h4 className="book-card-title">{product.pname}</h4>
                      <p className="book-card-desc flex-grow-1">{product.description}</p>
                      <div className="book-card-price mb-3">&#8377;{product.price}</div>
                      <Link
                        to={`/prodDetail/${product._id}`}
                        className="btn-book-action mt-auto"
                      >
                        Get More Info
                      </Link>
                    </div>
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      </main>
      <Footer />
    </>
  );
};

export default ProductPage;
