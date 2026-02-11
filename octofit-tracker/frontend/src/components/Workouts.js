import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
      console.log('Workouts - Fetching from:', apiUrl);
      
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Workouts - Fetched data:', data);
        
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      } catch (err) {
        console.error('Workouts - Error fetching data:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) {
    return (
      <div className="container mt-5">
        <div className="loading-spinner">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
          <p className="mt-3" style={{fontSize: '1.5rem'}}>💪 Preparando treinos insanos... 🏋️</p>
        </div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="container mt-5">
        <div className="alert alert-danger" role="alert">
          <h4 className="alert-heading">🤯 Os treinos deram ghosting!</h4>
          <p>{error}</p>
          <p className="mb-0">🎪 Parece que até os exercícios precisam de um dia de descanso!</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mt-5">
      <h2 className="mb-4">💪 Treinos Épicos! 🏋️</h2>
      <p className="lead mb-4">🎯 Escolha seu destino fitness e prepare-se para suar! 💦</p>
      <div className="row">
        {workouts.length > 0 ? (
          workouts.map((workout, index) => (
            <div key={workout.id} className="col-md-6 mb-4">
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">
                    {['🏃', '🚴', '🏊', '🤸', '🥊', '🧘'][index % 6]} {workout.name}
                  </h5>
                  <p className="card-text">{workout.description || '⚡ Prepare-se para o melhor treino da sua vida!'}</p>
                  <div className="d-flex justify-content-between align-items-center mt-3 flex-wrap">
                    <div>
                      <span className="badge bg-primary me-2 emoji-float">🎯 {workout.category || 'Geral'}</span>
                      <span className="badge bg-secondary">
                        {workout.difficulty === 'Easy' && '😊 Suave'}
                        {workout.difficulty === 'Medium' && '💪 Médio'}
                        {workout.difficulty === 'Hard' && '🔥 Hardcore'}
                        {!workout.difficulty && '💪 Médio'}
                      </span>
                    </div>
                    {workout.duration && (
                      <span className="badge bg-info text-dark mt-2">⏱️ {workout.duration} minutos</span>
                    )}
                  </div>
                  <div className="mt-3">
                    <button className="btn btn-sm btn-primary w-100">🚀 Bora Treinar!</button>
                  </div>
                </div>
                <div className="card-footer text-center" style={{background: 'transparent', border: 'none'}}>
                  <small className="text-muted">💥 Você consegue! 🌟</small>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info text-center" role="alert">
              <h3>🏖️</h3>
              <p className="lead">Ops! Parece que estamos sem treinos... 😴</p>
              <p className="mb-0">🎭 Mas não se preocupe! Mesmo sem treinos programados, você pode fazer polichinelos! 🤸</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Workouts;
