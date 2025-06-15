import React from "react";
import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-white shadow-md p-4 flex justify-between items-center">
      <h1 className="text-lg font-bold">Mini Instagram</h1>
      <div className="space-x-4">
        <Link to="/" className="text-blue-600">
          Feed
        </Link>
        <Link to="/profile" className="text-blue-600">
          Profile
        </Link>
      </div>
    </nav>
  );
}
