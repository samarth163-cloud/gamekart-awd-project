import React, { useState, useEffect } from "react";
import Navbar from "../Component/Navbar";
import Footer from "../Component/Footer";
import { Link } from "react-router-dom";

const Orders = () => {
  const [data, setData] = useState([]);
  const [paymentOrder, setPaymentOrder] = useState(null);

  const fetchData = async () => {
    const id = localStorage.getItem("id");
    if (!id) return;
    const response = await fetch("http://localhost:4000/orders", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ id }),
    });
    const result = await response.json();
    setData(result);
    console.log(data);
  };

  const handleDelete = async (orderId) => {
    try {
      const response = await fetch(
        `http://localhost:4000/Delorders/${orderId}`,
        {
          method: "DELETE",
        }
      );

      if (response.ok) {
        alert("Order deleted successfully");
        fetchData();
      } else {
        alert("Failed to delete order");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred");
    }
  };

  const handlePaymentClick = (order) => {
    setPaymentOrder(order);
  };

  const closePaymentPopup = () => {
    setPaymentOrder(null);
  };

  const handlePaymentDone = async () => {
    if (!paymentOrder?._id) return;
    try {
      const response = await fetch(
        `http://localhost:4000/Delorders/${paymentOrder._id}`,
        {
          method: "DELETE",
        }
      );

      if (response.ok) {
        alert("Payment completed successfully");
        setData((orders) =>
          orders.filter((order) => order._id !== paymentOrder._id)
        );
        closePaymentPopup();
      } else {
        alert("Payment completed, but failed to remove order");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred");
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const selectedProduct = paymentOrder?.product_details?.[0] || {};

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
              <li className="breadcrumb-item active" aria-current="page">
                My Orders
              </li>
            </ol>
          </nav>

          <div className="orders-panel">
            <div className="d-flex flex-column flex-sm-row justify-content-between align-items-sm-end gap-3 border-bottom pb-3 mb-4">
              <div>
                <p className="section-kicker mb-1">Account</p>
                <h2 className="h3 mb-0">Placed Orders</h2>
              </div>
              <Link to="/Product" className="btn-book-action orders-browse-link">
                Browse Gear
              </Link>
            </div>
            <div className="table-responsive">
              <table className="table table-hover align-middle orders-table">
                <thead className="table-light">
                  <tr>
                    <th>Item</th>
                    <th>Image</th>
                    <th>Price</th>
                    <th>Order Date</th>
                    <th className="text-end">Action</th>
                  </tr>
                </thead>
                <tbody>
                  {data.length === 0 ? (
                    <tr>
                      <td colSpan="5" className="text-center py-5 text-muted">
                        You have no placed orders yet. Add items from our{" "}
                        <Link to="/Product" className="text-primary">
                          collection
                        </Link>
                        .
                      </td>
                    </tr>
                  ) : (
                    data.map((order) => {
                      const carts = order.product_details?.[0] || {};
                      return (
                        <tr key={order._id}>
                          <td className="fw-semibold text-dark">{carts.pname || "Gaming Item"}</td>
                          <td>
                            {carts.pimg ? (
                              <img
                                src={`http://localhost:5000/uploads/${carts.pimg}`}
                                alt={carts.pname}
                                className="order-thumb"
                              />
                            ) : (
                              <span className="text-muted small">No image</span>
                            )}
                          </td>
                          <td className="fw-bold text-primary">&#8377;{carts.price}</td>
                          <td className="text-muted">
                            {new Date(order.order_date).toLocaleDateString()}
                          </td>
                          <td className="text-end">
                            <div className="order-action-group">
                              <button
                                onClick={() => handlePaymentClick(order)}
                                className="btn btn-payment btn-sm px-3"
                              >
                                Payment
                              </button>
                              <button
                                onClick={() => handleDelete(order._id)}
                                className="btn btn-outline-danger btn-sm px-3 btn-remove-order"
                              >
                                Remove
                              </button>
                            </div>
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
      </main>

      {paymentOrder && (
        <div className="payment-modal-backdrop" role="dialog" aria-modal="true">
          <div className="payment-modal">
            <button
              type="button"
              className="payment-modal-close"
              onClick={closePaymentPopup}
              aria-label="Close payment popup"
            >
              <i className="fa-solid fa-xmark"></i>
            </button>
            <p className="section-kicker mb-2">Payment</p>
            <h3 className="mb-3">Payment Details</h3>
            <div className="payment-summary">
              <div className="payment-summary-line">
                <span>Product</span>
                <strong>{selectedProduct.pname || "Book"}</strong>
              </div>
              <div className="payment-summary-line">
                <span>Amount</span>
                <strong>&#8377;{selectedProduct.price || 0}</strong>
              </div>
              <div className="payment-summary-line">
                <span>Order Date</span>
                <strong>{new Date(paymentOrder.order_date).toLocaleDateString()}</strong>
              </div>
            </div>
            <p className="text-muted small mt-3 mb-4">
              This is a payment popup. Payment gateway integration can be added
              later.
            </p>
            <button
              type="button"
              className="btn btn-primary rounded-3 w-100"
              onClick={handlePaymentDone}
            >
              Payment Done
            </button>
          </div>
        </div>
      )}

      <Footer />
    </>
  );
};

export default Orders;
