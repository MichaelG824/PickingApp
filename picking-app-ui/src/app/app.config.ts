import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';
import {HTTP_INTERCEPTORS, provideHttpClient, withInterceptorsFromDi} from "@angular/common/http";
import { provideStore } from '@ngrx/store';
import { pickListReducer } from './ngrx/reducers/pick-list.reducer';
import { provideEffects } from "@ngrx/effects";
import { PickListEffects } from "./ngrx/effect/pick-list.effects";
import {PickEffects} from "./ngrx/effect/pick.effects";
import {pickReducer} from "./ngrx/reducers/pick.reducer";
import {providePickSelectors} from "./ngrx/selectors/pick.selector";
import {CamelSnakeInterceptor} from "./interceptors/camel-snake-interceptor";
import {providePickListSelectors} from "./ngrx/selectors/pick-list.selector";

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideHttpClient(withInterceptorsFromDi()),
    provideStore({ pickList: pickListReducer, picks: pickReducer }),
    provideEffects([PickListEffects, PickEffects]),
    providePickListSelectors(),
    providePickSelectors(),
    {
      provide: HTTP_INTERCEPTORS,
      useClass: CamelSnakeInterceptor,
      multi: true
    }
  ]
};
