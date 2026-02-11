import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUsers = async () => {
      const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;
      console.log('Users - Fetching from:', apiUrl);
      
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Users - Fetched data:', data);
        
        // Handle both paginated (.results) and plain array responses
        const usersData = data.results || data;
        setUsers(Array.isArray(usersData) ? usersData : []);
        setLoading(false);
      } catch (err) {
        console.error('Users - Error fetching data:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  if (loading) {
    return (
      <div className="container mt-5">
        <div className="loading-spinner">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
          <p className="mt-3" style={{fontSize: '1.5rem'}}>👥 Reunindo a galera fitness... 🎉</p>
        </div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-5">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">😅 Eita! Cadê todo mundo?</h4>
          <p>{error}</p>
          <p className="mb-0">🤔 Parece que os usuários foram malhar... Ou bugar o sistema!</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <h2 className="mb-4">👤 Nossos Atletas Fenomenais! 🌟</h2>
      <p className="lead mb-4">🎪 Conheça os heróis que suam a camisa por aqui! 💦</p>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>🦸 Apelido</th>
              <th>📧 Contato</th>
              <th>🏆 Escuderia</th>
              <th>📅 Membro desde</th>
            </tr>
          </thead>
          <tbody>
            {users.length > 0 ? (
              users.map((user, index) => (
                <tr key={user.id}>
                  <td>
                    {['💪', '🔥', '⚡', '🌟', '🎯'][index % 5]} <strong>{user.username}</strong>
                  </td>
                  <td>
                    <a href={`mailto:${user.email}`} className="text-decoration-none">
                      📬 {user.email}
                    </a>
                  </td>
                  <td>
                    {user.team_name || user.team ? (
                      <span className="badge bg-secondary emoji-float">🏅 {user.team_name || user.team}</span>
                    ) : (
                      <span className="badge bg-light text-dark">🦸 Lobo Solitário</span>
                    )}
                  </td>
                  <td>🎂 {user.date_joined ? new Date(user.date_joined).toLocaleDateString() : '🤷 Mistério!'}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="4" className="text-center py-4">
                  <h3>👻</h3>
                  <em>Cadê todo mundo? 😱</em>
                  <p className="mt-2 mb-0">🎭 Parece um app fantasma! Convide seus amigos!</p>
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
      <div className="mt-3">
        <strong>🎊 Total de Atletas: {users.length}</strong>
        {users.length > 10 && <span className="ms-2">🔥 Estamos crescendo!</span>}
        {users.length > 50 && <span className="ms-2">🚀 VIRALIMOS!</span>}
      </div>
    </div>
  );
};

export default Users;
