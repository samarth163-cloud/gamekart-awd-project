import React from "react";
import Navbar from "../Component/Navbar";
import Footer from "../Component/Footer";
import contactbg from "../assets/contactbg.webp";

const locations = [
  {
    country: "London",
    address: "425 Broadway, 20th floor pharchard view, London",
    phone: "+91 123 456 7890",
    email: "support@store.com",
    flag: "https://atleto-demo1.myshopify.com/cdn/shop/files/London_cf52e309-3541-4178-8d87-ca4432d2693b.jpg?v=1749192812",
  },
  {
    country: "France",
    address: "27 Eden walk eden centre orchard view, Paris, France",
    phone: "+91 123 456 7890",
    email: "support@store.com",
    flag: "https://atleto-demo1.myshopify.com/cdn/shop/files/France_b4257e2c-fc8b-47be-a42c-297cf2009cd0.jpg?v=1749192812",
  },
  {
    country: "Canada",
    address: "523 North stockport road bridge, Toronto, Canada",
    phone: "+91 123 456 7890",
    email: "support@store.com",
    flag: "https://atleto-demo1.myshopify.com/cdn/shop/files/Canada_c157d3e1-4923-4e51-9a13-f8827c097e18.jpg?v=1749192812",
  },
  {
    country: "England",
    address: "048 Holburn street 20th floor camberley, England",
    phone: "+91 123 456 7890",
    email: "support@store.com",
    flag: "https://atleto-demo1.myshopify.com/cdn/shop/files/England_037d3fea-f508-4938-8dcf-e0eef2625ddf.jpg?v=1749192812",
  },
];

const Contact = () => {
  return (
    <>
      <Navbar />
      <section
        className="contact-hero py-5 text-center text-white d-flex align-items-center"
        style={{ backgroundImage: `url(${contactbg})` }}
      >
        <div className="container">
          <div className="text-center mb-5">
            <p className="section-kicker">Contact Us</p>
            <h1 className="section-title text-white">Get in Touch</h1>
            <p className="text-white-50 mb-0">Find us across the globe</p>
          </div>

          <div className="row g-4">
            {locations.map((loc, index) => (
              <div className="col-12 col-md-6 col-lg-3" key={index}>
                <div className="contact-card text-center shadow-sm p-3 h-100">
                  <img
                    src={loc.flag}
                    alt={loc.country}
                    className="mx-auto mb-3 rounded"
                    width="72"
                    height="44"
                  />
                  <p className="mb-3 text-muted">{loc.address}</p>
                  <a href={`tel:${loc.phone}`} className="d-block text-decoration-none text-primary">
                    {loc.phone}
                  </a>
                  <a href={`mailto:${loc.email}`} className="d-block text-decoration-none text-secondary">
                    {loc.email}
                  </a>
                  <h6 className="fw-bold mt-3 mb-0">{loc.country}</h6>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>
      <section className="py-5" id="contact">
        <div className="container">
          <div className="contact-form-card p-4 p-md-5">
            <div className="text-center mb-5">
              <p className="section-kicker mb-2">Message</p>
              <h2 className="fw-bold">Keep in Touch with Us</h2>
              <p className="text-muted">
                Have questions? Fill out the form below and we'll get back to you.
              </p>
            </div>

            <form>
              <div className="row g-3">
                <div className="col-md-6">
                  <label htmlFor="name" className="form-label">
                    Your Full Name
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    id="name"
                    placeholder="Enter your full name"
                    required
                  />
                </div>

                <div className="col-md-6">
                  <label htmlFor="email" className="form-label">
                    Your Email Address
                  </label>
                  <input
                    type="email"
                    className="form-control"
                    id="email"
                    placeholder="Enter your email"
                    required
                  />
                </div>

                <div className="col-md-6">
                  <label htmlFor="phone" className="form-label">
                    Your Mobile Number
                  </label>
                  <input
                    type="text"
                    className="form-control"
                    id="phone"
                    placeholder="Enter your mobile number"
                    required
                  />
                </div>

                <div className="col-md-6">
                  <label htmlFor="message" className="form-label">
                    Your Message
                  </label>
                  <textarea
                    className="form-control"
                    id="message"
                    rows="3"
                    placeholder="Write your message here..."
                    required
                  ></textarea>
                </div>

                <div className="col-12">
                  <div className="form-check">
                    <input
                      className="form-check-input"
                      type="checkbox"
                      id="terms"
                      required
                    />
                    <label className="form-check-label" htmlFor="terms">
                      I accept the terms & conditions and agree with the privacy
                      policy.
                    </label>
                  </div>
                </div>

                <div className="col-12 text-center">
                  <button type="submit" className="btn btn-primary rounded-3 px-4">
                    Send Message
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </section>
      <Footer />
    </>
  );
};

export default Contact;
