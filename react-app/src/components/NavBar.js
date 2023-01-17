
import React,  { useState } from 'react';
import { NavLink } from 'react-router-dom';
import './NavBar.css'
import logo from "../logo.png";
import LoginFormModal from "./auth/LoginModal"
import Cart from './Cart';

const NavBar = () => {
  const [cartOpen, setCartOpen] = useState(false)

  return (
    <nav>
      <div className='header'>
        <NavLink to='/' exact={true} >
          <img className='logo' src={logo} alt="logo"/>
        </NavLink>
        <input className='searchBar cursor-not-allowed' placeholder='Search for anything'></input>
        <button className='searchButton cursor-not-allowed'>
          <i className="fa-solid fa-magnifying-glass"></i>
        </button>
        <LoginFormModal />
        <button className='inline-flex justify-center rounded-xl bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none' onClick={()=>setCartOpen(true)}>
          <i className="fa-solid fa-cart-shopping"></i>
          <Cart setCartOpen={setCartOpen} cartOpen={cartOpen}/>
        </button>
      </div>

      <ul className='headerCategory'>
        <li className='eachCategory '>
          <NavLink to='/categories/holiday/' className='cursor-not-allowed' exact={true}>
            Holiday Shop
          </NavLink>
        </li>
        <li className='eachCategory'>
          <NavLink to='/categories/jewelry/' className='cursor-not-allowed' exact={true}>
            Jewerlry & Accessories
          </NavLink>
        </li>
        <li className='eachCategory'>
          <NavLink to='/categories/clothing/' className='cursor-not-allowed' exact={true}>
            Clothing & Shoes
          </NavLink>
        </li>
        <li className='eachCategory'>
          <NavLink to='/categories/home/'className='cursor-not-allowed' exact={true}>
            Home & Living
          </NavLink>
        </li>
        <li className='eachCategory'>
          <NavLink to='/categories/wedding/'className='cursor-not-allowed' exact={true}>
            Wedding & Party
          </NavLink>
        </li>
        <li className='eachCategory'>
          <NavLink to='/categories/toy/' className='cursor-not-allowed' exact={true}>
            Toy & Entertainment
          </NavLink>
        </li>
        <li className='eachCategory'>
          <NavLink to='/categories/Art/' className='cursor-not-allowed' exact={true}>
            Art & Collectibles
          </NavLink>
        </li>
        <li className='eachCategory'>
          <NavLink to='/categories/craft/' className='cursor-not-allowed' exact={true}>
            Craft Supplies
          </NavLink>
        </li>
        <li className='eachCategory'>
          <NavLink to='/categories/gift/' className='cursor-not-allowed' exact={true}>
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
