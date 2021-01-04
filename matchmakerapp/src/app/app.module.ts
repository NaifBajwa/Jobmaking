import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { TaskComponent } from './task/task.component';
import { MatCardModule } from '@angular/material/card';
import { DragDropModule } from '@angular/cdk/drag-drop';
import { MatButtonModule } from '@angular/material/button';
import { MatDialogModule, MAT_DIALOG_DEFAULT_OPTIONS } from '@angular/material/dialog';
// import { TaskDialogComponent } from './task-dialog/task-dialog.component';
// import { EventsComponent } from './events/events.component';
// import { EditComponent } from './edit/edit.component';
// import { FormsModule } from '@angular/forms';
// import { MatInputModule } from '@angular/material/input'

import { environment } from 'src/environments/environment';
import { AngularFireModule } from '@angular/fire';
import { AngularFirestoreModule } from '@angular/fire/firestore';

import { DailogboxComponent } from './dailogbox/dailogbox.component';
import {MatBadgeModule} from '@angular/material/badge';




@NgModule({
  declarations: [
    AppComponent,
    TaskComponent,
    DailogboxComponent
    // TaskDialogComponent,
    // EventsComponent,
    // EditComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatIconModule,
    MatToolbarModule,
    MatCardModule,
    DragDropModule,
    MatButtonModule,
    MatDialogModule,
    MatBadgeModule,
    
    AngularFireModule.initializeApp(environment.firebase),
    AngularFirestoreModule
    // FormsModule,
    // MatInputModule
  ],
  providers: [DailogboxComponent], // , {provide: MAT_DIALOG_DEFAULT_OPTIONS, useValue: {hasBackdrop: false}}
  bootstrap: [AppComponent]
})
export class AppModule { }



// import { BrowserModule } from '@angular/platform-browser';
// import { NgModule } from '@angular/core';

// import { AppComponent } from './app.component';
// import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
// import { MatToolbarModule } from '@angular/material/toolbar';
// import { MatIconModule } from '@angular/material/icon';
// import { TaskComponent } from './task/task.component';
// import { MatCardModule } from '@angular/material/card';
// import { DragDropModule } from '@angular/cdk/drag-drop';
// import { MatButtonModule } from '@angular/material/button';
// import { MatDialogModule } from '@angular/material/dialog';
// // import { TaskDialogComponent } from './task-dialog/task-dialog.component';
// // import { EventsComponent } from './events/events.component';
// // import { EditComponent } from './edit/edit.component';
// // import { FormsModule } from '@angular/forms';
// // import { MatInputModule } from '@angular/material/input'

// import { environment } from 'src/environments/environment';
// import { AngularFireModule } from '@angular/fire';
// import { AngularFirestoreModule } from '@angular/fire/firestore';
// import { DailogboxComponent } from './dailogbox/dailogbox.component';




// @NgModule({
//   declarations: [
//     AppComponent,
//     TaskComponent
//     // DailogboxComponent
//     // MatDialogModule
//     // TaskDialogComponent,
//     // EventsComponent,
//     // EditComponent
//   ],
//   imports: [
//     BrowserModule,
//     BrowserAnimationsModule,
//     MatIconModule,
//     MatToolbarModule,
//     MatCardModule,
//     DragDropModule,
//     MatButtonModule,
    
//     AngularFireModule.initializeApp(environment.firebase),
//     AngularFirestoreModule
//     // FormsModule,
//     // MatInputModule
//   ],

//   entryComponents: [
//     DailogboxComponent
//   ],

//   providers: [],
//   bootstrap: [AppComponent]
// })
// export class AppModule { }
