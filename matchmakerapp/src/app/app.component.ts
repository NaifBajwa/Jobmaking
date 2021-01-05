import { CdkDragDrop, transferArrayItem } from '@angular/cdk/drag-drop';
import { Component } from '@angular/core';
import { Task, Task1 } from './task/task';
import todo2 from '../assets/Matchning3.json'
import inProgress2 from '../assets/InProgress2.json'
import done2 from '../assets/DoneFile2.json'
import { AngularFirestore, AngularFirestoreCollection } from '@angular/fire/firestore';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'kanban-fire';
  // todo = this.store.collection('todo').valueChanges({ idField: 'id' });
  // inProgress = this.store.collection('inProgress').valueChanges({ idField: 'id' });
  // done = this.store.collection('done').valueChanges({ idField: 'id' });

  todo1: Task[] = [
    { title: 'Buy milk', description: 'Go to the store and buy milk.' },
    { title: 'Buy ogogoro', description: 'Go to system and buy ogogoro.' },
    { title: 'Create Kanban board', description: 'Develop a Kanban app' }
  ];

// todo : any['Observable<QuerySnapshot<unknown>>'] = this.store.collection('matchnin').doc('AEA3iF0gCJLaXq2peZaf');

// phone: string;
// email: string;
// iprogram: string;
// todo: Task1[] = 
//  [
//   {
//       "ID": "rec0TGDtfNq5k5oh0",
//       "Name": "Lena Andersson",
//       "Yrke": "S\u00e4ljare",
//       "num": "2",
//       "phone": "0762361001",
//       "email": "Lena.Andersson@gmail.com",
//       "iprogram": "Ja",
//       "jobb" :[ 
//         {
//         "id": "1",
//         "Annonstitel": "S\u00e4ljare Region Nord \u2013 V\u00e4sterbotten, V\u00e4sternorrland och J\u00e4mtland",
//         "Arbetsgivare": "Ramudden AB",
//         "Sistadatum": "2020-12-30",
//         "url": "http://www.cnn.com",
//       },
//       {
//       "id": "2",
//       "Annonstitel": "S\u00e4ljare Region Nord \u2013 V\u00e4sterbotten, V\u00e4sternorrland och J\u00e4mtland",
//       "Arbetsgivare": "Ramudden AB",
//       "Sistadatum": "2020-12-30",
//       "url": "http://www.cnn.com",
//     } ]
//   },
//   {
//       "ID": "rec0TGDtfNq5k5oh0",
//       "Name": "Anders Andersson",
//       "Yrke": "S\u00e4ljare",
//       "num": "1",
//       "phone": "0762361002",
//       "email": "Anders.Andersson@gmail.com",
//       "iprogram": "Nej",
//       "jobb" :[ 
//         {
//         "id": "1",
//         "Annonstitel": "S\u00e4ljare Region Nord \u2013 V\u00e4sterbotten, V\u00e4sternorrland och J\u00e4mtland",
//         "Arbetsgivare": "Ramudden AB",
//         "Sistadatum": "2020-12-30",
//         "url": "http://www.cnn.com",
//       }]
//   },
//   {
//       "ID": "rec0TGDtfNq5k5oh0",
//       "Name": "Marie Andersson",
//       "Yrke": "S\u00e4ljare",
//       "num": "3",
//       "phone": "0762361003",
//       "email": "Marie.Andersson@gmail.com",
//       "iprogram": "Ja",
//       "jobb" :[ 
//         {
//         "id": "1",
//         "Annonstitel": "S\u00e4ljare Region Nord \u2013 V\u00e4sterbotten, V\u00e4sternorrland och J\u00e4mtland",
//         "Arbetsgivare": "Ramudden AB",
//         "Sistadatum": "2020-12-30",
//         "url": "http://www.cnn.com",
//         },
//         {
//         "id": "2",
//         "Annonstitel": "S\u00e4ljare Region Nord \u2013 V\u00e4sterbotten, V\u00e4sternorrland och J\u00e4mtland",
//         "Arbetsgivare": "Ramudden AB",
//         "Sistadatum": "2020-12-30",
//         "url": "http://www.cnn.com",
//         },
//         {
//         "id": "3",
//         "Annonstitel": "S\u00e4ljare Region Nord \u2013 V\u00e4sterbotten, V\u00e4sternorrland och J\u00e4mtland",
//         "Arbetsgivare": "Ramudden AB",
//         "Sistadatum": "2020-12-30",
//         "url": "http://www.cnn.com",
//         }  ]
//   }   
//   // ,
//   // {
//   //     "ID": "rec0Vl8QMVAwOgvv6",
//   //     "Name": "karin Karlsson",
//   //     "Yrke": "Lastbilsf\u00f6rare",
//   //     "Annonstitel": "CE-chauff\u00f6rer s\u00f6kes f\u00f6r start omg\u00e5ende!",
//   //     "Arbetsgivare": "Nordic BR Norr AB",
//   //     "Sistadatum": "2020-12-31",
//   //     "url": "http://www.bcc.com"
//   // },
//   // {
//   //     "ID": "rec0gIaNjqFByL76P",
//   //     "Name": "Ali Ramalah",
//   //     "Yrke": "L\u00e4rare i grundskolan",
//   //     "Annonstitel": "L\u00e4rare i Samh\u00e4llsorienterade \u00e4mnen till N\u00e4ldens skola, J\u00e4mtland",
//   //     "Arbetsgivare": "Krokoms kommun",
//   //     "Sistadatum": "2021-01-01",
//   //     "url": "http://www.dn.se"
//   // },
//   // {
//   //     "ID": "rec1Bk2dk4ZdTXTez",
//   //     "Name": "Ingrid Larsson",
//   //     "Yrke": "Snickare",
//   //     "Annonstitel": "Mockfj\u00e4rds F\u00f6nster s\u00f6ker montagef\u00f6retag till V\u00e4sternorrland",
//   //     "Arbetsgivare": "Mockfj\u00e4rds F\u00f6nster AB",
//   //     "Sistadatum": "2021-01-07",
//   //     "url": "http://www.sr.se"
//   // },
//   // {
//   //     "ID": "rec26K5HeLY7xsWfh",
//   //     "Name": "Owen Sten",
//   //     "Yrke": "Utvecklare",
//   //     "Annonstitel": "Utvecklare/samordnare inom social h\u00e5llbarhet ",
//   //     "Arbetsgivare": "L\u00e4nsstyrelsen i V\u00e4sternorrlands l\u00e4n",
//   //     "Sistadatum": "2021-01-09",
//   //     "url": "http://www.svt.se"
//   // },
//   // {
//   //     "ID": "rec2GSsvKIVuUwZ2q",
//   //     "Name": "Ahmed Farah",
//   //     "Yrke": "L\u00e4kare",
//   //     "Annonstitel": "Tv\u00e5 vikarierande underl\u00e4kare i barn- och ungdomsmedicin vid \u00d6stersunds sjuk",
//   //     "Arbetsgivare": "REGION J\u00c4MTLAND H\u00c4RJEDALEN",
//   //     "Sistadatum": "2021-01-31",
//   //     "url": "http://www.st.nu"
//   // }
//   ];

//   inProgress: Task1[] = [
//     {
//         "ID": "rec0TGDtfNq5k5oh0",
//         "Name": "Per Andersson",
//         "Yrke": "S\u00e4ljare",
//         "num": "3",
//         "phone": "0762361004",
//         "email": "Per.Andersson@gmail.com",
//         "iprogram": "Nej",
//         "jobb" :[ 
//           {
//           "id": "1",
//           "Annonstitel": "S\u00e4ljare Region Nord \u2013 V\u00e4sterbotten, V\u00e4sternorrland och J\u00e4mtland",
//           "Arbetsgivare": "Ramudden AB",
//           "Sistadatum": "2020-12-30",
//           "url": "http://www.cnn.com",
//           },
//           {
//           "id": "2",
//           "Annonstitel": "S\u00e4ljare Region Nord \u2013 V\u00e4sterbotten, V\u00e4sternorrland och J\u00e4mtland",
//           "Arbetsgivare": "Ramudden AB",
//           "Sistadatum": "2020-12-30",
//           "url": "http://www.cnn.com",
//           },
//           {
//           "id": "3",
//           "Annonstitel": "S\u00e4ljare Region Nord \u2013 V\u00e4sterbotten, V\u00e4sternorrland och J\u00e4mtland",
//           "Arbetsgivare": "Ramudden AB",
//           "Sistadatum": "2020-12-30",
//           "url": "http://www.cnn.com",
//           }  ]
//     }];
//   done: Task1[] = [];

  todo: Task1[] = todo2;
  inProgress: Task1[] = inProgress2;
  done: Task1[] = done2;

  constructor( private store: AngularFirestore) {
    // this.store
    // .collection("matchnin")
    // .add(this.done[1])
    // .add({'id': '2333', 'Annonstitel':'Bla bla bla','Name': 'Najj', 'Sistadatum':'2021-01-09', 'Yrke': 'Yrke', 'url':'#'})
    // .then(res => {}, err => '');
    
    // console.log('Reading JSON');
    // console.log({'id': '2333', 'Annonstitel':'Bla bla bla','Name': 'Najj', 'Sistadatum':'2021-01-09', 'Yrke': 'Yrke', 'url':'#'});
  }

  drop(event: CdkDragDrop<Task1[]>): void {
    if (event.previousContainer == event.container){
      return;
    }
    transferArrayItem(
      event.previousContainer.data,
      event.container.data,
      event.previousIndex,
      event.currentIndex
    );
  }

  edit(list: string, task: Task1): void {

  }

  // newTask(){
  //   const dialogRef = this.dialog.open(TaskDialogComponent, {
  //     width: '270px',
  //     data: {
  //       task: {}
  //     }
  //   });
  //   dialogRef
  //   .afterClosed()
  //   .subscribe((result: TaskDialogResult) => this.todo.push(result.task) );
  // }
}
