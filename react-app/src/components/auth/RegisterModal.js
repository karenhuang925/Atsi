import React, { useState } from 'react';
import { Modal } from '../../context/Modal';
import SignUpForm from './SignUpForm';
import { useSelector } from 'react-redux';

function RegisterModal() {
    const [showModal, setShowModal] = useState(false);
    const user = useSelector(state => state.session.user);

    if (user) {
        return (
        <button>
            {`Hi ${user.first_name}`}
        </button>)
    }
    return (
        <>
            <button className='flex items-center justify-center rounded-2xl border border-black bg-white py-1 px-3 text-sm font-medium text-black hover:shadow focus:ring-2 focus:ring-black-100 focus:ring-offset-2' onClick={() => setShowModal(true)}>Register</button>
            {showModal && (
                <Modal onClose={() => setShowModal(false)}>
                    <SignUpForm />
                </Modal>
            )}
        </>
    );
}

export default RegisterModal;
