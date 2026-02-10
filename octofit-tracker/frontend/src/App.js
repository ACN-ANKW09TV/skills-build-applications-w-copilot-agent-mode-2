import logo from './logo.svg';
import './App.css';

import octofitLogo from './octofitapp-small.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={octofitLogo} className="App-logo" alt="Octofit Logo" />
        <span style={{ fontWeight: 'bold', fontSize: '2rem', marginLeft: '20px' }}>Octofit Tracker</span>
      </header>
      <nav>
        <ul>
          <li><Link to="/activities">Activities</Link></li>
          <li><Link to="/leaderboard">Leaderboard</Link></li>
          <li><Link to="/teams">Teams</Link></li>
          <li><Link to="/users">Users</Link></li>
          <li><Link to="/workouts">Workouts</Link></li>
        </ul>
      </nav>
      <Routes>
        <Route path="/activities" element={<Activities />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
        <Route path="/teams" element={<Teams />} />
        <Route path="/users" element={<Users />} />
        <Route path="/workouts" element={<Workouts />} />
      </Routes>
    </div>
  );
}

export default App;
