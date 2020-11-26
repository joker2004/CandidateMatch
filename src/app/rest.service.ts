import { Injectable, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { JobData } from './JobData';

@Injectable({
  providedIn: 'root'
})
export class RestService implements OnInit {

  constructor(private http : HttpClient) { }

  ngOnInit(){
  }

  dataUrl : string = "http://127.0.0.1:5000/jobData/";

  readData()
  {
    return this.http.get<JobData[]>(this.dataUrl);
  }
}
