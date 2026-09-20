import React from "react";

const Sidebar = () => {
  return (
    <div className="content flex-grow-1">
      <nav className="navbar admin-header">
        <button className="btn btn-soft btn-sm" id="menu-toggle" type="button">
          <i className="fa-solid fa-bars"></i>
        </button>
        <span className="navbar-brand mb-0">GameKart</span>
      </nav>
    </div>
  );
};

export default Sidebar;
