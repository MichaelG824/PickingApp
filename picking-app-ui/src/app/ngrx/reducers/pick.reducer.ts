import {createReducer, on} from "@ngrx/store";
import {
  loadCurrentPickSuccess,
  loadPickIdsSuccess,
  updateCurrentPickIndexSuccess
} from "../action/pick.actions";

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
    return ({
      ...state,
      currentPick: currentPick,
      loading: false,
      error: null,
    })
  }),
  on(loadPickIdsSuccess, (state, { pickIds }) => {
    return ({
      ...state,
      pickIds,
      loading: false,
      error: null,
    })
  }),
  on(updateCurrentPickIndexSuccess, (state, { currentIndex }) => {
    return ({
      ...state,
      currentIndex,
      loading: false,
      error: null,
    })
  })
);
