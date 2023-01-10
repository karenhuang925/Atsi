import React, { useState } from 'react';
import { Modal } from '../../context/Modal';
import { useSelector } from 'react-redux';

function AddProductModal() {
    const [showModal, setShowModal] = useState(false);
    const user = useSelector(state => state.session.user);
    const product = {
        address: 'abc',
        city: 'abc',
        state: 'abc',
        country: 'abc',
        name: 'abc',
        lat: 0,
        lng: 0,
        description: 'abc',
        price: 0,
        previewImage: ''
    };


    return (
        <>
            <div>
                <button className='flex items-center justify-center rounded-xl border border-black bg-white py-1 px-4 text-base font-medium text-black hover:shadow focus:ring-2 focus:ring-black-100 focus:ring-offset-2 mr-3'>
                <i className='fa-solid fa-edit'></i> Add product</button>
            </div>
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
            <form className='pageForm' onSubmit={handleSubmit} >
            <h2>{formType}</h2>
            <h3>Let's get started</h3>
            <p>Where's your place located? Enter your address</p>
            <ul >
                {errors.map((error, idx) => <li className='error' key={idx}>{error}</li>)}
            </ul>
            <label className='pageInput'>
                Address
                <input
                    type="text"
                    value={address}
                    onChange={e => setAddress(e.target.value)}
                    required
                    />
            </label>
            <label>
                City
                <input
                    className='pageInput'
                    type="text"
                    value={city}
                    onChange={e => setCity(e.target.value)}
                    required
                    />
            </label>
            <label>
                State
                <input
                    className='pageInput'
                    type="text"
                    value={state}
                    onChange={e => setState(e.target.value)}
                    required
                    />
            </label>
            <label>
                Country
                <input
                    className='pageInput'
                    type="text"
                    value={country}
                    onChange={e => setCountry(e.target.value)}
                    required
                    />
            </label>

            <p>Let us know more about your spot <br/>Enter Your House Details </p>

            <label>
                Name
                <input
                    className='pageInput'
                    type="text"
                    value={name || ""}
                    onChange={e => setName(e.target.value)}
                    required
                    />
            </label>
            <label>
                Price
                <input
                    className='pageInput'
                    type="number"
                    value={price}
                    onChange={e => setPrice(e.target.value)}
                    required
                    />
            </label>
            <label>
                Description
                <input
                    className='pageInput'
                    type="text"
                    value={description}
                    onChange={e => setDescription(e.target.value)}
                    required
                    />
            </label>
            <label>
                lat
                <input
                    className='pageInput'
                    type="number"
                    value={lat}
                    onChange={e => setLat(e.target.value)}
                    />
            </label>
            <label>
                lng
                <input
                    className='pageInput'
                    type="number"
                    value={lng}
                    onChange={e => setLng(e.target.value)}
                    />
            </label>
            <label>
                PreviewImage
                <input
                    className='pageInput'
                    type="url"
                    value={previewImage}
                    onChange={e => setPreviewImage(e.target.value)}
                    required
                    />
            </label>
            <input className="pageButton" type="submit" value={formType} />
        </form>
                </Modal>
            )}
        </>
    );
}

export default AddProductModal;
