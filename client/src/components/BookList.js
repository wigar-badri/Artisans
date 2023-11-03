import React from 'react'
import Book from './Book'

function BookList ({books}) {
    return (
        <div className=''>
            <ul className='cards'>
                {books.map( book => {return <Book key={book.id} book={book} /> })}
            </ul>
        </div>
    )
}

export default BookList