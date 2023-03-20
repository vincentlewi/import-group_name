import { useState, useEffect } from 'react'
import './Cart.css'

function Cart(props: any) {
  const [cart, setCart] = useState(Array())
  const [loading, setLoading] = useState(false)
  return (
    <div className='cart'>
      {props.selectedMovies.map((movie: Object) => <div key={movie.title}>{movie.userRating} Stars {movie.title}</div>)}
      <button 
        disabled={!props.selectedMovies.length}
        onClick={() => {console.log(props.selectedMovies)}}
      >
        Get Recommendation
      </button>
    </div>
  )
}

export default Cart