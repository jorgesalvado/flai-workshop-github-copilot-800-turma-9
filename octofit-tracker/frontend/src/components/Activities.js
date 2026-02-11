import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchActivities = async () => {
      const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
      console.log('Activities - Fetching from:', apiUrl);
      
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Activities - Fetched data:', data);
        
        // Handle both paginated (.results) and plain array responses
        const activitiesData = data.results || data;
        setActivities(Array.isArray(activitiesData) ? activitiesData : []);
        setLoading(false);
      } catch (err) {
        console.error('Activities - Error fetching data:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchActivities();
  }, []);

  if (loading) {
    return (
      <div className="container mt-5">
        <div className="loading-spinner">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
          <p className="mt-3" style={{fontSize: '1.5rem'}}>🏃‍♀️ Buscando suas aventuras fitness... 💪</p>
        </div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-5">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">😱 Ops! Algo deu errado!</h4>
          <p>{error}</p>
          <p className="mb-0">💡 Tente dar um refresh... As atividades estão se escondendo!</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <h2 className="mb-4">📊 Suas Atividades Épicas! 🎯</h2>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th>🎭 Tipo de Atividade</th>
              <th>⏱️ Duração (min)</th>
              <th>🔥 Calorias</th>
              <th>👤 Guerreiro(a)</th>
              <th>📅 Data</th>
            </tr>
          </thead>
          <tbody>
            {activities.length > 0 ? (
              activities.map((activity) => (
                <tr key={activity.id}>
                  <td>
                    <span className="badge bg-primary emoji-float">{activity.activity_type}</span>
                  </td>
                  <td>{activity.duration} min</td>
                  <td><strong>{activity.calories}</strong> 🔥</td>
                  <td>💪 {activity.user_name || activity.user}</td>
                  <td>{new Date(activity.date).toLocaleDateString()}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="5" className="text-center py-4">
                  <h3>🦥</h3>
                  <em>Nenhuma atividade por aqui... Ainda! 😴</em>
                  <p className="mt-2 mb-0">💭 Que tal sair do sofá e criar sua primeira aventura?</p>
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
      <div className="mt-3">
        <strong>🏆 Total de Atividades: {activities.length}</strong>
        {activities.length > 0 && <span className="ms-2">👏 Você é incrível!</span>}
      </div>
    </div>
  );
};

export default Activities;
