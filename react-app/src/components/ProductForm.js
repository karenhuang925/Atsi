import React, {useEffect, useState} from "react";
import { Redirect, useParams } from 'react-router-dom';
import { add_product_fetch, edit_product_fetch, get_category_products_fetch, get_user_products_fetch } from "../store/product";
import { get_categories_fetch } from "../store/category";
import { useDispatch, useSelector } from 'react-redux';



const ProductForm = ({formType, product, setShowModal}) => {

    const dispatch = useDispatch()
    const [redirect, setRedirect] = useState(false);
    const [category_id, setCategory_id] = useState(product.category_id);
    const [title, setTitle] = useState(product.title);
    const [price, setPrice] = useState(product.price);
    const [original_price, setOriginal_price] = useState(product.original_price);
    const [inventory, setInventory] = useState(product.inventory);
    const [desc, setDesc] = useState(product.desc);
    const [shipping_fee, setShipping_fee] = useState(product.shipping_fee);
    const [delivery_days, setDelivery_days] = useState(product.delivery_days);
    const [preview_image, setPreview_image] = useState(product.preview_image);
    const [errors, setErrors] = useState([]);

    useEffect(()=>{
        dispatch(get_categories_fetch())
    }, [dispatch])

    const categories = useSelector((state => state.category))
    const sessionUser = useSelector((state => state.session.user))
    const {userId} = useParams()
    if (!categories) return null
    if (!sessionUser) return null

    if(redirect){
        return (
            <Redirect to={`/users/${sessionUser.id}/products/`} />
        )
    }

    const handleSubmit = async (e) => {

        e.preventDefault();
        setErrors([]);
        product = { ...product, title, category_id, price, original_price, shipping_fee, delivery_days, preview_image };
        if (formType === "Add"){
            const data = await dispatch(add_product_fetch(product))
            if (data) {
              setErrors(data)
            }
            else{
                setShowModal(false)
            }
        }
        if (formType === "Edit"){
            const data = await dispatch(edit_product_fetch(product, product.id))
            if (data) {
                setErrors(data)
            }
            else{
                setShowModal(false)
            }
            dispatch(get_category_products_fetch((product.Category.name.split(' ')[0])))
            dispatch(get_user_products_fetch(sessionUser.id))
        }
    }

    return (
        <div >
        <div className="md:grid md:grid-cols-3 md:gap-6 max-w-screen-lg max-h-min">
            <div className="md:col-span-1">
                <div className="px-4 sm:px-0">
                <h3 className="text-lg font-medium leading-6 text-gray-900">{formType} Product</h3>
                <p className="mt-1 text-sm text-gray-600">
                    This information will be displayed publicly so be careful what you share.
                </p>
                </div>
            </div>
        <div className="mt-5 md:col-span-2 md:mt-0 ">
        <form className='product_modal' onSubmit={handleSubmit} >
            <ul >
                {errors.map((error, idx) => <li className='error pl-4 border border-red-300' key={idx}>{error}</li>)}
            </ul>
            <div className="overflow-hidden shadow sm:rounded-md">
            <div className="bg-white px-4 py-5 sm:p-6">
            <div className="grid grid-cols-6 gap-6">
            <div className="col-span-6 sm:col-span-6">
            <label className="block text-sm font-medium text-gray-700">
                Product Title
                <input
                    className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                    type="text"
                    value={title}
                    onChange={e => setTitle(e.target.value)}
                    required
                    />
            </label>
            </div>

            <div className="col-span-6 sm:col-span-3">
            <label className="block text-sm font-medium text-gray-700">
                Price
                <input
                    className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                    type="number"
                    value={price}
                    onChange={e => setPrice(e.target.value)}
                    required
                    />
            </label>
            </div>
            <div className="col-span-6 sm:col-span-3">
                <label className="block text-sm font-medium text-gray-700">
                    Original price
                    <input
                        className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        type="number"
                        value={original_price}
                        onChange={e => setOriginal_price(e.target.value)}
                        />
                </label>
            </div>

            <div className="col-span-6 sm:col-span-3">
            <label  className="block text-sm font-medium text-gray-700">
                Inventory
                <input
                    className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                    type="number"
                    value={inventory}
                    onChange={e => setInventory(e.target.value)}
                    required
                    />
            </label>
            </div>

            <div className="col-span-6 sm:col-span-3">
            <label  className="block text-sm font-medium text-gray-700">
                Category
                <select
                    className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                    type="number"
                    // defaultValue={category_id}
                    onChange={e => setCategory_id(e.target.value)}
                    required
                >
                    {categories.map((category)=>{
                        return <option key={category.id} value={category.id}>{category.name}</option>
                    })}
                    </select>
            </label>
            </div>
            <div className="col-span-6 sm:col-span-6">
            <label className="block text-sm font-medium text-gray-700">
                desc
                <textarea
                    className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                    type="text"
                    value={desc}
                    onChange={e => setDesc(e.target.value)}
                    required
                    />
            </label>
            </div>
            <div className="col-span-6 sm:col-span-3">
            <label className="block text-sm font-medium text-gray-700">
                Shipping fee
                <input
                    className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                    type="text"
                    value={shipping_fee}
                    onChange={e => setShipping_fee(e.target.value)}
                    required
                    />
            </label>
            </div>
            <div className="col-span-6 sm:col-span-3">
            <label className="block text-sm font-medium text-gray-700">
                Delivery Days
                <input
                    className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                    type="number"
                    value={delivery_days}
                    onChange={e => setDelivery_days(e.target.value)}
                    required
                    />
            </label>
            </div>
            <div className="col-span-6 sm:col-span-6">
                <label className="block text-sm font-medium text-gray-700">Preview Image</label>
                <div className="mt-1 flex justify-center rounded-md border-2 border-dashed border-gray-300 px-6 pt-5 pb-6">
                    <div className="space-y-1 text-center">
                        <svg className="mx-auto h-12 w-12 text-gray-400" stroke="currentColor" fill="none" viewBox="0 0 48 48" aria-hidden="true">
                            <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02"
                        strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" />
                        </svg>
                    <div className="flex text-sm text-gray-600">
                        <label htmlFor="file-upload" className="relative cursor-pointer rounded-md bg-white font-medium text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-500 focus-within:ring-offset-2 hover:text-indigo-500">
                        <span>Upload a file</span>
                        </label>
                        <p className="pl-1">or drag and drop</p>
                    </div>
                <p className="text-xs text-gray-500">PNG, JPG, GIF up to 10MB</p>
                <input className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" type="url" value={preview_image} onChange={e => setPreview_image(e.target.value)} required placeholder="Use URL here"/>
                </div>
            </div>
            <input className="inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2" type="submit" value={formType} />
            </div>
            </div>
            </div>
            </div>
        </form>
        </div>
        </div>
        </div>
    )
}

export default ProductForm
