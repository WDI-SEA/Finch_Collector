import React, { useState, Fragment, useEffect } from 'react'
import { Route, Routes } from 'react-router-dom'
import './App.css';
import CreateBrand from './components/pages/CreateBrand';

const App = () => {

  const [brand, setBrand] = useState()

  return (
    <Fragment>
    <div className="App">
      <header className="App-header">
        <h1>DJANGO MEET REACT</h1>
      </header>
      {/* <Route
					path='/brands/'
					element={<CreateBrand />}
				/> */}
    </div>
    </Fragment>
  )
}

export default App;
