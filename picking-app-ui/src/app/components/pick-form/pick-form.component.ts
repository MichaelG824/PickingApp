import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {FormControl, FormGroup, ReactiveFormsModule, Validators} from "@angular/forms";
import {ExceptionModalComponent} from "../exception-modal/exception-modal.component";
import {MatDialog} from "@angular/material/dialog";

@Component({
  selector: 'app-pick-form',
  standalone: true,
  imports: [
    ReactiveFormsModule
  ],
  templateUrl: './pick-form.component.html',
  styleUrl: './pick-form.component.scss'
})
export class PickFormComponent implements OnInit {
  pickForm!: FormGroup;
  @Input() currentPick: any;
  @Output() handleExceptionEvent = new EventEmitter<any>();
  @Output() handleSubmitEvent = new EventEmitter<any>();


  constructor(public dialog: MatDialog) {}
  ngOnInit() {
    this.pickForm = new FormGroup({
      location: new FormControl(this.currentPick?.location, [Validators.required]),
      sku: new FormControl(this.currentPick?.sku, [Validators.required]),
      title: new FormControl(this.currentPick?.title, [Validators.required]),
      quantity: new FormControl(this.currentPick?.pickQty, [Validators.required, Validators.min(1)])
    });
  }
  onSubmit() {
    console.log('Form submitted:', this.pickForm?.value);
    this.handleSubmitEvent.emit(this.pickForm?.value);
  }

  openExceptionModal() {
    const dialogRef = this.dialog.open(ExceptionModalComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log('The exception dialog was closed', result);
      if (result) {
        this.handleException(result);
      }
    });
  }

  private handleException(exceptionReason: string) {
    this.handleExceptionEvent.emit(exceptionReason);
  }
}
