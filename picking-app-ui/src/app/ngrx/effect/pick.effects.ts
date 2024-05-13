import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import {of, switchMap, take, withLatestFrom} from 'rxjs';
import { catchError, map, mergeMap } from 'rxjs/operators';
import {
  loadCurrentPick,
  loadCurrentPickFailure,
  loadCurrentPickSuccess,
  loadPickIds,
  loadPickIdsFailure,
  loadPickIdsSuccess,
  updateCurrentPick,
  updateCurrentPickIndex,
  updateCurrentPickIndexFailure,
  updateCurrentPickIndexSuccess,
  updateCurrentPickSuccess
} from "../action/pick.actions";
import {PickService} from "../../services/pick.service";
import {Router} from "@angular/router";
import {select, Store} from "@ngrx/store";
import {selectPickIds} from "../selectors/pick.selector";

@Injectable()
export class PickEffects {
  constructor(
    private actions$: Actions,
    private pickService: PickService,
    private router: Router,
    private store: Store,
  ) {}

  loadCurrentPick$ = createEffect(() => this.actions$.pipe(
    ofType(loadCurrentPick),
    mergeMap(({ currentPickId }) => this.pickService.getCurrentPick(currentPickId)
      .pipe(
        map(pick => {
          return loadCurrentPickSuccess({ currentPick: pick })
        }),
        catchError(error => of(loadCurrentPickFailure({ error })))
      ))
  ));
  updateCurrentPick$ = createEffect(() => this.actions$.pipe(
    ofType(updateCurrentPick),
    mergeMap(({ currentPickId, status, exceptionDetails }) => this.pickService.updateCurrentPick(currentPickId, status, exceptionDetails)
      .pipe(
        map(pick => {
          return updateCurrentPickSuccess({ currentPick: pick })
        }),
        catchError(error => of(loadCurrentPickFailure({ error })))
      ))
  ));
  loadPickIds$ = createEffect(() => this.actions$.pipe(
    ofType(loadPickIds),
    map(({ pickIds }) => {
      return loadPickIdsSuccess({ pickIds });
    }),
    catchError(error => of(loadPickIdsFailure({ error })))
  ));
  updateCurrentPickIndex$ = createEffect(() => this.actions$.pipe(
    ofType(updateCurrentPickIndex),
    withLatestFrom(this.store.pipe(select(selectPickIds))),
    switchMap(([{ currentIndex }, pickIds]) => {
      if (pickIds.length === 0) {
        return of(updateCurrentPickIndexFailure({ error: 'No pickIds found from store' }));
      }
      const newIndex = currentIndex % pickIds.length;
      return this.router.navigate(['/verify-pick', pickIds[newIndex]]).then(() => {
        return updateCurrentPickIndexSuccess({ currentIndex: newIndex });
      }).catch(error => updateCurrentPickIndexFailure({ error }));
    }),
    catchError(error => of(updateCurrentPickIndexFailure({ error })))
  ));
}
