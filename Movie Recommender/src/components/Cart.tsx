import { useState, useEffect } from 'react'
import './Cart.css'

function Cart(props: any) {
  const [cart, setCart] = useState(Array())
  const [loading, setLoading] = useState(false)

  const userCart = [ // this is dummy. Replace with actual cart data
    {
      "title": "The Shawshank Redemption (1994)", 
      "user_rating": 4.5
    },
    {
        "title": "Pulp Fiction (1994)", 
        "user_rating": 4.5
    },
    {
        "title": "The Silence of the Lambs (1991)", 
        "user_rating": 4
    },
    {
        "title": "Forrest Gump (1994)", 
        "user_rating": 3.5
    },
    {
        "title": "The Avengers (2012)", 
        "user_rating": 2.5
    },
    {
        "title": "Avatar (2009)", 
        "user_rating": 2
    },
    {
        "title": "Guardians of the Galaxy (2014)", 
        "user_rating": 4.5
    },
    {
        "title": "American History X (1998)", 
        "user_rating": 4
    },
    {
        "title": "Reservoir Dogs (1992)", 
        "user_rating": 4
    },
    {
        "title": "No Country for Old Men (2007)", 
        "user_rating": 4.5,
        "movieId": "55820"
    },
    {
        "title": "The League of Extraordinary Gentlemen (2003)", 
        "user_rating": 5,
        "movieId": "260207"
    }
  ]
  
  function getRecomm(selectedMovies: Object) {  
    fetch("http://127.0.0.1:5000/cb_kev", {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(selectedMovies)
  })
  .then((response) => response.json())
  .then((data) => {
    props.setRecommendations(data)
    props.setLoading(false)
  })
  }
  // useEffect(() => {
  //   getRecomm();
  // }, []);

  return (
    <div className='cart'>
      <h2 className='cart-title'>Movies You've Rated</h2>
      <div className='cart-content'>
        {props.selectedMovies.map((movie: Object) => <div key={movie.title}>{movie.userRating}★ - {movie.title}</div>)}
      </div>
        <button 
          disabled={!props.selectedMovies.length}
          onClick={() => {props.setLoading(true), getRecomm(props.selectedMovies), console.log(props.selectedMovies)}}
        >
          Get Recommendation
        </button>
    </div>
  )
}

export default Cart