import { createReducer, on } from '@ngrx/store';
import {loadPickListDataSuccess} from "../action/pick-list.actions";

export interface PickListState {
  pickListData: any[];
  loading: boolean;
  error: any;
}

export const initialState: PickListState = {
  pickListData: [],
  loading: false,
  error: null
};

export const pickListReducer = createReducer(
  initialState,
  on(loadPickListDataSuccess, (state, { pickListData }) => {
    return ({
      ...state,
      pickListData: pickListData,
      loading: false,
      error: null
    })
  })
);
