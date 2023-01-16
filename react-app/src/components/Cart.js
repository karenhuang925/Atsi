import { Fragment, useState, useEffect } from 'react'
import { Dialog, Transition } from '@headlessui/react'
import { XMarkIcon } from '@heroicons/react/24/outline'
import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { get_cart_fetch, edit_cart_fetch, create_cart_fetch, delete_cart_fetch } from '../store/cart'
import { useHistory } from 'react-router-dom'

export default function Cart({cartOpen, setCartOpen}) {
    let history = useHistory();
    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user);


    useEffect(()=> {
        dispatch(get_cart_fetch())
    },[dispatch, user])

    const cart = useSelector((state => state.cart))
    const products = useSelector((state => state.cart?.Items))

    const removeItemHandle = (id) => {
        let updateItem = {product_id: id, quantity: 0}
        dispatch(edit_cart_fetch(updateItem))
    }

    const checkoutHandle = () => {
        setCartOpen(false)
        dispatch(delete_cart_fetch())
        history.push('/order/new')
    }

    // if(!cart){
    //     return null
    // }
    return (
        <Transition.Root show={cartOpen} as={Fragment}>
        <Dialog as="div" className="relative z-10 " onClose={setCartOpen}>
            <Transition.Child
            as={Fragment}
            enter="ease-in-out duration-500"
            enterFrom="opacity-0"
            enterTo="opacity-100"
            leave="ease-in-out duration-500"
            leaveFrom="opacity-100"
            leaveTo="opacity-0"
            >
            <div className="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
            </Transition.Child>

            <div className="fixed inset-0 overflow-hidden">
            <div className="absolute inset-0 overflow-hidden">
                <div className="pointer-events-none fixed inset-y-0 right-0 flex max-w-full pl-10">
                <Transition.Child
                    as={Fragment}
                    enter="transform transition ease-in-out duration-500 sm:duration-700"
                    enterFrom="translate-x-full"
                    enterTo="translate-x-0"
                    leave="transform transition ease-in-out duration-500 sm:duration-700"
                    leaveFrom="translate-x-0"
                    leaveTo="translate-x-full"
                >
                    <Dialog.Panel className="pointer-events-auto w-screen max-w-md">
                    <div className="flex h-full flex-col overflow-y-scroll bg-white shadow-xl">
                        <div className="flex-1 overflow-y-auto py-6 px-4 sm:px-6">
                        <div className="flex items-start justify-between">
                            <Dialog.Title className="text-lg font-medium text-gray-900">Shopping cart</Dialog.Title>
                            <div className="ml-3 flex h-7 items-center">
                            <button
                                type="button"
                                className="-m-2 p-2 text-gray-400 hover:text-gray-500"
                                onClick={() => setCartOpen(false)}
                            >
                                <span className="sr-only">Close panel</span>
                                <XMarkIcon className="h-6 w-6" aria-hidden="true" />
                            </button>
                            </div>
                        </div>

                        <div className="mt-8">
                            <div className="flow-root">
                            <ul role="list" className="-my-6 divide-y divide-gray-200">
                                {products?.length == 0 && (
                                    <div className="flex py-6"><h1>Empty Cart</h1></div>
                                )}
                                {cart == null && (
                                    <div className="flex py-6"><h1>Empty Cart</h1></div>
                                )}
                                {products?.map((product) => (
                                <li key={product.id} className="flex py-6">
                                    <div className="h-24 w-24 flex-shrink-0 overflow-hidden rounded-md border border-gray-200">
                                    <img
                                        src={product.product.preview_image}
                                        alt={product.product.title}
                                        className="h-full w-full object-cover object-center"
                                    />
                                    </div>

                                    <div className="ml-4 flex flex-1 flex-col">
                                    <div>
                                        <div className="flex justify-between text-base font-medium text-gray-900">
                                        <h3 className='overflow-hidden wt-text-truncate'>
                                            <a href={`/products/${product.product.id}`}>{product.product.title}</a>
                                        </h3>
                                        <p className="ml-4">${product.product.price}</p>
                                        </div>
                                    </div>
                                    <div className="flex flex-1 items-end justify-between text-sm">
                                        <p className="text-gray-500">Qty {product.quantity}</p>

                                        <div className="flex">
                                        <button
                                            type="button"
                                            className="font-medium text-indigo-600 hover:text-indigo-500"
                                            onClick={()=>removeItemHandle(product.product_id)}
                                        >
                                            Remove
                                        </button>
                                        </div>
                                    </div>
                                    </div>
                                </li>
                                ))}
                            </ul>
                            </div>
                        </div>
                        </div>

                        <div className="border-t border-gray-200 py-6 px-4 sm:px-6">
                        <div className="flex justify-between text-base font-medium text-gray-900">
                            <p>Subtotal</p>
                            <p>${cart?.amount?.toFixed(2) || 0}</p>
                        </div>
                        <p className="mt-0.5 text-sm text-gray-500">By clicking place order, you agree to pay this amount</p>
                        {cart ? <div className="mt-6">
                            <a
                            onClick={checkoutHandle}
                            className="cursor-pointer flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-6 py-3 text-base font-medium text-white shadow-sm hover:bg-indigo-700"
                            >
                            Place Order
                            </a>
                        </div> : <div className="mt-6 ">
                            <div
                            className="cursor-not-allowed flex items-center justify-center rounded-md border border-transparent bg-gray-500 px-6 py-3 text-base font-medium text-white shadow-sm "
                            >
                            Place Order
                            </div>
                        </div>}
                        <div className="mt-6 flex justify-center text-center text-sm text-gray-500">
                            <p>
                            or
                            <button
                                type="button"
                                className="font-medium text-indigo-600 hover:text-indigo-500 ml-2"
                                onClick={() => setCartOpen(false)}
                            >
                                Continue Shopping
                                <span aria-hidden="true"> &rarr;</span>
                            </button>
                            </p>
                        </div>
                        </div>
                    </div>
                    </Dialog.Panel>
                </Transition.Child>
                </div>
            </div>
            </div>
        </Dialog>
        </Transition.Root>
    )
}
