import { Component } from '@angular/core';
import {MatDialogRef} from "@angular/material/dialog";
import {FormsModule} from "@angular/forms";

@Component({
  selector: 'app-exception-modal',
  standalone: true,
  imports: [
    FormsModule
  ],
  templateUrl: './exception-modal.component.html',
  styleUrl: './exception-modal.component.scss'
})
export class ExceptionModalComponent {
  exceptionReason: string = '';

  constructor(public dialogRef: MatDialogRef<ExceptionModalComponent>) {}

  onNoClick(): void {
    this.dialogRef.close();
  }
}
