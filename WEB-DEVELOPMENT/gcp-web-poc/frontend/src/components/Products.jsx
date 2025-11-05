import React, { useEffect, useState } from 'react';
import { getProducts } from '../api';

export default function Products() {
  const [products, setProducts] = useState([]);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        setLoading(true);
        const data = await getProducts();
        if (data.length === 0) {
          setError('No products found');
        } else {
          setProducts(data);
          setError('');
        }
      } catch (err) {
        setError('Failed to fetch products');
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h2>Products</h2>

      {loading ? (
        <p>Loading products...</p>
      ) : error ? (
        <p style={{ color: '#c33' }}>❌ {error}</p>
      ) : products.length === 0 ? (
        <p>No products available</p>
      ) : (
        <ul style={{ listStyleType: 'none', padding: 0 }}>
          {products.map((p) => (
            <li 
              key={p.id}
              style={{
                padding: '15px',
                margin: '10px 0',
                border: '1px solid #ddd',
                borderRadius: '8px',
                backgroundColor: '#f9f9f9'
              }}
            >
              <strong style={{ fontSize: '18px' }}>{p.name}</strong>
              <div style={{ color: '#666', marginTop: '5px' }}>
                ₹{p.price.toLocaleString()}
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

