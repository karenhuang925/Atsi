// constants
const SET_CART = 'cart/SET_CART';
const CREATE_CART = 'cart/CREATE_CART';
const EDIT_CART = 'cart/EDIT_CART';
const DELETE_CART = 'cart/DELETE_CART';

const setCart = (cart) => ({
  type: SET_CART,
  payload: cart
});
const createCart = (cart) => ({
  type: CREATE_CART,
  payload: cart
});
const editCart = (cart) => ({
  type: EDIT_CART,
  payload: cart
});
const deleteCart = () => ({
  type: DELETE_CART,
});

const initialState =  null ;

export const get_cart_fetch = () => async (dispatch) => {
  const response = await fetch('/api/carts/', {
    headers: {
      'Content-Type': 'application/json'
    }
  });
  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return;
    }
    dispatch(setCart(data));
  }
}
export const create_cart_fetch = () => async (dispatch) => {
  const response = await fetch('/api/carts/', {
    method: "POST"
  });
  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return;
    }
    dispatch(createCart(data));
  }
}
export const edit_cart_fetch = (itemInfo) => async (dispatch) => {
  const response = await fetch('/api/carts/', {
    method: "PUT",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(itemInfo)
  });
  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return;
    }
    dispatch(editCart(data));
  }
}
export const delete_cart_fetch = () => async (dispatch) => {
  const response = await fetch('/api/carts/', {
    method: "DELETE",
  });
  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return;
    }
    dispatch(deleteCart());
  }
}

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case SET_CART:
      return action.payload
    case CREATE_CART:
      return action.payload
    case EDIT_CART:
      return action.payload
    case DELETE_CART:
      return { cart: null }
    default:
      return state;
  }
}
