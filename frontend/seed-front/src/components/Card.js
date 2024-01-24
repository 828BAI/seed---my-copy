import React from "react";
import "./Card.css";
import Tags from "./Tags";
import { useNavigate } from "react-router-dom";
import { Link, Outlet } from "react-router-dom";

const displayTags = (tags) => {
  return tags.map((tag) => {
    return <Tags>{tag}</Tags>;
  });
};

const Card = ({
  project_name,
  imageUrl,
  description,
  country,
  investment,
  end_date,
  industry,
  slug,
}) => {
  const navigate = useNavigate();
  const handleCardClick = (slug) => {
    navigate(`${slug}`);
  };
  return (
    <div className="card-container" onClick={() => handleCardClick(slug)}>
      <div className="image-container">
        <img src={imageUrl} alt="" />
      </div>
      <div className="card-industries">{displayTags(industry)}</div>

      <div className="card-title">
        <h1>{project_name} </h1>
      </div>
      <div className="card-body">
        <h3> {description} </h3>
        <p> {country}</p>
        <div className="money">
          <p> {investment} in demand</p>
        </div>
        <p> {end_date} days left</p>
      </div>
    </div>
  );
};

export default Card;
