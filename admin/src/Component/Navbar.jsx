import React from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import logo from "../assets/gamekart-logo.svg";
import profile from "../assets/admin.png";

const Navbar = ({ children }) => {
  const location = useLocation();
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("id");
    navigate("/login");
  };

  return (
    <div className="wrapper">
      <aside className="sidebar">
        <div className="sidebar-brand">
          <div>
            <div className="sidebar-logo">
              <img src={logo} alt="GameKart Logo" />
            </div>
            <h5 className="sidebar-title">Admin Panel</h5>
            <p className="sidebar-subtitle">GameKart Control Center</p>
          </div>
        </div>

        <nav className="sidebar-nav">
          <Link to="/" className={location.pathname === "/" ? "active-link" : ""}>
            <i className="fa-solid fa-box-open"></i>
            <span>Manage Products</span>
          </Link>
          <Link
            to="/orders"
            className={location.pathname === "/orders" ? "active-link" : ""}
          >
            <i className="fa-solid fa-cart-shopping"></i>
            <span>View Orders</span>
          </Link>
          <Link
            to="/users"
            className={location.pathname === "/users" ? "active-link" : ""}
          >
            <i className="fa-solid fa-users"></i>
            <span>Manage Users</span>
          </Link>
          <button type="button" onClick={handleLogout}>
            <i className="fa-solid fa-right-from-bracket"></i>
            <span>Log Out</span>
          </button>
        </nav>

        <div className="sidebar-account">
          <div className="d-flex align-items-center gap-3">
            <img src={profile} alt="Admin" />
            <div>
              <p className="m-0">
                <strong>Admin</strong>
                <br />
                <span>admin@gamekart.com</span>
              </p>
            </div>
          </div>
        </div>
      </aside>

      <div className="content">
        <nav className="navbar admin-header">
          <div>
            <span className="navbar-brand mb-0">GameKart Admin Dashboard</span>
            <br />
            <small>Manage products, orders, and users</small>
          </div>
          <button className="btn btn-soft btn-sm" id="menu-toggle" type="button">
            <i className="fa-solid fa-bars"></i>
          </button>
        </nav>
        <main className="admin-main">{children}</main>
      </div>
    </div>
  );
};

export default Navbar;
