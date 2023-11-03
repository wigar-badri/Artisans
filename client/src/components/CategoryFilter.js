import React, { useState } from 'react';

function CategoryFilter({ books, onFilterChange }) {
  const [selectedGenre, setSelectedGenre] = useState('');
  const genres = ['All', 'Antique', 'YA/Childrens', 'Adult Fiction', 'Non Fiction', 'Used'];

  const handleFilter = genre => {
    setSelectedGenre(genre);
    onFilterChange(genre);
  };

  return (
    <div className="category-filter-container">
      <div className="button-container">
      <h2>Select Category</h2>
        {genres.map(genre => (
          <button
            key={genre}
            onClick={() => handleFilter(genre)}
            className={selectedGenre === genre ? 'active' : ''}
          >
            {genre}
          </button>
        ))}
      </div>
    </div>  
  );
}

export default CategoryFilter;