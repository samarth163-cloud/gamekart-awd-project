import React, { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Navbar from "../Component/Navbar";
import Footer from "../Component/Footer";

const Cart = () => {
  const [data, setData] = useState([]);
  const [placing, setPlacing] = useState(false);
  const navigate = useNavigate();
  const uid = localStorage.getItem("id");

  const fetchCart = async () => {
    if (!uid) return;
    try {
      const response = await fetch(`http://localhost:4000/cart/${uid}`);
      if (response.ok) {
        const result = await response.json();
        setData(result);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const handleDelete = async (cartId) => {
    try {
      const response = await fetch(`http://localhost:4000/Delorders/${cartId}`, {
        method: "DELETE",
      });

      if (response.ok) {
        alert("Item removed from cart");
        fetchCart();
      } else {
        alert("Failed to remove item");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred");
    }
  };

  const handlePlaceOrder = async () => {
    if (data.length === 0) return;
    setPlacing(true);
    try {
      const response = await fetch("http://localhost:4000/placeOrder", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ id: uid }),
      });

      if (response.ok) {
        alert("Order placed successfully");
        navigate("/orders");
      } else {
        alert("Failed to place order");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred");
    } finally {
      setPlacing(false);
    }
  };

  useEffect(() => {
    fetchCart();
  }, [uid]);

  const total = data.reduce((sum, item) => {
    const product = item.product_details?.[0] || {};
    return sum + Number(product.price || 0);
  }, 0);

  return (
    <>
      <Navbar />
      <main className="page-shell cart-page">
        <div className="container">
          <nav aria-label="breadcrumb" className="mb-4">
            <ol className="breadcrumb">
              <li className="breadcrumb-item">
                <Link to="/" className="text-decoration-none text-primary">
                  Home
                </Link>
              </li>
              <li className="breadcrumb-item active" aria-current="page">
                Cart
              </li>
            </ol>
          </nav>

          {!uid ? (
            <div className="cart-panel text-center p-5">
              <p className="section-kicker">Cart</p>
              <h1 className="section-title">Login Required</h1>
              <p className="section-subtitle mb-4">
                Please login before viewing your cart.
              </p>
              <Link to="/login" className="btn btn-primary rounded-3 px-4">
                Login
              </Link>
            </div>
          ) : (
            <div className="row g-4">
              <div className="col-12 col-lg-8">
                <div className="cart-panel">
                  <div className="d-flex flex-column flex-sm-row justify-content-between align-items-sm-end gap-3 border-bottom pb-3 mb-4">
                    <div>
                      <p className="section-kicker mb-1">Shopping Cart</p>
                      <h1 className="h3 mb-0">Added Items</h1>
                    </div>
                    <Link to="/Product" className="btn-book-action orders-browse-link">
                      Add More
                    </Link>
                  </div>

                  <div className="table-responsive">
                    <table className="table table-hover align-middle orders-table">
                      <thead className="table-light">
                        <tr>
                          <th>Item</th>
                          <th>Image</th>
                          <th>Price</th>
                          <th>Added Date</th>
                          <th className="text-end">Action</th>
                        </tr>
                      </thead>
                      <tbody>
                        {data.length === 0 ? (
                          <tr>
                            <td colSpan="5" className="text-center py-5 text-muted">
                              Your cart is empty. Browse our{" "}
                              <Link to="/Product" className="text-primary">
                                collection
                              </Link>
                              .
                            </td>
                          </tr>
                        ) : (
                          data.map((item) => {
                            const product = item.product_details?.[0] || {};
                            return (
                              <tr key={item._id}>
                                <td className="fw-semibold text-dark">
                                  {product.pname || "Gaming Item"}
                                </td>
                                <td>
                                  {product.pimg ? (
                                    <img
                                      src={`http://localhost:5000/uploads/${product.pimg}`}
                                      alt={product.pname}
                                      className="order-thumb"
                                    />
                                  ) : (
                                    <span className="text-muted small">No image</span>
                                  )}
                                </td>
                                <td className="fw-bold text-primary">
                                  &#8377;{product.price || 0}
                                </td>
                                <td className="text-muted">
                                  {new Date(item.order_date).toLocaleDateString()}
                                </td>
                                <td className="text-end">
                                  <button
                                    onClick={() => handleDelete(item._id)}
                                    className="btn btn-outline-danger btn-sm px-3 btn-remove-order"
                                  >
                                    Remove
                                  </button>
                                </td>
                              </tr>
                            );
                          })
                        )}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>

              <div className="col-12 col-lg-4">
                <aside className="cart-panel cart-summary">
                  <p className="section-kicker mb-1">Checkout</p>
                  <h2 className="h4 mb-4">Order Summary</h2>
                  <div className="cart-summary-line">
                    <span>Total Items</span>
                    <strong>{data.length}</strong>
                  </div>
                  <div className="cart-summary-line">
                    <span>Total Amount</span>
                    <strong>&#8377;{total}</strong>
                  </div>
                  <button
                    type="button"
                    className="btn btn-primary rounded-3 w-100 mt-4"
                    onClick={handlePlaceOrder}
                    disabled={data.length === 0 || placing}
                  >
                    {placing ? "Placing Order..." : "Place Order"}
                  </button>
                </aside>
              </div>
            </div>
          )}
        </div>
      </main>
      <Footer />
    </>
  );
};

export default Cart;
