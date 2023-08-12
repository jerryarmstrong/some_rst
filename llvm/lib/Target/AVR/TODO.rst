llvm/lib/Target/AVR/TODO.md
===========================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: md

    # Write an XFAIL test for this `FIXME` in `AVRInstrInfo.td`

```
// :FIXME: DAGCombiner produces an shl node after legalization from these seq:
// BR_JT -> (mul x, 2) -> (shl x, 1)
```



