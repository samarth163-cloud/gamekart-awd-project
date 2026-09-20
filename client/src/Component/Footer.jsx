import React from "react";
import { Link } from "react-router-dom";

const Footer = () => {
  return (
    <footer className="site-footer">
      <div className="container py-5">
        <div className="row g-4">
          <div className="col-12 col-md-6 col-lg-3">
            <h6 className="footer-title">GameKart</h6>
            <p className="footer-desc">
              GameKart is a modern, high-performance online gaming store
              providing gamers with instant access to consoles, controllers,
              accessories, and top-tier digital titles.
            </p>
          </div>

          <div className="col-6 col-md-3 col-lg-2 offset-lg-1">
            <h6 className="footer-title">Categories</h6>
            <ul className="footer-links-list">
              <li>
                <Link to="/Product">Gaming Consoles</Link>
              </li>
              <li>
                <Link to="/Product">Controllers &amp; Gear</Link>
              </li>
              <li>
                <Link to="/Product">VR &amp; Headsets</Link>
              </li>
              <li>
                <Link to="/Product">Action &amp; RPG Games</Link>
              </li>
            </ul>
          </div>

          <div className="col-6 col-md-3 col-lg-2">
            <h6 className="footer-title">Quick Links</h6>
            <ul className="footer-links-list">
              <li>
                <Link to="/Product">All Products</Link>
              </li>
              <li>
                <Link to="/orders">Your Orders</Link>
              </li>
              <li>
                <Link to="/login">Account</Link>
              </li>
              <li>
                <Link to="/signup">Register</Link>
              </li>
            </ul>
          </div>

          <div className="col-12 col-md-6 col-lg-3 offset-lg-1">
            <h6 className="footer-title">Support</h6>
            <p className="footer-contact-item">
              <i className="fa-solid fa-location-dot me-2"></i> Cyber City, Gaming Hub 10012
            </p>
            <p className="footer-contact-item">
              <i className="fa-solid fa-envelope me-2"></i> support@gamekart.com
            </p>
            <p className="footer-contact-item">
              <i className="fa-solid fa-phone me-2"></i> +1 800 426 3527
            </p>
          </div>
        </div>

        <hr className="footer-divider my-4" />

        <div className="d-flex flex-column flex-sm-row justify-content-between align-items-center gap-3">
          <div className="footer-copyright">
            &copy; 2026 GameKart. All rights reserved.
          </div>
          <div className="footer-social-links d-flex gap-3">
            <a href="#twitter" aria-label="Twitter" className="footer-social-link">
              <i className="fa-brands fa-twitter"></i>
            </a>
            <a href="#facebook" aria-label="Facebook" className="footer-social-link">
              <i className="fa-brands fa-facebook-f"></i>
            </a>
            <a href="#instagram" aria-label="Instagram" className="footer-social-link">
              <i className="fa-brands fa-instagram"></i>
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
