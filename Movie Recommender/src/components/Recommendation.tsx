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
  let [recommendations, setRecommendations] = useState(props.recommendations)
  const [movies, setMovies] = useState(Array())
  const [search, setSearch] = useState('')
  const [query, setQuery] = useState('')
  const [loading, setLoading] = useState(false)

  function fetchData() {  
    fetch("http://127.0.0.1:5000/", {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(recommendations)
  })
    .then((response) => response.json())
    .then((data) => {
        setMovies(data)
        console.log(data)
    })
  }
  useEffect(() => {
    fetchData();
  }, []);

  // const menu = movies.map((movie: any) => 
  //   1
  // ) 

  return (
    <div className='list'>
        <div className='divider'>Top Movies for You</div>
        {/* <ScrollMenu
            LeftArrow={LeftArrow} 
            RightArrow={RightArrow}
            dragging={true}
            wheel={false}
            alignCenter={false}
            clickWhenDrag={false}
        >
            {movies.map((movie: any) => 
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
        </ScrollMenu>    */}
        <div className='recommendation-list'>
          <HorizontalScroll>
              {movies.map((movie: any) => 
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
