import React, {useState} from "react";
import { Redirect } from 'react-router-dom';
import { add_product_fetch } from "../store/product";
import { useDispatch } from 'react-redux';



const ProductForm = ({formType, product}) => {

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

    if(redirect){
        return (
            <Redirect to={`/products`} />
        )
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        setErrors([]);
        product = { ...product, title, category_id, price, original_price, shipping_fee, delivery_days, preview_image };
        if (formType === "Create spot"){
            dispatch(add_product_fetch(product))
            // .then((()=> {
            //     setRedirect(true)}))
            // .catch(
            //     async (res) => {
            //         const data = await res.json();
            //         if (data && data.errors) setErrors(data.errors);
            //     }
            // );
        }
    }

    return (
        <form className='product_modal' onSubmit={handleSubmit} >
            <h2>{formType}</h2>
            <h3>Let's get started</h3>
            <ul >
                {errors.map((error, idx) => <li className='error' key={idx}>{error}</li>)}
            </ul>
            <label className='pageInput'>
                Price
                <input
                    type="number"
                    value={price}
                    onChange={e => setPrice(e.target.value)}
                    required
                    />
            </label>
            <label>
                Original price
                <input
                    className='pageInput'
                    type="number"
                    value={original_price}
                    onChange={e => setOriginal_price(e.target.value)}

                    />
            </label>
            <label>
                Inventory
                <input
                    className='pageInput'
                    type="text"
                    value={inventory}
                    onChange={e => setInventory(e.target.value)}
                    required
                    />
            </label>
            <label>
                desc
                <input
                    className='pageInput'
                    type="text"
                    value={desc}
                    onChange={e => setDesc(e.target.value)}
                    required
                    />
            </label>

            <p>Let us know more about your spot <br/>Enter Your House Details </p>

            <label>
                Shipping fee
                <input
                    className='pageInput'
                    type="text"
                    value={shipping_fee}
                    onChange={e => setShipping_fee(e.target.value)}
                    required
                    />
            </label>
            <label>
                Delivery Days
                <input
                    className='pageInput'
                    type="number"
                    value={delivery_days}
                    onChange={e => setDelivery_days(e.target.value)}
                    required
                    />
            </label>
            <label>
                Preview Image
                <input
                    className='pageInput'
                    type="url"
                    value={preview_image}
                    onChange={e => setPreview_image(e.target.value)}
                    required
                    />
            </label>
            <input className="pageButton" type="submit" value={formType} />
        </form>
    )
}

export default ProductForm
