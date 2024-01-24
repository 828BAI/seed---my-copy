import React, { useEffect, useState } from "react";
import { Navigate } from "react-router-dom";
import PropTypes from "prop-types";
import { BrowserRouter, Link, Route, Routes } from "react-router-dom";
import "./Login.css";
import { useNavigate } from "react-router-dom";
import logo from "../../imgs/logo.png";
import axios from "axios";
import { useDispatch, useSelector } from "react-redux";
import { resetRegistered, login } from "../../features/user";

function Login() {
  const dispatch = useDispatch();
  const { user, loading, isAuthenticated, registered } = useSelector(
    (state) => state.user
  );

  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  useEffect(() => {
    if (registered) dispatch(resetRegistered());
  }, [registered]);

  const { email, password } = formData;
  const handleChange = (event) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    dispatch(login({ email, password }));
  };
  if (isAuthenticated && user !== null) {
    if (user.user.is_founder) {
      return <Navigate to="/founder/dashboard" />;
    } else {
      return <Navigate to="/investor/dashboard" />;
    }
  }

  return (
    <div className="Login">
      <nav>
        <div id="nav-container">
          <div id="logo">
            <img src={logo} alt="" />
          </div>
          <div id="menu">
            <p>
              {" "}
              Don't have an account?<Link to="/signup">Sign Up </Link>
            </p>
          </div>
        </div>
      </nav>

      <div className="fillform-login">
        <div className="slogan-login">
          <h1 className="log"> Login</h1>
          <p className="welcome">Welcome back.</p>
        </div>

        <div className="info">
          <form className="form-wrapper" onSubmit={handleSubmit}>
            {/* {error && <p className="error">{error}</p>} */}
            <div className="email">
              <input
                className="input"
                type="email"
                name="email"
                placeholder="Email"
                onChange={handleChange}
              />{" "}
            </div>
            <div className="password">
              <input
                className="input"
                type="password"
                name="password"
                placeholder="Password"
                onChange={handleChange}
              />{" "}
            </div>
            {loading && user === null ? (
              <div className="spinner-border" role="status">
                <span className="sr-only">Loading...</span>
              </div>
            ) : (
              <button type="submit">Login</button>
            )}
            ;
          </form>
        </div>
      </div>
    </div>
  );
}

export default Login;
