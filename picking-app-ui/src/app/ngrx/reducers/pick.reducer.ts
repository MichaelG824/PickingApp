import {createReducer, on} from "@ngrx/store";
import {loadOrdersSuccess} from "../action/order.actions";
import {loadCurrentPickSuccess} from "../action/pick.actions";

export interface PickState {
  pickIds: number[];
  currentIndex: number;
  currentPick: any;
  loading: boolean;
  error: any;
}

export const initialState: PickState = {
  pickIds: [],
  currentIndex: 0,
  currentPick: null,
  loading: false,
  error: null
};

export const pickReducer = createReducer(
  initialState,
  on(loadCurrentPickSuccess, (state, { currentPick }) => {
    console.log('hit current pick reducer: ', currentPick);
    return ({
      ...state,
      currentPick: currentPick,
      loading: false,
      error: null,
    })
  })
);
