import { Component, OnInit } from '@angular/core';
import { RestService } from './rest.service';
import { JobData } from './JobData';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  isShow = false;

toggleDisplay() {
  console.log("searching");
this.isShow = !this.isShow;
}

  title = 'AngularFlask';

  constructor(private rs : RestService){}

  headers = ["Job Description","Company","Name"]

  data : JobData[] = [];

  ngOnInit()
  {
      this.rs.readData()
      .subscribe
        (
          (response) =>
          {
            this.data= response[0]["data"];
          },
          (error) =>
          {
            console.log("No Data Found" + error);
          }

        )





  // readData()
  // {
  //   this.rs.readFile()
  //   .subscribe
  //       (
  //         (response) =>
  //         {
  //           this.weather = response[0]["data"];
  //         },
  //         (error) =>
  //         {
  //           console.log("File doesn't exist..." + error);
  //         }

  //       )
  // }

}
}
