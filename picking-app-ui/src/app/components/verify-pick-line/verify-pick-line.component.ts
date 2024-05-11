import {Component, OnInit} from '@angular/core';
import {Store} from "@ngrx/store";
import {ActivatedRoute} from "@angular/router";
import {loadCurrentPick} from "../../ngrx/action/pick.actions";
import {selectCurrentPick} from "../../ngrx/selectors/pick.selector";

@Component({
  selector: 'app-verify-pick-line',
  standalone: true,
  imports: [],
  templateUrl: './verify-pick-line.component.html',
  styleUrl: './verify-pick-line.component.scss'
})
export class VerifyPickLineComponent implements OnInit {
  currentPick: any;
  pickId: string | undefined;

  constructor(private store: Store,  private route: ActivatedRoute) { }

  ngOnInit(): void {
    console.log('hit this file')
    this.route.params.subscribe((params: { [x: string]: any; }) => {
      this.pickId = params['pickId'];
      console.log('PickId: ', this.pickId);
      this.store.dispatch(loadCurrentPick({ currentPickId: this.pickId }))
    });
    this.store.select(selectCurrentPick).subscribe((currentPick) => {
      console.log('Current pick: ', currentPick);
      this.currentPick = currentPick;
    });
  }
}
