import React, { useState, useEffect } from "react";
import Navbar from "../Component/Navbar";

const Users = () => {
  const [users, setUsers] = useState([]);

  const fetchUsers = async () => {
    try {
      const response = await fetch("http://localhost:5000/users");
      if (response.ok) {
        const data = await response.json();
        setUsers(data);
      }
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <Navbar>
      <section className="admin-panel">
        <div className="admin-panel-header">
          <div>
            <p className="admin-kicker">Customers</p>
            <h3 className="admin-panel-title">Manage Users</h3>
            <p className="admin-panel-subtitle">
              View registered users and their profile information.
            </p>
          </div>
          <span className="stat-pill">
            <i className="fa-solid fa-user-group"></i>
            {users.length} Users
          </span>
        </div>
        <div className="admin-panel-body">
          <div className="table-responsive">
            <table className="table table-hover align-middle admin-table">
              <thead>
                <tr>
                  <th>Profile</th>
                  <th>Name</th>
                  <th>Email</th>
                  <th>Gender</th>
                  <th>City</th>
                </tr>
              </thead>
              <tbody>
                {users.length === 0 ? (
                  <tr>
                    <td colSpan="5" className="empty-state">
                      No registered users found.
                    </td>
                  </tr>
                ) : (
                  users.map((user) => (
                    <tr key={user._id}>
                      <td>
                        {user.profile ? (
                          <img
                            src={`http://localhost:4000/uploads/${user.profile}`}
                            alt={user.name}
                            className="profile-thumb"
                          />
                        ) : (
                          <span className="text-muted">No Photo</span>
                        )}
                      </td>
                      <td className="fw-semibold">{user.name}</td>
                      <td>{user.email}</td>
                      <td className="text-capitalize">{user.gender || "-"}</td>
                      <td>{user.city || "-"}</td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </div>
      </section>
    </Navbar>
  );
};

export default Users;
