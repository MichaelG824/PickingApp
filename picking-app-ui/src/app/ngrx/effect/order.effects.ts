import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { of } from 'rxjs';
import { catchError, map, mergeMap } from 'rxjs/operators';
import {loadOrders, loadOrdersFailure, loadOrdersSuccess} from "../action/order.actions";
import {DataService} from "../../services/orders.service";

@Injectable()
export class OrderEffects {
  constructor(
    private actions$: Actions,
    private dataService: DataService
  ) {}

  loadOrders$ = createEffect(() => this.actions$.pipe(
    ofType(loadOrders),
    mergeMap(() => this.dataService.getOrders()
      .pipe(
        map(orders => {
          return loadOrdersSuccess({ orders })
        }),
        catchError(error => of(loadOrdersFailure({ error })))
      ))
  ));



}
