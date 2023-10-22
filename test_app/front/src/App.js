import logo from './logo.svg';
import './App.css';
import React, { useEffect } from 'react';
import { Chart } from './Chart';

function onLoad() {
  makeRequest();
  // Use the data passed from Django
}

export async function makeRequest() {
  let promise = await fetch('http://localhost:8000/servers');
  let data = await promise.json();
  return data;  
}

function App() {
  useEffect(onLoad);

  return (
     <div className='container'>
      <h1>Responce chart</h1>
      <Chart/>
    </div>
  );
}

export default App;
