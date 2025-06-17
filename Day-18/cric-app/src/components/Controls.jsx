import React from "react";

export default function Controls({ addRuns, addWicket }) {
  return (
    <div className="controls">
      <button onClick={() => addRuns(1)}>+1 Run</button>
      <button onClick={() => addRuns(4)}>+4 Runs</button>
      <button onClick={() => addRuns(6)}>+6 Runs</button>
      <button
        style={{
          backgroundColor: "#dc3545",
          color: "white",
          padding: "10px 15px",
          border: "none",
          cursor: "pointer",
          borderRadius: "5px",
          fontSize: "16px",
        }}
        onClick={addWicket}
      >
        🏏 Out
      </button>
    </div>
  );
}
