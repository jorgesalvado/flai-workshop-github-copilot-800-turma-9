import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import logo from './octofitapp-small.png';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary sticky-top">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              <img src={logo} alt="OctoFit Logo" />
              OctoFit Tracker
            </Link>
            <button 
              className="navbar-toggler" 
              type="button" 
              data-bs-toggle="collapse" 
              data-bs-target="#navbarNav" 
              aria-controls="navbarNav" 
              aria-expanded="false" 
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ms-auto">
                <li className="nav-item">
                  <Link className="nav-link" to="/users">👤 Users</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">👥 Teams</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">📊 Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">💪 Workouts</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">🏆 Leaderboard</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={
            <div className="container mt-5">
              <div className="jumbotron">
                <h1 className="display-4">🎉 Bem-vindo ao OctoFit Tracker! 💪</h1>
                <p className="lead">Transforme suor em conquistas, treinos em troféus, e cansaço em curtição! 🏆</p>
                <hr className="my-4" />
                <p>Seu app fitness com atitude! Acompanhe atividades, monte equipes fodas, e prove que você é o mestre da malhação! 🔥</p>
                <div className="d-grid gap-2 d-md-flex justify-content-md-center mt-4">
                  <Link to="/activities" className="btn btn-light btn-lg px-4 me-md-2">
                    📊 Ver Minhas Aventuras
                  </Link>
                  <Link to="/workouts" className="btn btn-outline-light btn-lg px-4">
                    💪 Treinos Insanos
                  </Link>
                </div>
              </div>
              
              <div className="row mt-5">
                <div className="col-md-4 mb-4">
                  <div className="card text-center">
                    <div className="card-body">
                      <h2>🔥</h2>
                      <h5 className="card-title">Queime Calorias</h5>
                      <p className="card-text">Registre seus treinos épicos e veja suas calorias derreterem como sorvete no verão! ☀️</p>
                      <Link to="/activities" className="btn btn-primary btn-sm">🚀 Bora Lá!</Link>
                    </div>
                  </div>
                </div>
                <div className="col-md-4 mb-4">
                  <div className="card text-center">
                    <div className="card-body">
                      <h2>👯</h2>
                      <h5 className="card-title">Forma o Bonde</h5>
                      <p className="card-text">Monte seu squad fitness e dominem os treinos juntos. Porque sozinho é difícil, mas em grupo é show! 🎪</p>
                      <Link to="/teams" className="btn btn-primary btn-sm">👥 Ver Times</Link>
                    </div>
                  </div>
                </div>
                <div className="col-md-4 mb-4">
                  <div className="card text-center">
                    <div className="card-body">
                      <h2>🏆</h2>
                      <h5 className="card-title">Seja o Rei/Rainha</h5>
                      <p className="card-text">Conquiste o topo do ranking e mostre quem manda nos treinos. A coroa te espera! 👑</p>
                      <Link to="/leaderboard" className="btn btn-primary btn-sm">🎯 Ver Ranking</Link>
                    </div>
                  </div>
                </div>
              </div>

              <div className="row mt-4">
                <div className="col-12">
                  <div className="card" style={{background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)', color: 'white'}}>
                    <div className="card-body text-center py-4">
                      <h3 style={{color: 'white', WebkitTextFillColor: 'white'}}>💡 Dica de Mestre</h3>
                      <p className="lead mb-0">
                        "A única má decisão é não se mover. Então levanta daí e bora treinar! Sua versão fiteira está te esperando!" 🚀
                      </p>
                      <small style={{opacity: 0.8}}>~ Sabedoria fitness anônima ~</small>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          } />
          <Route path="/users" element={<Users />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
