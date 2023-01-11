import React, { useState } from 'react';
import { Modal } from '../context/Modal';
import { useSelector } from 'react-redux';
import ProductForm from './ProductForm'

function AddProductModal() {
    const [showModal, setShowModal] = useState(false);
    const user = useSelector(state => state.session.user);
    const product = {
        category_id: 1,
        title: 'Colour cloud - Flowers - Floral - Art Print -Coloured Lino Print - Hand Printed - Wall Art - Block Print- Digital Print',
        price: 20,
        original_price: 30,
        inventory: 10,
        desc: 'This is a digital reproduction of an original lino print. It is taken from the #luizaholub100dayprintproject Instagram: @luizaholu',
        shipping_fee: 0,
        delivery_days: 1,
        preview_image: 'https://i.etsystatic.com/9765767/r/il/13cc71/2870974651/il_1588xN.2870974651_dycz.jpg'
    };

    return (
        <>
            <div onClick={()=>setShowModal(true)}>
                <button className='flex items-center justify-center rounded-xl border border-black bg-white py-1 px-4 text-base font-medium text-black hover:shadow focus:ring-2 focus:ring-black-100 focus:ring-offset-2 mr-3'>
                <i className='fa-solid fa-edit mr-2'></i> Add product</button>
            </div>
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    <ProductForm formType='Add' product={product} setShowModal={setShowModal}/>
                </Modal>
            )}
        </>
    );
}

export default AddProductModal;
