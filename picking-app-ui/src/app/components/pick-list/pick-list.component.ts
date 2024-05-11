import { Component, OnInit } from '@angular/core';
import {NgClass, NgForOf} from "@angular/common";
import {Store} from "@ngrx/store";
import {loadOrders} from "../../ngrx/action/order.actions";
import {selectAllOrders} from "../../ngrx/selectors/order.selector";
import {Router} from "@angular/router";
import {loadPickIds, updateCurrentPickIndex} from "../../ngrx/action/pick.actions";
import {selectPickIds} from "../../ngrx/selectors/pick.selector";
import {take} from "rxjs";

@Component({
  selector: 'app-pick-list',
  standalone: true,
  imports: [
    NgForOf,
    NgClass
  ],
  templateUrl: './pick-list.component.html',
  styleUrl: './pick-list.component.scss'
})
export class PickListComponent implements OnInit {
  orders: any = [];

  constructor(private store: Store,  private router: Router) { }

  ngOnInit(): void {
    this.store.dispatch(loadOrders());
    this.store.select(selectAllOrders).subscribe((orders: any) => {
      this.orders = orders;
      // Fill out the pick id array
      this.getPicksFromPickListAndLoad(this.orders);
    });
  }

  public async navigateToDetail(pickId: number) {

    this.store.select(selectPickIds).pipe(take(1)).subscribe((pickIds) => {
      const currentIndex= pickIds.indexOf(pickId);
      this.store.dispatch(updateCurrentPickIndex({ currentIndex }));

    });
  }

  private getPicksFromPickListAndLoad(orders: { itemNames: any[]; }[]) {
    const pickIds = orders.flatMap((order: { itemNames: any[]; }) => order.itemNames.map(item => item.pickId));
    console.log('PickIds', pickIds);
    this.store.dispatch(loadPickIds({ pickIds }))
  }
}
