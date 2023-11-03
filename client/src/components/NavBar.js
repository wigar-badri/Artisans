import {FaBars, FaTimes} from 'react-icons/fa'
import {useRef} from 'react'

function NavBar() {

    const navRef= useRef()

    const showNavBar = () => {
        navRef.current.classList.toggle('responsive_nav')
    }
    
    return (
        <header>
            <h1>Artisans Book & Coffee</h1>
            <nav ref={navRef}>
                <a href='/home'>Home</a>
                <a href='/shop'>Shop</a>
                <a href='/menus'>Menu</a>
                <a href='/events'>Events</a>
                <button className='nav-btn nav-close-btn' onClick={showNavBar}>
                    <FaTimes/>
                </button>
            </nav>
            <button className='nav-btn' onClick={showNavBar}> 
                    <FaBars />
                </button>
        </header>
    )
}

export default NavBar