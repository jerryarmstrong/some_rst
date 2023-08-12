__tests__/App-test.js
=====================

Last edited: 2022-08-19 17:27:27

Contents:

.. code-block:: js

    /**
 * @format
 */

import 'react-native';
import React from 'react';
import App from '../App';

// Note: test renderer must be required after react-native.
import renderer from 'react-test-renderer';

it('renders correctly', () => {
  renderer.create(<App />);
});


