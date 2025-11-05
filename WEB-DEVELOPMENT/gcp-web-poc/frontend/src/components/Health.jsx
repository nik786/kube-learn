import React, { useEffect, useState } from 'react';
import { getHealth } from '../api';

export default function Health() {
  const [status, setStatus] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const checkHealth = async () => {
      try {
        setLoading(true);
        const data = await getHealth();
        setStatus(data);
        setError('');
      } catch (err) {
        setError('Failed to connect to backend');
        setStatus(null);
      } finally {
        setLoading(false);
      }
    };

    checkHealth();
    
    // Refresh health check every 5 seconds
    const interval = setInterval(checkHealth, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h2>Health Check</h2>
      
      {loading ? (
        <p>Checking backend health...</p>
      ) : error ? (
        <div style={{ padding: '10px', backgroundColor: '#fee', border: '1px solid #fcc', borderRadius: '4px' }}>
          <p style={{ color: '#c33', margin: 0 }}>❌ {error}</p>
        </div>
      ) : (
        <div style={{ padding: '10px', backgroundColor: '#efe', border: '1px solid #cfc', borderRadius: '4px' }}>
          <p style={{ color: '#3c3', margin: 0 }}>✅ Backend is healthy!</p>
          {status && (
            <pre style={{ marginTop: '10px', fontSize: '14px' }}>
              {JSON.stringify(status, null, 2)}
            </pre>
          )}
        </div>
      )}
    </div>
  );
}

