import React from "react";

function Navbar() {
  const navStyle = {
    background: "#FFFFFF",
    boxShadow: "0px 2px 4px rgba(0, 0, 0, 0.1)",
    padding: "20px",
    marginBottom: "20px",
  };

  const ulStyle = {
    display: "flex",
    alignItems: "center",
    listStyle: "none",
    margin: 0,
    padding: 0,
  };

  const linkStyle = {
    color: "#333333",
    fontSize: "18px",
    fontWeight: 500,
    textDecoration: "none",
    textTransform: "uppercase",
    padding: "10px",
    transition: "color 0.2s ease-in-out",
  };

  const searchStyle = {
    background: "#F6F6F6",
    border: "none",
    borderRadius: "8px",
    color: "#333333",
    fontSize: "16px",
    padding: "10px",
    width: "200px",
    marginLeft: "150px",
  };

  const buttonStyle = {
    marginLeft: "10px",
    background: "#0070F3",
    border: "none",
    borderRadius: "8px",
    color: "#FFFFFF",
    cursor: "pointer",
    fontSize: "16px",
    padding: "10px",
    transition: "background 0.2s ease-in-out",
  };

  return (
    <nav style={navStyle}>
      <ul style={ulStyle}>
        <li>
          <a href="/" style={linkStyle}>
            Ürünler
          </a>
        </li>

        <li>
          <form style={{ display: "flex", alignItems: "center" }}>
            <input type="text" placeholder="Arama" style={searchStyle} />
            <button type="submit" style={buttonStyle}>
              Ara
            </button>
          </form>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
