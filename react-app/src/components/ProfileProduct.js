
import React, {useEffect, useState} from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams, Link} from 'react-router-dom';
import { get_user_products_fetch } from '../store/product';
import AddProductModal from './AddProductModal';
import RecommendProduct from './RecommendProduct'

const ProfileProduct=()=>{
    const {userId} = useParams()
    const user = useSelector(state => state.session.user);


    // useEffect(()=> {
    //     dispatch(get_user_products_fetch(userId))
    // },[dispatch])
    // const product = useSelector((state=>state.product.currentProduct))

    return (
        <>
            <div className="overflow-hidden bg-white shadow sm:rounded-lg px-3 pt-10 flex justify-between">
                <div className="px-4 py-5 sm:px-6">
                    <h3 className="text-xl font-medium leading-6 text-gray-900">Welcome to {user.first_name} {user.last_name}'s shop: {user.shop_name}!</h3>
                    <p className="mt-1 max-w-2xl text-base text-gray-500">Current products</p>
                </div>
                <AddProductModal />
            </div>
            <RecommendProduct type='shop' value={userId} ></RecommendProduct>
        </>
    )
}

export default ProfileProduct
