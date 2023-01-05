// constants
const SET_HOMEPAGE_PRODUCT = 'product/SET_HOMEPAGE_PRODUCT';
const SET_CATEGORY_PRODUCT = 'product/SET_CATEGORY_PRODUCT';
const SET_USER_PRODUCT = 'product/SET_USER_PRODUCT';
const SET_PRODUCT_DETAIL = 'product/SET_PRODUCT_DETAIL';
const ADD_PRODUCT = 'product/ADD_PRODUCT';
const EDIT_PRODUCT = 'product/EDIT_PRODUCT';
const DELETE_PRODUCT = 'product/DELETE_PRODUCT';

const setHomepageProduct = (product) => ({
  type: SET_HOMEPAGE_PRODUCT,
  payload: product
});
const setCategoryProduct = (product) => ({
  type: SET_CATEGORY_PRODUCT,
  payload: product
});
const setUserProduct = (product) => ({
  type: SET_USER_PRODUCT,
  payload: product
});
const setProductDetail = (product) => ({
  type: SET_PRODUCT_DETAIL,
  payload: product
});
const addProduct = (product) => ({
  type: ADD_PRODUCT,
  payload: product
});
const editProduct = (product) => ({
  type: EDIT_PRODUCT,
  payload: product
});
const deleteProduct = (id) => ({
  type: DELETE_PRODUCT,
  payload: id
});

const initialState =  [] ;

export const get_homepage_products_fetch = () => async (dispatch) => {
  const response = await fetch('/api/products/', {
    headers: {
      'Content-Type': 'application/json'
    }
  });
  if (response.ok) {
    const data = await response.json();
    if (data.errors) return
    dispatch(setHomepageProduct(data));
  }
}

export const get_category_products_fetch = (name) => async (dispatch) => {
  const response = await fetch(`/api/categories/${name}/products`, {
    headers: {
      'Content-Type': 'application/json'
    }
  });
  if (response.ok) {
    const data = await response.json();
    if (data.errors) return
    dispatch(setCategoryProduct(data));
  }
}
export const get_user_products_fetch = (userId) => async (dispatch) => {
  const response = await fetch(`/api/users/${userId}/products`, {
    headers: {
      'Content-Type': 'application/json'
    }
  });
  if (response.ok) {
    const data = await response.json();
    if (data.errors) return
    dispatch(setUserProduct(data));
  }
}
export const get_product_detail_fetch = (productId) => async (dispatch) => {
  const response = await fetch(`/api/products/${productId}`, {
    headers: {
      'Content-Type': 'application/json'
    }
  });
  if (response.ok) {
    const data = await response.json();
    if (data.errors) return
    dispatch(setProductDetail(data));
  }
}

export const add_product_fetch = (product) => async (dispatch) => {
  const response = await fetch(`/api/products`, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(product)
  });
  if (response.ok) {
    const data = await response.json();
    if (data.errors) return
    dispatch(addProduct(data));
  }
}
export const edit_product_fetch = (product, id) => async (dispatch) => {
  const response = await fetch(`/api/products/${id}`, {
    method: "PUT",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(product)
  });
  if (response.ok) {
    const data = await response.json();
    if (data.errors) return
    dispatch(editProduct(data));
  }
}
export const delete_product_fetch = (id) => async (dispatch) => {
  const response = await fetch(`/api/products/${id}`, {
    method: "DELETE",
  });
  if (response.ok) {
    const data = await response.json();
    if (data.errors) return
    dispatch(deleteProduct(id));
  }
}

export default function reducer(state = initialState, action) {
  let newState;
  switch (action.type) {
    case SET_HOMEPAGE_PRODUCT:
      newState = [...state,
                  ...action.payload.Products]
      return newState
    case SET_CATEGORY_PRODUCT:
      newState = {...state,
        ...action.payload.Products}
      return newState
    case SET_USER_PRODUCT:
      newState = {...state,
        ...action.payload.Products}
      return newState
    case SET_PRODUCT_DETAIL:
      newState = {...state,
        currentProduct: action.payload}
      return newState
    case ADD_PRODUCT:
      newState = {...state,
        currentProduct: action.payload}
      return newState
    case EDIT_PRODUCT:
      newState = {...state,
        currentProduct: action.payload}
      return newState
    case DELETE_PRODUCT:
      let productIndex;
      for (let i = 0; i < state.product.length; i++) {
        if (state?.product[i].id === action.payload) {
          productIndex = i;
          break
        }
      }
      newState = {
        ...state,
        product: [
          ...state.product,
        ],
      };
      newState.product.splice(productIndex, 1)
      return newState;
    default:
      return state;
  }
}
