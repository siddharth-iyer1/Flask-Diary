// App.js

import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { makeStyles } from '@material-ui/core/styles';
import { Calendar, momentLocalizer } from 'react-big-calendar';
import moment from 'moment';

import 'react-big-calendar/lib/css/react-big-calendar.css';

import Journal from './Journal';

const localizer = momentLocalizer(moment);

const events = [
  {
    id: 0,
    title: 'Event 1',
    start: new Date(2022, 2, 20),
    end: new Date(2022, 2, 20),
  },
  {
    id: 1,
    title: 'Event 2',
    start: new Date(2022, 2, 21),
    end: new Date(2022, 2, 21),
  },
  {
    id: 2,
    title: 'Event 3',
    start: new Date(2022, 2, 22),
    end: new Date(2022, 2, 22),
  },
];

const useStyles = makeStyles((theme) => ({
  calendar: {
    height: '80vh',
  },
}));

function App() {
  const classes = useStyles();

  return (
    <Router>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
        </ul>
      </nav>
      <Routes>
        <Route exact path="/">
          <div className={classes.calendar}>
            <Calendar
              localizer={localizer}
              events={events}
              startAccessor="start"
              endAccessor="end"
              style={{ height: '100%' }}
              onSelectEvent={(event) => window.location.href=`/journal/${event.id}`}
            />
          </div>
        </Route>
        <Route path="/journal/:id" component={Journal} />
      </Routes>
    </Router>
  );
}

export default App;

