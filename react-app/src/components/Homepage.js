import React, { useEffect } from 'react';
import { NavLink } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import {get_categories_fetch } from '../store/category'
import { get_homepage_products_fetch, get_category_products_fetch, get_user_products_fetch, get_product_detail_fetch } from '../store/product';
import './Homepage.css'

const HomePage = () => {
    const dispatch = useDispatch()

    useEffect(()=> {
        dispatch(get_categories_fetch())
        dispatch(get_homepage_products_fetch())
    },[dispatch])
    const categories = useSelector((state=>state.category))
    const products = useSelector((state=>state.product))

    if (!categories) return null
    if (!products) return null
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
        <div className="bg-white">
            <div className="mx-auto max-w-2xl py-16 px-4 sm:py-24 sm:px-6 lg:max-w-7xl lg:px-8">
                <h2 className="text-2xl font-bold tracking-tight text-gray-900">Popular Gifts Rights Now</h2>

                <div className="mt-6 grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
                {products.map((product) => (
                    <div key={product.id} className="group relative">
                    <div className="min-h-80 aspect-w-1 aspect-h-1 w-full overflow-hidden rounded-md bg-gray-200 group-hover:opacity-75 lg:aspect-none lg:h-80">
                        <img
                        src={product.preview_image}
                        alt={product.title}
                        className="h-full w-full object-cover object-center lg:h-full lg:w-full"
                        />
                    </div>
                    <div className="mt-4 flex justify-between">
                        <div>
                        <h3 className="text-sm text-gray-700">
                            <a href={product.href}>
                            <span aria-hidden="true" className="absolute inset-0" />
                            {product.title}
                            </a>
                        </h3>
                        <p className="mt-1 text-sm text-gray-500">{product.color}</p>
                        </div>
                        <p className="text-sm font-medium text-gray-900">{product.price}</p>
                        {product.original_price && <strike className="text-sm font-medium text-gray-900 ">{product.original_price}</strike>}
                    </div>
                    </div>
                ))}
                </div>
            </div>
        </div>
    </div>

    )
}



export default HomePage;
