import React from "react";
import ReactDOM from "react-dom";
import "./Mainpage.css";

import { useNavigate } from "react-router-dom";
import logo from "../../imgs/logo.png";
import background from "../../imgs/background.png";
import { Link } from "react-router-dom";

function Mainpage() {
  const navigate = useNavigate();

  return (
    <div className="Main">
      <div className="container">
        <nav>
          <div id="nav-container">
            <div id="logo">
              <img src={logo} alt="" />
            </div>
            <div id="menu">
              <Link to="/features">Features </Link>
              <Link to="/features">Contact Us </Link>

              <button
                onClick={() => {
                  navigate("/login");
                }}
              >
                Login
              </button>
            </div>
          </div>
        </nav>

        <div className="hero-container">
          <h1>Platfrom for startups and investors</h1>
          <p>We help startups and investors find each other</p>
          <button
            onClick={() => {
              navigate("/survey");
            }}
          >
            SignUp
          </button>
        </div>
      </div>
    </div>
  );
}

export default Mainpage;
