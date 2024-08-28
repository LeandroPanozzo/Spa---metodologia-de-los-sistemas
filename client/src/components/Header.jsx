import { Link } from "react-router-dom";
import './Header.css'; // Asegúrate de crear y enlazar un archivo CSS
import { useAuth } from './AuthContext'; // Importa el hook de autenticación

export function Header() {
  const { isAuthenticated, logout } = useAuth(); // Obtén el estado y la función de logout

  return (
    <header className="header">
      <nav className="nav">
        <div className="nav-left">
          <div className="logo">
            <img src="/path/to/logo.png" alt="Logo" /> {/* Reemplaza con la ruta a tu logo */}
          </div>
          <div className="links">
            <Link to="/">Home</Link>
            <Link to="/about">About</Link>
          </div>
        </div>
        <div className="nav-right">
          {isAuthenticated ? (
            <>
              <button onClick={logout}>Cerrar sesión</button>
              <Link to="/contact">Consultar</Link>
            </>
          ) : (
            <>
              <Link to="/login">Iniciar sesión</Link>
              <Link to="/register">Registrarse</Link>
            </>
          )}
        </div>
      </nav>
    </header>
  );
}
