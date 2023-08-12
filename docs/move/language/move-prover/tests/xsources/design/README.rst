language/move-prover/tests/xsources/design/README.md
====================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: md

    A set of examples for illustrating how the bytecode transformation pipeline works.

This directory contains the bytecode dump of each of the Move
examples. You can run an individual example as in:

```
mvp -k --v2 --dump-bytecode <example>.move
```

The `-k` option will also let the Move prover leave the generated Boogie output
in `output.bpl`.


