import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
      console.log('Leaderboard - Fetching from:', apiUrl);
      
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Leaderboard - Fetched data:', data);
        
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      } catch (err) {
        console.error('Leaderboard - Error fetching data:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, []);

  if (loading) {
    return (
      <div className="container mt-5">
        <div className="loading-spinner">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
          <p className="mt-3" style={{fontSize: '1.5rem'}}>🏆 Calculando quem é o mestre fitness... ⚡</p>
        </div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-5">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">😵 Houston, temos um problema!</h4>
          <p>{error}</p>
          <p className="mb-0">🎲 Os rankings estão jogando esconde-esconde!</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <h2 className="mb-4">🏆 Placar dos Campeões! 🎖️</h2>
      <p className="lead mb-4">🔥 Quem mandou ver nos treinos? Vamos descobrir! 💪</p>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>🎯 Posição</th>
              <th>🦸 Atleta</th>
              <th>⭐ Pontos</th>
              <th>📊 Atividades</th>
            </tr>
          </thead>
          <tbody>
            {leaderboard.length > 0 ? (
              leaderboard.map((entry, index) => (
                <tr key={entry.id || index} style={{fontSize: index < 3 ? '1.1rem' : '1rem'}}>
                  <td>
                    {index === 0 && <span className="badge bg-warning text-dark" style={{fontSize: '1.2rem'}}>🥇 #1 LENDA!</span>}
                    {index === 1 && <span className="badge bg-secondary" style={{fontSize: '1.1rem'}}>🥈 #2 FERA!</span>}
                    {index === 2 && <span className="badge" style={{backgroundColor: '#CD7F32', fontSize: '1.1rem'}}>🥉 #3 BRABO!</span>}
                    {index > 2 && <span className="badge bg-light text-dark">#{index + 1}</span>}
                  </td>
                  <td><strong>{entry.user_name || entry.user}</strong> {index === 0 && '👑'}</td>
                  <td><span className="badge bg-success" style={{fontSize: '1rem'}}>{entry.total_points || entry.points || 0} 🌟</span></td>
                  <td>{entry.activity_count || entry.activities || 0} 💪</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="4" className="text-center py-4">
                  <h3>🏜️</h3>
                  <em>Placar vazio... Por enquanto! 😏</em>
                  <p className="mt-2 mb-0">🎯 Seja o primeiro a dominar o ranking!</p>
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
      {leaderboard.length > 0 && (
        <div className="mt-4 text-center">
          <p className="lead">🎊 Parabéns a todos os atletas! Continue arrasando! 💥</p>
        </div>
      )}
    </div>
  );
};

export default Leaderboard;
