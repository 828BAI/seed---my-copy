import React from "react";
import "./Tags.css";

const Tags = (industry) => {
  return (
    <div className="tag">
      <p>{industry.children}</p>
    </div>
  );
};

export default Tags;
