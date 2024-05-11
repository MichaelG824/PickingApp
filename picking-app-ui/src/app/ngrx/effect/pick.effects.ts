import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { of } from 'rxjs';
import { catchError, map, mergeMap } from 'rxjs/operators';
import {loadCurrentPick, loadCurrentPickFailure, loadCurrentPickSuccess} from "../action/pick.actions";
import {PickService} from "../../services/pick.service";

@Injectable()
export class PickEffects {
  constructor(
    private actions$: Actions,
    private pickService: PickService
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

}
