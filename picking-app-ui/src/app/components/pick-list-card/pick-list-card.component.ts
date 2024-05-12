import {Component, Input} from '@angular/core';
import {NgClass} from "@angular/common";

@Component({
  selector: 'app-pick-list-card',
  standalone: true,
  imports: [
    NgClass
  ],
  templateUrl: './pick-list-card.component.html',
  styleUrl: './pick-list-card.component.scss'
})
export class PickListCardComponent {
  @Input() pick: any;
}
