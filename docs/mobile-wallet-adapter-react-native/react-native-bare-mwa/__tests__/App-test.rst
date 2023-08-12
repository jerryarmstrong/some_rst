react-native-bare-mwa/__tests__/App-test.tsx
============================================

Last edited: 2023-02-17 20:13:33

Contents:

.. code-block:: tsx

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


