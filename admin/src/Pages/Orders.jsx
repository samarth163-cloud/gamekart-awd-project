import React, { useState, useEffect } from "react";
import Navbar from "../Component/Navbar";

const Orders = () => {
  const [orders, setOrders] = useState([]);

  const fetchOrders = async () => {
    try {
      const response = await fetch("http://localhost:5000/orders");
      if (response.ok) {
        const data = await response.json();
        setOrders(data);
      }
    } catch (error) {
      console.error("Error fetching orders:", error);
    }
  };

  useEffect(() => {
    fetchOrders();
  }, []);

  return (
    <Navbar>
      <section className="admin-panel">
        <div className="admin-panel-header">
          <div>
            <p className="admin-kicker">Sales</p>
            <h3 className="admin-panel-title">Manage Orders</h3>
            <p className="admin-panel-subtitle">
              Track customer orders and view the purchased product details.
            </p>
          </div>
          <span className="stat-pill">
            <i className="fa-solid fa-receipt"></i>
            {orders.length} Orders
          </span>
        </div>
        <div className="admin-panel-body">
          <div className="table-responsive">
            <table className="table table-hover align-middle admin-table">
              <thead>
                <tr>
                  <th>Order Date</th>
                  <th>Customer Name</th>
                  <th>Product Image</th>
                  <th>Product Name</th>
                  <th>Price</th>
                </tr>
              </thead>
              <tbody>
                {orders.length === 0 ? (
                  <tr>
                    <td colSpan="5" className="empty-state">
                      No orders placed yet.
                    </td>
                  </tr>
                ) : (
                  orders.map((order) => {
                    const user = order.user_details?.[0] || {};
                    const product = order.product_details?.[0] || {};
                    return (
                      <tr key={order._id}>
                        <td>{new Date(order.order_date).toLocaleDateString()}</td>
                        <td className="fw-semibold">{user.name || "Guest / UID: " + order.uid}</td>
                        <td>
                          {product.pimg ? (
                            <img
                              src={`http://localhost:5000/uploads/${product.pimg}`}
                              alt={product.pname}
                              className="order-thumb"
                            />
                          ) : (
                            <span className="text-muted">No Image</span>
                          )}
                        </td>
                        <td>{product.pname || "Product ID: " + order.pid}</td>
                        <td className="price-text">&#8377;{product.price || 0}</td>
                      </tr>
                    );
                  })
                )}
              </tbody>
            </table>
          </div>
        </div>
      </section>
    </Navbar>
  );
};

export default Orders;
