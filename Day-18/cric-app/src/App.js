import React, { useState } from "react";
import ScoreBoard from "./components/ScoreBoard";
import Controls from "./components/Controls";
import "./App.css";

function App() {
  const [score, setScore] = useState(0);
  const [wickets, setWickets] = useState(0);
  const [showPopup, setShowPopup] = useState(false);

  const addRuns = (runs) => {
    if (wickets < 10) {
      setScore(score + runs);
    }
  };

  const addWicket = () => {
    if (wickets < 10) {
      setWickets(wickets + 1);
      if (wickets + 1 === 10) {
        setShowPopup(true);
      }
    }
  };

  const nextInnings = () => {
    setScore(0);
    setWickets(0);
    setShowPopup(false);
  };

  return (
    <div className="app">
      <h1>🏏 Cricket Score Tracker</h1>
      <ScoreBoard score={score} wickets={wickets} />
      <Controls addRuns={addRuns} addWicket={addWicket} />

      {showPopup && (
        <div className="popup">
          <div className="popup-content">
            <h2>🏏 First Innings Finished!</h2>
            <button onClick={nextInnings}>Next Innings</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
