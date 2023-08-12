language/move-bytecode-verifier/bytecode-verifier-tests/METER_TESTING.md
========================================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: md

    This testsuite can be run in a specific way to print the time until a 'complex' program is detected or accepted. Call as in:

```
cargo test --release --features=address32   -- --nocapture 1>/dev/null
```


