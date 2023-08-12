src/store/index.js
==================

Last edited: 2020-07-22 13:30:11

Contents:

.. code-block:: js

    import { configure } from 'mobx';

configure({
  enforceActions: 'observed',
});

export { default as AppStore } from './app';
export { default as StatsStore } from './stats';


