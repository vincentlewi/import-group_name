import React from 'react'
import { useState } from 'react'
import productpics from '../assets/logofornow.jpg'
import StarRating from './StarRating'


function Movie(props: any) {
  let [rating, setRating] = useState(0)
  const selectedMovie = {movieId: props.movieId, title: props.title, userRating: rating}
  return (
    <div className='movie-card'>
        <img src = {productpics} alt="movie pic"/>
        <div className='movie-desc'>
          <p className='movie-title'>{props.title}</p>
          <p className='short-desc'>Genres: {props.genres}</p>
          <p className='rating'>{props.imdb_rating} STAR</p>
        </div>
        <div>
          <StarRating setRating={setRating}/>
        </div>
        <button disabled={!rating}
          className='movie-button'
          onClick={() => props.setSelectedMovies(
            props.selectedMovies.find((movie: Object) => JSON.stringify(movie.title) === JSON.stringify(selectedMovie.title))
            ? props.selectedMovies.filter((movie: Object) => JSON.stringify(movie.title) != JSON.stringify(selectedMovie.title))
            : [...props.selectedMovies, selectedMovie]
          )}
        >
          Add To Cart
        </button>
    </div>
  )
}

export default Movie