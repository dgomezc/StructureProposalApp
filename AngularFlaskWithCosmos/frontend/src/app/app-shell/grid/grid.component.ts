import { Component, OnInit } from '@angular/core';

import { GridService } from './grid.service';
import { IGridItem } from './grid.model';
import {catchError, map} from 'rxjs/operators';
import {Observable, of} from 'rxjs';

@Component({
  selector: 'app-grid',
  templateUrl: './grid.component.html',
  styleUrls: ['./grid.component.css']
})
export class GridComponent implements OnInit {
  greyBoxUrl = '../../../assets/GreyBox.svg';
  warningMessageText = '';
  warningMessageOpen = false;
  gridItems$: Observable<IGridItem[]>;

  constructor(private gridService: GridService) {}

  ngOnInit(): void {
    this.gridItems$ = this.gridService.getGridItems().pipe(catchError((error) => {
      this.warningMessageText =  `Request to get grid text failed: ${error}`;
      this.warningMessageOpen = true;
      return of(null);
    }));
  }

  handleWarningClose(open: boolean): void {
    this.warningMessageOpen = open;
    this.warningMessageText = '';
  }
}
