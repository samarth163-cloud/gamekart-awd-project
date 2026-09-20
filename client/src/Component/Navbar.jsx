import React from "react";
import logo from "../assets/gamekart-logo.svg";
import { Link, useNavigate, useLocation } from "react-router-dom";

const Navbar = () => {
  const id = localStorage.getItem("id");
  const navigate = useNavigate();
  const location = useLocation();

  const handleLogout = () => {
    localStorage.removeItem("id");
    navigate("/login");
  };

  return (
    <header className="navbar-header">
      <div className="container navbar-inner d-flex align-items-center justify-content-between">
        <Link to="/" className="navbar-brand-logo d-flex align-items-center">
          <img src={logo} alt="GameKart Logo" className="brand-logo-img" />
          <span className="brand-name">GameKart</span>
        </Link>

        <nav className="d-flex align-items-center nav-menu-links">
          <Link to="/" className={location.pathname === "/" ? "active-link" : ""}>
            Home
          </Link>
          <Link
            to="/Product"
            className={location.pathname === "/Product" ? "active-link" : ""}
          >
            Products
          </Link>
          <Link
            to="/orders"
            className={location.pathname === "/orders" ? "active-link" : ""}
          >
            Orders
          </Link>
          <Link
            to="/cart"
            className={location.pathname === "/cart" ? "active-link" : ""}
          >
            Cart
          </Link>
        </nav>

        <div className="nav-auth-actions d-flex align-items-center gap-2">
          {id !== null ? (
            <button onClick={handleLogout} className="btn-nav-action btn-nav-outline">
              Log Out
            </button>
          ) : (
            <Link to="/signup" className="btn-nav-action btn-nav-primary">
              Sign Up
            </Link>
          )}
        </div>
      </div>
    </header>
  );
};

export default Navbar;
