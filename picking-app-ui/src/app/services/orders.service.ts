import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  BASE_URL = 'http://127.0.0.1:3000'
  constructor(private http: HttpClient) { }

  getOrders(): Observable<any> {
    return this.http.get(`${this.BASE_URL}/api/v1/picks/get-pick-list-data`);
  }
}
