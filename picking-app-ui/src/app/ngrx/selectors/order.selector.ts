import { createFeatureSelector, createSelector } from '@ngrx/store';
import { OrderState } from '../reducers/order.reducer';

export const selectOrderFeature = createFeatureSelector<OrderState>('orders');

export const selectAllOrders = createSelector(
  selectOrderFeature,
  (state: OrderState) => state.orders
);

export const provideOrderSelectors = () => [
  selectAllOrders
];
