import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useAuth } from '../components/AuthContext';
import { useNavigate } from 'react-router-dom';

export function QueryAndResponseComponent() {
  const [queries, setQueries] = useState([]);
  const [newQuery, setNewQuery] = useState({ title: '', content: '' });
  const [newResponse, setNewResponse] = useState({ content: '', queryId: null });
  const [error, setError] = useState('');
  const { isAuthenticated, logout } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (!isAuthenticated) {
      navigate('/login');
    } else {
      fetchQueries();
    }
  }, [isAuthenticated, navigate]);

  axios.interceptors.request.use(
    (config) => {
      const token = localStorage.getItem('access_token');
      if (token) {
        config.headers['Authorization'] = `Bearer ${token}`;
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );

  axios.interceptors.response.use(
    (response) => response,
    async (error) => {
      const originalRequest = error.config;
      if (error.response.status === 401 && !originalRequest._retry) {
        originalRequest._retry = true;
        try {
          const refreshToken = localStorage.getItem('refresh_token');
          const response = await axios.post('http://localhost:8000/sentirseBien/api/v1/token/refresh/', { refresh: refreshToken });
          localStorage.setItem('access_token', response.data.access);
          axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
          return axios(originalRequest);
        } catch (refreshError) {
          logout();
          return Promise.reject(refreshError);
        }
      }
      return Promise.reject(error);
    }
  );

  const fetchQueries = async () => {
    try {
      const response = await axios.get('http://localhost:8000/sentirseBien/api/v1/queries/');
      setQueries(response.data);
    } catch (error) {
      setError('Error al cargar las consultas');
    }
  };

  const handleNewQuerySubmit = async (event) => {
    event.preventDefault();
    try {
      await axios.post('http://localhost:8000/sentirseBien/api/v1/queries/', newQuery);
      setNewQuery({ title: '', content: '' });
      fetchQueries();
    } catch (error) {
      setError('Error al crear la consulta');
    }
  };

  const handleNewResponseSubmit = async (event) => {
    event.preventDefault();
    try {
      await axios.post('http://localhost:8000/sentirseBien/api/v1/responses/', newResponse);
      setNewResponse({ content: '', queryId: null });
      fetchQueries();
    } catch (error) {
      setError('Error al crear la respuesta');
    }
  };

  if (!isAuthenticated) {
    return <p>Por favor, inicia sesión para ver y crear consultas.</p>;
  }

  return (
    <div style={styles.container}>
      <h2>Consultas y Respuestas</h2>
      
      {/* Formulario para nueva consulta */}
      <form onSubmit={handleNewQuerySubmit} style={styles.form}>
        <h3>Nueva Consulta</h3>
        <input
          type="text"
          value={newQuery.title}
          onChange={(e) => setNewQuery({...newQuery, title: e.target.value})}
          placeholder="Título de la consulta"
          style={styles.input}
          required
        />
        <textarea
          value={newQuery.content}
          onChange={(e) => setNewQuery({...newQuery, content: e.target.value})}
          placeholder="Contenido de la consulta"
          style={styles.textarea}
          required
        />
        <button type="submit" style={styles.button}>Crear Consulta</button>
      </form>

      {/* Lista de consultas */}
      <div style={styles.queryList}>
        <h3>Consultas Existentes</h3>
        {queries.map((query) => (
          <div key={query.id} style={styles.query}>
            <h4>{query.title}</h4>
            <p style={styles.author}>Por: {query.user.username}</p>
            <p>{query.content}</p>
            
            {/* Respuestas */}
            <div style={styles.responses}>
              <h5>Respuestas:</h5>
              {query.responses.map((response) => (
                <div key={response.id} style={styles.response}>
                  <p>{response.content}</p>
                  <p style={styles.responseAuthor}>Respondido por: {response.user.username}</p>
                </div>
              ))}
            </div>

            {/* Formulario para nueva respuesta */}
            <form onSubmit={handleNewResponseSubmit} style={styles.form}>
              <textarea
                value={newResponse.queryId === query.id ? newResponse.content : ''}
                onChange={(e) => setNewResponse({content: e.target.value, queryId: query.id})}
                placeholder="Tu respuesta"
                style={styles.textarea}
                required
              />
              <button type="submit" style={styles.button}>Responder</button>
            </form>
          </div>
        ))}
      </div>

      {error && <p style={styles.errorText}>{error}</p>}
    </div>
  );
}

const styles = {
  container: {
    maxWidth: '800px',
    margin: '0 auto',
    padding: '20px',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
    marginBottom: '20px',
  },
  input: {
    marginBottom: '10px',
    padding: '8px',
    borderRadius: '4px',
    border: '1px solid #ccc',
  },
  textarea: {
    marginBottom: '10px',
    padding: '8px',
    borderRadius: '4px',
    border: '1px solid #ccc',
    minHeight: '100px',
  },
  button: {
    padding: '10px',
    borderRadius: '4px',
    border: 'none',
    backgroundColor: '#28a745',
    color: '#fff',
    cursor: 'pointer',
  },
  queryList: {
    marginTop: '20px',
  },
  query: {
    marginBottom: '20px',
    padding: '15px',
    border: '1px solid #ddd',
    borderRadius: '4px',
  },
  responses: {
    marginTop: '10px',
    paddingLeft: '20px',
  },
  errorText: {
    color: 'red',
  },
  author: {
    fontSize: '0.9em',
    color: '#666',
    marginBottom: '10px',
  },
  response: {
    marginBottom: '10px',
    padding: '10px',
    backgroundColor: '#f0f0f0',
    borderRadius: '4px',
  },
  responseAuthor: {
    fontSize: '0.8em',
    color: '#666',
    marginTop: '5px',
  },
};