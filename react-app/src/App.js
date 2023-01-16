import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import NavBar from './components/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
import Profile from './components/Profile';
import User from './components/User';
import HomePage from './components/Homepage'
import ProductDetail from './components/ProductDetail'
import ProfileProduct from './components/ProfileProduct'
import PlaceOrder from './components/PlaceOrder'
import { authenticate } from './store/session';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar />
      <Switch>
        <ProtectedRoute path='/users/my/' exact={true} >
          <Profile/>
        </ProtectedRoute>
        <Route path='/users/:userId/products/' exact={true} >
          <ProfileProduct />
        </Route>
        <Route path='/products/:productId/' exact={true} >
          <ProductDetail />
        </Route>
        <Route path='/order/new' exact={true} >
          <PlaceOrder />
        </Route>
        <Route path='/' exact={true} >
          <HomePage />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
