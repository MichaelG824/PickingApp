import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {FormControl, FormGroup, ReactiveFormsModule, Validators} from "@angular/forms";
import {ExceptionModalComponent} from "../exception-modal/exception-modal.component";
import {MatDialog} from "@angular/material/dialog";
import { ValidatorFn, AbstractControl } from '@angular/forms';

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
  _currentPick: any;
  @Output() handleExceptionEvent = new EventEmitter<any>();
  @Output() handleSubmitEvent = new EventEmitter<any>();
  @Input() set currentPick(value: any) {
    this._currentPick = value;
    this.updateForm();
  }

  constructor(public dialog: MatDialog) {}
  ngOnInit() {
    this.pickForm = new FormGroup({
      location: new FormControl('', [Validators.required]),
      skuOrTitle: new FormControl('', [Validators.required]),
      quantity: new FormControl('', [Validators.required, Validators.min(1)])
    });
  }
  onSubmit() {
    this.handleSubmitEvent.emit(this.pickForm?.value);
  }

  openExceptionModal() {
    const dialogRef = this.dialog.open(ExceptionModalComponent);

    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        this.handleException(result);
      }
    });
  }

  private handleException(exceptionReason: string) {
    this.handleExceptionEvent.emit(exceptionReason);
  }

  private updateForm() {
    if (this._currentPick && this.pickForm) {
      this.pickForm.controls['location'].setValidators([Validators.required, this.currentPickValidator([this._currentPick.location])]);
      this.pickForm.controls['skuOrTitle'].setValidators([Validators.required, this.currentPickValidator([this._currentPick.sku.toString(), this._currentPick.title])]);
      this.pickForm.controls['quantity'].setValidators([Validators.required, this.currentPickValidator([this._currentPick.pickQty])]);

      this.pickForm.patchValue({
        location: this._currentPick.location,
        skuOrTitle: '',
        quantity: this._currentPick.pickQty
      });

      this.pickForm.updateValueAndValidity();
    }
  }

  currentPickValidator(validValues: any[]): ValidatorFn {
    return (control: AbstractControl): { [key: string]: any } | null => {
      const isMatching = validValues.includes(control.value);
      return isMatching ? null : { 'valueMismatch': { value: control.value } };
    };
  }
}
