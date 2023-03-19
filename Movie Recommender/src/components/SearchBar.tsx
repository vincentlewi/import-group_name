import { useState, useEffect } from 'react'
import AsyncSelect from 'react-select/async';
import './SearchBar.css'

function SearchBar(props: any) {
  const [search, setSearch] = useState('')
  const [query, setQuery] = useState('')

  // useEffect(() => {
  //   if (search) {
  //     fetch("http://127.0.0.1:5000/search/" + search)
  //     .then((response) => response.json())
  //     .then((data) => {
  //       console.log(data)
  //     })
  //   }
  // }, [search])

  const searchMovies = (inputValue: string) => {
    if(search){
      fetch("http://127.0.0.1:5000/search/" + search)
      .then((response) => response.json())
      .then((data) => {
        return data
        })
    }
  }
  
  const filterColors = (inputValue: string) => {
    return colourOptions.filter((i) =>
      i.label.toLowerCase().includes(inputValue.toLowerCase())
    );
  };

  const promiseOptions = (inputValue: string) =>
  new Promise<ColourOption[]>((resolve) => {
    setTimeout(() => {
      resolve(filterColors(inputValue));
    }, 1000);
  });

  return (
    <div className='search-bar'>
      <AsyncSelect cacheOptions loadOptions={promiseOptions} defaultOptions />
      <input 
        className='search-input'
        type='text' 
        value={search} 
        onChange={(e) => setSearch(e.target.value)}
      />
      <button className='search-button' onClick={() => setSearch(search)}>Search</button>
    </div>
  )
}

export default SearchBar