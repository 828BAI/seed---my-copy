import React, { useEffect } from "react";
import { useDispatch } from "react-redux";
import { checkAuth } from "./features/user";
import "./App.css";

import { BrowserRouter, Routes, Route } from "react-router-dom";

import Mainpage from "./pages/Main/Mainpage";
import Login from "./pages/Login/Login";
import RegistrationForm from "./pages/Signup/SignUp";
import Survey from "./pages/Survey/Survey";
import Dashboard from "./pages/Investor/Dashboard";
import Dashboard_founder from "./pages/Founder/Dashboard_founder";
import Founder_meetings from "./pages/Founder/Founder_meetings";
import Project from "./pages/Founder/Project";
import Features from "./pages/Features";
import { useSelector } from "react-redux";
import ProjectDetailView from "./containers/ProjectDetailView";
import AllProjects from "./pages/Investor/AllProjects";

const App = () => {
  const dispatch = useDispatch();
  const { user } = useSelector((state) => state.user);

  useEffect(() => {
    dispatch(checkAuth());
  }, []);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Mainpage />} />

        <Route exact path="/features" element={<Features />} />

        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<RegistrationForm />} />
        <Route path="/survey" element={<Survey />} />
        <Route path="/investor/dashboard/*" element={<Dashboard />}>
          <Route path="browse" element={<AllProjects />} />
        </Route>

        <Route path="/founder/dashboard/*" element={<Dashboard_founder />}>
          <Route path="mymeetings" element={<Founder_meetings />} />

          <Route path="myproject" element={<Project />}>
            <Route path=":slug" element={<ProjectDetailView />} />
          </Route>
          <Route path="explanation" element={<Project />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default App;
