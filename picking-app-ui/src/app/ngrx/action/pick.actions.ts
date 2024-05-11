// src/app/store/actions/item.actions.ts
import { createAction, props } from '@ngrx/store';

export const navigateNextPick = createAction('[Item] Navigate Next Pick');
export const navigateNextPickSuccess = createAction('[Item] Navigate Next Pick Success', props<{ nextPick: any }>());
export const navigateNextPickFailure = createAction('[Item] Navigate Next Pick Failure', props<{ error: any }>());


export const loadCurrentPick = createAction('[Pick] Load Current Pick', props<{ currentPickId: any }>());
export const loadCurrentPickSuccess = createAction('[Pick] Load Current Pick Success', props<{ currentPick: any }>());
export const loadCurrentPickFailure = createAction('[Pick] Load Current Pick Failure', props<{ error: any }>());
