import React from 'react'
import productpics from '../assets/logofornow.jpg'


function Products(props: any) {
  return (
    <div className='movie-card'>
        <img src = {productpics} alt="movie pic"/>
        <div className='movie-desc'>
          <p className='movie-title'>{props.title}</p>
          <p className='short-desc'>Genres: {props.genres}</p>
          <p className='rating'>{Math.round(props.AvgRating *100)/100} STAR</p>
        </div>
        <button 
          className='movie-button'
          onClick={() => props.setSelectedMovies(
            props.selectedMovies.includes(props.title) 
            ? props.selectedMovies.filter((title: string) => title !== props.title) 
            : [...props.selectedMovies, props.title]
          )}
        >
          Add To Cart
        </button>
        
    </div>
  )
}

export default Products