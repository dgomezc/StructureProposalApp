import { Component, OnInit } from '@angular/core';

import { ListService } from './list.service';
import { IListItem } from './list.model';
import { Subject, Observable } from 'rxjs';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {
  listItems$: Observable<IListItem[]> = new Observable();
  private dataSource: Subject<IListItem[]> = new Subject();
  warningMessageText = '';
  warningMessageOpen = false;

  constructor(private listService: ListService) {}

  ngOnInit(): void {
    this.listItems$ = this.dataSource.asObservable();
    this.loadItems();
  }

  loadItems(): void {
    this.listService.getListItems().subscribe(
      (listItem: IListItem[]) => this.dataSource.next(listItem),
      error => this.handleError(`Request to get list items failed: ${error}`)
    );
  }

  addItem(inputText: string): void {
    this.listService.addListItem(inputText).subscribe(
      () => this.loadItems(), error => this.handleError(`Request to add item failed: ${error}`)
    );
  }

  deleteItem(id: string): void {
    this.listService.deleteListItem(id).subscribe(
      () => this.loadItems(), error => this.handleError(`Request to delete item failed: ${error}`)
    );
  }

  handleWarningClose(open: boolean): void {
    this.warningMessageOpen = open;
    this.warningMessageText = '';
  }

  private handleError(warningMessageText: string): void {
    this.warningMessageOpen = true;
    this.warningMessageText = warningMessageText;
  }
}
