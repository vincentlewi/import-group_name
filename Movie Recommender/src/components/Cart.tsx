import { useState, useEffect } from 'react'
import './Cart.css'

function Cart(props: any) {
  function getRecomm(selectedMovies: Object) {  
    fetch("http://127.0.0.1:5000/cb_kev_multi", {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(selectedMovies)
    })
    .then((response) => response.json())
    .then((data) => {
      props.setCbKevMulti(data)
    })
    
    fetch("http://127.0.0.1:5000/cb_kev", {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(selectedMovies)
    })
    .then((response) => response.json())
    .then((data) => {
      props.setCbKev(data)
      props.setLoading(false)
    })    
  }

  return (
    <div className='cart'>
      <h2 className='cart-title'>Movies You've Rated</h2>
      <div className='cart-content'>
        {props.selectedMovies.map((movie: Object) => <div key={movie.title}>{movie.userRating}★ - {movie.title}</div>)}
      </div>
        <button 
          disabled={!props.selectedMovies.length}
          onClick={() => {props.setLoading(true), getRecomm(props.selectedMovies)}}
        >
          Get Recommendation
        </button>
    </div>
  )
}

export default Cart