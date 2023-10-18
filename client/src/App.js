import React from 'react'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css'
import NavBar from './components/NavBar'
import Home from './pages/Home'
import Menu from './pages/Menu'
import Shop from './pages/Shop'
import Events from './pages/Events'
import Footer from './components/Footer'

function App() {
  return (
    <div>
      <NavBar />
      <BrowserRouter>
        <Routes>
          <Route index element={<Home />} />
          <Route path='/home' element={<Home />} />
          <Route path='/menus' element={<Menu />} />
          <Route path='/shop' element={<Shop />} />
          <Route path='/events' element={<Events />} />
        </Routes>
      </BrowserRouter>
      <Footer />
    </div>
    
  );
}

export default App;
