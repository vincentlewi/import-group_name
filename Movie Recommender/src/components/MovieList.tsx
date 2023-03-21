import { useState, useEffect } from 'react'
import Movie from './Movie'
import './Movie.css'
import SearchBar from './SearchBar'

function MovieList(props: any) {
  const [movies, setMovies] = useState(Array())
  const [search, setSearch] = useState('')
  const [query, setQuery] = useState('')
  const [loading, setLoading] = useState(false)

  function fetchData() {  
    fetch("http://127.0.0.1:5000/")
    .then((response) => response.json())
    .then((data) => {
        setMovies(data)
        console.log(data)
    })
  }
  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className='movie-list'>
        <SearchBar setSelectedMovies={props.setSelectedMovies} selectedMovies={props.selectedMovies}  />
        {movies.map((movie: any) => 
          <Movie 
            key={movie.movieId} 
            movieId={movie.movieId} 
            title={movie.title}
            genres={movie.genres}
            imdb_rating={movie.imdb_rating}
            selectedMovies={props.selectedMovies} 
            setSelectedMovies={props.setSelectedMovies}
          />
        )}      
    </div>
  )
}

export default MovieList
