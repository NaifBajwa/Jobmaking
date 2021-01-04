import { Component, OnInit, Input, Inject } from '@angular/core';
import {MatDialog, MAT_DIALOG_DATA} from '@angular/material/dialog';
import { Task, Task1 } from '../task/task';

@Component({
  selector: 'app-dailogbox',
  templateUrl: './dailogbox.component.html',
  styleUrls: ['./dailogbox.component.css'],
})
export class DailogboxComponent implements OnInit {

  hidden = false;
  toggleBadgeVisibility() {
    this.hidden = !this.hidden;
  }

  constructor(@Inject(MAT_DIALOG_DATA) public data: { task: Task1; }) { }

  ngOnInit(): void {
  }
  
}