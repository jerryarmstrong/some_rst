expo-managed-mwa/index.js
=========================

Last edited: 2023-02-17 20:13:33

Contents:

.. code-block:: js

    import { registerRootComponent } from 'expo';

import App from './App';

// registerRootComponent calls AppRegistry.registerComponent('main', () => App);
// It also ensures that whether you load the app in Expo Go or in a native build,
// the environment is set up appropriately
registerRootComponent(App);


