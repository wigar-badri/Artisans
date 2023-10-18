import React from 'react';
import Carousel from 'react-bootstrap/Carousel';
import HomeCard from '../components/HomeCard'; // Assuming HomeCard is a React component in the same directory

function Home() {
    const carouselItems = [
        {
            src: 'https://pbs.twimg.com/media/FwnIEYYacAA-cdf?format=jpg&name=4096x4096',
            alt: 'First slide',
            caption: 'Shop books, coffee, and more!',
            description: 'Check out our gift shop for local and handmade art, books, coffee, and more.',
            buttonLabel: 'Shop',
        },
        {
            src: 'https://pbs.twimg.com/media/FwnIEYWaAAABnhE?format=jpg&name=4096x4096',
            alt: 'Second slide',
            caption: 'Our Menus',
            description: 'Breakfast, Lunch, Dinner, Local coffee\'s, Wines, Beers, and Handcrafted mocktails.',
            buttonLabel: 'Menus',
        },
        {
            src: 'https://img.evbuc.com/https%3A%2F%2Fcdn.evbuc.com%2Fimages%2F522782269%2F495665025423%2F1%2Foriginal.20230207-191025?h=230&w=460&auto=format%2Ccompress&q=75&sharp=10&rect=0%2C199%2C1422%2C711&s=1866c6d8212cbd041ff613b2cf91608d',
            alt: 'Third slide',
            caption: 'Coming Events',
            description: 'RSVP to any of our upcoming events!',
            buttonLabel: 'Events',
        }
    ];

    return (
        <div>
            <Carousel>
                {carouselItems.map((item, index) => (
                    <Carousel.Item key={index}>
                        <img style={{ height: '70vh' }} className='d-block w-100' src={item.src} alt={item.alt} />
                        <Carousel.Caption>
                            <h3>{item.caption}</h3>
                            <p>{item.description}</p>
                            <button>{item.buttonLabel}</button>
                        </Carousel.Caption>
                    </Carousel.Item>
                ))}
            </Carousel>
            <HomeCard />
        </div>
    );
}

export default Home;
