import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


import {environment} from '../../environments/environment';
@Injectable({
  providedIn: 'root'
})
export class HistorialEntrenamientoService {
  private apiUrl = `${environment.endpoint}/historial/`; 
  constructor(private http: HttpClient) {




   }

   obtenerHistorial(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }
}
