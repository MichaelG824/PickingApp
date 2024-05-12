import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PickService {
  BASE_URL = 'http://0.0.0.0:8000'
  constructor(private http: HttpClient) { }

  getCurrentPick(id: any): Observable<any> {
    console.log('Get Current Pick ID: ', id);
    return this.http.get(`${this.BASE_URL}/api/v1/picks/${id}`);
  }

  updateCurrentPick(pickId: number, status: string, exceptionDetails: string | undefined): Observable<any> {
    return this.http.put(`${this.BASE_URL}/api/v1/picks/update-status-and-exception-details`, { pickId, status, exceptionDetails });
  }
}
