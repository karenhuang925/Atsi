import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect } from 'react-router-dom';
import { login } from '../../store/session';
import RegisterModal from './RegisterModal'

const LoginForm = ({setShowLoginModal}) => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };


  return (
    <div>
      <div className='flex justify-between mb-3'>
        <p className='text-2xl'>Sign in</p>
        <RegisterModal onClose={()=>setShowLoginModal(false)}/>
      </div>
      <form onSubmit={onLogin}>
        <div>
          {errors.map((error, ind) => (
            <div key={ind} className='text-low-red'>{error}</div>
          ))}
        </div>
        <div className='flex flex-col mb-4'>
          <label htmlFor='email' className=''>Email address</label>
          <input
            name='email'
            type='text'
            value={email}
            onChange={updateEmail}
            className='h-12 border border-b-2 shadow-inner rounded-lg pl-3'
          />
        </div>
        <div className='flex flex-col mb-4'>
          <label htmlFor='password'>Password</label>
          <input
            name='password'
            type='password'
            value={password}
            onChange={updatePassword}
            className='h-12 border border-b-2 shadow-inner rounded-lg pl-3'

          />
          <button type='submit' className=" w-full mt-10 flex items-center justify-center rounded-3xl border border-transparent bg-gray-900 py-3 px-10 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">Sign in</button>
        </div>
      </form>
    </div>
  );
};

export default LoginForm;
