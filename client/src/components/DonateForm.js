import React, { useState } from 'react'

function DonateForm({ onAddBook}) {
  const [title, setTitle] = useState('')
  const [author, setAuthor] = useState('')
  const [image, setImage] = useState('')
  const [price, setPrice] = useState('')
  const [genre, setGenre] = useState('')
  const [description, setDescription] = useState('')


  // console.log (title)

  function handleSubmit(e) {
    e.preventDefault()
    const OPTIONS = {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({title, author, image, price, description})
    }
    fetch('http://localhost:3000/books', OPTIONS)
    .then(res => res.json())
    .then( newBook => onAddBook(newBook))
  }
  return (
    <div className="donate-form">
      <form onSubmit={handleSubmit}>
        <h2><span>Donate a Book !</span></h2>
        <input type="text" name="title" placeholder="Book title" value={title} onChange={e => setTitle(e.target.value)} />
        <input type="text" name="author" placeholder="Author" value={author} onChange={e => setAuthor(e.target.value)} />
        <input type="text" name="image" placeholder="Image URL" value={image} onChange={e => setImage(e.target.value)} />
        <input type="type" name="genre" placeholder="genre" value={genre} onChange={e => setGenre(e.target.value)} />
        <input type="number" name="price" step="0.01" placeholder="Price" value={price} onChange={e => setPrice(parseFloat(e.target.value))} />
        <textarea type="text" name="description" id="" cols="38" rows="9" placeholder="Type here ..." value={description} onChange={e => setDescription(e.target.value)} />
        <button type="submit">submit</button>
      </form>
    </div>
  )
}

export default DonateForm