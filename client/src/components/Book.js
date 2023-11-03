import React, {useState} from 'react'

function Book ({book}) {

  const [inCart, setInCart] = useState (true)

  function handleClick () {
      setInCart(!inCart)
  }

    return (
      <li className='card' style={{width:'18rem'}}>
        <img orientation='top' src={book.image} alt={book.title} />
        <h1>{book.title}</h1>
        <h5> by {book.author}</h5>
        <p>{book.description}</p>
        <p>Price: ${book.price}</p>
        {inCart ? 
        <button className='primary' onClick={handleClick}>Add to Cart</button>
        :
        <button onClick={handleClick}>In Cart</button>}
      </li>
    ) 
}

export default Book