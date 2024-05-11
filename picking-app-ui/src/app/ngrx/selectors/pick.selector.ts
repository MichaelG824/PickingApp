import { createFeatureSelector, createSelector } from '@ngrx/store';
import {PickState} from "../reducers/pick.reducer";

export const selectOrderFeature = createFeatureSelector<PickState>('picks');

export const selectCurrentPick = createSelector(
  selectOrderFeature,
  (state: PickState) => state.currentPick
);

export const selectPickIds= createSelector(
  selectOrderFeature,
  (state: PickState) => state.pickIds
)

export const selectCurrentPickIndex = createSelector(
  selectOrderFeature,
  (state: PickState) => state.currentIndex
)
export const providePickSelectors = () => [
  selectCurrentPick,
  selectPickIds,
  selectCurrentPickIndex,
];
