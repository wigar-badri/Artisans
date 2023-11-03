import React from "react";


const MenuCard = ({ items }) => {
    return (
        <div className="section-center">
          {items.map((item) => {
            const { id, title, img, desc, price } = item;
            return (
              <article key={id} className="MenuCard-item">
                <div className="image-container">
                  <img src={img} alt={title} className="photo" />
                </div>
                <div className="item-info">
                  <header>
                    <h4>{title}</h4>
                    <h4 className="price">${price}</h4>
                  </header>
                  <p className="item-text">{desc}</p>
                </div>
              </article>
            );
          })}
        </div>
      );
    };
    
export default MenuCard;