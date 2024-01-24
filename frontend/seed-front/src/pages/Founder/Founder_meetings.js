import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./meetings.css";
import Calendar from "react-calendar";

const Founder_meetings = () => {
  const [date, setDate] = useState(new Date());
  return (
    <div className="rightcontent">
      <div className="meetings-top">
        <h1> Meetings</h1>
      </div>
      <div className="meetings-container">
        <div className="togglebar">
          <Link to="scheduled" className="a-sched">
            {" "}
            Scheduled{" "}
          </Link>
          <Link to="invitations" className="a-inv">
            {" "}
            Invitations{" "}
          </Link>

          <div className="date_and_events">
            <div className="selected-date">
              Selected date: {date.toDateString()}
            </div>
          </div>
        </div>
      </div>

      <div className="meetings-calendar">
        <Calendar onChange={setDate} value={date} />
      </div>
    </div>
  );
};

export default Founder_meetings;
