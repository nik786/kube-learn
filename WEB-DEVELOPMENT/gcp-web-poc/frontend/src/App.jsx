import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import Health from './components/Health';
import Products from './components/Products';

export default function App() {
  return (
    <Router>
      <div style={{ minHeight: '100vh' }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/fleet-app/v1/health-check" element={<Health />} />
          <Route path="/fleet-app/v1/products" element={<Products />} />
        </Routes>
      </div>
    </Router>
  );
}
