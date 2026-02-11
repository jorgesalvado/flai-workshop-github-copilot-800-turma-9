import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTeams = async () => {
      const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
      console.log('Teams - Fetching from:', apiUrl);
      
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Teams - Fetched data:', data);
        
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      } catch (err) {
        console.error('Teams - Error fetching data:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchTeams();
  }, []);

  if (loading) {
    return (
      <div className="container mt-5">
        <div className="loading-spinner">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
          <p className="mt-3" style={{fontSize: '1.5rem'}}>🔍 Procurando os melhores times... 🎪</p>
        </div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-5">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">🚨 Alerta! Os times fugiram!</h4>
          <p>{error}</p>
          <p className="mb-0">🕵️ Talvez estejam fazendo exercícios em outro lugar...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <h2 className="mb-4">👥 Times Incríveis! 🎪</h2>
      <p className="lead mb-4">🤝 Junte-se a equipe perfeita e domine os treinos! 💥</p>
      <div className="row">
        {teams.length > 0 ? (
          teams.map((team, index) => (
            <div key={team.id} className="col-md-4 mb-4">
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">
                    {['🦁', '🐯', '🦅', '🐺', '🦊', '🐉'][index % 6]} {team.name}
                  </h5>
                  <p className="card-text">{team.description || '✨ Um time misterioso e incrível!'}</p>
                  <div className="d-flex justify-content-between align-items-center mt-3">
                    <span className="badge bg-info text-dark emoji-float">
                      👥 {team.member_count || team.members?.length || 0} Guerreiros
                    </span>
                    <button className="btn btn-sm btn-outline-primary">🎯 Ver Time</button>
                  </div>
                </div>
                <div className="card-footer text-center" style={{background: 'transparent', border: 'none'}}>
                  <small className="text-muted">💪 Unidos somos mais fortes!</small>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info text-center" role="alert">
              <h3>🏝️</h3>
              <p className="lead">Ninguém criou um time ainda? 😱</p>
              <p className="mb-0">🎨 Seja o pioneiro e forme o time dos sonhos! 🚀</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Teams;
