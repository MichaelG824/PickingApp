import { createFeatureSelector, createSelector } from '@ngrx/store';
import {PickListState} from "../reducers/pick-list.reducer";

export const selectPickListFeature= createFeatureSelector<PickListState>('pickList');

export const selectPickListData= createSelector(
  selectPickListFeature,
  (state: PickListState) => state.pickListData
);

export const providePickListSelectors = () => [
  selectPickListData
];
