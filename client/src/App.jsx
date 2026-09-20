import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Home from "./Pages/Home";
import "./theme.css";
import "./style.css";
import ProductPage from "./Pages/Product";
import Signup from "./Pages/Signup";
import Login from "./Pages/Login";
import ProdDetails from "./Pages/ProdDetails";
import Orders from "./Pages/Orders";
import Cart from "./Pages/Cart";
function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/Product" element={<ProductPage />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          <Route path="/cart" element={<Cart />} />
          <Route path="/orders" element={<Orders />} />
          <Route path="/prodDetail/:id" element={<ProdDetails />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
