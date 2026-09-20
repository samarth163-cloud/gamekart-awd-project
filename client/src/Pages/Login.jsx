import React, { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch("http://localhost:4000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    if (response.ok) {
      const data = await response.json();
      console.log(data);
      alert("Login successful");
      localStorage.setItem("id", data.id);
      navigate("/Product");
    } else {
      alert("Invalid email or password");
    }
  };

  useEffect(() => {
    const id = localStorage.getItem("id");
    if (id) {
      navigate("/Product");
    }
  }, []);

  return (
    <main className="auth-page page-shell">
      <div className="container">
        <div className="row justify-content-center">
          <div className="col-12 col-sm-10 col-md-8 col-lg-5">
            <div className="auth-card p-4 p-sm-5">
              <div className="text-center mb-4">
                <p className="section-kicker mb-2">Welcome Back</p>
                <h2 className="mb-2 fw-bold">Sign In</h2>
                <p className="text-muted small mb-0">
                  Login to manage your gaming orders and wishlist.
                </p>
              </div>
              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <label htmlFor="email" className="form-label">
                    Email Address
                  </label>
                  <input
                    type="email"
                    name="email"
                    className="form-control form-control-lg fs-6"
                    id="email"
                    placeholder="name@example.com"
                    onChange={(e) => setEmail(e.target.value)}
                    required
                  />
                </div>
                <div className="mb-4">
                  <label htmlFor="password" className="form-label">
                    Password
                  </label>
                  <input
                    type="password"
                    name="password"
                    className="form-control form-control-lg fs-6"
                    id="password"
                    placeholder="Enter password"
                    onChange={(e) => setPassword(e.target.value)}
                    required
                  />
                </div>

                <button type="submit" className="btn btn-primary btn-lg w-100 rounded-3 fs-6 fw-semibold py-2">
                  Sign In
                </button>
                <p className="text-center mt-4 mb-0 text-muted small">
                  Don't have an account?{" "}
                  <Link to="/signup" className="text-primary text-decoration-none fw-semibold">
                    Sign up here
                  </Link>
                </p>
              </form>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
};

export default Login;
