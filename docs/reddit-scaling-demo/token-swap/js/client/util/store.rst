token-swap/js/client/util/store.js
==================================

Last edited: 2020-08-26 08:56:56

Contents:

.. code-block:: js

    /**
 * Simple file-based datastore
 *
 * @flow
 */

import path from 'path';
import fs from 'mz/fs';
import mkdirp from 'mkdirp-promise';

export class Store {
  dir = path.join(__dirname, 'store');

  async load(uri: string): Promise<Object> {
    const filename = path.join(this.dir, uri);
    const data = await fs.readFile(filename, 'utf8');
    const config = JSON.parse(data);
    return config;
  }

  async save(uri: string, config: Object): Promise<void> {
    await mkdirp(this.dir);
    const filename = path.join(this.dir, uri);
    await fs.writeFile(filename, JSON.stringify(config), 'utf8');
  }
}


