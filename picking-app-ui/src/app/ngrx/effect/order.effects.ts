import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { of } from 'rxjs';
import { catchError, map, mergeMap } from 'rxjs/operators';
import {loadPickListDataFailure, loadPickListData, loadPickListDataSuccess} from "../action/pick-list.actions";
import {PickService} from "../../services/pick.service";

@Injectable()
export class OrderEffects {
  constructor(
    private actions$: Actions,
    private pickService: PickService,
  ) {}

  loadOrders$ = createEffect(() => this.actions$.pipe(
    ofType(loadPickListData),
    mergeMap(() => this.pickService.getPickListData()
      .pipe(
        map(orders => {
          return loadPickListDataSuccess({ orders })
        }),
        catchError(error => of(loadPickListDataFailure({ error })))
      ))
  ));
}
