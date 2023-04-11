import { useState } from "react";
import products from "../data/teknosa.json";
import ProductList from "./ProductList";

const filter = {
  border: "1px solid #ccc",
  borderRadius: "4px",
  padding: "10px",
  marginBottom: "20px",
  height: "150px",
  overflowY: "scroll",
  width: "200px",
  fontSize: "16px",
};

const btnStyle = {
  border: "1px solid #007bff",
  borderRadius: "5px",
  backgroundColor: "#007bff",
  color: "white",
  padding: "5px",
  marginBottom: "10px",
  cursor: "pointer",
  transition: "background-color 0.3s ease-in-out",
};

const Filter = () => {
  const [brandFilters, setBrandFilters] = useState([]);
  const [ramFilters, setRamFilters] = useState([]);
  const [hddFilters, setHddFilters] = useState([]);
  const [ssdFilters, setSsdFilters] = useState([]);
  const [cpuFilters, setCpuFilters] = useState([]);
  const [screenFilters, setScreenFilters] = useState([]);
  const [isPriceSortedAsc, setIsPriceSortedAsc] = useState(true);

  const handleBrandChange = (event) => {
    const brand = event.target.value;
    const checked = event.target.checked;

    if (checked) {
      setBrandFilters([...brandFilters, brand]);
    } else {
      setBrandFilters(brandFilters.filter((b) => b !== brand));
    }
  };

  const handleRamChange = (event) => {
    const ram = event.target.value;
    const checked = event.target.checked;

    if (checked) {
      setRamFilters([...ramFilters, ram]);
    } else {
      setRamFilters(ramFilters.filter((r) => r !== ram));
    }
  };

  const handleHddChange = (event) => {
    const hdd = event.target.value;
    const checked = event.target.checked;

    if (checked) {
      setHddFilters([...hddFilters, hdd]);
    } else {
      setHddFilters(hddFilters.filter((h) => h !== hdd));
    }
  };

  const handleCpuChange = (event) => {
    const cpu = event.target.value;
    const checked = event.target.checked;

    if (checked) {
      setCpuFilters([...cpuFilters, cpu]);
    } else {
      setCpuFilters(cpuFilters.filter((c) => c !== cpu));
    }
  };

  const handleSsdChange = (event) => {
    const ssd = event.target.value;
    const checked = event.target.checked;

    if (checked) {
      setSsdFilters([...ssdFilters, ssd]);
    } else {
      setSsdFilters(ssdFilters.filter((h) => h !== ssd));
    }
  };

  const handleScreenChange = (event) => {
    const screen = event.target.value;
    const checked = event.target.checked;

    if (checked) {
      setScreenFilters([...screenFilters, screen]);
    } else {
      setScreenFilters(screenFilters.filter((s) => s !== screen));
    }
  };

  const handlePriceSort = () => {
    setIsPriceSortedAsc(!isPriceSortedAsc);
  };

  const filterProducts = () => {
    let filteredProducts = [...products];
    if (brandFilters.length > 0) {
      filteredProducts = filteredProducts.filter((p) =>
        brandFilters.includes(p.Marka)
      );
    }
    if (ramFilters.length > 0) {
      filteredProducts = filteredProducts.filter((p) =>
        ramFilters.includes(p.Ram)
      );
    }
    if (hddFilters.length > 0) {
      filteredProducts = filteredProducts.filter((p) =>
        hddFilters.includes(p["HDD Kapasitesi"])
      );
    }
    if (cpuFilters.length > 0) {
      filteredProducts = filteredProducts.filter((p) =>
        cpuFilters.includes(p["İşlemci"])
      );
    }
    if (ssdFilters.length > 0) {
      filteredProducts = filteredProducts.filter((p) =>
        ssdFilters.includes(p["SSD Kapasitesi"])
      );
    }
    if (screenFilters.length > 0) {
      filteredProducts = filteredProducts.filter((p) =>
        screenFilters.includes(p["Ekran Boyutu"])
      );
    }
    if (isPriceSortedAsc) {
      filteredProducts.sort((a, b) => a.Fiyat - b.Fiyat);
    } else {
      filteredProducts.sort((a, b) => b.Fiyat - a.Fiyat);
    }
    return filteredProducts;
  };

  const filteredProducts = filterProducts();

  return (
    <div style={{ display: "flex", flexDirection: "row" }}>
      <div style={{ marginLeft: "20px" }}>
        {isPriceSortedAsc ? (
          <button style={btnStyle} onClick={handlePriceSort}>
            Azalan Fiyat Sıralaması
          </button>
        ) : (
          <button style={btnStyle} onClick={handlePriceSort}>
            Artan Fiyat Sıralaması
          </button>
        )}
        <div style={filter}>
          <h3 style={{ fontWeight: "bold" }}>Marka</h3>
          {Array.from(new Set(products.map((p) => p.Marka))).map((brand) => (
            <div key={brand}>
              <label>
                <input
                  type="checkbox"
                  value={brand}
                  onChange={handleBrandChange}
                  checked={brandFilters.includes(brand)}
                />
                {brand}
              </label>
            </div>
          ))}
        </div>
        <div style={filter}>
          <h3 style={{ fontWeight: "bold" }}>Ram</h3>
          {Array.from(new Set(products.map((p) => p.Ram))).map((ram) => (
            <div key={ram}>
              <label>
                <input
                  type="checkbox"
                  value={ram}
                  onChange={handleRamChange}
                  checked={ramFilters.includes(ram)}
                />
                {ram}
              </label>
            </div>
          ))}
        </div>

        <div style={filter}>
          <h3 style={{ fontWeight: "bold" }}>İşlemci</h3>
          {Array.from(new Set(products.map((p) => p["İşlemci"]))).map((cpu) => (
            <div key={cpu}>
              <label>
                <input
                  type="checkbox"
                  value={cpu}
                  onChange={handleCpuChange}
                  checked={cpuFilters.includes(cpu)}
                />
                {cpu}
              </label>
            </div>
          ))}
        </div>

        <div style={filter}>
          <h3 style={{ fontWeight: "bold" }}>HDD Kapasitesi</h3>
          {Array.from(new Set(products.map((p) => p["HDD Kapasitesi"]))).map(
            (hdd) => (
              <div key={hdd}>
                <label>
                  <input
                    type="checkbox"
                    value={hdd}
                    onChange={handleHddChange}
                    checked={hddFilters.includes(hdd)}
                  />
                  {hdd}
                </label>
              </div>
            )
          )}
        </div>
        <div style={filter}>
          <h3 style={{ fontWeight: "bold" }}>SSD Kapasitesi</h3>
          {Array.from(new Set(products.map((p) => p["SSD Kapasitesi"]))).map(
            (ssd) => (
              <div key={ssd}>
                <label>
                  <input
                    type="checkbox"
                    value={ssd}
                    onChange={handleSsdChange}
                    checked={ssdFilters.includes(ssd)}
                  />
                  {ssd}
                </label>
              </div>
            )
          )}
        </div>
        <div style={filter}>
          <h3 style={{ fontWeight: "bold" }}>Ekran Boyutu</h3>
          {Array.from(new Set(products.map((p) => p["Ekran Boyutu"]))).map(
            (screen) => (
              <div key={screen}>
                <label>
                  <input
                    type="checkbox"
                    value={screen}
                    onChange={handleScreenChange}
                    checked={screenFilters.includes(screen)}
                  />
                  {screen}
                </label>
              </div>
            )
          )}
        </div>
      </div>
      <ProductList products={filteredProducts} />
    </div>
  );
};

export default Filter;
