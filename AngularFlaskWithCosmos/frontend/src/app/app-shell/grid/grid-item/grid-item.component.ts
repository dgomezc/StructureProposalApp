import { Component, OnInit, Input } from '@angular/core';
import { IGridItem } from '../grid.model';

@Component({
  selector: 'app-grid-item',
  templateUrl: './grid-item.component.html',
  styleUrls: ['./grid-item.component.css']
})
export class GridItemComponent implements OnInit {
  @Input() key: number;
  @Input() gridItem: IGridItem;

  constructor() {}

  ngOnInit(): void {}
}
