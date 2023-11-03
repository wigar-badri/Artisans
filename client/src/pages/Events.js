import React from "react";
import { Calendar, momentLocalizer } from "react-big-calendar";
import moment from "moment";
import "react-big-calendar/lib/css/react-big-calendar.css";


const localizer = momentLocalizer(moment);

const events = [
    {
      id: 1,
      title: "Chess Night",
      start: moment().add(1, "days").set({ hour: 16, minute: 0 }).toDate(), // Set start time to 4 PM
      end: moment().add(1, "days").set({ hour: 18, minute: 0 }).toDate(), // Set end time to 6 PM
    },
    {
      id: 2,
      title: "Writers Salon",
      start: moment().add(3, "days").set({ hour: 16, minute: 0 }).toDate(),
      end: moment().add(3, "days").set({ hour: 18, minute: 0 }).toDate(),
    },
    {
      id: 3,
      title: "Kevin McAdam - Live set",
      start: moment().add(6, "days").set({ hour: 16, minute: 0 }).toDate(),
      end: moment().add(6, "days").set({ hour: 18, minute: 0 }).toDate(),
    },
  ];

const Sidebar = () => (
  <div className="sidebar">
    <h2>Upcoming Events</h2>
    <ul>
      {events.map((event) => (
        <li key={event.id}>
          {moment(event.start).format("MMMM D, YYYY h:mm A")} - {event.title}
        </li>
      ))}
    </ul>
  </div>
);

function Events () {

    return (
        <div>
            <Sidebar />
            <div className="calendar-container">
            <Calendar
                localizer={localizer}
                events={events}
                startAccessor="start"
                endAccessor="end"
                style={{ height: 500 }}
            />
            </div>
        </div>
    )
}

export default Events