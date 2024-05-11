import { Routes } from '@angular/router';
import {PickListComponent} from "./components/pick-list/pick-list.component";
import {VerifyPickLineComponent} from "./components/verify-pick-line/verify-pick-line.component";

export const routes: Routes = [
  { path: 'orders', component: PickListComponent },
  { path: 'verify-pick/:pickId', component: VerifyPickLineComponent },
  { path: '', redirectTo: '/orders', pathMatch: 'full' }
];

