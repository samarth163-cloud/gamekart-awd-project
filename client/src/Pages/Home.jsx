import React, { useEffect, useState } from "react";
import Navbar from "../Component/Navbar";
import Footer from "../Component/Footer";
import bg from "../assets/hero-banner.jpg";
import book1 from "../assets/book1.webp";
import { Link } from "react-router-dom";

const Home = () => {
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

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <>
      <Navbar />

      <section className="hero-banner-section">
        <div className="container">
          <div className="hero-image-wrapper">
            <img src={bg} alt="GameKart Gaming Store" className="hero-banner-img" />
            <div className="hero-content">
              <span className="eyebrow">Next-Gen Gaming Store</span>
              <h1>Level Up Your Gaming Experience.</h1>
              <p>
                Explore next-gen consoles, pro controllers, high-performance
                accessories, and top-tier games in one seamless store.
              </p>
              <Link to="/Product" className="btn-hero-primary">
                Browse Gear
              </Link>
              <div className="hero-highlights">
                <span>Next-Gen Gear</span>
                <span>Fast Dispatch</span>
                <span>Pro Gamer Choice</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="catalog-section py-5">
        <div className="container">
          <div className="section-header text-center mb-5">
            <p className="section-kicker">Featured Gear &amp; Games</p>
            <h2 className="section-title">Pick Your Battle Station Setup</h2>
            <p className="section-subtitle">
              Verified gaming products, clear pricing, and instant specs breakdown.
            </p>
            <div className="section-divider-line mx-auto"></div>
          </div>

          <div className="row g-4">
            {products.length === 0 ? (
              <div className="col-12 text-center py-5">
                <p className="text-muted fs-5">No gaming products available at the moment.</p>
              </div>
            ) : (
              products.map((product) => (
                <div className="col-12 col-md-6 col-lg-4" key={product._id}>
                  <div className="book-card h-100 d-flex flex-column">
                    <div className="book-card-image-wrap">
                      <img
                        src={`http://localhost:5000/uploads/${product.pimg}`}
                        alt={product.pname}
                        className="book-card-img"
                        onError={(e) => {
                          e.target.src = book1;
                        }}
                      />
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
      </section>

      <section className="about-section py-5 bg-surface">
        <div className="container py-3">
          <div className="row align-items-center g-5">
            <div className="col-12 col-lg-6">
              <div className="about-text-wrapper pe-lg-4">
                <h2 className="about-title">About GameKart</h2>
                <p className="about-paragraph">
                  Welcome to GameKart, your premier gaming ecommerce hub built for
                  casual players, hardcore gamers, and esports enthusiasts alike.
                  We deliver cutting-edge gaming hardware, wireless controllers,
                  VR headsets, and trending game editions directly to your door.
                </p>
                <p className="about-paragraph">
                  Our mission is to elevate your setup with authentic gaming gear,
                  unbeatable prices, rapid delivery, and 24/7 dedicated support.
                  Every product is curated to ensure peak performance and minimal latency.
                </p>
                <p className="about-paragraph highlight-text">
                  At GameKart, we power your passion for play and help you conquer
                  every virtual arena.
                </p>
              </div>
            </div>

            <div className="col-12 col-lg-6 text-center">
              <div className="about-image-wrapper">
                <img src={book1} alt="About GameKart" className="about-img" />
              </div>
            </div>
          </div>
        </div>
      </section>

      <Footer />
    </>
  );
};

export default Home;
