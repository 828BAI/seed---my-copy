import React, { useState } from "react";
import logo_d from "../imgs/logo-d.svg";
import "./Sidebar.css";
import calendar from "../imgs/calendar.svg";
import file from "../imgs/how-it-works.svg";
import rocket from "../imgs/rocket-02.svg";
import { Link, Outlet } from "react-router-dom";

const Sidebar_data_inv = [
  { img: rocket, link: "myproject" },
  { img: calendar, link: "mymeetings" },
  { img: file, link: "explanation" },
];

const Sidebar = ({ children }) => {
  return (
    <div className="sidebar-container">
      <div className="sidebar">
        <div className="sidebar-logo">
          <img src={logo_d} alt="" />
        </div>
        <div className="row">
          {Sidebar_data_inv.map((val, index) => (
            <Link to={val.link} key={index} className="link">
              <div className="icon">
                <img src={val.img} />
              </div>
            </Link>
          ))}
        </div>
      </div>
      <Outlet />
      <main>{children}</main>
    </div>
  );
};

export default Sidebar;
