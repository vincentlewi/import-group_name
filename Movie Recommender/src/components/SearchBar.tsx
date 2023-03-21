import { useState } from 'react';
import AsyncSelect from 'react-select/async';
import './SearchBar.css';
import StarRating from './StarRating';

function SearchBar(props: any) {

  const searchMovies = async (inputValue: string) => {
    if (inputValue) {
      const response = await fetch(`http://127.0.0.1:5000/search/${inputValue}`);
      const data = await response.json();
      return data;
    }
    return [];
  };

  const loadOptions = async (inputValue: string, callback: (options: any[]) => void) => {
    const options = await searchMovies(inputValue);
    callback(options);
  };

  const colourStyles = {
    container: (style: Object) => ({...style,flex: 1}),
    control: (style: Object) => ({ ...style, backgroundColor: '#333', color: '#fff' }),
    singleValue: (style: Object) => ({...style, color: '#fff',}),
    input: (style: Object) => ({...style, color: '#fff',}),
    menu: (style: Object) => ({ ...style, backgroundColor: '#333', color: '#fff' }),
    option: (style: Object, { isDisabled, isFocused, isSelected }) => {
      const backgroundColor = isDisabled ? '#444' : isSelected ? '#666' : isFocused ? '#555' : '#333';
      const color = isDisabled ? '#888' : isSelected ? '#ccc' : isFocused ? '#fff' : '#ccc';
      return {
        ...style,
        backgroundColor,
        color,
        cursor: isDisabled ? 'not-allowed' : 'default'
      };
    },
  };

  let [rating, setRating] = useState(0) 
  let [movie, setMovie] = useState({movieId: 0, title: ''})
  let selectedMovie = {movieId: movie.movieId, title: movie.title, userRating: rating}

  return (
    <div className='search-bar'>
      <AsyncSelect
        cacheOptions
        loadOptions={loadOptions}
        defaultOptions
        placeholder='Search for a movie...'
        onChange={(selectedOption: Object) => {setMovie({movieId: selectedOption.value, title: selectedOption.label}), setRating(0)}}
        styles={colourStyles}
      />
      <div> 
        <StarRating rating={rating} setRating={setRating}/>
      </div>
      {/* <input
        className='search-input'
        type='text'
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      /> */}
      <button 
        disabled={!rating||!movie.movieId}
        className='search-button' 
        onClick={() => props.setSelectedMovies(
          props.selectedMovies.find((movie: Object) => JSON.stringify(movie.title) === JSON.stringify(selectedMovie.title))
          ? props.selectedMovies.filter((movie: Object) => JSON.stringify(movie.title) != JSON.stringify(selectedMovie.title))
          : [...props.selectedMovies, selectedMovie], console.log(selectedMovie)
        )}
      >
        Add to Cart
      </button>
    </div>
  );
}

export default SearchBar;
