import React from "react";
import { Link, useNavigate } from "react-router-dom";

const Signup = () => {
  const [formData, setFormData] = React.useState({});
  const navigate = useNavigate();
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };
  const handleChangeImg = (e) => {
    setFormData({ ...formData, profile: e.target.files[0] });
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    const formDataToSend = new FormData();
    formDataToSend.append("name", formData.name);
    formDataToSend.append("email", formData.email);
    formDataToSend.append("password", formData.password);
    formDataToSend.append("gender", formData.gender);
    formDataToSend.append("city", formData.city);
    formDataToSend.append("profile", formData.profile);
    try {
      const response = await fetch("http://localhost:4000/signup", {
        method: "POST",
        body: formDataToSend,
      });

      if (response.ok) {
        alert("User registered successfully");
        navigate("/login");
      } else {
        alert("Failed to register user");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred");
    } finally {
      setFormData({
        name: "",
        email: "",
        password: "",
        gender: "",
        city: "",
        profile: null,
      });
      if (document.getElementById("profile")) {
        document.getElementById("profile").value = "";
      }
    }
  };
  return (
    <main className="auth-page page-shell">
      <div className="container">
        <div className="row justify-content-center">
          <div className="col-12 col-sm-10 col-md-8 col-lg-6">
            <div className="auth-card p-4 p-sm-5">
              <div className="text-center mb-4">
                <p className="section-kicker mb-2">Join The Squad</p>
                <h2 className="mb-2 fw-bold">Create Account</h2>
                <p className="text-muted small mb-0">
                  Join GameKart and gear up with exclusive deals.
                </p>
              </div>
              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <label htmlFor="name" className="form-label">
                    Full Name
                  </label>
                  <input
                    type="text"
                    onChange={(e) => handleChange(e)}
                    name="name"
                    className="form-control"
                    id="name"
                    placeholder="Enter your name"
                    required
                  />
                </div>
                <div className="mb-3">
                  <label htmlFor="email" className="form-label">
                    Email Address
                  </label>
                  <input
                    type="email"
                    onChange={(e) => handleChange(e)}
                    name="email"
                    className="form-control"
                    id="email"
                    placeholder="name@example.com"
                    required
                  />
                </div>
                <div className="mb-3">
                  <label htmlFor="password" className="form-label">
                    Password
                  </label>
                  <input
                    type="password"
                    name="password"
                    onChange={(e) => handleChange(e)}
                    className="form-control"
                    id="password"
                    placeholder="Create a strong password"
                    required
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label d-block">Gender</label>
                  <div className="d-flex gap-4">
                    <div className="form-check">
                      <input
                        type="radio"
                        className="form-check-input"
                        id="male"
                        onChange={(e) => handleChange(e)}
                        name="gender"
                        value="male"
                      />
                      <label className="form-check-label" htmlFor="male">
                        Male
                      </label>
                    </div>
                    <div className="form-check">
                      <input
                        type="radio"
                        className="form-check-input"
                        id="female"
                        onChange={(e) => handleChange(e)}
                        name="gender"
                        value="female"
                      />
                      <label className="form-check-label" htmlFor="female">
                        Female
                      </label>
                    </div>
                  </div>
                </div>
                <div className="mb-3">
                  <label htmlFor="city" className="form-label">
                    City
                  </label>
                  <select
                    name="city"
                    className="form-select"
                    id="city"
                    required
                    onChange={(e) => handleChange(e)}
                  >
                    <option value="">Select City</option>
                    <optgroup label="Gujarat">
                      <option value="Surat">Surat</option>
                      <option value="Vapi">Vapi</option>
                      <option value="Baroda">Baroda</option>
                      <option value="Bharuch">Bharuch</option>
                    </optgroup>
                    <optgroup label="Maharashtra">
                      <option value="Mumbai">Mumbai</option>
                      <option value="Pune">Pune</option>
                      <option value="Nagpur">Nagpur</option>
                    </optgroup>
                  </select>
                </div>
                <div className="mb-4">
                  <label htmlFor="profile" className="form-label">
                    Profile Picture
                  </label>
                  <input
                    type="file"
                    name="profile"
                    onChange={(e) => handleChangeImg(e)}
                    className="form-control"
                    id="profile"
                  />
                </div>
                <button type="submit" className="btn btn-primary btn-lg w-100 rounded-3 fs-6 fw-semibold py-2">
                  Create Account
                </button>
                <p className="text-center mt-4 mb-0 text-muted small">
                  Already have an account?{" "}
                  <Link to="/login" className="text-primary text-decoration-none fw-semibold">
                    Login here
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

export default Signup;
