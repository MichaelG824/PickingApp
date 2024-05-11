// src/app/store/reducers/order.reducer.ts
import { createReducer, on } from '@ngrx/store';
import {loadOrdersSuccess} from "../action/order.actions";

export interface OrderState {
  orders: any[];
  loading: boolean;
  error: any;
}

export const initialState: OrderState = {
  orders: [],
  loading: false,
  error: null
};

export const orderReducer = createReducer(
  initialState,
  on(loadOrdersSuccess, (state, { orders }) => {
    console.log('hit orders reducer: ', orders);
    return ({
      ...state,
      orders: orders,
      loading: false,
      error: null
    })
  })
);
