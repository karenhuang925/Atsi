
import React, {useEffect, useState} from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams, Link, Redirect} from 'react-router-dom';
import './ProductDetail.css'
import { get_product_detail_fetch, delete_product_fetch, get_category_products_fetch, get_user_products_fetch } from '../store/product';
import RecommendProduct from './RecommendProduct';
import EditProductModal from './EditProductModal';

const ProductDetail = () => {
    const dispatch = useDispatch()
    const {productId} = useParams()
    const [redirect, setRedirect] = useState(false);
    const [currentIndex, setCurrentIndex] = useState(0);
    const [isExpanded, setIsExpanded] = useState(true);
    const [isShippingExpanded, setIsShippingExpanded] = useState(true);
    const [descHeight, setDescHeight] = useState(60);


    useEffect(()=> {
        dispatch(get_product_detail_fetch(productId))
    },[dispatch])
    useEffect(()=> {
        dispatch(get_product_detail_fetch(productId))
    },[productId])
    const product = useSelector((state=>state.product.currentProduct))
    const user = useSelector(state => state.session.user);
    let cartItems = useSelector((state => state.cart?.Items))

    if (!product) return null
    if (!cartItems) return null

    let images = product.Images
    if (images?.length == 0 || images == undefined) {
        images = [{url: product.preview_image}]
    }


    const length = images?.length ? images.length : null

    const nextImage = () => {
        setCurrentIndex(currentIndex === length - 1 ? 0 : currentIndex + 1)
    }
    const prevImage = () => {
        setCurrentIndex(currentIndex === 0 ? length - 1 : currentIndex - 1)
    }
    const currentImage = (index) =>{
        setCurrentIndex(index)
    }
    if (!Array.isArray(images) || images?.length <= 0) return null

    // shipping date
    var date = new Date();
    date.setDate(date.getDate() + product.delivery_days);
    var month = date.toLocaleString("default", { month: "short" });
    var day = date.toLocaleString("default", { day: "2-digit" });
    var formattedDate = [month, day].join(" ");

    //edit and delete button
    if(redirect){
        return (
            <Redirect to={`/users/${user.id}/products/`} />
        )
    }
    const deleteProdcut = (e) => {
        e.preventDefault();
        dispatch(delete_product_fetch(product.id)).then((()=> {
            setRedirect(true)}))
    };

    const handleAddToCart = (e) =>{
        e.preventDefault();
        let itemIndex = cartItems.findIndex(item => item.product.id == product.id)
        console.log(itemIndex)
        if (itemIndex !== -1){
            let theItem = cartItems[itemIndex]
            let quantity = theItem.quantity
            let updateItems = cartItems
            updateItems[itemIndex] = {...updateItems[itemIndex], quantity: quantity}
            console.log(updateItems)
        }
    }



    let editAndDelete;
    if (user?.id === product?.Vendor?.id) {
        editAndDelete = (
            <div className='flex justify-evenly'>
                <EditProductModal product={product}/>
                <button className='flex items-center justify-center rounded-xl border border-black bg-white py-1 px-4 text-base font-medium text-black hover:shadow focus:ring-2 focus:ring-black-100 focus:ring-offset-2' onClick={deleteProdcut}>
                    <i className='fa-solid fa-trash mr-2'></i> Delete this product
                    </button>
            </div>
        );
    }

    return (
        <div className="bg-white">
            <div className="pt-6">

            {/* <!-- Image gallery --> */}
            <div className='flex justify-start mt-6 mx-auto'>
            <div className="gallary ml-5 w-full">
                {images.map((image, i) => {
                    return (
                    <div className={i === currentIndex ? "row mb-2 mt-2 rounded-lg active" : "rounded-lg row mb-2 mt-2"} key={i} onClick={() => currentImage(i)} >
                        <img src={image.url} className=" w-full h-full" />
                    </div>
                )})}
            </div>
            <div className='image-swiper max-w-2xl sm:px-6 w-full lg:max-w-2xl'>
                {length > 1 && <div className='right-arrow' onClick={nextImage}><i className="fa-solid fa-chevron-right"></i></div>}
                {length > 1 && <div className='left-arrow' onClick={prevImage}><i className="fa-solid fa-chevron-left"></i></div>}
                {images.map((image, index) => {
                    return (
                        <div className='image-container' key={index}>
                            {index === currentIndex &&
                                <img
                                    className='post-media'
                                    src={image?.url}
                                    alt='aPicture'
                                />
                            }
                        </div>
                    )
                })}
            </div>
            <div className="pb-10 w-full mr-4">
                <div>
                    <div className='flex justify-between'>
                        <p className='text-base mb-3'>Shop: {product.Vendor.shop_name}</p>
                        {editAndDelete}
                    </div>
                    <div className="text-sm font-medium text-indigo-600 hover:text-indigo-500 mb-3 flex "><i className="fa fa-certificate mr-1"></i><p className='underline-dotted'>Star Seller</p></div>
                    <p className='text-sm mb-3'>{product.sold_num} sales | {[...Array(5)].map((e, i) => <i className="fa fa-star checked text-xs "></i>)}</p>
                </div>
                <h1 className="text-2xl tracking-tight text-gray-900 sm:text-3xl mb-8">{product.title}</h1>
                <div className='flex justify-between'>
                    <div className='flex'>
                        <p className="text-3xl font-bold tracking-tight text-gray-900 ">${product.price}</p>
                        {product.original_price && (
                                <div className='flex align-center '>
                                    <strike className="text-base text-discount-green px-3">${product.original_price}</strike>
                                    <p className="text-base text-discount-green">({((product.original_price-product.price)/product.original_price).toFixed(2)*100}% off)</p>
                                </div>
                            )}
                    </div>
                    {product.inventory < 10 && <p className="text-low-red font-bold mr-3">Low in Stock</p>}
                </div>
                <button onClick={handleAddToCart}className=" w-full mt-10 flex items-center justify-center rounded-3xl border border-transparent bg-gray-900 py-3 px-10 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
                    Add to cart
                </button>
                <div div className="py-10 w-full">
                    <h3 onClick={()=>{
                        setDescHeight(isExpanded ? 0 : 100)
                        setIsExpanded(!isExpanded)
                        }} className="text-xl bg-white hover:bg-slate-300 rounded-3xl p-3 flex justify-between align-center"><p>Description</p>
                    {isExpanded ? <i className='fa fa-chevron-up'></i> : <i className='fa fa-chevron-down'></i>}
                    </h3>
                    <div >
                        <p className="text-base text-gray-900 px-3 overflow-scroll text-ellipsis transition-height" style={{ height: `${descHeight}px` }}>{product.desc}</p>
                    </div>
                    <div div className="py-10 w-full">
                    <h3 onClick={()=>{
                        setIsShippingExpanded(!isShippingExpanded)
                        }} className="text-xl bg-white hover:bg-slate-300 rounded-3xl p-3 flex justify-between align-center"><p>Shipping</p>
                        {isShippingExpanded ? <i className='fa fa-chevron-up'></i> : <i className='fa fa-chevron-down'></i>}
                    </h3>
                    {isShippingExpanded &&
                        <div className='px-3'>
                            <p className='underline-dotted text-base text-gray-900 py-2 mb-1'>Estimated Arrival</p>
                            {product.shipping_fee == 0 && <p className='bg-low-red w-fit rounded-2xl px-2 mb-2'>free shipping</p>}
                            <p className='text-3xl'>{formattedDate}</p>
                        </div>
                    }
                    </div>
                    </div>
                </div>
            </div>
            </div>
            <div>
                <div className='more-from-this-shop px-6 flex justify-between'>
                    <p className='text-3xl'>More from this shop</p>
                    <Link to={`/users/${product.Vendor.id}`}>
                        <button className="flex items-center justify-center rounded-xl border border-black bg-white py-1 px-4 text-base font-medium text-black hover:shadow focus:ring-2 focus:ring-black-100 focus:ring-offset-2">See more</button>
                    </Link>
                </div>
                    <RecommendProduct type='shop' value={product.Vendor.id} ></RecommendProduct>
            </div>
            <div className='mb-10'>
                <div className='more-from-this-shop px-6 flex justify-between'>
                    <p className='text-3xl'>More from this category</p>
                    <Link to={`/category/${product.Category.name.split(" ")[0]}/`}>
                    <button className="flex items-center justify-center rounded-xl border border-black bg-white py-1 px-4 text-base font-medium text-black hover:shadow focus:ring-2 focus:ring-black-100 focus:ring-offset-2">See more</button>
                    </Link>
                </div>
                    <RecommendProduct type='category' value={product.Category.name} ></RecommendProduct>
            </div>
        </div>

    )
}


export default ProductDetail;
