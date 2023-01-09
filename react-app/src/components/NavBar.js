
import React from 'react';
import { NavLink } from 'react-router-dom';
import './NavBar.css'

const NavBar = () => {
  return (
    <nav>
      <div className='header'>
        <NavLink to='/' exact={true} >
          <img className='logo' src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Etsy_logo.svg/2560px-Etsy_logo.svg.png' alt="logo"/>
        </NavLink>
        <input className='searchBar' placeholder='Search for anything'></input>
        <button className='searchButton'>
          <i className="fa-solid fa-magnifying-glass"></i>
        </button>
        <NavLink to='/login' exact={true} className='signIn' >Sign in</NavLink>
        <NavLink to='/carts' exact={true} className='shoppingCart' >
          <i className="fa-solid fa-cart-shopping"></i>
        </NavLink>
      </div>

      <ul className='headerCategory'>
        <li className='eachCategory'>
          <NavLink to='/categories/holiday' exact={true}>
            Holiday Shop
          </NavLink>
        </li>
        <li className='eachCategory'>
          <NavLink to='/categories/jewelry' exact={true}>
            Jewerlry & Accessories
          </NavLink>
        </li>
        <li className='eachCategory'>
          <NavLink to='/categories/clothing' exact={true}>
            Clothing & Shoes
          </NavLink>
        </li>
        <li className='eachCategory'>
          <NavLink to='/categories/home' exact={true}>
            Home & Living
          </NavLink>
        </li>
        <li className='eachCategory'>
          <NavLink to='/categories/wedding' exact={true}>
            Wedding & Party
          </NavLink>
        </li>
        <li className='eachCategory'>
          <NavLink to='/categories/toy' exact={true}>
            Toy & Entertainment
          </NavLink>
        </li>
        <li className='eachCategory'>
          <NavLink to='/categories/Art' exact={true}>
            Art & Collectibles
          </NavLink>
        </li>
        <li className='eachCategory'>
          <NavLink to='/categories/craft' exact={true}>
            Craft Supplies
          </NavLink>
        </li>
        <li className='eachCategory'>
          <NavLink to='/categories/gift' exact={true}>
            Gift & Gift Cards
          </NavLink>
        </li>
      </ul>
      {/* <ul>
        <li>
          <NavLink to='/sign-up' exact={true} activeClassName='active'>
            Sign Up
          </NavLink>
        </li>
        <li>
          <NavLink to='/users' exact={true} activeClassName='active'>
            Users
          </NavLink>
        </li>
        <li>
          <LogoutButton />
        </li>
      </ul> */}
    </nav>
  );
}

export default NavBar;
