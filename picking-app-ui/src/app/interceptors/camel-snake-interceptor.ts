import { Injectable } from '@angular/core';
import { HttpEvent, HttpInterceptor, HttpHandler, HttpRequest, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { decamelizeKeys, camelizeKeys } from 'humps';

@Injectable()
export class CamelSnakeInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const modifiedReq = req.clone({ body: decamelizeKeys(req.body) });
    console.log('Modified Request: ', modifiedReq);
    return next.handle(modifiedReq).pipe(
      map(event => {
        if (event instanceof HttpResponse && event.body) {
          console.log('Received response', event);
          return event.clone({ body: camelizeKeys(event.body) });
        }
        return event;
      })
    );
  }
}
