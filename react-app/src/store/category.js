// constants
const SET_CATEGORY = 'category/SET_CATEGORY';

const setCategory = (category) => ({
  type: SET_CATEGORY,
  payload: category
});

const initialState =  null ;

export const get_categories = () => async (dispatch) => {
  const response = await fetch('/api/categories/', {
    headers: {
      'Content-Type': 'application/json'
    }
  });
  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return;
    }
    dispatch(setCategory(data));
  }
}

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case SET_CATEGORY:
      return action.payload.Category
    default:
      return state;
  }
}
