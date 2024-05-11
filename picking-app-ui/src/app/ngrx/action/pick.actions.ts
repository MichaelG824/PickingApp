import { createAction, props } from '@ngrx/store';


export const navigateNextPick = createAction('[Item] Navigate Next Pick');
export const navigateNextPickSuccess = createAction('[Item] Navigate Next Pick Success', props<{ nextPick: any }>());
export const navigateNextPickFailure = createAction('[Item] Navigate Next Pick Failure', props<{ error: any }>());


export const loadCurrentPick = createAction('[Pick] Load Current Pick', props<{ currentPickId: any }>());
export const loadCurrentPickSuccess = createAction('[Pick] Load Current Pick Success', props<{ currentPick: any }>());
export const loadCurrentPickFailure = createAction('[Pick] Load Current Pick Failure', props<{ error: any }>());

export const updateCurrentPick = createAction('[Pick] Update Current Pick', props<{ currentPickId: any, status: any, exceptionDetail?: string }>());
export const updateCurrentPickSuccess = createAction('[Pick] Update Current Pick Success', props<{ currentPick: any }>());
export const updateCurrentPickFailure = createAction('[Pick] Update Current Pick Failure', props<{ error: any }>());

export const loadPickIds= createAction('[Pick] Load PickIds', props<{ pickIds: number[] }>());
export const loadPickIdsSuccess= createAction('[Pick] Load PickIds Success', props<{ pickIds: number[] }>());
export const loadPickIdsFailure= createAction('[Pick] Load PickIds Failure', props<{ error: any }>());

export const updateCurrentPickIndex= createAction('[Pick] Update Current Pick Index', props<{ currentIndex: number }>());
export const updateCurrentPickIndexSuccess= createAction('[Pick] Update Current Pick Index Success', props<{ currentIndex: number }>());
export const updateCurrentPickIndexFailure= createAction('[Pick] Update Current Pick Index Failure', props<{ error: any }>());
