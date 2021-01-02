import { Component, Input, OnInit, Output } from '@angular/core';
import { EventEmitter } from 'events';
import { Task, Task1 } from './task';


// import {colorDate2} from './script.js';
// declare var tesing: any;


function colorDate2(date: string) {
  let calculatedAge = (new Date(date).getTime() - new Date().getTime()) / 3600000;
  calculatedAge = Math.round(calculatedAge / 24);
  alert(calculatedAge)
  if (calculatedAge < 2) {
      return 'task-red';
  } else if (calculatedAge < 10) {
      return 'task-yellow'; 
  } else {
      return 'task-green';
  }
}


@Component({
  selector: 'app-task',
  templateUrl: './task.component.html',
  styleUrls: ['./task.component.css']
})
export class TaskComponent implements OnInit {
  @Input() task: Task1; 
  @Output() edit = new EventEmitter();
   
  constructor() { this.task = { Name:'', Yrke: '', Annonstitel:'', Arbetsgivare: '', Sistadatum: '', url: '' } };

  ngOnInit(): void {
  };

}