import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListaServidores } from './lista-servidores';

describe('ListaServidores', () => {
  let component: ListaServidores;
  let fixture: ComponentFixture<ListaServidores>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListaServidores],
    }).compileComponents();

    fixture = TestBed.createComponent(ListaServidores);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
