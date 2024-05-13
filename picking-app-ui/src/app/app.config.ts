import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';
import {HTTP_INTERCEPTORS, provideHttpClient, withInterceptorsFromDi} from "@angular/common/http";
import { provideStore } from '@ngrx/store';
import { orderReducer } from './ngrx/reducers/order.reducer';
import { provideEffects } from "@ngrx/effects";
import { OrderEffects } from "./ngrx/effect/order.effects";
import { provideOrderSelectors } from "./ngrx/selectors/order.selector";
import {PickEffects} from "./ngrx/effect/pick.effects";
import {pickReducer} from "./ngrx/reducers/pick.reducer";
import {providePickSelectors} from "./ngrx/selectors/pick.selector";
import {CamelSnakeInterceptor} from "./interceptors/camel-snake-interceptor";

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideHttpClient(withInterceptorsFromDi()),
    provideStore({ orders: orderReducer, picks: pickReducer }),
    provideEffects([OrderEffects, PickEffects]),
    provideOrderSelectors(),
    providePickSelectors(),
    {
      provide: HTTP_INTERCEPTORS,
      useClass: CamelSnakeInterceptor,
      multi: true
    }
  ]
};
