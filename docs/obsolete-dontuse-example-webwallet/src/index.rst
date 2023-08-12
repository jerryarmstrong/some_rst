src/index.js
============

Last edited: 2020-08-30 15:21:22

Contents:

.. code-block:: js

    import React from 'react';
import ReactDOM from 'react-dom';

import {Wallet} from './wallet';
import {Store} from './store';

import './styles/index.scss';

class App extends React.Component {
  state = {
    store: new Store(),
    initialized: false,
  };

  async componentDidMount() {
    await this.state.store.init();
    this.setState({initialized: true});
  }

  render() {
    if (!this.state.initialized) {
      return <div />; // TODO: Loading screen?
    }
    return <Wallet store={this.state.store} />;
  }
}

ReactDOM.render(<App />, document.getElementById('app'));
module.hot.accept();


