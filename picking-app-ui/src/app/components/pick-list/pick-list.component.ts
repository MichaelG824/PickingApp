import { Component, OnInit } from '@angular/core';
import {NgForOf} from "@angular/common";
import {Store} from "@ngrx/store";
import {loadOrders} from "../../ngrx/action/order.actions";
import {selectAllOrders} from "../../ngrx/selectors/order.selector";
import {Router} from "@angular/router";

@Component({
  selector: 'app-pick-list',
  standalone: true,
  imports: [
    NgForOf
  ],
  templateUrl: './pick-list.component.html',
  styleUrl: './pick-list.component.scss'
})
export class PickListComponent implements OnInit {
  orders: any = [];

  constructor(private store: Store,  private router: Router) { }

  ngOnInit(): void {
    this.store.dispatch(loadOrders());
    this.store.select(selectAllOrders).subscribe((orders) => {
      this.orders = orders;
    });
  }

  public async navigateToDetail(pickId: number) {
    console.log('Pick Id: ', pickId);
    // get pickId, find in
    await this.router.navigate(['/verify-pick', pickId]);
  }
}
