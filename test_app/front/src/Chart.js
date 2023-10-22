import React from 'react';
import {makeRequest} from './App'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';


ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

export const options = {
  responsive: true,
  plugins: {
    legend: {
      position: 'top'
    },
    title: {
      display: true,
      text: 'Responce Chart',
    },
  },
};

let promise = await fetch('http://localhost:8000/servers');
let responce = await promise.json();

const labels = []
for(let i = 0; i<24;i++){
  labels.push(String(i))
}

export const data = {
  labels: labels,
  datasets: responce['dataset']
};

export function Chart() {
  return <Bar options={options} data={data} />;
}
