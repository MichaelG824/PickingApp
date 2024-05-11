import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {
  PickListComponent
} from "./components/pick-list/pick-list.component";
import {VerifyPickLineComponent} from "./components/verify-pick-line/verify-pick-line.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, PickListComponent, VerifyPickLineComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'picking-app-ui';
}
