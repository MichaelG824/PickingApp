import {Component, Input} from '@angular/core';
import {NgForOf} from "@angular/common";
import {Router} from "@angular/router";

@Component({
  selector: 'app-current-pick-details',
  standalone: true,
  imports: [
    NgForOf
  ],
  templateUrl: './current-pick-details.component.html',
  styleUrl: './current-pick-details.component.scss'
})
export class CurrentPickDetailsComponent {
  @Input() currentPick: any;

  constructor(private router: Router) {}

  public async navigateToPickList() {
    await this.router.navigate(['/pick-list']);

  }
}
