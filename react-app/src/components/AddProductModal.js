import React, { useState } from 'react';
import { Modal } from '../context/Modal';
import { useSelector } from 'react-redux';
import ProductForm from './ProductForm'

function AddProductModal() {
    const [showModal, setShowModal] = useState(false);
    const user = useSelector(state => state.session.user);
    const product = {
        category_id: 1,
        title: 'abc',
        price: 0,
        original_price: 0,
        inventory: 10,
        desc: 0,
        shipping_fee: 0,
        delivery_days: 1,
        preview_image: ''
    };

    return (
        <>
            <div onClick={()=>setShowModal(true)}>
                <button className='flex items-center justify-center rounded-xl border border-black bg-white py-1 px-4 text-base font-medium text-black hover:shadow focus:ring-2 focus:ring-black-100 focus:ring-offset-2 mr-3'>
                <i className='fa-solid fa-edit'></i> Add product</button>
            </div>
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    <ProductForm formtype='Add' product={product}/>
                </Modal>
            )}
        </>
    );
}

export default AddProductModal;
