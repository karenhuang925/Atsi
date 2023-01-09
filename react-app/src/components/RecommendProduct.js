import React, {useEffect, useState} from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { get_user_products_fetch, get_category_products_fetch } from '../store/product';
import { Link } from 'react-router-dom';

const RecommendProduct = ({type, value}) => {
    const dispatch = useDispatch()


        useEffect(()=>{
            if (type == 'shop') {
                dispatch(get_user_products_fetch(value))
            }
            if  (type == 'category') {
                dispatch(get_category_products_fetch(value.split(' ')[0]))
            }
        }, [dispatch])

        const productsSelector = useSelector((state => state.product))
        let products

        if (type === 'shop') {
            products = productsSelector.shopProduct?.Products}
        if  (type === 'category') {
            products = productsSelector.categoryProduct?.Products}
        if (!products) return null

    return(
    <div className="mt-6 px-6 grid grid-cols-1 gap-y-10 gap-x-6 sm:grid-cols-2 lg:grid-cols-6 xl:gap-x-10">
    {products.map((product) => (
        <div key={product.id} className="group relative">
            <div className="min-h-60 aspect-w-1 aspect-h-1 w-full overflow-hidden rounded-md bg-gray-200 group-hover:opacity-75 lg:aspect-none lg:h-40">
                <img
                src={product.preview_image}
                alt={product.title}
                className="h-full w-full object-cover object-center lg:h-full lg:w-full"
                />
            </div>
            <div className="mt-4 flex justify-between">
                <div>
                    <h3 className="text-medium text-gray-700 font-bold ">
                        <Link to={`/products/${product.id}`} title={product.title}>
                            <span aria-hidden="true" className="absolute inset-0 " />
                            <p className='wt-text-truncate'>{product.title}</p>
                        </Link>
                    </h3>
                </div>

            </div>
            <div className='flex align-center'>
                <p className="text-medium font-bold font text-gray-900">${product.price}</p>
                {product.original_price && (
                    <div className='flex align-center'>
                        <p>&nbsp;</p>
                        <strike className="text-sm font-sm text-discount-green">${product.original_price}</strike>
                        <p>&nbsp;</p>
                        <p className="text-sm font-sm text-discount-green">({((product.original_price-product.price)/product.original_price).toFixed(2)*100}% off)</p>
                    </div>
                )}
            </div>
        </div>
    ))}
    </div>
    )
}

export default RecommendProduct
