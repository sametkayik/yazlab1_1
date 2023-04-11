import React, { useState, useEffect } from "react";

function ProductList(props) {
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const products = props.products;
  const pageSize = props.pageSize || 5;

  const productStyle = {
    display: "flex",
    alignItems: "center",
    marginBottom: "10px",
    marginLeft: "60px",
    backgroundColor: "white",
    borderRadius: "10px",
    boxShadow: "0px 4px 4px rgba(0, 0, 0, 0.25)",
    padding: "10px",
    height: "140px",
    width: "1000px",
    boxSizing: "border-box",
  };

  const imageStyle = {
    width: "100px",
    height: "90px",
    marginRight: "20px",
  };

  const titleStyle = {
    fontSize: "16px",
    fontWeight: "bold",
    marginBottom: "10px",
  };

  const brandStyle = {
    fontSize: "16px",
    color: "grey",
    marginBottom: "10px",
  };

  const priceStyle = {
    fontSize: "16px",
    fontWeight: "bold",
    color: "green",
    marginBottom: "10px",
  };

  const productListStyle = {
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
  };

  const containerStyle = {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "flex-start",
    marginTop: "20px",
  };

  const btnStyle = {
    border: "1px solid #007bff",
    borderRadius: "5px",
    backgroundColor: "#007bff",
    color: "white",
    padding: "10px 15px",
    margin: "0 5px",
    cursor: "pointer",
    transition: "background-color 0.3s ease-in-out",
  };

  useEffect(() => {
    const newTotalPages = Math.ceil(products.length / pageSize);
    setTotalPages(newTotalPages);
    setCurrentPage(1);
  }, [products, pageSize]);

  const handlePageChange = (newPage) => {
    setCurrentPage(newPage);
  };

  const getPageProducts = () => {
    const startIndex = (currentPage - 1) * pageSize;
    const endIndex = startIndex + pageSize;
    return products.slice(startIndex, endIndex);
  };

  return (
    <div style={{ display: "flex", flexDirection: "column" }}>
      <div>
        <div style={containerStyle}>
          <div style={productListStyle}>
            {getPageProducts().map((product, index) => (
              <a
                key={index}
                href={product["Ürün URL"]}
                target="_blank"
                rel="noreferrer"
              >
                <div key={index} style={productStyle}>
                  <img
                    src={product["Görsel URL"]}
                    alt={product["Başlık"]}
                    style={imageStyle}
                  />
                  <div key={index}>
                    <h2 style={titleStyle}>{product["Başlık"]}</h2>
                    <p style={brandStyle}>Marka: {product["Marka"]}</p>
                    <p style={priceStyle}>Fiyat: {product["Fiyat"]}</p>
                  </div>
                </div>
              </a>
            ))}
          </div>
        </div>
      </div>

      <div style={{ textAlign: "center" }}>
        {currentPage > 1 && (
          <button
            onClick={() => handlePageChange(1)}
            style={btnStyle}
            disabled={currentPage > 1}
          >
            1
          </button>
        )}
        {currentPage > 1 && (
          <button
            onClick={() => handlePageChange(currentPage - 1)}
            style={btnStyle}
          >
            Önceki
          </button>
        )}

        {currentPage < totalPages && (
          <button
            onClick={() => handlePageChange(currentPage + 1)}
            style={btnStyle}
          >
            Sonraki
          </button>
        )}
        {currentPage < totalPages && (
          <button onClick={() => handlePageChange(totalPages)} style={btnStyle}>
            {totalPages}
          </button>
        )}
        <p>
          Sayfa: {currentPage} / {totalPages}
        </p>
      </div>
    </div>
  );
}

export default ProductList;
