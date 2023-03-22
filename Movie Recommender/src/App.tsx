import { useState, useEffect } from 'react'
import './App.css'
import Cart from './components/Cart'
import MovieList from './components/MovieList'
import Recommendation from './components/Recommendation'

function App() {
  let [selectedMovies, setSelectedMovies] = useState(Array())
  let [movieList, setMovieList] = useState(Array())
  let [loading, setLoading] = useState(true)
  let [cbKevMulti, setCbKevMulti] = useState(Array())
  let [cbKev, setCbKev] = useState(Array())
  let [cfCb, setCfCb] = useState(Array())

    // fetch initial movieList
    useEffect(() => {
      fetch("http://127.0.0.1:5000/")
      .then((response) => response.json())
      .then((data) => {
          setMovieList(data)
          setLoading(false)
      })
    }, []);

  return (
    <div className="App">
      {!cbKev[0]
      ? !loading
        ? <>
            <MovieList selectedMovies={selectedMovies} setSelectedMovies={setSelectedMovies} movies={movieList}/>
            <Cart selectedMovies={selectedMovies} setLoading={setLoading} setCbKevMulti={setCbKevMulti} setCbKev={setCbKev} setCfCb={setCfCb}/>
          </>
        : <div>Loading...</div>
      : <Recommendation cbKevMulti={cbKevMulti} cbKev={cbKev} cfCb={cfCb}/>
      }
    </div>
  )
}

export default App
