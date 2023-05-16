## app.html

{{title}}
<app-c1 (y)="foo($event)"></app-c1>

## app comp

import { Component } from '@angular/core';

@Component({
selector: 'app-root',
templateUrl: './app.component.html',
styleUrls: ['./app.component.css']
})
export class AppComponent {
title: string;

foo(e): void {
this.title = e;
}
}

## c1 html

<button (click)="bar()">bar</button>

## c1 comp

import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';

@Component({
selector: 'app-c1',
templateUrl: './c1.component.html',
styleUrls: ['./c1.component.css']
})
export class C1Component implements OnInit {
constructor() { }

ngOnInit(): void {
}
@Output() y = new EventEmitter<string>();
bar() {
this.y.emit('hello fromm child');
}
}

## ====================================

import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';

@Component({
selector: 'app-c1',
templateUrl: './c1.component.html',
styleUrls: ['./c1.component.css']
})
export class C1Component implements OnInit {

@Input() x: string;

constructor() { }

ngOnInit(): void {
}
}

{{x}}

import { Component } from '@angular/core';

@Component({
selector: 'app-root',
templateUrl: './app.component.html',
styleUrls: ['./app.component.css']
})
export class AppComponent {
title = 'parent';
}
<app-c1 [x]="title"></app-c1>
