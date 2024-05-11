import {Component, OnInit} from '@angular/core';
import {Store} from "@ngrx/store";
import {ActivatedRoute} from "@angular/router";
import {
  loadCurrentPick, loadPickIds,
  updateCurrentPick,
  updateCurrentPickIndex
} from "../../ngrx/action/pick.actions";
import {selectCurrentPick, selectCurrentPickIndex, selectPickIds} from "../../ngrx/selectors/pick.selector";
import {PickFormComponent} from "../pick-form/pick-form.component";
import {CurrentPickDetailsComponent} from "../current-pick-details/current-pick-details.component";
import {selectAllOrders} from "../../ngrx/selectors/order.selector";
import {loadOrders} from "../../ngrx/action/order.actions";

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
  pickId: number;
  pickIndex: number;

  constructor(private store: Store,  private route: ActivatedRoute) {
    this.pickIndex = 0;
    this.pickId = -1;
  }

  ngOnInit(): void {
    this.store.select(selectAllOrders).subscribe((orders: any) => {
      if (!orders?.length) {
        this.store.dispatch(loadOrders());
      } else {
        this.getPicksFromPickListAndLoad(orders);
      }
    });
    this.route.params.subscribe((params: { [x: string]: any; }) => {
      this.pickId = Number(params['pickId']);
      this.store.dispatch(loadCurrentPick({ currentPickId: this.pickId }))
    });
    this.store.select(selectCurrentPick).subscribe((currentPick) => {
      this.currentPick = currentPick;
    });
    this.store.select(selectCurrentPickIndex).subscribe((pickIndex) => {
      this.pickIndex = pickIndex;
    });

    this.store.select(selectPickIds).subscribe((pickIds) => {
      const currentIndex= pickIds.indexOf(this.pickId);
      if (currentIndex > -1) {
        this.store.dispatch(updateCurrentPickIndex({ currentIndex }));
      }
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
  private getPicksFromPickListAndLoad(orders: { itemNames: any[]; }[]) {
    const pickIds = orders.flatMap((order: { itemNames: any[]; }) => order.itemNames.map(item => item.pickId));
    console.log('PickIds: ', pickIds);
    this.store.dispatch(loadPickIds({ pickIds }))
  }
}
