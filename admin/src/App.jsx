import "bootstrap/dist/css/bootstrap.min.css";
import './theme.css'
import './App.css'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Product from './Pages/Product';
import Orders from './Pages/Orders';
import Users from './Pages/Users';
import Login from './Pages/Login';

function App() {
  
  return (
    <>
      <BrowserRouter>
      {/* <Navbar/> */}
      
        <Routes>
          {/* <Route path="/" element={<Home />} />
          <Route path="/contact" element={<Contact />} /> */}
          <Route path="/" element={<Product />} />
          <Route path="/orders" element={<Orders />} />
          <Route path="/users" element={<Users />} />
          <Route path="/login" element={<Login />} />
          {/* <Route path="/signup" element={<Signup />} /> */}
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
