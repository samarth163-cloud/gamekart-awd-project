import React, { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import Navbar from "../Component/Navbar";
import Footer from "../Component/Footer";

const ProdDetails = () => {
  const [data, setData] = useState({});
  const [inCart, setInCart] = useState(false);
  const { id } = useParams();
  const navigate = useNavigate();
  const uid = localStorage.getItem("id");
  const fetchData = async () => {
    const response = await fetch(`http://localhost:4000/prodDetails/${id}`);
    const result = await response.json();
    setData(result);
    console.log(data);
  };
  const checkCart = async () => {
    if (!uid) return;
    const response = await fetch(
      `http://localhost:4000/checkCart/${uid}/${id}`
    );
    const result = await response.json();
    setInCart(result.inCart);
  };
  const handleSubmit = async () => {
    const response = await fetch("http://localhost:4000/addToCart", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ pid: id, uid }),
    });
    const result = await response.json();
    console.log(result);
    alert("Product added to cart");
    setInCart(true);
    navigate("/cart");
  };
  useEffect(() => {
    fetchData();
    checkCart();
  }, [id, uid]);

  return (
    <>
      <Navbar />
      <main className="page-shell">
        <div className="container">
          <nav aria-label="breadcrumb" className="mb-4">
            <ol className="breadcrumb">
              <li className="breadcrumb-item">
                <Link to="/" className="text-decoration-none text-primary">
                  Home
                </Link>
              </li>
              <li className="breadcrumb-item">
                <Link to="/Product" className="text-decoration-none text-primary">
                  Products
                </Link>
              </li>
              <li className="breadcrumb-item active" aria-current="page">
                {data.pname || "Details"}
              </li>
            </ol>
          </nav>

          <div className="detail-panel">
            <div className="row g-5 align-items-center">
              <div className="col-12 col-md-6 text-center">
                <div className="detail-image-panel">
                  <img
                    src={`http://localhost:5000/uploads/${data.pimg}`}
                    alt={data.pname}
                    className="img-fluid detail-image"
                  />
                </div>
              </div>
              <div className="col-12 col-md-6">
                <div className="detail-summary">
                  <h1 className="text-capitalize mb-3">{data.pname}</h1>
                  <div className="price-label mb-4">&#8377; {data.price}</div>
                  <div className="description-box mb-4">
                    <h5 className="mb-2">Description</h5>
                    <p className="m-0 text-muted lh-base">
                      {data.description || "No description provided."}
                    </p>
                  </div>
                  {uid === null ? (
                    <Link
                      to="/login"
                      className="btn btn-primary btn-lg rounded-3 px-5 shadow-sm"
                    >
                      Login to Add to Cart
                    </Link>
                  ) : inCart ? (
                    <div>
                      <div className="alert in-cart-alert d-inline-block rounded-3 px-4 py-2 mb-3">
                        This product is in your cart.
                      </div>
                      <br />
                      <Link to="/cart" className="btn btn-primary btn-lg rounded-3 px-5 shadow-sm">
                        View Cart
                      </Link>
                    </div>
                  ) : (
                    <button
                      className="btn btn-primary btn-lg rounded-3 px-5 shadow-sm"
                      onClick={handleSubmit}
                    >
                      Add to Cart
                    </button>
                  )}
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
      <Footer />
    </>
  );
};

export default ProdDetails;
