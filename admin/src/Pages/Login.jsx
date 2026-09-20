import React, { useEffect } from "react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch("http://localhost:5000/login", {
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
      navigate("/");
    } else {
      alert("invalid emailid or password");
    }
  };

  useEffect(() => {
    const id = localStorage.getItem("id");
    if (id) {
      // If user is already logged in, redirect to dashboard
      navigate("/");
    }
  });
  return (
    <main className="login-page">
      <div className="container">
        <form onSubmit={handleSubmit} className="login-card">
          <p className="admin-kicker">Admin Access</p>
          <h2 className="mb-2">Login Here</h2>
          <p className="text-muted mb-4">
            Sign in to manage the GameKart admin dashboard.
          </p>
          <div className="mb-3">
            <label htmlFor="email" className="form-label">
              Enter Email
            </label>
            <input
              type="email"
              placeholder="Email"
              name="email"
              className="form-control"
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div className="mb-4">
            <label htmlFor="password" className="form-label">
              Enter Password
            </label>
            <input
              type="password"
              placeholder="Password"
              name="password"
              className="form-control"
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>

          <button type="submit" className="btn btn-primary rounded-3 w-100">
            Login
          </button>
        </form>
      </div>
    </main>
  );
};

export default Login;
