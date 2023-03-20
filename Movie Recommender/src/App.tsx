import { useState, useEffect } from 'react'
import './App.css'
import Cart from './components/Cart'
import MovieList from './components/MovieList'
import Recommendation from './components/Recommendation'

function App() {
  let [selectedMovies, setSelectedMovies] = useState(Array())
  let [loading, setLoading] = useState(false)
  let [recommendations, setRecommendations] = useState(Array())

  return (
    <div className="App">
      {!recommendations[0]
      ? !loading
        ? <>
            <MovieList selectedMovies={selectedMovies} setSelectedMovies={setSelectedMovies}/>
            <Cart selectedMovies={selectedMovies}/>
          </>
        : <div>Loading...</div>
      : <Recommendation />
      }
    </div>
  )
}

export default App
