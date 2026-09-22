import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetalleServidor } from './detalle-servidor';

describe('DetalleServidor', () => {
  let component: DetalleServidor;
  let fixture: ComponentFixture<DetalleServidor>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DetalleServidor],
    }).compileComponents();

    fixture = TestBed.createComponent(DetalleServidor);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
