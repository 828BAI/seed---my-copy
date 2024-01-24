import React, { useState, useEffect } from "react";
import "./SignUp.css";
import { Link } from "react-router-dom";
import logo from "../../imgs/logo.png";
import axios from "axios";
import { Navigate, useLocation } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { register } from "../../features/user";

function RegistrationForm() {
  const dispatch = useDispatch();

  const { registered, loading } = useSelector((state) => state.user);
  const location = useLocation();
  const userType = new URLSearchParams(location.search).get("userType");
  let founder = false;

  if (userType == "founder") {
    founder = "true";
  } else {
    founder = "false";
  }

  const [formData, setFormData] = useState({
    email: "",
    name: "",
    last_name: "",
    password: "",
    re_password: "",
    is_founder: founder,
  });

  const { name, last_name, email, password, re_password, is_founder } =
    formData;
  const handleChange = (event) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    dispatch(
      register({ name, last_name, email, password, re_password, is_founder })
    );
    console.log({ name, last_name, email, password, re_password, is_founder });
  };
  if (registered) return <Navigate to="/login" />;

  return (
    <div className="Register">
      <nav>
        <div id="nav-container-sign">
          <div id="logo">
            <img src={logo} alt="" />
          </div>
          <div id="menu">
            <p>
              {" "}
              Already have an account?<Link to="/login">Login </Link>
            </p>
          </div>
        </div>
      </nav>
      <div className="fillform">
        <div className="slogan">
          <h1> Sign Up</h1>
          <p>Start your way with SEED today</p>
        </div>
        <div className="info">
          <form className="form-wrapper" onSubmit={handleSubmit}>
            <input
              className="input"
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="Email"
            />
            <br />
            <input
              className="input"
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              placeholder="Name"
            />
            <br />
            <input
              className="input"
              type="text"
              name="last_name"
              value={formData.last_name}
              onChange={handleChange}
              placeholder="Last Name"
            />
            <br />
            <input
              className="input"
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              placeholder="Password"
            />
            <br />
            <input
              className="input"
              type="password"
              name="re_password"
              value={formData.re_password}
              onChange={handleChange}
              placeholder="Confirm Password"
            />
            <br />
            <input
              type="hidden"
              name="is_founder"
              value={formData.is_founder}
              onChange={handleChange}
            />
            <br />
            <br />
            <input
              type="hidden"
              name="is_founder"
              value={formData.is_investor}
              onChange={handleChange}
            />
            <br />
            {loading ? (
              <div className="spinner-border" role="status">
                <span className="sr-only">Loading...</span>
              </div>
            ) : (
              <button type="submit">Sign Up</button>
            )}
            ;
          </form>
        </div>
      </div>
    </div>
  );
}

export default RegistrationForm;
