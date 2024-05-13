import { createAction, props } from '@ngrx/store';

export const loadPickListData= createAction('[PickList] Load Pick List Data');
export const loadPickListDataSuccess= createAction('[PickList] Load Pick List Success', props<{ orders: any }>());
export const loadPickListDataFailure= createAction('[PickList] Load Orders Failure', props<{ error: any }>());
