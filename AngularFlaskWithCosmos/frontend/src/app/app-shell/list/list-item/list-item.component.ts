import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { IListItem } from '../list.model';

@Component({
  selector: 'app-list-item',
  templateUrl: './list-item.component.html',
  styleUrls: ['./list-item.component.css']
})
export class ListItemComponent implements OnInit {
  // tslint:disable-next-line:variable-name
  @Input() id: string;
  @Input() listItem: IListItem;
  @Output() deleteItem = new EventEmitter<string>();

  constructor() {}

  ngOnInit(): void {}

  deleteItemFn(): void {
    this.deleteItem.emit(this.id);
  }
}
