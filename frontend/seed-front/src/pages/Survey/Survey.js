import React from "react";
import "./Survey.css";
import logo from "../../imgs/logo.png";
import { useNavigate } from "react-router-dom";
import RegistrationForm from "../Signup/SignUp";

function Survey() {
  const handleFounderClick = () => {
    // Navigate to the registration form and pass the user type as a prop
    window.location.href = "/signup?userType=founder";
  };

  const handleInvestorClick = () => {
    // Navigate to the registration form and pass the user type as a prop
    window.location.href = "/signup?userType=investor";
  };
  return (
    <div className="survey">
      <nav>
        <div id="nav-container">
          <div id="logo">
            <img src={logo} alt="" />
          </div>
          <div id="menu">
            <p> Hello!</p>
          </div>
        </div>
      </nav>

      <div className="content">
        <h1>Welcome to SEEDStartups</h1>
        <p> Make a selection below</p>
        <div className="selections">
          <button onClick={handleFounderClick}>I am a startup founder</button>
          <button onClick={handleInvestorClick}>I am an investor</button>
        </div>
      </div>
    </div>
  );
}

export default Survey;
