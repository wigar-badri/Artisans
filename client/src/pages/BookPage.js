import React, { useState, useEffect } from 'react'
import BookList from '../components/BookList'
import CategoryFilter from '../components/CategoryFilter'
import DonateForm from '../components/DonateForm'

function BookPage() {
  const [allBooks, setAllBooks] = useState([])
  const [filteredBooks, setFilteredBooks] = useState([])
  const [selectedGenre, setSelectedGenre] = useState('All')

  useEffect(() => {
    fetch('http://localhost:3000/books')
      .then(res => res.json())
      .then(books => {
        console.log(books)
        setAllBooks(books)
        setFilteredBooks(books)
      })
  }, [])

  function handleAddBook(newBook) {
    const updatedBookArray = [...allBooks, newBook];
    setAllBooks(updatedBookArray);
  }

  function handleFilterChange(genre) {
    setSelectedGenre(genre)
    if (genre === 'All') {
      setFilteredBooks(allBooks)
    } else {
      const filtered = allBooks.filter(book => book.genre === genre)
      setFilteredBooks(filtered)
    }
  }

  return (
    <main className='page-container'>
      <div className='sidebar'>
        <CategoryFilter books={allBooks} onFilterChange={handleFilterChange} />
        <DonateForm onAddBook={handleAddBook} />
      </div >
      <BookList books={filteredBooks} />
    </main>
  );
}

export default BookPage;