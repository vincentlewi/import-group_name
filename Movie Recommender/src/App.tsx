import { useState, useEffect } from 'react'
import './App.css'
import Cart from './components/Cart'
import MovieList from './components/MovieList'

function App() {
  let [selectedMovies, setSelectedMovies] = useState(Array())

  return (
    <div className="App">
      <MovieList selectedMovies={selectedMovies} setSelectedMovies={setSelectedMovies}/>
      <Cart selectedMovies={selectedMovies}/>
    </div>
  )
}

export default App
