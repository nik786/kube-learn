
// Use empty string for relative URLs - routed by Traefik proxy
// Docker: Traefik routes /api/* to backend:8080
// Local dev: Uses localhost:8080 via package.json proxy or Express proxy

export const getHealth = async () => {
  try {
    const response = await fetch('/api/fleet-app/v1/health-check');
    if (!response.ok) throw new Error('Health check failed');
    return await response.json();
  } catch (err) {
    console.error('API Error:', err);
    throw err;
  }
};

export const getProducts = async () => {
  try {
    // Use relative path which will be routed by Traefik to backend
    const response = await fetch('/api/fleet-app/v1/products');
    if (!response.ok) throw new Error('Failed to fetch products');
    return await response.json();
  } catch (err) {
    console.error('API Error:', err);
    return [];
  }
};
