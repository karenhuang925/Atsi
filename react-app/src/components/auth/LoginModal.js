import React, { useState, Fragment } from 'react';
import { Modal } from '../../context/Modal';
import LoginForm from './LoginForm';
import { useSelector } from 'react-redux';
import { Menu, Transition } from '@headlessui/react'
import { ChevronDownIcon } from '@heroicons/react/20/solid'
import { useDispatch } from 'react-redux';
import { Link } from 'react-router-dom'
import { logout } from '../../store/session';


function LoginFormModal() {
    const dispatch = useDispatch()
    const [showLoginModal, setShowLoginModal] = useState(false);
    const user = useSelector(state => state.session.user);
    function classNames(...classes) {
        return classes.filter(Boolean).join(' ')
    }
    const onLogout = async (e) => {
        await dispatch(logout());
    };

    if (user) {
        return (
            <>
            <Menu as="div" className="relative inline-block text-left">
      <div>
        <Menu.Button className="inline-flex w-full justify-center rounded-xl bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:ring-offset-gray-100">
        {`Hi ${user.first_name}`}
          <ChevronDownIcon className="-mr-1 ml-2 h-5 w-5" aria-hidden="true" />
        </Menu.Button>
      </div>

      <Transition
        as={Fragment}
        enter="transition ease-out duration-100"
        enterFrom="transform opacity-0 scale-95"
        enterTo="transform opacity-100 scale-100"
        leave="transition ease-in duration-75"
        leaveFrom="transform opacity-100 scale-100"
        leaveTo="transform opacity-0 scale-95"
      >
        <Menu.Items className="absolute right-0 z-10 mt-2 w-56 origin-top-right divide-y divide-gray-100 rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
          <div className="py-1">
            <Menu.Item>
              {({ active }) => (
                <Link
                  to="/users/my"
                  className={classNames(
                    active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                    'block px-4 py-2 text-sm'
                  )}
                >
                  Profile
                </Link>
              )}
            </Menu.Item>
          </div>
          <div className="py-1">
            <Menu.Item>
              {({ active }) => (
                <Link
                  to={`/users/${user.id}/products/`}
                  className={classNames(
                    active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                    'block px-4 py-2 text-sm'
                  )}
                >
                    Sell on Atsi
                </Link>
              )}
            </Menu.Item>
          </div>
          <div className="py-1">
            <Menu.Item>
              {({ active }) => (
                <a
                  onClick={onLogout}
                  className={classNames(
                    active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                    'block px-4 py-2 text-sm'
                  )}
                >
                  Sign out
                </a>
              )}
            </Menu.Item>
          </div>
        </Menu.Items>
      </Transition>
    </Menu>
        </>
        )
    }
    return (
        <>
            <button onClick={() => setShowLoginModal(true)}>Sign In</button>
            {showLoginModal && (
                <Modal onClose={() => setShowLoginModal(false)} >
                    <LoginForm setShowLoginModal={setShowLoginModal} className='auth_modal'/>
                </Modal>
            )}
        </>
    );
}

export default LoginFormModal;
