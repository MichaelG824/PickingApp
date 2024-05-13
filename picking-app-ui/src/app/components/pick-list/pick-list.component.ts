import { Component, OnInit } from '@angular/core';
import {NgClass, NgForOf} from "@angular/common";
import {Store} from "@ngrx/store";
import {selectAllOrders} from "../../ngrx/selectors/order.selector";
import {Router} from "@angular/router";
import {PickListCardComponent} from "../pick-list-card/pick-list-card.component";
import {loadPickListData} from "../../ngrx/action/pick-list.actions";


@Component({
  selector: 'app-pick-list',
  standalone: true,
  imports: [
    NgForOf,
    NgClass,
    PickListCardComponent
  ],
  templateUrl: './pick-list.component.html',
  styleUrl: './pick-list.component.scss'
})
export class PickListComponent implements OnInit {
  orders: any = [];

  constructor(private store: Store,  private router: Router) { }

  ngOnInit(): void {
    this.store.dispatch(loadPickListData());
    this.store.select(selectAllOrders).subscribe((orders: any) => {
      this.orders = orders;
    });
  }

  public async navigateToDetail(pickId: number) {
    await this.router.navigate(['/verify-pick', pickId]);
  }
}
