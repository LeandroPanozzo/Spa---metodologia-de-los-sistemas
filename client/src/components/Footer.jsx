// Footer.jsx
import React from 'react';
import './Footer.css';

export function Footer() {
  return (
    <footer className="footer">
      <div className="footer-content">
        <h2>Serenidad Spa</h2>
        <p>Calle Principal 123, Ciudad</p>
        <p>Teléfono: (123) 456-7890</p>
      </div>
      <div className="footer-buttons">
        <button>Reservar Cita</button>
        <button>Contáctanos</button>
      </div>
    </footer>
  );
}
