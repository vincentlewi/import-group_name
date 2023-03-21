import React from 'react'
import { useState } from 'react'
import productpics from '../assets/logofornow.jpg'
import StarRating from './StarRating'
import './Moviee.css'


function Movie(props: any) {
  let [rating, setRating] = useState(0)
  const selectedMovie = {movieId: props.movieId, title: props.title, userRating: rating}
  return (
    <div className='movie-cardd'>
        <img src = {productpics} />
        <div className='movie-desc'>
          <p className='movie-title'>{props.title}</p>
          <p className='short-desc'>Genres: {props.genres}</p>
          <p className='rating'>{props.imdb_rating} STAR</p>
        </div>
    </div>
  )
}

export default Movie