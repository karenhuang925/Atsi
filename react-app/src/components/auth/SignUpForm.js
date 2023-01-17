import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect, useHistory } from 'react-router-dom';
import { signUp } from '../../store/session';
import { LockClosedIcon } from '@heroicons/react/20/solid'
import { create_cart_fetch } from '../../store/cart';


const SignUpForm = () => {
  const [errors, setErrors] = useState([]);
  const [firstName, setFirstName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const [disableSubmit, setDisableSubmit] = useState(true);
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  const history = useHistory()

  useEffect(() => {
    const errors = [];
    if((firstName.length < 2) || (firstName.trim().length === 0)) errors.push("- Invalid first name");
    if(!email.includes("@") || !email.endsWith(".com")) errors.push("- Invalid email");
    if(password.length < 5) errors.push("- Password length must be greater than 4 characters.");
    if(repeatPassword.length < 5) errors.push("- Repeat Password length must be greater than 4 characters.");
    setErrors(errors)
    if(!errors.length) setDisableSubmit(false)
}, [firstName, email, password, repeatPassword]);


  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const data = await dispatch(signUp(email, firstName, password));
      if (data) {
        setErrors(data)
      }
    }
    else {
      errors.push("- Passwords don't match")
    }
    dispatch(create_cart_fetch())
    history.push('/')

  };

  const updateFirstName = (e) => {
    setFirstName(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (user) {
    history.push('/')
  }

  return (
    <form onSubmit={onSignUp} className='auth_modal'>
      <p className='text-2xl font-medium mb-3'>Create your account</p>
      <p className='text-xl mb-5'>Registration is easy</p>
      <div>
        {errors.map((error, ind) => (
          <div key={ind} className='text-low-red mb-3 '>{error}</div>
        ))}
      </div>
      <div className='flex flex-col mb-4'>
        <label className="flex flex-row">Email <p className='text-low-red pl-2'>*</p>
        </label>
        <input
          type='text'
          name='email'
          onChange={updateEmail}
          value={email}
          required={true}
          className='h-12 border border-b-2 shadow-inner rounded-lg pl-3'

        ></input>
      </div>
      <div className='flex flex-col mb-4'>
        <label className="flex flex-row">First name <p className='text-low-red pl-2'>*</p>
        </label>
        <input
          type='text'
          name='firstName'
          onChange={updateFirstName}
          value={firstName}
          required={true}
          className='h-12 border border-b-2 shadow-inner rounded-lg pl-3'

        ></input>
      </div>
      <div className='flex flex-col mb-4'>
      <label className="flex flex-row">Password <p className='text-low-red pl-2'>*</p>
        </label>
        <input
          type='password'
          name='password'
          onChange={updatePassword}
          value={password}
          required={true}
          className='h-12 border border-b-2 shadow-inner rounded-lg pl-3'

        ></input>
      </div>
      <div className='flex flex-col mb-4'>
      <label className="flex flex-row">Repeat password<p className='text-low-red pl-2'>*</p>
        </label>
        <input
          type='password'
          name='repeat_password'
          onChange={updateRepeatPassword}
          value={repeatPassword}
          required={true}
          className='h-12 border border-b-2 shadow-inner rounded-lg pl-3'

        ></input>
      </div>
      <button type='submit' disabled={disableSubmit} className=" w-full mt-10 flex items-center justify-center rounded-3xl border border-transparent bg-gray-900 py-3 px-10 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">
        {disableSubmit &&
          <span className="flex items-center pr-6">
          <LockClosedIcon className="h-5 w-5 text-indigo-500 group-hover:text-indigo-400"/>
        </span>}
      Register</button>
    </form>
  );
};

export default SignUpForm;
