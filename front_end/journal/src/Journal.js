import React from 'react';
import { useParams } from 'react-router-dom';

function Journal() {
  const { id } = useParams();

  return (
    <div>
      <h1>Journal entry for event {id}</h1>
      <p>TODO: add journal form and integrate with backend</p>
    </div>
  );
}

export default Journal;