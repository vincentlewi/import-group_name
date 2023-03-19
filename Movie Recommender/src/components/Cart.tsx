import { useState, useEffect } from 'react'
import './Cart.css'

function Cart(props: any) {
  const [cart, setCart] = useState(Array())
  const [loading, setLoading] = useState(false)

  return (
    <div className='cart'>
        {props.selectedMovies.map((movie: any) => <div key={movie}>{movie}</div>)}
    </div>
  )
}

export default Cart