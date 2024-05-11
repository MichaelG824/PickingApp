import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';
import { provideHttpClient } from "@angular/common/http";
import { provideStore } from '@ngrx/store';
import { orderReducer } from './ngrx/reducers/order.reducer';
import { provideEffects } from "@ngrx/effects";
import { OrderEffects } from "./ngrx/effect/order.effects";
import { provideOrderSelectors } from "./ngrx/selectors/order.selector";
import {PickEffects} from "./ngrx/effect/pick.effects";
import {pickReducer} from "./ngrx/reducers/pick.reducer";
import {providePickSelectors} from "./ngrx/selectors/pick.selector";

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideHttpClient(),
    provideStore({ orders: orderReducer, picks: pickReducer }), // Provide the feature state key
    provideEffects([OrderEffects, PickEffects]),
    provideOrderSelectors(),
    providePickSelectors()
  ]
};
