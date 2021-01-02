// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.

export const environment = {
  production: false,
  
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  firebase: {
    apiKey: "AIzaSyDjKmdDOb21JymyfkkgDru9c6zHfE-sCh8",
    authDomain: "jobbmatchningar.firebaseapp.com",
    databaseURL: 'https://kanban-fire-workshop.firebaseio.com',
    projectId: "jobbmatchningar",
    storageBucket: "jobbmatchningar.appspot.com",
    messagingSenderId: "670927707210",
    appId: "1:670927707210:web:879c8830e82a87d7715ab3",
    measurementId: "G-7151EHMKCR",
    production: true
  }
};

/* production: boolean;
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.
