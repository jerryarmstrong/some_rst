example/index.js
================

Last edited: 2023-03-22 19:27:07

Contents:

.. code-block:: js

    import 'foo';
import './foo.js';
import './foo.json';
import json from './foo.json?raw';
// eslint-disable-next-line require-extensions/require-extensions
import queryNoExt from './foo?raw';
// eslint-disable-next-line require-extensions/require-extensions
import './foo';
// eslint-disable-next-line require-extensions/require-extensions
import './bar.json';
// eslint-disable-next-line require-extensions/require-index
import './dir';


