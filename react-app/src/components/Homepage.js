import React, { useEffect } from 'react';
import { NavLink } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import {get_categories } from '../store/category'
import './Homepage.css'

const HomePage = () => {
    const dispatch = useDispatch()

    useEffect(()=> {
        dispatch(get_categories())
    },[])
    const categories = useSelector((state=>state.category))


    if (!categories) return null
    // console.log(categories)
    return (

    <div>
        <div className='Banner'>
            <p className='BannerCaption'>
                Find things you’ll love. Support independent sellers. Only on Atsi.
            </p>
            <div className='BannerImage'>
                <ul className='BannerImageList'>
                    <li >
                        <NavLink to='/categories/gift' exact={true} className='BannerImageItem'>
                            <img className="BannerRoundImage" alt='gift' src={categories[8].preview_image} />
                            <p>Personalized Gifts</p>
                        </NavLink>
                    </li>
                    <li >
                        <NavLink to='/categories/home' exact={true} className='BannerImageItem'>
                            <img className="BannerRoundImage" alt='plant' src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrNLhvA_G9H4oZm7pRQS6qRJEMavzok8KsxA&usqp=CAU' />
                            <p>Plants</p>

                        </NavLink>
                    </li>
                    <li >
                        <NavLink to='/categories/clothing' exact={true} className='BannerImageItem'>
                            <img className="BannerRoundImage" alt='clothing' src={categories[2].preview_image} />
                            <p>Clothing & Shoes</p>
                        </NavLink>
                    </li>
                    <li >
                    <NavLink to='/categories/jewelry' exact={true} className='BannerImageItem'>
                        <img className="BannerRoundImage" alt='jewelry' src={categories[1].preview_image} />
                            <p>Jewelry</p>

                    </NavLink>
                    </li>
                    <li >
                    <NavLink to='/categories/home' exact={true} className='BannerImageItem'>
                    <img className="BannerRoundImage" alt='furniture' src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRggcujbuOWBzqySN04EzsCNTsqeX1vn6WXqw&usqp=CAU' />
                            <p>Furniture</p>
                    </NavLink>
                    </li>
                    <li >
                    <NavLink to='/categories/sale' exact={true} className='BannerImageItem'>
                    <img className="BannerRoundImage" alt='sale' src={categories[9].preview_image} />
                            <p>On Sale</p>
                    </NavLink>
                    </li>
                </ul>
            </div>
        </div>
    </div>

    )
}



export default HomePage;
