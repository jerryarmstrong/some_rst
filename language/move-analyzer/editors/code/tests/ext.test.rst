language/move-analyzer/editors/code/tests/ext.test.ts
=====================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: ts

    // Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

import * as assert from 'assert';
import * as Mocha from 'mocha';
import * as vscode from 'vscode';

Mocha.suite('ext', () => {
    Mocha.test('ext_exists', () => {
        const ext = vscode.extensions.getExtension('move.move-analyzer');
        assert.ok(ext);
    });
});


