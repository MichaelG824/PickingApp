import {Component, OnInit} from '@angular/core';
import {Store} from "@ngrx/store";
import {ActivatedRoute} from "@angular/router";
import {
  loadCurrentPick,
  navigateNextPick,
  updateCurrentPick,
  updateCurrentPickIndex
} from "../../ngrx/action/pick.actions";
import {selectCurrentPick, selectCurrentPickIndex} from "../../ngrx/selectors/pick.selector";
import {PickFormComponent} from "../pick-form/pick-form.component";
import {CurrentPickDetailsComponent} from "../current-pick-details/current-pick-details.component";

@Component({
  selector: 'app-verify-pick-line',
  standalone: true,
  imports: [
    PickFormComponent,
    CurrentPickDetailsComponent
  ],
  templateUrl: './verify-pick-line.component.html',
  styleUrl: './verify-pick-line.component.scss'
})
export class VerifyPickLineComponent implements OnInit {
  currentPick: any;
  pickId: string | undefined;
  pickIndex: number;

  constructor(private store: Store,  private route: ActivatedRoute) {
    this.pickIndex = 0;
  }

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
    this.store.select(selectCurrentPickIndex).subscribe((pickIndex) => {
      this.pickIndex = pickIndex;
    });
  }

  handleException(exceptionDetail: string) {
    this.store.dispatch(updateCurrentPick({ currentPickId: this.pickId, exceptionDetail, status: 'Exception' }));
    this.store.dispatch(updateCurrentPickIndex({ currentIndex: this.pickIndex + 1 }));
  }

  handlePickSubmission(pickInfo: any) {
    this.store.dispatch(updateCurrentPick({ currentPickId: this.pickId, status: 'Picked' }));
    this.store.dispatch(updateCurrentPickIndex({ currentIndex: this.pickIndex + 1 }));
  }
}
