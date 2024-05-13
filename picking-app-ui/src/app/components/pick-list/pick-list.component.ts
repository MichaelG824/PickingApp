import { Component, OnInit } from '@angular/core';
import {NgClass, NgForOf} from "@angular/common";
import {Store} from "@ngrx/store";
import {Router} from "@angular/router";
import {PickListCardComponent} from "../pick-list-card/pick-list-card.component";
import {loadPickListData} from "../../ngrx/action/pick-list.actions";
import {selectPickListData} from "../../ngrx/selectors/pick-list.selector";


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
  pickListData: any = [];

  constructor(private store: Store,  private router: Router) { }

  ngOnInit(): void {
    this.store.dispatch(loadPickListData());
    this.store.select(selectPickListData).subscribe((pickListData: any) => {
      this.pickListData = pickListData;
    });
  }

  public async navigateToDetail(pickId: number) {
    await this.router.navigate(['/verify-pick', pickId]);
  }
}
