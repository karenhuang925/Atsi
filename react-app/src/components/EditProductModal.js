import React, { useState } from 'react';
import { Modal } from '../context/Modal';
import { useSelector } from 'react-redux';
import ProductForm from './ProductForm'

function EditProductModal({product}) {
    const [showModal, setShowModal] = useState(false);

    return (
        <>
            <div onClick={()=>setShowModal(true)}>
                <button className='flex items-center justify-center rounded-xl border border-black bg-white py-1 px-4 text-base font-medium text-black hover:shadow focus:ring-2 focus:ring-black-100 focus:ring-offset-2 mr-3'>
                <i className='fa-solid fa-edit mr-2'></i> Edit product</button>
            </div>
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    <ProductForm formType='Edit' product={product} setShowModal={setShowModal}/>
                </Modal>
            )}
        </>
    );
}

export default EditProductModal;
