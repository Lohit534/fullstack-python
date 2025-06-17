import React from "react";

export default function ScoreBoard({ score, wickets }) {
  return (
    <div className="score-board">
      <h2>Score: {score}</h2>
      <h2>Wickets: {wickets}/10</h2>
    </div>
  );
}
