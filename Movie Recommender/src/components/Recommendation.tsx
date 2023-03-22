import { useState, useEffect } from 'react'
import Moviee from './Moviee'
import './Recommendation.css'
import { ScrollMenu } from "react-horizontal-scrolling-menu";
import HorizontalScroll from 'react-horizontal-scrolling'

const Arrow = ({ text, className }) => {
    return <div className={className}>{text}</div>;
  };
  
  const LeftArrow = Arrow({ text: "<", className: "arrow-prev" });
  const RightArrow = Arrow({ text: ">", className: "arrow-next" });

function Recommendation(props: any) {
  
  let [cbKevMultiMovies, setCbKevMultiMovies] = useState(Array())
  let [cbKevMovies, setCbKevMovies] = useState(Array())

  function fetchData(movies: Object, setMovies: Function) {  
    fetch("http://127.0.0.1:5000/", {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(movies)
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data)
      setMovies(data)
    })
  }

  useEffect(() => {
    fetchData(props.cbKevMulti, setCbKevMultiMovies);
  }, [props.cbKevMulti]);

  useEffect(() => {
    fetchData(props.cbKev, setCbKevMovies);
  }, [props.cbKev]);

  // const menu = movies.map((movie: any) => 
  //   1
  // ) 

  return (
    <div className='list'>
        <div className='divider'>Top Movies for You</div>
        <div className='recommendation-list'>
          <HorizontalScroll>
              {cbKevMultiMovies.map((movie: any) => 
                  <Moviee 
                      key={movie.movieId} 
                      movieId={movie.movieId} 
                      title={movie.title}
                      genres={movie.genres}
                      imdb_rating={movie.imdb_rating}
                      selectedMovies={props.selectedMovies} 
                      setSelectedMovies={props.setSelectedMovies}
                  />
              )}
          </HorizontalScroll>
        </div>
        <div className='divider'>Because You Watched...</div>
        <div className='recommendation-list'>
          <HorizontalScroll>
              {cbKevMovies.map((movie: any) => 
                  <Moviee 
                      key={movie.movieId} 
                      movieId={movie.movieId} 
                      title={movie.title}
                      genres={movie.genres}
                      imdb_rating={movie.imdb_rating}
                      selectedMovies={props.selectedMovies} 
                      setSelectedMovies={props.setSelectedMovies}
                  />
              )}
          </HorizontalScroll>
        </div>
    </div>
  )
}

export default Recommendation
