app/packages/twamm-types/__tests__/twamm-types.test.ts
======================================================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: ts

    import { strict as assert } from "assert";
import * as twammTypes from "../lib/index";

assert.deepEqual(Object.keys(twammTypes), ["OrderSide"]);
console.info("@twamm/types tests passed"); // eslint-disable-line no-console


