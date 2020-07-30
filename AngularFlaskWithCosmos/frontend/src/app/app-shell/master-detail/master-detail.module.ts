import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MasterDetailComponent } from './master-detail.component';
import { MasterListComponent } from './master-list/master-list.component';
import { WarningMessageModule } from '../../shared/warning-message/warning-message.module';
import { DetailComponent } from './detail/detail.component';
import { MasterDetailRoutingModule } from './master-detail-routing.module';

@NgModule({
  declarations: [MasterDetailComponent, MasterListComponent, DetailComponent],
  imports: [
    CommonModule,
    WarningMessageModule,
    MasterDetailRoutingModule
  ]
})
export class MasterDetailModule { }
